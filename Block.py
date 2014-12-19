import pygame
from pygame import *
import random
import math

class Block(pygame.sprite.Sprite):

    def __init__(self, color):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        self.rect = self.image.get_rect()
    def update(self):
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        if(dx,dy != 0,0):
          dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
          self.rect.x -= dx * 1
          self.rect.y -= dy * 1