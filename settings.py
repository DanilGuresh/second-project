class Settings:
    """Class to store all Alien Invasion game settings"""
    def __init__(self):
        """Initializes game settings"""
        # Screen settings
        self.screen_width = 1360
        self.screen_height = 710
        self.bg_color = (85, 170, 255)
        # Settings ship
        self.ship_speed_factor = 1.5
