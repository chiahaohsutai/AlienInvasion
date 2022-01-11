import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """To keep track of the game score"""

    def __init__(self, ai_game):
        """Initialize the scoreboard"""
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats
        # Text/font attribute
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 38)
        self.display_score()
        self.display_high_score()
        self.display_level()
        self.display_ships()

    def display_score(self):
        """Turn the score to a rendered image"""
        rounded_score = round(self.stats.score, -1)  # rounds to a multiple of 10
        # adds commas to make numerical value more clear
        score_str = "Score: " + "{:,}".format(rounded_score)
        # Render the text as image
        self.score_img = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_img.get_rect()
        # Place image on correct location
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def display_high_score(self):
        """Turn the high score to a rendered image"""
        rounded_score = round(self.stats.high_score, -1)  # rounds to a multiple of 10
        # adds commas to make numerical value more clear
        score_str = "HighScore: " + "{:,}".format(rounded_score)
        # Render the text as image
        self.high_score_img = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_img.get_rect()
        # Place image on correct location
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def show_score(self):
        """Draws the image onto the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_img_react)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Checks if there is a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.new_record = True
            self.stats.high_score = self.stats.score
            self.display_high_score()

    def display_level(self):
        """Renders a image with the current level"""
        level_str = "Level: " + str(self.stats.level)
        self.level_img = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_img_react = self.level_img.get_rect()
        self.level_img_react.top = self.screen_rect.top + 55
        self.level_img_react.right = self.screen_rect.right - 20

    def display_ships(self):
        """Show how many ships are left"""
        self.ships = Group()
        for pos in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 20 + self.screen_rect.left + ship.rect.width * pos
            ship.rect.y = self.screen_rect.top + 20
            self.ships.add(ship)
