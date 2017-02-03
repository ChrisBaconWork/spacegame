import pygame
from pygame.locals import *
from random import randrange
from classes.Entity import *
from classes.Bullet import *

class Enemy(Entity):
    def __init__(self, path, display):
        super().__init__(display, randrange(800), randrange(200), "Enemy")
        self.ship_img = pygame.image.load(path)
        self.rect = self.ship_img.get_rect()
        self.load_weapons = 100

    def draw(self):
        #blit() draws one surface object onto another - place_to.blit(source, (x-, y-tuple))
        self.display.blit(self.ship_img, (self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y

    def hit(self, bullet, player):
        if bullet.success_hit == False and bullet.y <= self.y + 100 and (self.x - 200 <= bullet.x <= self.x + 200):
            if bullet.shooter_type == "Player":
                bullet.success_hit = True
                bullet.destroy()
                player.score += 1
                self.death()
                return 1

    def fire(self):
        b = Bullet(self.display, self)
        return b

    def death(self):
        self.ship_img.fill((0, 0 ,0))
