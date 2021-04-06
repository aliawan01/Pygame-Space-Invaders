import pygame
from pygame.locals import *

from ship import *

class Lasers(Ship):
	def __init__(self, laser_x, laser_y, laser_img):
		super().__init__(laser_x, laser_y, laser_img)
		super().player()
		super().enemy()
		self.laser_x = laser_x + 24
		self.laser_y = 461 - 23
		self.laser_img = laser_img

		self.laser_state = True
		self.laser_velocity = 10

	def laser_glow_effect(self):
		# probably needs a color and a radius for the circle which we are going to make look like the circle
		pass

	def move_laser(self):
		if self.laser_state == True:
			self.laser_y -= self.laser_velocity
			self.real_laser = self.screen.blit(self.laser_img, (self.laser_x, self.laser_y))
			self.laser_rectangle()
		# Checking if the laser is off the screen
		if self.laser_y <= 0:
			self.laser_state = False

	def collision_masks(self, object1, object2, object1_pos, object2_pos):
		self.object1_mask = pygame.mask.from_surface(object1)
		self.object2_mask = pygame.mask.from_surface(object2)
		self.object1_o = self.object1_mask.outline()
		pygame.draw.lines(self.screen, self.COLORS['white'], True, self.object1_o, 2)
		self.screen.blit(self.laser_img, (32, 5))

		offset = (int(object2_pos[0] - object1_pos[0]), int(object2_pos[1] - object1_pos[1]))
		self.collide_or_not = self.object1_mask.overlap(self.object2_mask, offset)

		if self.collide_or_not != None:
			print(self.collide_or_not)
			print(offset)



	def laser_rectangle(self):
		self.laser_rect = self.laser_img.get_rect(topleft = (self.laser_x, self.laser_y))
		pygame.draw.rect(self.screen, self.COLORS['white'], self.laser_rect, 1)

		# Variables for the laser's collision
		laser_pos = (self.laser_x, self.laser_y)
		enemy_pos = (self.enemy_x, self.enemy_y)

		if hasattr(self, 'laser_rect') == True and hasattr(self, 'enemy_rect'):
			self.collision_masks(self.laser_img, self.enemy_img, laser_pos, enemy_pos)

			# pygame.draw.line(self.screen, self.COLORS['white'], (self.laser_x, self.laser_y), (self.enemy_x, self.enemy_y))

