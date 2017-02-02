import pygame

class Menu(object):
    def __init__(self):
        self.button_colour = (68, 22, 34)

    def draw(self, display):
        display.fill(self.button_colour, (200, 200, 200, 200))
        display.fill(self.button_colour, (600, 200, 200, 200))
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        start = fontObj.render('START', True, (255, 255, 255), self.button_colour)
        quit = fontObj.render('Quit', True, (255, 255, 255), self.button_colour)
        start_rect = start.get_rect()
        quit_rect = start.get_rect()

        start_rect.center = (300, 300)
        quit_rect.center = (700, 300)

        display.blit(start, start_rect)
        display.blit(quit, quit_rect)

    def destroy(self, display):
        display.fill((0, 0, 0), (200, 200, 200, 200))
        display.fill((0, 0, 0), (600, 200, 200 ,200))
