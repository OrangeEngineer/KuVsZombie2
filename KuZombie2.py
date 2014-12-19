import pygame
from pygame.locals import *
from pygame import *
import random
import math
import gamelib
import time

from Player import *
from Bullet import *
	
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = ( 120, 0, 0)
BLUE = ( 0, 0, 255)

class KuZombie2(gamelib.ZombieGame):
    DEFAULT_LIST_ITEM_PLUS_MINUS = ['plus'] * 1 + ['minus']
    LIST_ITEM_NUMBER = [0] * 10 + range(1, 12) * 7 + [4] * 40
    
    def __init__(self):
    	super(KuZombie2, self).__init__('You Gonna Die!!', RED)
        self.player = player(pos=(self.window_size[0]/2,self.window_size[1]/2),color=RED)
        self.setTimeInterval = 0
        self.Bullets = []
    
    def init(self):
        super(KuZombie2, self).init()
    
    def update(self):
    	if self.is_key_pressed(K_w):
            self.player.move_up()
        elif self.is_key_pressed(K_s):
            self.player.move_down()
        elif self.is_key_pressed(K_a):
            self.player.move_left()
        elif self.is_key_pressed(K_d):
            self.player.move_right()
        
        mouse_x,mouse_y = pygame.mouse.get_pos()
        self.player.rotate(mouse_x,mouse_y)
        self.player.update()
        self.updateBullet()
        
    def addBullet(self):    
        mouse_x,mouse_y = pygame.mouse.get_pos()
        self.Bullets += [Bullet(pos = (self.player.getX(),self.player.getY()),mousex = mouse_x,mousey = mouse_y)]    
    
    def renderBullet(self, surface):
        for Bullet in self.Bullets :
            Bullet.render(surface)

    def updateBullet(self):
        deltatime = pygame.time.get_ticks() / 500
        if deltatime > self.setTimeInterval :
            self.setTimeInterval = deltatime
            KuZombie2.LIST_ITEM_NUMBER += [4]

        for x in range(len(self.Bullets), deltatime - len(self.Bullets)) :
            if  self.is_key_pressed(K_SPACE):
                self.addBullet()
        for Bullet in self.Bullets :
            Bullet.update()

    def render(self, surface):
        self.player.render(surface)
        self.renderBullet(surface)
        mouse_x,mouse_y = pygame.mouse.get_pos()
        self.player.rotate(mouse_x,mouse_y)


def main():
    game = KuZombie2()
    game.run()
if __name__ == '__main__':
    main()