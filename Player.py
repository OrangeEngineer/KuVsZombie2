import pygame
import math
from pygame.locals import *


class player(object):
   
    def __init__(self,color,pos,heroheight=16,herowidth=16):
        (self.x, self.y) = pos
        self.width= 20
        self.height= 20
        self.image = pygame.image.load("res/Player.png")
        self.original=self.image
        self.image = pygame.transform.rotate(self.image,30)
        self.rectPlayer=pygame.Rect(self.x,self.y,self.width,self.height)
        

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5
    def render(self,surface):
		pos = (int(self.x),int(self.y))
		surface.blit(self.image,pos)
    
    def getX(self):
		return self.x
    def getY(self):
		return self.y
		
    def update(self):
        self.rectPlayer=pygame.Rect(self.x,self.y,self.width,self.height)


    def rotate(self,mouse_x,mouse_y):
    	MouseAngle = (360- math.atan2(self.y - mouse_y,self.x - mouse_x)) * (180 / math.pi)
        self.image = pygame.transform.rotate(self.original,MouseAngle)
	


