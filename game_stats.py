class GameStats:
    """Aliens Invasion game stats tracker"""
    def __init__(self, ai_settings):
        """Initializes statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # The game Aliens starts in an active state
        self.game_active = True

    def reset_stats(self):
        """Initializes statistics that change during the game"""
        self.ships_left = self.ai_settings.ship_limit
