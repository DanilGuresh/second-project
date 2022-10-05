import pygame


class Ship:
    def __init__(self, screen):
        """Initializes the ship and sets its initial position"""
        self.screen = screen
        # Loading the image of the box and getting the rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Each new ship appears at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draws the ship at the current position"""
        self.screen.blit(self.image, self.rect)


class Alien:
    def __init__(self, screen):
        """Initializes the alien and sets its initial position"""
        self.screen = screen
        # Loading the image
        self.image = pygame.image.load('images/alien.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        #
        self.screen.blit(self.image, self.rect)
