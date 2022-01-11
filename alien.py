import pygame
from pygame.sprite import Sprite
import random


class Alien(Sprite):
    """A class to manage an alien"""

    def __init__(self, ai_game):
        """Initializes an instance of an alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien bitmap into the class
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Position the alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's x-position as a float
        self.x = float(self.rect.x)
        self.direction = random.randrange(-1, 2, 2)

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed * self.direction
        self.rect.x = self.x

    def check_edge(self):
        """Checks if the alien has reached a border"""
        if self.rect.right > self.settings.screen_width:
            return 1
        elif self.rect.left < 0:
            return 0

