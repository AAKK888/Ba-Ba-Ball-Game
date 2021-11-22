import random
import pygame
import time
from ball import *
from player import *
import vari
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
score = 0
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((vari.WIDTH, vari.HEIGHT))
pygame.display.set_caption("Ba-Ba-Ball Game (Help from KidsCanCode)")
clock = pygame.time.Clock()


font_name = pygame.font.match_font('arial')


def draw_text(text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, vari.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


def show_go_screen():
    screen.fill(vari.BLUE)
    draw_text("Ba-Ba-Ball Game!", 64, vari.WIDTH / 2, vari.HEIGHT / 4)
    draw_text("Press a key to begin", 18, vari.WIDTH / 2, vari.HEIGHT * 5 / 6)
    draw_text("Controls are WASD and arrow keys", 18, vari.WIDTH / 2, vari.HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True

    while waiting:
        clock.tick(vari.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                time.sleep(0.2)
                waiting = False


timer = 0
# Game loop
running = True
game_over = True
while running:
    if game_over:
        print(score)
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        ballgroup = pygame.sprite.Group()
        umpha = BallSpeed(15, 15)
        ball = Ball(9, 9)
        ball2 = Ball(2, 2)
        ball3 = Ball(2, 1)
        ball4 = Ball(1, 2)
        ball5 = Ball(1, 3)
        ball6 = Ball(3, 1)
        ball7 = Ball(3, 1)
        ball8 = Ball(1, 3)
        ball9 = Ball(1, 4)
        ball10 = Ball(4, 1)
        ball11 = Ball(4, 4)
        ball12 = Ball(6, 6)
        playerthing = Player()
        all_sprites.add(ball)
        all_sprites.add(ball2)
        all_sprites.add(ball3)
        all_sprites.add(ball4)
        all_sprites.add(ball5)
        all_sprites.add(ball6)
        all_sprites.add(ball7)
        all_sprites.add(ball8)
        all_sprites.add(ball9)
        all_sprites.add(ball10)
        all_sprites.add(ball11)
        all_sprites.add(ball12)

        all_sprites.add(playerthing)
        all_sprites.add(umpha)

        ballgroup.add(umpha)
        ballgroup.add(ball)
        ballgroup.add(ball2)
        ballgroup.add(ball3)
        ballgroup.add(ball4)
        ballgroup.add(ball5)
        ballgroup.add(ball6)
        ballgroup.add(ball7)
        ballgroup.add(ball8)
        ballgroup.add(ball9)
        ballgroup.add(ball10)
        ballgroup.add(ball11)
        ballgroup.add(ball12)

        score = 0
    # keep loop running at the desired speed
    clock.tick(vari.FPS)

    score = float(score)
    score += 0.5
    score = str(score)

    # 1. process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # 2. Update
    all_sprites.update()
    pygame.display.update()
    collide = pygame.sprite.spritecollide(playerthing, ballgroup, True)
    if collide:
        game_over = True

    # 3. Draw / render
    screen.fill(vari.ORANGE)
    all_sprites.draw(screen)
    draw_text(score, 40, 100, 20)
    score = float(score)

    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
