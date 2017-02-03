import pygame
from pygame.locals import *
from random import randrange
from classes.Entity import *

class Enemy(Entity):
    def __init__(self, path, display):
        super().__init__(display, randrange(800), randrange(200))
        self.ship_img = pygame.image.load(path)
        self.image = self.ship_img
        self.alive = True
        self.rect = self.image.get_rect()

    def draw(self):
        self.display.blit(self.image, (self.x, self.y)) #blit() draws one surface object onto another - place_to.blit(source, (x-, y-tuple))
        self.rect.x = self.x
        self.rect.y = self.y

    def hit(self, bullet, player):
        if self.alive == True and bullet.success_hit == False and bullet.y <= self.y + 100 and (self.x - 200 <= bullet.x <= self.x + 200):
            bullet.success_hit = True
            bullet.destroy()
            self.death(bullet, player)
            return 1

    def fire(self):
        b = Bullet(self, self.display)
        return b

    def death(self, bullet, player):
        self.image.fill((0, 0 ,0))
        player.score += 1
        self.alive = False
