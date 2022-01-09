
class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initializes the game's settings."""

        # Dimensions of the game window/canvas
        self.screen_width = 1200
        self.screen_height = 800
        # Canvas/background color
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_bottom_border_distance = 25
        self.ship_limit = 3  # number of lives available

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3  # max number of bullets

        # Alien Settings
        self.drop_speed = 10
        self.alien_fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.1
        self.dynamic_settings(-1)

    def dynamic_settings(self, difficulty):
        """Initializes the dynamic settings of the game"""
        if difficulty == -1:
            self.ship_speed = 2.5
            self.alien_speed = 3
            self.bullet_speed = 4
            self.alien_point = 50
        elif difficulty == 0:
            self.ship_speed = 3
            self.alien_speed = 4
            self.bullet_speed = 5
            self.alien_point = int(50 * self.score_scale)
        elif difficulty == 1:
            self.ship_speed = 3.5
            self.alien_speed = 5
            self.bullet_speed = 6
            self.alien_point = int(50 * self.score_scale**2)

    def increase_speeds(self):
        """Increases the value of dynamic settings"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_point = int(self.score_scale *
                               self.alien_point)
