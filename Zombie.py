import pygame
import math
from pygame.locals import *
from Player import *
import random

class Zombie(object):
   
    def __init__(self,mousex,mousey,health,height=20,width=20):
        self.x = random.randint(0,600)
        self.y = -30
        self.mouse_x = mousex
        self.mouse_y = mousey
        self.width= width
        self.height= height
        self.ZombieHealth = health
        self.image = pygame.image.load("res/Zombie/Zombie1.png")
        self.image = pygame.transform.rotate(self.image,math.pi)
        self.original=self.image
        self.image = pygame.transform.rotate(self.image,30)
        self.rectZombie = pygame.Rect(self.x,self.y,self.width,self.height)

    def render(self,surface):
        pos = (int(self.x),int(self.y))
        surface.blit(self.image,pos)
    
    def getX(self):
		return self.x

    def getY(self):
		return self.y
    def getrectZombie(self):
        return self.rectZombie
    def getHealth(self):
        return self.ZombieHealth
    def Die(self):
        self.ZombieHealth -= 1
    def update(self,x,y):
        self.mouse_x = x
        self.mouse_y = y
        self.degrees =  getAngle(self.x,self.y,self.mouse_x,self.mouse_y)
        self.y -= 2*(math.sin(self.degrees))
        self.x += 2*(math.cos(self.degrees))
        self.rectZombie = pygame.Rect(self.x,self.y,self.width,self.height)
    
    def rotate(self,mouse_x,mouse_y):
        MouseAngle = (360- math.atan2(self.y - mouse_y,self.x - mouse_x)) * (180 / math.pi)
        self.image = pygame.transform.rotate(self.original,MouseAngle)
    
def getAngle(x1, y1, x2, y2):
        # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
        rise = y2 - y1+0.001
        run = x2 - x1+0.001
        angle = math.atan2(rise, run)
        return angle *(-1)