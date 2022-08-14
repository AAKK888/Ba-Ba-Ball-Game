import pygame
import t
pygame.init()
import random


class Obsticle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((400, 400))
        self.image.fill(t.CAMORED)
        self.image.set_colorkey(t.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(0, t.WIDTH), random.randrange(0, t.HEIGHT))

    def update(self):
        # xnum = random.randrange(40, 60)
        # ynum = random.randrange(40, 60)
        # self.rect.x += xnum
        # self.rect.y += ynum
        # self.rect.x -= ynum
        # self.rect.y -= xnum
        # if self.rect.right > t.WIDTH:
        #     self.rect.left = 0
        # if self.rect.left < 0:
        #     self.rect.right = t.WIDTH
        # if self.rect.bottom > t.HEIGHT:
        #     self.rect.top = 0
        # if self.rect.top < 0:
        #     self.rect.bottom = t.HEIGHT
        pass
