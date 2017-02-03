import pygame
from pygame.locals import *
from classes.Entity import *

class Bullet(Entity):
    def __init__(self, player, display):
        self.bX = player.x + 125
        self.bY = player.y - 35
        super().__init__(display, self.bX, self.bY)
        self.y_change = 0
        self.success_hit = False

    def draw(self, y_rate): #y_rate is the rate of change on the y-axis
        self.y = self.y - y_rate
        if self.success_hit == False:
            pygame.draw.rect(self.display, (0, 255, 0), (self.x, self.y, 10, 40))

    def destroy(self):
        pygame.draw.rect(self.display, (0, 0, 0), (self.x, self.y, 10, 40))
