import random
import pygame
import time
from ball import *
from player import *
import t
from os import path
from Obsticles import *
img_dir = path.join(path.dirname(__file__), 'img')
score = 0
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((t.WIDTH, t.HEIGHT))
pygame.display.set_caption("Ba-Ba-Ball Game (Help from KidsCanCode)")
clock = pygame.time.Clock()
highscore = 0
diry = path.dirname(__file__)
with open(path.join(diry, t.SCORE_FILE), 'w') as f:
    try:
        global highscoreread
        highscoreread = int(f.read())

    except:
        highscoreread = 2090

newscore = highscoreread
font_name = pygame.font.match_font('arial')


def draw_text(text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, t.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


def show_go_screen(highscoreread = newscore):
    screen.fill(t.BLUE)
    draw_text("Ba-Ba-Ball Game!", 64, t.WIDTH / 2, t.HEIGHT / 4)
    draw_text("Press space to begin", 18, t.WIDTH / 2, t.HEIGHT * 5 / 6)
    draw_text("Controls are WASD and arrow keys", 18, t.WIDTH / 2, t.HEIGHT * 3 / 4)
    if score > highscoreread:
        draw_text("NEW HIGH SCORE!", 22,  t.WIDTH / 2, t.HEIGHT * 1 / 8)
        with open(path.join(diry, t.SCORE_FILE), 'w') as f:
            f.write(str(score))
        highscoreread = score

    else:
        draw_text(" Score: " + str(score), 22,  t.WIDTH / 2, t.HEIGHT * 1 / 8)

    pygame.display.flip()
    waiting = True

    while waiting:
        clock.tick(t.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keypress = pygame.key.get_pressed()
            if keypress[pygame.K_SPACE]:
                time.sleep(0.2)
                waiting = False


randomcolor = (t.WHITE, t.YELLOW, t.BLUE)
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
        umphagroup = pygame.sprite.Group()
        umpha = BallSpeed(16, 16)
        umpha2 = BallSpeed(18, 18)
        ball = Ball(10, 10)
        ball2 = Ball(4, 4)
        ball9 = Ball(3, 5)
        ball10 = Ball(5, 3)
        ball11 = Ball(5, 5)
        ball12 = Ball(8, 8)
        obsticle = Obsticle()
        obsticle2 = Obsticle()
        playerthing = Player()
        all_sprites.add(ball)
        all_sprites.add(ball2)
        all_sprites.add(ball9)
        all_sprites.add(ball10)
        all_sprites.add(ball11)
        all_sprites.add(ball12)

        all_sprites.add(playerthing)
        all_sprites.add(umpha)
        umphagroup.add(umpha)
        all_sprites.add(umpha2)
        all_sprites.add(obsticle2)
        all_sprites.add(obsticle)
        umphagroup.add(umpha2)
        ballgroup.add(umpha)
        ballgroup.add(ball)
        ballgroup.add(ball2)
        ballgroup.add(ball9)
        ballgroup.add(ball10)
        ballgroup.add(ball11)
        ballgroup.add(ball12)

        score = 0
        death_count = 0
    # keep loop running at the desired speed
    clock.tick(t.FPS)

    score = int(score)
    score += 1
    score = str(score)

    # 1. process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerthing.image.fill(random.choice(randomcolor))

    # 2. Update
    all_sprites.update()
    pygame.display.update()
    collide2 = pygame.sprite.spritecollide(playerthing, ballgroup, True)
    if collide2:
        game_over = True

    # 3. Draw / render
    screen.fill(t.ORANGE)
    all_sprites.draw(screen)
    draw_text(score, 40, 100, 20)
    score = int(score)

    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()



