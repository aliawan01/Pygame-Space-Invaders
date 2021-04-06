import pygame
from pygame.locals import *

import random

from main import *

class Ship(Main):
    def __init__(self, ship_x, ship_y, ship_img, ship_type):
        super().__init__()
        self.enemy_x = ship_x
        self.enemy_y = ship_y
        self.enemy_img = ship_img

        # Amount the enemy will move in x and y direction
        self.enemy_move_x = 2
        self.enemy_move_y = 50
        
        self.enemy_off_screen = False

        self.laser_list = []
        self.ship_type = ship_type

    def draw_enemy_ship(self):
        self.enemy_ship = self.screen.blit(self.enemy_img, (self.enemy_x, self.enemy_y))
        self.enemy_rect = self.enemy_img.get_rect(topleft = (self.enemy_x, self.enemy_y))
        self.enemy_ship_movement(self.enemy_rect)

    def enemy_ship_movement(self, enemy_rect):
        if self.enemy_off_screen == False:

            self.enemy_x += self.enemy_move_x

        if self.enemy_x >= (self.screen_x - (self.enemy_img.get_width())):
            self.enemy_y += self.enemy_move_y
            self.enemy_off_screen = True

        if self.enemy_off_screen == True:
            self.enemy_x -= self.enemy_move_x
            if self.enemy_x <= 1:
                self.enemy_y += self.enemy_move_y
                self.enemy_off_screen = False

    def enemy(self):
        self.draw_enemy_ship()

    def collision(self, object1, object2):
        if pygame.Rect.colliderect(object1, object2) == True:
            print("Collision has taken place\n")


    # Drawing and adding player controls
    def draw_player(self):
        self.player_ship = self.screen.blit(self.PLAYER_SHIP, (self.player_x, self.player_y))
        self.player_rect = self.PLAYER_SHIP.get_rect(topleft = (self.player_x, self.player_y))

    def player_controls(self, player_move):
        key_pressed = pygame.key.get_pressed()

        # Adding controls and boundaries
        if key_pressed[K_LEFT] and self.player_x >= 0:
            self.player_x -= player_move

        if key_pressed[K_RIGHT] and self.player_x <= (self.screen_x - 100):
            self.player_x += player_move

    def player(self):
        self.draw_player()
        self.player_controls(self.screen_x // 100)
        # if hasattr(self, 'player_rect') == True and hasattr(self, 'enemy_rect') == True:
        #     # self.collision(self.player_rect, self.enemy_rect)
        #     pygame.draw.line(self.screen, self.COLORS['white'], (self.player_x, self.player_y), (self.enemy_x, self.enemy_y))

    def shoot_laser(self, laser_instance, update_laser):
        # Only adding a new laser if the space bar is pressed
        if update_laser == False:
            self.laser_list.append(laser_instance)

        for laser in self.laser_list:
            if laser.laser_y >= (-1 * (laser.laser_img.get_height())):
                laser.laser(self.ship_type)
                print(self.laser_list)

            if laser.laser_y < (-1 * (laser.laser_img.get_height())):
                self.laser_list.pop(self.laser_list.index(laser))
