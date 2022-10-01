import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # Initializes pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Creation of a ship
    ship = Ship(screen)
    # Running the main game loop
    while True:
        # Tracking Keyboard and Mouse Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # The screen is redrawn on each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # Displaying the last drawn screen
        pygame.display.flip()


run_game()
