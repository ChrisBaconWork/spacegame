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
        self.colour = {"Player": (0, 255, 0), "Enemy": (255, 0, 0)}
        self.bullet_speed = {"Player": 10, "Enemy": 7}

    def draw(self):
        """Draw the bullet and set the speed, in pixels"""
        if self.shooter_type == "Player":
            self.y = self.y - self.bullet_speed["Player"]
        elif self.shooter_type == "Enemy":
            self.y = self.y + self.bullet_speed["Enemy"]
        pygame.draw.rect(self.display, self.colour[self.shooter_type], (self.x, self.y, 10, 40))

    def destroy(self):
        pygame.draw.rect(self.display, (0, 0, 0), (self.x, self.y, 10, 40))
