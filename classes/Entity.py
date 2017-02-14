import pygame

class Entity(object):
    """This class is the basis of all others, and contains all fundamental properties"""
    def __init__(self, display, x, y, type_entity, health, img):
        # Set up the display that all subclasses will use
        self.display = display
        self.type_entity = type_entity
        # x and y co-ordinates
        self.x = x
        self.y = y
        if self.x > 500:
            # The world is a torus
            self.x = 0 + (self.x - 1080)
        self.health = health
        self.img = img

    def death(self):
        """Death comes to all things"""
        self.img.fill((0, 0 ,0))
