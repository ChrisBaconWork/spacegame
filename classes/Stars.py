import pygame
import random

class Stars:
    def __init__(self, width, height):
        self.x = random.randrange(0, width)
        self.y = random.uniform(0, height)
        self.size = random.randrange(1, 5)
        self.movement = random.uniform(0.10, 0.25)

    def draw(self, display):
        self.y += self.movement
        pygame.draw.circle(display, (255, 255, 255), (self.x, int(self.y)), self.size)
