#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys
from hitemup_sprites import *

# game init
score = 0
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("HitEmUp Game - Score: %s" % score)
clock = pygame.time.Clock()

# group & sprites
hits = pygame.sprite.Group()
hit = Hit()
hits.add(hit)

# game loop
while True:
	# check for click on sprite
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				if hit.rect.collidepoint(event.pos):
					hit.update()
					score = score + 1
					pygame.display.set_caption("HitEmUp Game - Score: %s" % score)

	# render sprites
	window.fill((0, 0, 0))
	hits.draw(window)

	# refresh screen
	clock.tick(60)
	pygame.display.flip()
