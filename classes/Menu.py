import pygame

class Menu(object):
    def __init__(self, display, settings):
        self.colour = {"unclicked": (68, 22, 34), "clicked": (138, 71, 71)}
        self.display = display
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.resolution = settings.settings["Resolution"]

    def title(self):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 42)
        start = self.fontObj.render('SPACEGAME...', True, (0, 255, 0), (0, 0, 0))
        start_rect = start.get_rect(center = (self.resolution["X"] / 2, 100))
        self.display.blit(start, start_rect)

    def start_button(self, clicked="unclicked"):
        X = 200
        Y = 200
        self.display.fill(self.colour[clicked], (X, Y, 200, 200))
        start = self.fontObj.render('START', True, (255, 255, 255), self.colour[clicked])
        start_rect = start.get_rect(center = (300, 300))
        self.display.blit(start, start_rect)

    def quit_button(self, clicked="unclicked"):
        X = 600
        Y = 200
        self.display.fill(self.colour[clicked], (X, Y, 200, 200))
        quit = self.fontObj.render('Quit', True, (255, 255, 255), self.colour[clicked])
        quit_rect = quit.get_rect(center = (700, 300))
        self.display.blit(quit, quit_rect)

    def toggle_music_button(self, clicked="unclicked"):
        X = 400
        Y = 600
        self.display.fill(self.colour[clicked], (X, Y, 200, 200))
        toggle_music = self.fontObj.render('Music', True, (255, 255, 255), self.colour[clicked])
        toggle_music_rect = toggle_music.get_rect(center = (500, 700))
        self.display.blit(toggle_music, toggle_music_rect)

    def draw(self, start="unclicked", quit="unclicked", toggle_music="unclicked"):
        self.title()
        self.start_button(start)
        self.quit_button(quit)
        self.toggle_music_button(toggle_music)

    def destroy(self, display):
        display.fill((0, 0, 0), (200, 200, 200, 200))
        display.fill((0, 0, 0), (600, 200, 200 ,200))
