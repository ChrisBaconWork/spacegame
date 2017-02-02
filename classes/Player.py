import pygame
from pygame.locals import *
from classes.Bullet import *
from classes.Entity import *

class Player(Entity):
    def __init__(self, path, display):
        super().__init__(display, 500, 800)
        self.player_ship = pygame.image.load(path)
        self.health = 3
        self.score = 0

    def draw(self):
        self.display.blit(self.player_ship, (self.x, self.y)) #blit() draws one surface object onto another - place_to.blit(source, (x-, y-tuple))

    def fire(self):
        b = Bullet(self, self.display)
        return b
