import pygame
import random
import t

pygame.init()


class Ball(pygame.sprite.Sprite):
    def __init__(self, x_speed, y_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((23, 23))
        self.image.fill(t.RED)
        self.image.set_colorkey(t.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(5, 400), random.randint(5, 400))
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.number = 0

    def update(self):

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.bottom < t.HEIGHT:
            self.y_speed = -self.y_speed
        if self.rect.top > 0:
            self.y_speed = -self.y_speed
        if self.rect.right > t.WIDTH:
            self.x_speed = -self.x_speed
        if self.rect.left < 0:
            self.x_speed = -self.x_speed


class BallSpeed(pygame.sprite.Sprite):
    def __init__(self, x_speed, y_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(t.DARKRED)
        self.image.set_colorkey(t.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(5, 400), random.randint(5, 400))
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.number = 0

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.bottom < t.HEIGHT:
            self.y_speed = -self.y_speed
        if self.rect.top > 0:
            self.y_speed = -self.y_speed
        if self.rect.right > t.WIDTH:
            self.x_speed = -self.x_speed
        if self.rect.left < 0:
            self.x_speed = -self.x_speed
