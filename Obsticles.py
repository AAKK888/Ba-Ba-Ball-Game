import pygame
import vari
pygame.init()
import random


class Obsticle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(vari.GREEN)
        self.image.set_colorkey(vari.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(0, vari.WIDTH), random.randrange(0, vari.HEIGHT))

    def update(self):
        xnum = random.randrange(5, 50)
        ynum = random.randrange(5, 50)
        self.rect.x += xnum
        self.rect.y += ynum
        self.rect.x -= ynum
        self.rect.y -= xnum
        if self.rect.right > vari.WIDTH:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = vari.WIDTH
        if self.rect.bottom > vari.HEIGHT:
            self.rect.top = 0
        if self.rect.top < 0:
            self.rect.bottom = vari.HEIGHT
