import pygame
from pygame.locals import *

from main import *


class Lasers(Main):
    def __init__(self, laser_x, laser_y, laser_img):
        super().__init__()
        self.laser_x = laser_x + 24
        self.laser_y = 461 - 23
        self.laser_img = laser_img

        self.laser_velocity = 5
        self.laser_mask = pygame.mask.from_surface(laser_img)

    def draw_laser(self):
        self.screen.blit(self.laser_img, (self.laser_x, self.laser_y))

    def move_laser(self, sprite):
        """
        sprite = integer 1 or 0 -> if 0 sprite = enemy_ship, if 1 sprite = player_ship
        """
        if sprite == 1:
            self.laser_y -= self.laser_velocity

        if sprite == 0:
            self.laser_y += self.laser_velocity
            
    # This method runs the 2 methods above it
    def laser(self, sprite):
        self.draw_laser()
        self.move_laser(sprite)
