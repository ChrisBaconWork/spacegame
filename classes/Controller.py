import pygame
from pygame.locals import *
import sys

class Controller(object):
    """This is the event controller"""
    def __init__(self, display):
        self.display = display

    def control_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    def control_menu(self, m):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and ((200, 200) < pygame.mouse.get_pos() < (400, 400)):
                m.destroy(self.display)
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN and ((600, 200) < pygame.mouse.get_pos() < (800, 400)):
                m.destroy(self.display)
                return 0
