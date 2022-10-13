import pygame
from settings import Settings
from ship import Ship, Alien
import game_functions as gf


def run_game():
    # Initializes pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Creation of a ship
    ship = Ship(ai_settings, screen)
    alien = Alien(screen)
    # Running the main game loop
    while True:
        # Tracking Keyboard and Mouse Events
        gf.cheek_events(ship)
        ship.update()
        # The screen is redrawn on each pass through the loop
        gf.update_screen(ai_settings, screen, ship, alien)
        # Displaying the last drawn screen
        pygame.display.flip()


run_game()
