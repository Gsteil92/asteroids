"""
Creator Name: George Steil
Creation Date: 10/30/2024
Update Date: N/A
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

# Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        pygame.display.flip()


# Print statements
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()