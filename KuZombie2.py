import pygame
import sys
from pygame.locals import *
from pygame import *
import random
import math
import gamelib
import time

from Player import *
from Bullet import *
from Zombie import *
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = ( 120, 0, 0)
BLUE = ( 0, 0, 255)

class KuZombie2(gamelib.ZombieGame):
    WHITE = pygame.Color('white')
    def __init__(self):
    	super(KuZombie2, self).__init__('You Gonna Die!!', RED)
        self.player = player(pos=(self.window_size[0]/2,self.window_size[1]/2),color=RED)
        self.setTimeIntervalBullet = 0
        self.setTimeIntervalZombie = 0
        self.score = 0
        self.GameOver = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.Bullets = []
        self.Zombies = []

    
    def init(self):
        super(KuZombie2, self).init()
        self.render_score()
        pygame.mixer.music.load('res/ZombieAppear.wav')
        pygame.mixer.music.play()

    
    def update(self):
        if not(self.GameOver):
            self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
            self.player.rotate(self.mouse_x,self.mouse_y)
            self.player.update()
            self.render_score()
            self.updateBullet()
            self.updateZombie()
            self.checkCollisionBullet()
            self.checkCollisionPlayer()
            if self.is_key_pressed(K_w):
                self.player.move_up()
            elif self.is_key_pressed(K_s):
                self.player.move_down()
            elif self.is_key_pressed(K_a):
                self.player.move_left()
            elif self.is_key_pressed(K_d):
                self.player.move_right()
            

    def addBullet(self):    
        mouse_x,mouse_y = pygame.mouse.get_pos()
        self.Bullets += [Bullet(pos = (self.player.getX(),self.player.getY()),mousex = mouse_x,mousey = mouse_y)]    
    
    def renderBullet(self, surface):
        for Bullet in self.Bullets :
            Bullet.render(surface)

    def updateBullet(self):
        deltatime = pygame.time.get_ticks() / 100
        if deltatime > self.setTimeIntervalBullet :
            self.setTimeIntervalBullet = deltatime

        for x in range(len(self.Bullets), deltatime - len(self.Bullets)) :
            if  self.is_key_pressed(K_SPACE):
                pygame.mixer.music.load('res/GUN_FIRE.wav')
                pygame.mixer.music.play(0)
                self.addBullet()
        for Bullet in self.Bullets :
            Bullet.update()
            if (0<Bullet.getY<600) or (0<Bullet.getX<1080):
                self.Bullets.remove(Bullet)

    def addZombie(self):    
        mouse_x,mouse_y = pygame.mouse.get_pos()
        self.Zombies += [Zombie(mousex = self.player.getX(),mousey = self.player.getY(),health = 2)]    
    
    def renderZombie(self, surface):
        for Zombie in self.Zombies :
            Zombie.render(surface)

    def updateZombie(self):
        deltatime = pygame.time.get_ticks() / 200
        if deltatime > self.setTimeIntervalZombie :
            self.setTimeIntervalZombie = deltatime

        for x in range(len(self.Zombies), deltatime - len(self.Zombies)) :
                self.addZombie()
        for Zombie in self.Zombies :
            Zombie.rotate(self.player.getX(),self.player.getY())
            Zombie.update(x = self.player.getX(),y = self.player.getY())
    
    def checkCollisionBullet(self):
        for Bullet in self.Bullets [:]:
            for Zombie in self.Zombies[:]:
                if(Bullet.getrectBullet().colliderect(Zombie.getrectZombie())) :
                    try:
                        self.Bullets.remove(Bullet)
                        self.Zombies.remove(Zombie)
                        self.score += 1
                    except ValueError:
                        pass
    def checkCollisionPlayer(self):
        for Zombie in self.Zombies:
            if(Zombie.getrectZombie().colliderect(self.player.getRectPlayer())):
                self.GameOver = True
                pygame.mixer.music.load('res/Torture.wav')
                pygame.mixer.music.play(-1)

    def render_score(self):
        self.score_image = self.font.render("Killed = %d" % self.score, 0,KuZombie2.WHITE)
        print self.score

    def render(self, surface):
        self.player.render(surface)
        self.renderBullet(surface)
        self.renderZombie(surface)
        mouse_x,mouse_y = pygame.mouse.get_pos()
        self.player.rotate(mouse_x,mouse_y)
        surface.blit(self.score_image, (10,10))
        if self.GameOver == True :
            self.GameOver_image = self.font.render("Game Over!!!", 0,KuZombie2.WHITE)
            surface.blit(self.GameOver_image,(500,300))


def main():
    game = KuZombie2()
    game.run()
if __name__ == '__main__':
    main()