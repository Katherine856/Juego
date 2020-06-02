from productos import *

class FabricaAbstracta():
    def crear_derecha(self): pass
    def crear_izquierda(self): pass
    def crear_morirD(self): pass
    def crear_morirI(self): pass
    def crear_atacarD(self): pass
    def crear_atacarI(self): pass
    def crear_quietoD(self): pass
    def crear_quietoI(self): pass

class FabricaZombis(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaZombi()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaZombi()
        return derecha.get_sprites()

    def crear_morirD(self):
        morirD = MorirDZombi()
        return morirD.get_sprites()

    def crear_morirI(self):
        morirI = MorirIZombi()
        return morirI.get_sprites()

    def crear_atacarD(self):
        atacarD = AtacarDZombi()
        return atacarD.get_sprites()

    def crear_atacarI(self):
        atacarI = AtacarIZombi()
        return atacarI.get_sprites()

    def crear_quietoD(self):
        quietoD = QuietoDZombi()
        return quietoD.get_sprites()

    def crear_quietoI(self):
        quietoI = QuietoIZombi()
        return quietoI.get_sprites()


class FabricaCaballeros(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaCaballero()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaCaballero()
        return derecha.get_sprites()

    def crear_morirD(self):
        morirD = MorirDCaballero()
        return morirD.get_sprites()

    def crear_morirI(self):
        morirI = MorirICaballero()
        return morirI.get_sprites()

    def crear_atacarD(self):
        atacarD = AtacarDCaballero()
        return atacarD.get_sprites()

    def crear_atacarI(self):
        atacarI = AtacarICaballero()
        return atacarI.get_sprites()

    def crear_quietoD(self):
        quietoD = QuietoDCaballero()
        return quietoD.get_sprites()

    def crear_quietoI(self):
        quietoI = QuietoICaballero()
        return quietoI.get_sprites()


class FabricaNinjas(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaNinja()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaNinja()
        return derecha.get_sprites()

    def crear_morirD(self):
        morirD = MorirDNinja()
        return morirD.get_sprites()

    def crear_morirI(self):
        morirI = MorirINinja()
        return morirI.get_sprites()

    def crear_atacarD(self):
        atacarD = AtacarDNinja()
        return atacarD.get_sprites()

    def crear_atacarI(self):
        atacarI = AtacarINinja()
        return atacarI.get_sprites()

    def crear_quietoD(self):
        quietoD = QuietoDNinja()
        return quietoD.get_sprites()

    def crear_quietoI(self):
        quietoI = QuietoINinja()
        return quietoI.get_sprites()


class FabricaSatiros(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaSatiro()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaSatiro()
        return derecha.get_sprites()

    def crear_morirD(self):
        morirD = MorirDSatiro()
        return morirD.get_sprites()

    def crear_morirI(self):
        morirI = MorirISatiro()
        return morirI.get_sprites()

    def crear_atacarD(self):
        atacarD = AtacarDSatiro()
        return atacarD.get_sprites()

    def crear_atacarI(self):
        atacarI = AtacarISatiro()
        return atacarI.get_sprites()

    def crear_quietoD(self):
        quietoD = QuietoDSatiro()
        return quietoD.get_sprites()

    def crear_quietoI(self):
        quietoI = QuietoISatiro()
        return quietoI.get_sprites()
