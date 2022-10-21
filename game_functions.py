import sys
import pygame
from bullet import Bullet


def cheek_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responds to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Creating a new bullet and including it in a group bullets
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def cheek_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def cheek_events(ai_settings, screen, ship, bullets):
    """Handles key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            cheek_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            cheek_keyup_events(event, ship)


def update_screen(ai_setting, screen, ship, alien, bullets):
    """Refreshes the screen image and displays the new screen"""
    # The screen is redrawn on each iteration of the loop
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    alien.blitme()
    # Displaying the last drawn screen
    pygame.display.flip()
    # All bullets are displayed behind the image of the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
