import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    """A class to manage bullets"""

    def __init__(self, ai_game):
        """Create a bullet at ship's position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a rect bullet and set to the ship's position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullets position as a decimal value
        self.y = float(self.rect.y)

    def update(self):  # Override update for sprites
        """Move the bullet up the screen"""
        # Update the position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the bullets rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        