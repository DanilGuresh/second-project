import sys
import pygame


def cheek_events(ship):
    """Handles key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move ship to the right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_setting, screen, ship, alien):
    """Refreshes the screen image and displays the new screen"""
    # The screen is redrawn on each iteration of the loop
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    alien.blitme()
    # Displaying the last drawn screen
    pygame.display.flip()