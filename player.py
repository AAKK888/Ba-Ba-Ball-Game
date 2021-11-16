import pygame 
import random
import vari
pygame.init()

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((20,20))
    self.image.fill(vari.BLUE)
    self.image.set_colorkey(vari.BLACK)
    self.rect = self.image.get_rect()
    self.rect.center = (vari.WIDTH / 2, vari.HEIGHT / 2)
    self.speedx = 0
    self.speedy = 0
    
  def update(self):
    self.speedx = 0
    self.speedy = 0
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_a]:
      self.speedx = -8
    if keypress[pygame.K_d]:
      self.speedx = 8
    if keypress[pygame.K_w]:
      self.speedy = -8
    if keypress[pygame.K_s]:
      self.speedy = 8
      
    self.rect.x += self.speedx
    self.rect.y += self.speedy
    if self.rect.right > vari.WIDTH:
      self.rect.left = 0
    if self.rect.left < 0:
      self.rect.right = vari.WIDTH
    if self.rect.bottom > vari.HEIGHT:
      self.rect.top = 0
    if self.rect.top < 0:
      self.rect.bottom = vari.HEIGHT
