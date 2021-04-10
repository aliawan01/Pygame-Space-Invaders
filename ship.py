import pygame
from pygame.locals import *

import random

from main import *

class Ship(Main):
    def __init__(self, ship_img, ship_type):
        super().__init__()
        self.enemy_x = 2
        self.enemy_y = 1

        # self.enemy_img = self.ENEMY_SHIPS['blue_ship'][0] 
        enemy = self.ENEMY_SHIPS[random.choice(list(self.ENEMY_SHIPS))] 
        self.enemy_img = enemy[0] 
        self.enemy_laser = enemy[1] 

        self.player_x = self.screen_x // 2
        self.player_y = self.screen_y // 1.3

        # Amount the enemy will move in x and y direction
        self.enemy_move_x = 2
        self.enemy_move_y = 50
        self.enemy_off_screen = False

        """
        ship_img = integer 1 or 0 -> if 0 ship_type = enemy_ship, if 1 ship_type = player_ship
        """
        self.ship_type = ship_type
        self.old_time = pygame.time.get_ticks()

        self.laser_cooldown_time = 1000
        self.laser_list = []

    def draw_enemy_ship(self):
        self.enemy_ship = self.screen.blit(self.enemy_img, (self.enemy_x, self.enemy_y))

    def enemy_ship_movement(self):
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
        self.enemy_ship_movement()

    # Drawing and adding player controls
    def draw_player(self):
        self.player_ship = self.screen.blit(self.PLAYER_SHIP, (self.player_x, self.player_y))

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

    def collision(self, object1, object1_x, object1_y, object2, object2_x, object2_y):
        object1_mask = pygame.mask.from_surface(object1)
        object2_mask = pygame.mask.from_surface(object2)
        offset = (int((object1_x - object2_x)), int((object1_y - object2_y)))
        collision = object1_mask.overlap(object2_mask, offset)
        if collision != None:
            return True

    def laser_cooldown(self, laser_instance):
        if len(self.laser_list) > 0:
            current_time = pygame.time.get_ticks()

            if (current_time - self.old_time) > self.laser_cooldown_time:
                self.laser_list.append(laser_instance)
                self.old_time = pygame.time.get_ticks()

    def shoot_laser(self, laser_instance, update_laser, object_x, object_y, object_img):
        # Only adding a new laser if the space bar is pressed
        if update_laser == False:
            self.laser_cooldown(laser_instance)

            if len(self.laser_list) == 0:
                self.laser_list.append(laser_instance)
                self.old_time = pygame.time.get_ticks()


        for laser in self.laser_list:

            # Checking if the laser is on the screen
            if laser.laser_y >= (-1 * (laser.laser_img.get_height())):
                laser.laser(self.ship_type)

            # Checking if the laser is off the screen
            if laser.laser_y < (-1 * (laser.laser_img.get_height())):
                self.laser_list.pop(self.laser_list.index(laser))

            # Checking for collisions
            if self.collision(laser.laser_img, laser.laser_x, laser.laser_y, object_img, object_x, object_y) == True:
                self.laser_list.pop(self.laser_list.index(laser))
