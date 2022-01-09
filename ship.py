import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position in the canvas"""
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Load in the ship image and its rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen (aligns at midbottom)
        self.center_ship()
        # Flag to determine direction of movement
        self.movement_right = False
        self.movement_left = False

    def center_ship(self):
        """Center the ship to in the canvas"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= self.settings.ship_bottom_border_distance  # adds small offset b/t ship and bottom border
        self.x = float(self.rect.x)

    def update_movement(self):
        """Move the ship according to the flag"""
        if self.movement_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.movement_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def draw_ship(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        