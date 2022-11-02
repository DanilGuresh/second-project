import sys
import pygame
from bullet import Bullet
from alien import Alien


def cheek_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responds to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fires a bullet if the maximum has not yet been reached"""
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


def update_screen(ai_setting, screen, ship, aliens, bullets):
    """Refreshes the screen image and displays the new screen"""
    # The screen is redrawn on each iteration of the loop
    screen.fill(ai_setting.bg_color)
    # Displaying the last drawn screen
    pygame.display.flip()
    # All bullets are displayed behind the image of the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Displaying the last drawn screen
    pygame.display.flip()


def update_bullets(bullets):
    """Updates bullet positions and destroys old ones"""
    # Bullet positions update
    bullets.update()
    # Removing bullets that have gone off the edge of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    """Creates an alien fleet"""
    # Creating an alien and calculating the number of aliens in a row
    # The interval between neighboring aliens is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2 * alien_width))
    # Creation of the first row of aliens
    for alien_number in range(number_aliens_x):
        # Creating an alien and placing it in a row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
