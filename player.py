import pygame
import random
import t

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(t.BLUE)
        self.image.set_colorkey(t.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (t.WIDTH / 2, t.HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_a] or keypress[pygame.K_LEFT]:
            self.speedx = -6
        if keypress[pygame.K_d] or keypress[pygame.K_RIGHT]:
            self.speedx = 6
        if keypress[pygame.K_w] or keypress[pygame.K_UP]:
            self.speedy = -6
        if keypress[pygame.K_s] or keypress[pygame.K_DOWN]:
            self.speedy = 6

        if self.speedx != 0 and self.speedy != 0:
            self.speedx /= 1.414
            self.speedy /= 1.414
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > t.WIDTH:
            self.rect.left = t.WIDTH - 75
        if self.rect.left < 0:
            self.rect.right = 75
        if self.rect.bottom > t.HEIGHT:
            self.rect.top = t.HEIGHT - 75
        if self.rect.top < 0:
            self.rect.bottom = 75
