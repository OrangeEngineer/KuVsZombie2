import pygame
import math
from pygame.locals import *


class Bullet(object):
   
    def __init__(self,pos,mousex,mousey,height=5,width=5):
        (self.x, self.y) = pos
        self.mouse_x = mousex
        self.mouse_y = mousey
        self.width= height
        self.height= width
        self.image = pygame.image.load("res/bullet.png")
        self.rectBullet=pygame.Rect(self.x,self.y,self.width,self.height)
        self.rotate(self.mouse_x,self.mouse_y)
        self.shoot = False
        self.degrees =  getAngle(self.x,self.y,mousex,mousey)

    def render(self,surface):
        pos = (int(self.x),int(self.y))
        surface.blit(self.image,pos)
    
    def getX(self):
		return self.x
    
    def getY(self):
		return self.y
		
    def update(self):
        self.y -= 60*(math.sin(self.degrees))
        self.x += 60*(math.cos(self.degrees))
        self.rectBullet=pygame.Rect(self.x,self.y,self.width,self.height)

    
    def rotate(self,mouse_x,mouse_y):
        MouseAngle = (360- math.atan2(self.y - mouse_y,self.x - mouse_x)) * (180 / math.pi)
        self.image = pygame.transform.rotate(self.image,MouseAngle)
    
    def getrectBullet(self):
        return self.rectBullet

def getAngle(x1, y1, x2, y2):
        rise = y2 - y1+0.001
        run = x2 - x1+0.001
        angle = math.atan2(rise, run)
        return angle *(-1)