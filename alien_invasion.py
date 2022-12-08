import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


def run_game():
    # Initializes pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Creating a Play button
    play_button = Button(ai_settings, screen, 'Play')
    # Creating an instance to store game statistics and Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Creation of a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Creation of an alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Running the main game loop
    while True:
        # Tracking Keyboard and Mouse Events
        gf.cheek_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            # Removing bullets that have gone off the edge of the screen
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # The screen is redrawn on each pass through the loop
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
            # Displaying the last drawn screen
            pygame.display.flip()
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
