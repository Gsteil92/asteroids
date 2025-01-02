"""
Project Name: Asteroids with Python
Creation Date: 12/24/2024
Creator Name: George Steil
Modified Date:
"""

import pygame
from constants import *
from player import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(x = (SCREEN_WIDTH / 2), y = (SCREEN_HEIGHT / 2))
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return	
		screen.fill("black")
		for object in updatable:
			object.update(dt)
			
		for object in drawable:
			object.draw(screen)
		
		pygame.display.flip()
		dt = clock.tick(60) / 1000
	



if __name__ == "__main__":
	main()
