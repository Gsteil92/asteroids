"""
Project Name: Asteroids with Python
Creation Date: 12/24/2024
Creator Name: George Steil
Modified Date:
"""

import pygame
from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return	
	screen.fill("black")
	pygame.display.flip()
	



if __name__ == "__main__":
	main()
