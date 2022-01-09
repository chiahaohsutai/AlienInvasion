import pygame.font


class Button:
    """A class that represents a button"""

    def __init__(self, ai_game, msg):
        """Initialize button attributes"""
        self.msg = msg
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # Dimensions of button
        self.width = 200
        self.height = 50
        # Color of text & button
        self.button_color = (0, 204, 204)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Makes a surface for the button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._display_msg(self.msg)  # Renders a text image

    def _display_msg(self, msg):
        """Display the given message"""
        self.msg_display = self.font.render(msg, True, self.text_color, self.button_color)  # Renders a text image
        self.msg_display_rect = self.msg_display.get_rect()
        self.msg_display_rect.center = self.rect.center  # Centers a surface where the text is going to be diplayed on

    def draw_button(self):
        """Draw the button onto the screen"""
        self.screen.fill(self.button_color, self.rect)  # Draws button onto the screen
        self.screen.blit(self.msg_display, self.msg_display_rect)  # Places the text on top of the screen

