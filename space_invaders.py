import pygame
from pygame.locals import *


from main import *
from new_lasers import *
from ship import *

def main():
	main = Main()

	pygame.init()

	pygame.display.set_caption("Space Invaders")

	player_ship = Ship(2, 1, main.ENEMY_BLUE_SHIP, 1)
	enemy_ship = Ship(2, 1, main.ENEMY_BLUE_SHIP, 0)

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
					player_ship.shoot_laser(player_laser, False)

		player_ship.player()
		enemy_ship.enemy()

		if 'player_laser' in locals():
			player_ship.shoot_laser(player_laser, True)

		main.update_display()


if __name__ == '__main__':
	main()
