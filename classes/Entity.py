import pygame

class Entity(object):
    def __init__(self, display, x, y):
        self.display = display # Set up the display that all subclasses will use
        self.x = x # x co-ordinate
        self.y = y # y co-ordinate
