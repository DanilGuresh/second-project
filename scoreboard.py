import pygame.font


class Scoreboard:
    """Class for displaying game information"""
    def __init__(self, ai_settings, screen, stats,):
        """Initializes scoring attributes"""
        self.screen = screen
        self.score_image = None
        self.score_rect = None
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # Setting the font for invoice output
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Preparing the original image
        self.prep_score(screen)
        self.prep_high_score(screen)

    def prep_score(self, screen):
        """Converts the current account to a graphic image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        # Invoice at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = 10

    def show_score(self):
        """Displays an invoice on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self, screen):
        """Converts a record score to a graphic"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        # The record is centered on the top side
        self.high_score_rect = self.high_score_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top = 10
