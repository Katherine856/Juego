import pygame
import random
import player
from pygame.locals import *
import recursos 
from constuctores import *

class main():
    pygame.init()
    ventana = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Ventana Principal")
    clock = pygame.time.Clock()
    clock = pygame.time.Clock()
    cursor1 = recursos.Cursor()
    imgFondo = pygame.image.load("Img/FondoP.png").convert()
    img1 = pygame.image.load("Img/spritesZ/ZCD2.png")
    botonZ = recursos.Boton(img1,158,450)
    img2 = pygame.image.load("Img/spritesC/CCD2.png")
    botonC = recursos.Boton(img2,358,450)
    img3 = pygame.image.load("Img/spritesN/NCD2.png")
    botonN = recursos.Boton(img3,558,450)
    img4 = pygame.image.load("Img/spritesS/SCD2.png")
    botonS = recursos.Boton(img4,718,440)

    jugando = False
    ejecutando = True

    while ejecutando == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(botonZ.rect):
                    director = Director()
                    director.setBuilder(ConstructorZombis())
                    player = director.getHeroe()
                    jugando = True
                if cursor1.colliderect(botonC.rect):
                    director = Director()
                    director.setBuilder(ConstructorCaballeros())
                    player = director.getHeroe()
                    jugando = True
                if cursor1.colliderect(botonN.rect):
                    director = Director()
                    director.setBuilder(ConstructorNinjas())
                    player = director.getHeroe()
                    jugando = True
                if cursor1.colliderect(botonS.rect):
                    director = Director()
                    director.setBuilder(ConstructorSatiros())
                    player = director.getHeroe()
                    jugando = True

            if event.type == pygame.QUIT:
                ejecutando = False
            
        if jugando:
            pygame.mouse.set_visible(False)
            ventana.blit(imgFondo, [0, 0])
            player.dibujar(ventana)
            player.update()
            clock.tick(25)

        else:
            ventana.blit(imgFondo,[0,0])
            cursor1.actualizar()
            botonZ.actualizar(ventana)
            botonC.actualizar(ventana)
            botonN.actualizar(ventana)
            botonS.actualizar(ventana)

        pygame.display.flip()

    pygame.quit ()


if __name__ == "__main__":
    main()

