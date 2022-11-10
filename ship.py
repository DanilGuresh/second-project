import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """Initializes the ship and sets its initial position"""
        self.screen = screen
        self.ai_settings = ai_settings
        # Loading the image of the box and getting the rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Each new ship appears at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Saving the real coordinate of the center of the ship
        self.center = float(self.rect.centerx)
        # Move Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Updates the ship's position based on the flag
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        # Update attribute center, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Rect attribute update based on self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draws the ship at the current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Places the ship in the center of the bottom side"""
        self.center = self.screen_rect.centerx

