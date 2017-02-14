import pygame
from pygame.locals import *
from random import randrange
from classes.Entity import *
from classes.Bullet import *

class Enemy(Entity):
    def __init__(self, path, display):
        super().__init__(display,
                        x = randrange(800),
                        y = randrange(200),
                        type_entity = "Enemy",
                        health = 1,
                        img = pygame.image.load(path))
        self.load_weapons = 100
        self.speed = 0.5

    def get_hitbox(self):
        """This method returns the current hitbox"""
        self.hitbox = [self.y + 130, self.x, self.x + 240]

    def draw(self):
        self.y += self.speed
        self.display.blit(self.img, (self.x, self.y))

    def hit(self, bullet, player):
        """Determine whether the enemy has been successfully hit"""
        self.get_hitbox()
        if bullet.success_hit == False and bullet.y <= self.hitbox[0] and (self.hitbox[1] <= bullet.x <= self.hitbox[2]):
            if bullet.shooter_type == "Player":
                bullet.success_hit = True
                bullet.destroy()
                self.health -= 1
                if self.health < 1:
                    player.score += 1
                    self.death()
                    return "dead"
                return "hit"

    def fire(self):
        b = Bullet(self.display, self)
        return b
