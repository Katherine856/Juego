from fabricas import *
from player import *

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getHeroe(self):
        jugador = Personaje()
        jugador.set_sprites(self.__builder.get_sprites())
        return jugador


class Constructor():
    def get_sprites(self): 
        pass

class ConstructorZombis():
    def __init__(self):
        self.fabrica = FabricaZombis()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_morirD(),
                self.fabrica.crear_morirI(),
                self.fabrica.crear_atacarD(),
                self.fabrica.crear_atacarI(),
                self.fabrica.crear_quietoD(),
                self.fabrica.crear_quietoI()]

class ConstructorCaballeros():
    def __init__(self):
        self.fabrica = FabricaCaballeros()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_morirD(),
                self.fabrica.crear_morirI(),
                self.fabrica.crear_atacarD(),
                self.fabrica.crear_atacarI(),
                self.fabrica.crear_quietoD(),
                self.fabrica.crear_quietoI()]

class ConstructorNinjas():
    def __init__(self):
        self.fabrica = FabricaNinjas()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_morirD(),
                self.fabrica.crear_morirI(),
                self.fabrica.crear_atacarD(),
                self.fabrica.crear_atacarI(),
                self.fabrica.crear_quietoD(),
                self.fabrica.crear_quietoI()]

class ConstructorSatiros():
    def __init__(self):
        self.fabrica = FabricaSatiros()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_morirD(),
                self.fabrica.crear_morirI(),
                self.fabrica.crear_atacarD(),
                self.fabrica.crear_atacarI(),
                self.fabrica.crear_quietoD(),
                self.fabrica.crear_quietoI()]
