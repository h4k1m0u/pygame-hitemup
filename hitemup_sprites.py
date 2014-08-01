#!/usr/bin/env python
import pygame
import random

# constants
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
SPRITE_WIDTH, SPRITE_HEIGHT = 67, 60

class Hit(pygame.sprite.Sprite):
	""" Hit: Positionned randomly on the window.
    """
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		# load image & rect
		self.image = pygame.image.load('images/hit.png').convert() 
		self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect()
		self.move_to_random_position()
	
	def update(self):
		self.move_to_random_position()

	def move_to_random_position(self):
		# move the sprite to a random position
		sprite_x = random.randrange(WINDOW_WIDTH)
		sprite_y = random.randrange(WINDOW_HEIGHT)

		if sprite_x + SPRITE_WIDTH > WINDOW_WIDTH:
			sprite_x = WINDOW_WIDTH - SPRITE_WIDTH
		if sprite_y + SPRITE_HEIGHT > WINDOW_HEIGHT:
			sprite_y = WINDOW_HEIGHT - SPRITE_HEIGHT

		self.rect.x, self.rect.y = sprite_x, sprite_y
