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
        self.prep_score()

    def prep_score(self):
        """Converts the current account to a graphic image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        # Invoice at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right = 30
        self.score_rect.top = 10

    def show_score(self):
        """Displays an invoice on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
