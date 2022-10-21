import pygame
from settings import Settings
from ship import Ship, Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initializes pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Creation of a ship
    ship = Ship(ai_settings, screen)
    # Alien creation
    alien = Alien(screen)
    # Create a bullet storage group
    bullets = Group()
    # Running the main game loop
    while True:
        # Tracking Keyboard and Mouse Events
        gf.cheek_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Removing bullets that have gone off the edge of the screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # The screen is redrawn on each pass through the loop
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        # Displaying the last drawn screen
        pygame.display.flip()



run_game()
