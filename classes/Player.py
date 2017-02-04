import pygame
from pygame.locals import *
from classes.Bullet import *
from classes.Entity import *

class Player(Entity):
    def __init__(self, path, display):
        super().__init__(display, 500, 800, "Player")
        self.player_ship = pygame.image.load(path)
        self.health = 3
        self.score = 0

    def draw(self):
        #blit() draws one surface object onto another - place_to.blit(source, (x-, y-tuple))
        self.display.blit(self.player_ship, (self.x, self.y))

    def fire(self):
        b = Bullet(self.display, self)
        return b

    def hit(self, bullet):
        if bullet.shooter_type == "Enemy":
            if self.health > 0 and bullet.success_hit == False and bullet.y >= self.y + 10 and ((self.x + 25) <= bullet.x <= (self.x + 25) + 200):
                bullet.success_hit = True
                bullet.destroy()
                self.health -= 1
                return "hit"
            elif self.health < 1 and bullet.success_hit == False and bullet.y >= self.y + 10 and ((self.x + 25) <= bullet.x <= (self.x + 25) + 200):
                bullet.success_hit = True
                bullet.destroy()
                self.death()
                return "dead"

    def death(self):
        self.player_ship.fill((0, 0 ,0))
