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
        self.alien_speed_factor = 15
        self.fleet_drop_speed = 10
        # fleet_direction = 1 denotes movement to the right; a -1 to the left
        self.fleet_direction = 1
