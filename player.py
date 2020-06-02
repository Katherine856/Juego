import pygame
from pygame.sprite import Sprite
from pygame import *

class Personaje(Sprite):
    instance = None

    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance

    def __init__(self):
        Sprite.__init__(self)
        self.cont = 0
        self.state = 0
    
    def set_sprites(self, sprites):
        self.sprites = sprites
        self.image = self.sprites[self.state][self.cont]
        self.rect = self.image.get_rect()
        self.rect.move_ip(50, 50)

    def update(self):
        accion = pygame.key.get_pressed()
        if (accion[K_LEFT] or accion[K_RIGHT] or accion[K_UP] or accion[K_DOWN] or accion[K_SPACE]) and (self.state != 2 or self.state != 2):

            if accion[K_LEFT] and self.rect.x > 0:
                self.state = 1
                self.rect.x -= 5
            if accion[K_RIGHT] and self.rect.x < 920:
                self.state = 0
                self.rect.x += 5
            if accion[K_UP] and self.rect.y > 0:
                if self.state == 0 or self.state == 4:
                    self.state = 0
                if self.state == 1 or self.state == 5:
                    self.state = 1
                self.rect.y -= 5
            if accion[K_DOWN] and self.rect.y < 500:
                if self.state == 0 or self.state == 4:
                    self.state = 0
                if self.state == 1 or self.state == 5:
                    self.state = 1
                self.rect.y += 5
            if accion[K_SPACE]:
                if self.state == 0:
                    self.state = 4
                if self.state == 1:
                    self.state = 5

            self.image = self.animar_state(self.sprites[self.state])

        else:

            if (self.state == 0 or self.state == 4) and (self.state != 2 or self.state != 2):
                self.image = self.animar_state(self.sprites[6])
            if (self.state == 1 or self.state == 5) and (self.state != 2 or self.state != 2):
                self.image = self.animar_state(self.sprites[7])
            if accion[K_a]:
                if self.state == 0 or self.state == 4:
                    self.state = 2
                if self.state == 1 or self.state == 5:
                    self.state = 3
                if self.state == 2 and accion[K_a]:
                    self.image = self.sprites[self.state][7]
                if self.state == 3 and accion[K_a]:
                    self.image = self.sprites[self.state][7]

            if accion[K_l]:
                self.state = 0


    def dibujar(self, ventana):
        ventana.blit(self.image, self.rect)

    def animar_state(self, state):
        self.cont += 1
        if self.cont > (len(state) - 1):
            self.cont = 0
        return state[self.cont]
        

        
            


