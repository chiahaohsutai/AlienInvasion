import sys
import pygame
from settings import Settings
from ship import Ship
from bullets import Bullets
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)   # makes an instance to store game stats
        # Moving objs
        self.ship = Ship(self)  # input is an instance of this class
        self.bullets = pygame.sprite.Group()  # Initialize list of sprites (sprite = moving graphical obj)
        self.aliens = pygame.sprite.Group()
        # Buttons
        self.button = Button(self, "PLAY")
        self.button_1 = Button(self, "EASY")
        self.button_2 = Button(self, "MEDIUM")
        self.button_3 = Button(self, "HARD")
        self._difficulty_menu()
        self.difficulty = None
        self.scoreboard = Scoreboard(self)

    def _difficulty_menu(self):
        """Positions the menu in the correct location"""
        self.button_1.rect.midbottom = self.button.rect.midtop
        self.button_1.rect.y -= 25
        self.button_1.msg_display_rect.center = self.button_1.rect.center

        self.button_3.rect.midtop = self.button.rect.midbottom
        self.button_3.rect.y += 25
        self.button_3.msg_display_rect.center = self.button_3.rect.center

    def _create_alien_fleet(self):
        """Generate a fleet of aliens"""

        # Calculate how many aliens fit in a row
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        # Horizontal Space
        available_space_x = self.settings.screen_width - (2 * alien_width)
        max_num_aliens_x = available_space_x // (2 * alien_width)  # max number of aliens that fit horizontally
        # Vertical Space
        available_space_y = (self.settings.screen_height - (5 * alien_height) -
                             (self.ship.rect.height + self.settings.ship_bottom_border_distance))
        max_num_row = available_space_y // (2 * alien_height)

        # Generate a fleet of aliens in the same row
        for alien_row in range(max_num_row):
            for alien_column in range(max_num_aliens_x):
                self._create_alien(alien_column, alien_row)

    def _create_alien(self, column, row):
        """Creates an alien in the given row and column"""
        alien = Alien(self)
        alien.x = alien.rect.width + 2 * alien.rect.width * column
        alien.rect.x = alien.x  # sets the alien's position in the screen
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row + 20
        self.aliens.add(alien)  # adds alien to the group

    def _check_events(self):
        """Responds to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.set_new_record()
                sys.exit()
            # Responds to key being pressed
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            # Responds to key being released
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            # Responds to mouse event
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._play_game(pygame.mouse.get_pos())

    def _check_keydown(self, event):
        """Responds to key press"""
        if event.key == pygame.K_RIGHT:
            self.ship.movement_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.movement_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._play_game(self.button.rect.center)
        elif event.key == pygame.K_1 and self.stats.difficulty_selection_complete:
            self._add_difficulty(self.button_1.rect.center)
        elif event.key == pygame.K_2 and self.stats.difficulty_selection_complete:
            self._add_difficulty(self.button_2.rect.center)
        elif event.key == pygame.K_3 and self.stats.difficulty_selection_complete:
            self._add_difficulty(self.button_3.rect.center)
        elif event.key == pygame.K_r and self.stats.game_active:
            self._reset()
        elif event.key == pygame.K_q:
            self.stats.set_new_record()
            sys.exit()

    def _check_keyup(self, event):
        """Responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.movement_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.movement_left = False

    def _play_game(self, pos):
        """Sets the game state to active if button is clicked"""
        if (self.button.rect.collidepoint(pos) and not self.stats.game_active
                and not self.stats.difficulty_selection_complete):
            self.stats.reset_stats()  # resets game statistics
            self.aliens.empty()
            self.bullets.empty()
            self.ship.center_ship()
            self.stats.difficulty_selection_complete = True  # Sets the game to selection mode
        elif self.stats.difficulty_selection_complete and not self.stats.game_active:
            self._add_difficulty(pos)

    def _reset(self):
        """Stops and resets the game (take you back to play button menu)"""
        self.stats.game_active = False
        self.stats.difficulty_selection_complete = False
        pygame.mouse.set_visible(True)

    def _add_difficulty(self, pos):
        """Allows user to select a difficulty"""
        self.difficulty = pos
        if self.button_1.rect.collidepoint(pos):
            self.settings.dynamic_settings(-1)
        elif self.button_2.rect.collidepoint(pos):
            self.settings.dynamic_settings(0)
        elif self.button_3.rect.collidepoint(pos):
            self.settings.dynamic_settings(1)
        # Update the scoreboard back to initial values
        self.scoreboard.display_score()
        self.scoreboard.display_level()
        self.scoreboard.display_ships()
        self.stats.game_active = True
        self._create_alien_fleet()
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet and add it to the list/group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullets(self)  # makes a new instance of a bullet
            self.bullets.add(new_bullet)  # adds bullet to list/group bullets

    def _update_scene(self):
        """Updates images on the screen, and flip to new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        self.scoreboard.show_score()
        # Bullet movement
        for bullet in self.bullets:
            bullet.draw_bullet()
        # Alien fleet movement
        self.aliens.draw(self.screen)  # draws aliens in the group
        # Play button
        if not self.stats.game_active and not self.stats.difficulty_selection_complete:
            self.button.draw_button()  # Draws the button onto canvas when game inactive
        # Difficulty menu
        if self.stats.difficulty_selection_complete and not self.stats.game_active:
            self.button_1.draw_button()
            self.button_2.draw_button()
            self.button_3.draw_button()
        pygame.display.flip()  # make changes available

    def _update_bullet(self):
        """Update position of bullets and remove old bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_collisions()

    def _check_collisions(self):
        """Checks for collisions and re initiates the fleet"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            # collisions is a dict where its values are a list or rects that collided with the key
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)  # adds points to score
            self.scoreboard.display_score()  # makes a new image with new score
            self.scoreboard.check_high_score()  # checks if a new high score was reached
        # checks if there's no more aliens on the screen
        if not self.aliens:
            self.bullets.empty()
            self._create_alien_fleet()
            self.settings.increase_speeds()
            self.stats.level += 1
            self.scoreboard.display_level()

    def _update_aliens(self):
        """Update the position of aliens"""
        self._check_fleet_edge()  # checks if the fleet reached the right/left of screen
        self.aliens.update()
        # checks for collisions with the ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_fleet_bottom()  # checks if any alien reached the bottom of the screen

    def _check_fleet_edge(self):
        """Checks if any alien in the fleet has hit an edge/border"""
        for alien in self.aliens:
            if alien.check_edge():
                self._change_fleet_direction()  # changes the direction and moves fleet down
                break

    def _change_fleet_direction(self):
        """Drop fleet's y-position and change the fleet's direction"""
        for alien in self.aliens:
            alien.rect.y += self.settings.drop_speed
        self.settings.alien_fleet_direction *= -1

    def _check_fleet_bottom(self):
        """Checks if any alien has hit the bottom of the screen"""
        for alien in self.aliens:
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Responds to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1  # reduce ships limit
            self.scoreboard.display_ships()
            self.bullets.empty()  # remove bullets from screen
            self.aliens.empty()   # remove aliens from screen
            self._create_alien_fleet()  # generate a new fleet
            self.ship.center_ship()  # place ship in starting position
            sleep(0.5)  # freeze the game for a little bit
        else:
            self._reset()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()  # responds to key events
            if self.stats.game_active:
                self.ship.update_movement()  # update the ships movement
                self._update_bullet()  # controls updates and deletion of bullets
                self._update_aliens()  # controls alien fleet movement
            self._update_scene()  # re-draws canvas after updates are drawn


# Starts the game:
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
