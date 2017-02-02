#! /usr/bin/env python3
import sys
import pygame
from pygame.locals import *
from classes.Player import *
from classes.Enemy import *
from classes.Bullet import *
from classes.Menu import *

def menu(display):
    m = Menu()
    m.draw(display)
    pygame.display.update() # Draws Surface object to screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and ((200, 200) < pygame.mouse.get_pos() < (400, 400)):
                m.destroy(display)
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN and ((600, 200) < pygame.mouse.get_pos() < (800, 400)):
                m.destroy(display)
                return 0

def score(display, player):
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    score_text = fontObj.render('Score: ' + str(player.score), True, (0, 255, 0), (0, 0, 0))
    text_rect = score_text.get_rect()
    text_rect.center = (1000, 1000)
    display.blit(score_text, text_rect)

def initialise_game():
    pygame.init()
    pygame.key.set_repeat(500, 30)
    pygame.display.set_caption("Spacegame")
    return pygame.display.set_mode((1080, 1080)) # Takes a tuple as input

def start(display):
    ## INIT_OBJECTS
    player_img = "assets/player_ship.png"
    enemy_img = "assets/ship.png"
    bullet = False
    fired_bullets = []
    on_screen_enemies = 1
    enemy_exists = True
    turn_timer = 0
    enemy_list = [Enemy(enemy_img, display) for i in range(on_screen_enemies)]
    player = Player(player_img, display)
    FPS = 60
    FPS_CLOCK = pygame.time.Clock()

    ## Game loop
    while True:
        display.fill((0, 0, 0))
        if turn_timer > 250:
            on_screen_enemies += 1
            for e in [Enemy(enemy_img, display) for i in range(on_screen_enemies)]:
                enemy_list.append(e)
            print(enemy_list)
            turn_timer = 0
        for e in enemy_list:
            e.y += 0.5
            e.draw()
        if bullet == True: # If bullet has been fired, draw it and assess whether it hits the target or not
            for b in fired_bullets:
                b.draw(10) # param = rate of change in y-coordinate
                for e in enemy_list:
                    if e.hit(b, player) == 1:
                        enemy_list.remove(e)
        player.draw()
        score(display, player)

        for event in pygame.event.get(): # Checks what events have been created
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit() # Opposite of pygame.init()
                sys.exit()
            elif (event.type == KEYDOWN and event.key == K_a):
                player.x -= 25
            elif (event.type == KEYDOWN and event.key == K_d):
                player.x += 25
            elif (event.type == KEYDOWN and event.key == K_SPACE):
                fired_bullets.append(player.fire())
                bullet = True

        turn_timer += 1
        pygame.display.update() # Draws Surface object to screen
        FPS_CLOCK.tick(FPS)

if __name__ == "__main__":
    display = initialise_game()
    result = menu(display)
    if result == 1:
        start(display)
    elif result == 0:
        pygame.quit() # Opposite of pygame.init()
        sys.exit()
