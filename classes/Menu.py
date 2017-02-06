import pygame

class Menu(object):
    def __init__(self, display):
        self.colour = {"unclicked": (68, 22, 34), "clicked": (138, 71, 71)}
        self.display = display
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)

    def start_button(self, clicked="unclicked"):
        self.display.fill(self.colour[clicked], (200, 200, 200, 200))
        start = self.fontObj.render('START', True, (255, 255, 255), self.colour[clicked])
        start_rect = start.get_rect(center = (300, 300))
        self.display.blit(start, start_rect)

    def quit_button(self, clicked="unclicked"):
        self.display.fill(self.colour[clicked], (600, 200, 200, 200))
        quit = self.fontObj.render('Quit', True, (255, 255, 255), self.colour[clicked])
        quit_rect = quit.get_rect(center = (700, 300))
        self.display.blit(quit, quit_rect)

    def draw(self, start="unclicked", quit="unclicked"):
        self.start_button(start)
        self.quit_button(quit)

    def destroy(self, display):
        display.fill((0, 0, 0), (200, 200, 200, 200))
        display.fill((0, 0, 0), (600, 200, 200 ,200))
