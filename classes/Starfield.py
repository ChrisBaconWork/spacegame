import pygame
import random

class Starfield:
    def __init__(self, width, height):
        self.x = random.randrange(0, width)
        self.y = random.uniform(0, height)
        self.z = random.randrange(1, 3)
        self.size = random.randrange(1, 5)
        self.movement = random.uniform(0.25, 0.5)

    def draw(self, display, centre):
        xrate = ((self.x - centre[0]) * self.z) / 200
        yrate = ((self.y - centre[1]) * self.z) / 200

        self.x = self.x + xrate
        self.y = self.y + yrate

        pygame.draw.circle(display, (255, 255, 255), (int(self.x), int(self.y)), self.size)
