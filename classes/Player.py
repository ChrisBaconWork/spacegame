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

    def get_hitbox(self):
        # This is horrible, but better than before - hitbox: bullet between [y, x-left, and x-right]
        self.hitbox = [self.y + 10, self.x, self.x + 240]

    def draw(self):
        #blit() draws one surface object onto another - place_to.blit(source, (x-, y-tuple))
        self.display.blit(self.player_ship, (self.x, self.y))

    def fire(self):
        b = Bullet(self.display, self)
        return b

    def hit(self, bullet):
        if bullet.shooter_type == "Enemy":
            self.get_hitbox()
            if self.health > 0 and bullet.success_hit == False and bullet.y >= self.hitbox[0] and (self.hitbox[1] <= bullet.x <= self.hitbox[2]):
                bullet.success_hit = True
                bullet.destroy()
                self.health -= 1
                return "hit"
            elif self.health < 1 and bullet.success_hit == False and bullet.y >= self.hitbox[0] and (self.hitbox[1] <= bullet.x <= self.hitbox[2]):
                bullet.success_hit = True
                bullet.destroy()
                self.death()
                return "dead"

    def death(self):
        self.player_ship.fill((0, 0 ,0))
