import pygame
import math
from pygame.locals import *


class Bullet(object):
   
    def __init__(self,pos,mousex,mousey,height=3,width=3):
        (self.x, self.y) = pos
        self.mouse_x = mousex
        self.mouse_y = mousey
        self.width= 1
        self.height= 1
        self.image = pygame.image.load("res/bullet.png")
        self.rectPlayer=pygame.Rect(self.x,self.y,self.width,self.height)
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
    
    def rotate(self,mouse_x,mouse_y):
        MouseAngle = (360- math.atan2(self.y - mouse_y,self.x - mouse_x)) * (180 / math.pi)
        self.image = pygame.transform.rotate(self.image,MouseAngle)
    
def getAngle(x1, y1, x2, y2):
        # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
        rise = y2 - y1+0.001
        run = x2 - x1+0.001
        angle = math.atan2(rise, run) # get the angle in radians
        # angle = angle * (math.pi / 180) # convert to degrees
        # angle = (angle ) % 360 # adjust for a right-facing sprite
        return angle *(-1)