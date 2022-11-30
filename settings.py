class Settings:
    """Class to store all Alien Invasion game settings"""

    def __init__(self):
        """Initializes game settings"""
        # Screen settings
        self.screen_width = 1360
        self.screen_height = 710
        self.bg_color = (85, 170, 255)
        # Settings ship
        self.ship_speed_factor = 3
        self.ship_limit = 3
        # Setting bullet:
        self.bullet_speed_factor = 0.7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 denotes movement to the right; a -1 to the left
        self.fleet_direction = 1
        # Game acceleration rate
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        # The growth rate of the value of aliens
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes settings that change during the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 0.7
        self.alien_speed_factor = 1
        # fleet_direction = 1 means moving to the right; a -1 to the left
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 10

    def increase_speed(self):
        """Increases speed settings and cost of aliens"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
