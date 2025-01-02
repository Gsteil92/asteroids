"""
Project Name: Asteroids with Python
Creation Date: 12/24/2024
Creator Name: George Steil
Modified Date: 1/2/2025
"""

import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable_group = pygame.sprite.Group()
	drawable_group = pygame.sprite.Group()
	asteroids_group = pygame.sprite.Group()
	shots_group = pygame.sprite.Group()
	Player.containers = (updatable_group, drawable_group)
	Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
	AsteroidField.containers = (updatable_group,)
	Shot.containers = (shots_group, updatable_group, drawable_group)
	player = Player(x = (SCREEN_WIDTH / 2), y = (SCREEN_HEIGHT / 2))
	asteroid_field = AsteroidField()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return	
		screen.fill("black")
		for object in updatable_group:
			object.update(dt)

		for shot in shots_group:
			shot.update(dt)

		for shot in shots_group:
			for asteroid in asteroids_group:
				if asteroid.collisions(shot):
					asteroid.split()
					shot.kill()
			
		for object in asteroids_group:
			if object.collisions(player):
				print("Game over!")
				sys.exit()

		for object in drawable_group:
			object.draw(screen)

		for shot in shots_group:
			shot.draw(screen)
		
		pygame.display.flip()
		dt = clock.tick(60) / 1000
	



if __name__ == "__main__":
	main()
