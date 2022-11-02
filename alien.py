import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class representing a single alien"""
    def __init__(self, ai_settings, screen):
        """Initializes the alien and sets its initial position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Loading an alien image and assigning a rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Each new alien appears in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # saving the alien's accurate position
        self.x = float(self.rect.x)

    def blitme(self):
        # Displays the alien in its current position
        self.screen.blit(self.image, self.rect)
