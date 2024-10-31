"""
Creator Name: George Steil
Creation Date: 10/30/2024
Update Date: 10/31/2024
"""

import pygame
from constants import *

def main():
# Initialize Pygame
    pygame.init()

# Set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define color
    black = (0, 0, 0)

# Setting Delta Time
    clock = pygame.time.Clock()
    delta_time = 0

# Game loop
    running = True
    while running:
        # Gives the user the ability to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fills the screen with color black
        screen.fill(black)

        # Refereshes the screen with changes
        pygame.display.flip()

        # Sets the fps to 60 fps
        clock.tick(60)

        # Shows the delta time
        delta_time = clock.tick(60)/1000


# Print statements
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()