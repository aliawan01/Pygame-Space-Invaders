import pygame
from pygame.locals import *
import sys

from main import *
from lasers import *
from ship import *

def main():
	main = Main()

	pygame.init()
	old_time = pygame.time.get_ticks()

	pygame.display.set_caption("Space Invaders")
	pygame.display.set_icon(main.WINDOW_ICON)

	player_ship = Ship(main.ENEMY_BLUE_SHIP, 1)
	enemy_ship = Ship(main.ENEMY_BLUE_SHIP, 0)

	while True:
		main.draw_background()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			# Shooting Player laser
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					player_laser = Lasers(player_ship.player_x, player_ship.player_y, player_ship.PLAYER_LASER)
					player_ship.shoot_laser(player_laser, False, enemy_ship.enemy_x, enemy_ship.enemy_y, enemy_ship.enemy_img)

		player_ship.player()
		enemy_ship.enemy()

		if 'player_laser' in locals():
			player_ship.shoot_laser(player_laser, True, enemy_ship.enemy_x, enemy_ship.enemy_y, enemy_ship.enemy_img)

		main.update_display()


if __name__ == '__main__':
	main()
