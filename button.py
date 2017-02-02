import pygame
import sys

class Button(object):
    def __init__(self):
        self.x = 200
        self.y = 200

    def draw(self):
        screen.fill((0, 255, 0), (200, 200, 200, 200))
        screen.fill((0, 255, 0), (600, 200, 200 ,200))

    def destroy(self):
        screen.fill((0, 0, 0), (self.x, self.y, 200, 200))

class Controller(object):
    def control_event(self, button):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and ((200, 200) < pygame.mouse.get_pos() < (400, 400)):
                button.destroy()

#setup
pygame.init()
screen = pygame.display.set_mode((1080, 1080))
screen.fill((0, 0, 0))

controller = Controller()

button = Button()
button.draw()

while True:
    controller.control_event(button)
    FPS_CLOCK = pygame.time.Clock()
    pygame.display.update() #Draws Surface object to screen
    FPS_CLOCK.tick(60)
