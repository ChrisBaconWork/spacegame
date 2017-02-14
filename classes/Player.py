import pygame
from pygame.locals import *
from classes.Bullet import *
from classes.Entity import *

class Player(Entity):
    def __init__(self, path, display):
        super().__init__(display,
                        x = 500,
                        y = 750,
                        type_entity = "Player",
                        health = 5,
                        img = pygame.image.load(path))
        self.score = 0

    def get_hitbox(self):
        """This method returns the current hitbox"""
        self.hitbox = [self.y + 10, self.x, self.x + 240]

    def draw(self):
        """The world is a torus"""
        if self.x > 1080:
            self.x = 0 + (self.x - 1080)
        elif self.x < 0:
            self.x = 1080 - (0 - self.x)
            #blit() draws one surface object onto another - place_to.blit(source, (x-, y-tuple))
        self.display.blit(self.img, (self.x, self.y))

    def fire(self):
        b = Bullet(self.display, self)
        return b

    def hit(self, bullet):
        """Determine whether the player has been successfully hit"""
        if bullet.shooter_type == "Enemy":
            self.get_hitbox()
            if bullet.success_hit == False and bullet.y >= self.hitbox[0] and (self.hitbox[1] <= bullet.x <= self.hitbox[2]):
                bullet.success_hit = True
                bullet.destroy()
                self.health -= 1
                if self.health < 1:
                    self.death()
                    return "dead"
                return "hit"
