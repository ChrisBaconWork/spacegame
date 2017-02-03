import pygame

class Entity(object):
    """This class is the basis of all others, and contains all fundamental properties"""
    def __init__(self, display, x, y, type_entity):
        # Set up the display that all subclasses will use
        self.display = display
        self.type_entity = type_entity
        # x and y co-ordinates
        self.x = x
        self.y = y
