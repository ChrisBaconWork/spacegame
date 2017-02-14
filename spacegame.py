#! /usr/bin/env python3
import sys
import pygame
import json
from pygame.locals import *
from classes.Player import *
from classes.Enemy import *
from classes.Bullet import *
from classes.Menu import *
from classes.Settings import *

def terminate():
    pygame.quit()
    sys.exit()

def menu(display, settings):
    """This function creates a menu object, watches for input, and then returns an int based on the input"""
    if settings.settings["Music"] == "On":
        pygame.mixer.music.load('assets/main_menu.wav')
        # params: -1 plays the music indefinitely; 5 plays it once and then loops 5 times = 6 times
        pygame.mixer.music.play(-1)
    m = Menu(display, settings)
    m.draw()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and ((200, 200) < pygame.mouse.get_pos() < (400, 400)):
                m.destroy(display)
                m.draw("clicked", "unclicked")
                pygame.display.update()
                pygame.time.delay(750)
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN and ((600, 200) < pygame.mouse.get_pos() < (800, 400)):
                m.destroy(display)
                m.draw("unclicked", "clicked")
                pygame.display.update()
                return 0

def draw_text(display, player):
    """This function displays the score and player health"""
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    score_text = fontObj.render('Score: ' + str(player.score), True, (0, 255, 0), (0, 0, 0))
    text_rect = score_text.get_rect(center = (1000, 1000))
    display.blit(score_text, text_rect)

    health_text = fontObj.render('Health: ' + str(player.health), True, (0, 255, 0), (0, 0, 0))
    text_rect = health_text.get_rect(center = (1000, 960))
    display.blit(health_text, text_rect)

def initialise_game():
    """This function initialises the game"""
    pygame.init()
    pygame.key.set_repeat(250, 30)
    pygame.display.set_caption("Spacegame")
    settings = Settings()
    return settings, pygame.display.set_mode((settings.settings["Resolution"]["X"], settings.settings["Resolution"]["Y"]))

def create_boss(boss_img, display):
    boss = Enemy(boss_img, display)
    boss.health = 5
    boss.draw()
    return boss

def end_game(display, settings, player):
    """This function creates the end game screen and controls restart logic"""
    display.fill((0, 0, 0))

    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    score_text = fontObj.render('GAME OVER... Your Score: ' + str(player.score), True, (0, 255, 0), (0, 0, 0))
    text_rect = score_text.get_rect(center = (settings.settings["Resolution"]["X"] / 2, settings.settings["Resolution"]["Y"] / 2))
    display.blit(score_text, text_rect)

    display.fill((68, 22, 34), ((1080 / 2) - 100, 700, 200, 200))
    start = fontObj.render('RESTART', True, (255, 255, 255), (68, 22, 34))
    start_rect = start.get_rect(center = (settings.settings["Resolution"]["X"] / 2, 800))
    display.blit(start, start_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and (((settings.settings["Resolution"]["X"] / 2) - 100, 700) < pygame.mouse.get_pos() < ((1080 / 2) + 100, 900)):
                return 1

def start(display, settings):
    """This is the main body of the game logic"""
    # Initialise objects
    if settings.settings["Music"] == "On":
        pygame.mixer.music.load('assets/main_game.wav')
        pygame.mixer.music.play(-1)
    player_img, enemy_img, capital_ship_img = "assets/player_ship.png",  "assets/alienship.png", "assets/capital_ship.png"
    bullet, fired_bullets, on_screen_enemies, turn_timer = False, [], 1, 0
    enemy_list = [Enemy(enemy_img, display) for i in range(on_screen_enemies)]
    player = Player(player_img, display)
    FPS, FPS_CLOCK = settings.settings["Framerate"], pygame.time.Clock()

    boss_alive = False

    # Game loop
    while True:
        display.fill((0, 0, 0))
        if turn_timer > 500:
            on_screen_enemies += 1
            for e in [Enemy(enemy_img, display) for i in range(on_screen_enemies)]:
                enemy_list.append(e)
            turn_timer = 0
        for e in enemy_list:
            e.draw()
            if e.load_weapons < 1:
                e.load_weapons = 100
                fired_bullets.append(e.fire())
            e.load_weapons -= 1

        # If bullet has been fired, draw it and assess whether it hits the target or not
        for b in fired_bullets:
            # Remove the bullets at the bottom so you don't move into them
            if b.y > 1080:
                fired_bullets.remove(b)
            b.draw()
            player_status = player.hit(b)
            if player_status == "hit":
                # Handle edge case where bullet goes off screen but still has causal power
                try:
                    fired_bullets.remove(b)
                except:
                    pass
            elif player_status == "dead":
                try:
                    fired_bullets.remove(b)
                except:
                    pass
                # End game
                return True, player
            for e in enemy_list:
                hit_result = e.hit(b, player)
                if hit_result == "dead":
                    fired_bullets.remove(b)
                    enemy_list.remove(e)
                elif hit_result == "hit":
                    fired_bullets.remove(b)

        player.draw()
        draw_text(display, player)

        if player.score > 0 and boss_alive == False:
            boss_alive = True
            enemy_list.append(create_boss(capital_ship_img, display))

        # Checks what events have been created and takes them off the queue
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                terminate()
            elif (event.type == KEYDOWN and event.key == K_a):
                player.x -= 25
            elif (event.type == KEYDOWN and event.key == K_d):
                player.x += 25
            elif (event.type == KEYDOWN and event.key == K_SPACE):
                fired_bullets.append(player.fire())

        turn_timer += 1
        # update() draws Surface object to screen
        pygame.display.update()
        FPS_CLOCK.tick(FPS)

def main():
    """This function ties the game together recursively"""
    settings, display = initialise_game()
    result = menu(display, settings)
    if result == 1:
        game_over, player = start(display, settings)
    elif result == 0:
        terminate()
    if game_over:
        if end_game(display, settings, player):
            main()

if __name__ == "__main__":
    main()
