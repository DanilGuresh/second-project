import sys
import pygame


def run_game():
    # Creates a screen object
    pygame.init()
    screen = pygame.display.set_mode((1360, 710))
    # Running the main game loop
    while True:
        # Tracking Keyboard and Mouse Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Displaying the last drawn screen
        pygame.display.flip()


run_game()
