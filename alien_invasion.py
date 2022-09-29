import sys
import pygame


def run_game():
    # Creates a screen object
    pygame.init()
    pygame.display.set_caption("Alien Invarsion")
    screen = pygame.display.set_mode((1360, 710))
    # Assigning a background color
    bg_color = (230, 230, 230)
    # Running the main game loop
    while True:
        # Tracking Keyboard and Mouse Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # The screen is redrawn on each pass through the loop
        screen.fill(bg_color)
        # Displaying the last drawn screen
        pygame.display.flip()


run_game()
