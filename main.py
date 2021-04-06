import pygame
from pygame.locals import *

import sys

class Main:
	def __init__(self):

		# File Path ------------------------------------------------
		self.path = 'C:\\Dev\\Pygame Projects\\Space Invaders\\'

		# Screen Resolution ----------------------------------------
		self.screen_x = 600
		self.screen_y = 600

		# Display Surface ------------------------------------------
		self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))

		# Loading Stuff --------------------------------------------

		# Background
		self.BACKGROUND = pygame.transform.scale(pygame.image.load(self.path + 'assets\\background.png'), (self.screen_x, self.screen_y)).convert_alpha()

		# Buttons
		self.BUTTON = pygame.image.load(self.path + 'assets\\general_button.png').convert_alpha()
		self.OPTIONS_BUTTON = pygame.image.load(self.path + 'assets\\options_button.png').convert_alpha()
		self.PLAY_AGAIN_BUTTON = pygame.image.load(self.path + 'assets\\play_again_button.png').convert_alpha()
		self.START_BUTTON = pygame.image.load(self.path + 'assets\\start_button.png').convert_alpha()

		# Lasers
		self.BLUE_LASER = pygame.image.load(self.path + 'assets\\pixel_laser_blue.png').convert_alpha()
		self.GREEN_LASER = pygame.image.load(self.path + 'assets\\pixel_laser_green.png').convert_alpha()
		self.RED_LASER = pygame.image.load(self.path + 'assets\\pixel_laser_blue.png').convert_alpha()

		# Enemy Ships
		self.ENEMY_BLUE_SHIP = pygame.image.load(self.path + 'assets\\pixel_ship_blue_small.png').convert_alpha()
		self.ENEMY_GREEN_SHIP = pygame.image.load(self.path + 'assets\\pixel_ship_green_small.png').convert_alpha()
		self.ENEMY_RED_SHIP = pygame.image.load(self.path + 'assets\\pixel_ship_red_small.png').convert_alpha()

		# Player ---------------------------------------------------
		self.PLAYER_SHIP = pygame.transform.scale(pygame.image.load(self.path + 'assets\\pixel_ship_yellow.png'), (self.screen_x // 6, self.screen_x // 6)).convert_alpha()

		# Player Laser
		self.PLAYER_LASER = pygame.transform.scale(pygame.image.load(self.path + 'assets\\player_laser.png'), (50, 50)).convert_alpha()


		self.player_x = self.screen_x // 2
		self.player_y = self.screen_y // 1.3

		# Colors ---------------------------------------------------
		self.COLORS = {
			'red': (255, 0, 0),
			'green': (0, 255, 0),
			'blue': (0, 0, 255),
			'white': (255, 255, 255),
			'black': (0, 0, 0)
		}


		# Game Clock Object ----------------------------------------
		self.clock = pygame.time.Clock()

	def update_display(self):
		pygame.display.update()
		self.clock.tick(60)

	# Drawing the Background onto the screen
	def draw_background(self):
		self.screen.fill(self.COLORS['black'])
		self.screen.blit(self.BACKGROUND, (0, 0))
