import sys
import pygame


def cheek_events():
    """Handles key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_setting, screen, ship):
    """Refreshes the screen image and displays the new screen"""
    # The screen is redrawn on each iteration of the loop
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    # Displaying the last drawn screen
    pygame.display.flip()