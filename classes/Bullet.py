import pygame
from pygame.locals import *
from classes.Entity import *

class Bullet(Entity):
    def __init__(self, display, shooter):
        self.shooter_type = shooter.type_entity
        if self.shooter_type == "Player":
            self.bX = shooter.x + 125
            self.bY = shooter.y - 35
        elif self.shooter_type == "Enemy":
            self.bX = shooter.x + 110
            self.bY = shooter.y + 160
        super().__init__(display, self.bX, self.bY, "Bullet")
        self.y_change = 0
        self.success_hit = False

    def draw(self, y_rate):
        # y_rate is the rate of change on the y-axis
        colour = {"Player": (0, 255, 0), "Enemy": (255, 0, 0)}
        if self.shooter_type == "Player":
            self.y = self.y - y_rate
        elif self.shooter_type == "Enemy":
            self.y = self.y + y_rate
        pygame.draw.rect(self.display, colour[self.shooter_type], (self.x, self.y, 10, 40))

    def destroy(self):
        pygame.draw.rect(self.display, (0, 0, 0), (self.x, self.y, 10, 40))
