import pygame

class Derecha():
    def get_sprites(self): 
        pass

class DerechaZombi(Derecha):
    def get_sprites(self): 
        return [pygame.image.load('Img/spritesZ/ZCD1.png'),
                pygame.image.load('Img/spritesZ/ZCD2.png'),
                pygame.image.load('Img/spritesZ/ZCD3.png'),
                pygame.image.load('Img/spritesZ/ZCD4.png'),
                pygame.image.load('Img/spritesZ/ZCD5.png'),
                pygame.image.load('Img/spritesZ/ZCD6.png'),
                pygame.image.load('Img/spritesZ/ZCD7.png'),
                pygame.image.load('Img/spritesZ/ZCD8.png')]

class DerechaCaballero(Derecha):
    def get_sprites(self): 
        return [pygame.image.load('Img/spritesC/CCD1.png'),
                pygame.image.load('Img/spritesC/CCD2.png'),
                pygame.image.load('Img/spritesC/CCD3.png'),
                pygame.image.load('Img/spritesC/CCD4.png'),
                pygame.image.load('Img/spritesC/CCD5.png'),
                pygame.image.load('Img/spritesC/CCD6.png'),
                pygame.image.load('Img/spritesC/CCD7.png'),
                pygame.image.load('Img/spritesC/CCD8.png')]

class DerechaNinja(Derecha):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesN/NCD1.png'),
                pygame.image.load('Img/spritesN/NCD2.png'),
                pygame.image.load('Img/spritesN/NCD3.png'),
                pygame.image.load('Img/spritesN/NCD4.png'),
                pygame.image.load('Img/spritesN/NCD5.png'),
                pygame.image.load('Img/spritesN/NCD6.png'),
                pygame.image.load('Img/spritesN/NCD7.png'),
                pygame.image.load('Img/spritesN/NCD8.png')]

class DerechaSatiro(Derecha):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesS/SCD1.png'),
                pygame.image.load('Img/spritesS/SCD2.png'),
                pygame.image.load('Img/spritesS/SCD3.png'),
                pygame.image.load('Img/spritesS/SCD4.png'),
                pygame.image.load('Img/spritesS/SCD5.png'),
                pygame.image.load('Img/spritesS/SCD6.png'),
                pygame.image.load('Img/spritesS/SCD7.png'),
                pygame.image.load('Img/spritesS/SCD8.png')]


class Izquierda():
    def get_sprites(self): 
        pass

class IzquierdaZombi(Izquierda):
    def get_sprites(self): 
        return [pygame.image.load('Img/spritesZ/ZCI1.png'),
                pygame.image.load('Img/spritesZ/ZCI2.png'),
                pygame.image.load('Img/spritesZ/ZCI3.png'),
                pygame.image.load('Img/spritesZ/ZCI4.png'),
                pygame.image.load('Img/spritesZ/ZCI5.png'),
                pygame.image.load('Img/spritesZ/ZCI6.png'),
                pygame.image.load('Img/spritesZ/ZCI7.png'),
                pygame.image.load('Img/spritesZ/ZCI8.png')]

class IzquierdaCaballero(Izquierda):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesC/CCI1.png'),
                pygame.image.load('Img/spritesC/CCI2.png'),
                pygame.image.load('Img/spritesC/CCI3.png'),
                pygame.image.load('Img/spritesC/CCI4.png'),
                pygame.image.load('Img/spritesC/CCI5.png'),
                pygame.image.load('Img/spritesC/CCI6.png'),
                pygame.image.load('Img/spritesC/CCI7.png'),
                pygame.image.load('Img/spritesC/CCI8.png')]

class IzquierdaNinja(Izquierda):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesN/NCI1.png'),
                pygame.image.load('Img/spritesN/NCI2.png'),
                pygame.image.load('Img/spritesN/NCI3.png'),
                pygame.image.load('Img/spritesN/NCI4.png'),
                pygame.image.load('Img/spritesN/NCI5.png'),
                pygame.image.load('Img/spritesN/NCI6.png'),
                pygame.image.load('Img/spritesN/NCI7.png'),
                pygame.image.load('Img/spritesN/NCI8.png')]

class IzquierdaSatiro(Izquierda):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesS/SCI1.png'),
                pygame.image.load('Img/spritesS/SCI2.png'),
                pygame.image.load('Img/spritesS/SCI3.png'),
                pygame.image.load('Img/spritesS/SCI4.png'),
                pygame.image.load('Img/spritesS/SCI5.png'),
                pygame.image.load('Img/spritesS/SCI6.png'),
                pygame.image.load('Img/spritesS/SCI7.png'),
                pygame.image.load('Img/spritesS/SCI8.png')]


class MorirD():
    def get_sprites(self):
        pass

class MorirDZombi(MorirD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesZ/ZMD1.png'),
                pygame.image.load('Img/spritesZ/ZMD2.png'),
                pygame.image.load('Img/spritesZ/ZMD3.png'),
                pygame.image.load('Img/spritesZ/ZMD4.png'),
                pygame.image.load('Img/spritesZ/ZMD5.png'),
                pygame.image.load('Img/spritesZ/ZMD6.png'),
                pygame.image.load('Img/spritesZ/ZMD7.png'),
                pygame.image.load('Img/spritesZ/ZMD8.png')]

class MorirDCaballero(MorirD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesC/CMD1.png'),
                pygame.image.load('Img/spritesC/CMD2.png'),
                pygame.image.load('Img/spritesC/CMD3.png'),
                pygame.image.load('Img/spritesC/CMD4.png'),
                pygame.image.load('Img/spritesC/CMD5.png'),
                pygame.image.load('Img/spritesC/CMD6.png'),
                pygame.image.load('Img/spritesC/CMD7.png'),
                pygame.image.load('Img/spritesC/CMD8.png')]

class MorirDNinja(MorirD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesN/NMD1.png'),
                pygame.image.load('Img/spritesN/NMD2.png'),
                pygame.image.load('Img/spritesN/NMD3.png'),
                pygame.image.load('Img/spritesN/NMD4.png'),
                pygame.image.load('Img/spritesN/NMD5.png'),
                pygame.image.load('Img/spritesN/NMD6.png'),
                pygame.image.load('Img/spritesN/NMD7.png'),
                pygame.image.load('Img/spritesN/NMD8.png')]

class MorirDSatiro(MorirD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesS/SMD1.png'),
                pygame.image.load('Img/spritesS/SMD2.png'),
                pygame.image.load('Img/spritesS/SMD3.png'),
                pygame.image.load('Img/spritesS/SMD4.png'),
                pygame.image.load('Img/spritesS/SMD5.png'),
                pygame.image.load('Img/spritesS/SMD6.png'),
                pygame.image.load('Img/spritesS/SMD7.png'),
                pygame.image.load('Img/spritesS/SMD8.png')]


class MorirI():
    def get_sprites(self):
        pass

class MorirIZombi(MorirI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesZ/ZMI1.png'),
                pygame.image.load('Img/spritesZ/ZMI2.png'),
                pygame.image.load('Img/spritesZ/ZMI3.png'),
                pygame.image.load('Img/spritesZ/ZMI4.png'),
                pygame.image.load('Img/spritesZ/ZMI5.png'),
                pygame.image.load('Img/spritesZ/ZMI6.png'),
                pygame.image.load('Img/spritesZ/ZMI7.png'),
                pygame.image.load('Img/spritesZ/ZMI8.png')]

class MorirICaballero(MorirI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesC/CMI1.png'),
                pygame.image.load('Img/spritesC/CMI2.png'),
                pygame.image.load('Img/spritesC/CMI3.png'),
                pygame.image.load('Img/spritesC/CMI4.png'),
                pygame.image.load('Img/spritesC/CMI5.png'),
                pygame.image.load('Img/spritesC/CMI6.png'),
                pygame.image.load('Img/spritesC/CMI7.png'),
                pygame.image.load('Img/spritesC/CMI8.png')]

class MorirINinja(MorirI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesN/NMI1.png'),
                pygame.image.load('Img/spritesN/NMI2.png'),
                pygame.image.load('Img/spritesN/NMI3.png'),
                pygame.image.load('Img/spritesN/NMI4.png'),
                pygame.image.load('Img/spritesN/NMI5.png'),
                pygame.image.load('Img/spritesN/NMI6.png'),
                pygame.image.load('Img/spritesN/NMI7.png'),
                pygame.image.load('Img/spritesN/NMI8.png')]

class MorirISatiro(MorirI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesS/SMI1.png'),
                pygame.image.load('Img/spritesS/SMI2.png'),
                pygame.image.load('Img/spritesS/SMI3.png'),
                pygame.image.load('Img/spritesS/SMI4.png'),
                pygame.image.load('Img/spritesS/SMI5.png'),
                pygame.image.load('Img/spritesS/SMI6.png'),
                pygame.image.load('Img/spritesS/SMI7.png'),
                pygame.image.load('Img/spritesS/SMI8.png')]


class AtacarD():
    def get_sprites(self):
        pass

class AtacarDZombi(AtacarD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesZ/ZAD1.png'),
                pygame.image.load('Img/spritesZ/ZAD2.png'),
                pygame.image.load('Img/spritesZ/ZAD3.png'),
                pygame.image.load('Img/spritesZ/ZAD4.png'),
                pygame.image.load('Img/spritesZ/ZAD5.png'),
                pygame.image.load('Img/spritesZ/ZAD6.png'),
                pygame.image.load('Img/spritesZ/ZAD7.png'),
                pygame.image.load('Img/spritesZ/ZAD8.png')]

class AtacarDCaballero(AtacarD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesC/CAD1.png'),
                pygame.image.load('Img/spritesC/CAD2.png'),
                pygame.image.load('Img/spritesC/CAD3.png'),
                pygame.image.load('Img/spritesC/CAD4.png'),
                pygame.image.load('Img/spritesC/CAD5.png'),
                pygame.image.load('Img/spritesC/CAD6.png'),
                pygame.image.load('Img/spritesC/CAD7.png'),
                pygame.image.load('Img/spritesC/CAD8.png')]

class AtacarDNinja(AtacarD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesN/NAD1.png'),
                pygame.image.load('Img/spritesN/NAD2.png'),
                pygame.image.load('Img/spritesN/NAD3.png'),
                pygame.image.load('Img/spritesN/NAD4.png'),
                pygame.image.load('Img/spritesN/NAD5.png'),
                pygame.image.load('Img/spritesN/NAD6.png'),
                pygame.image.load('Img/spritesN/NAD7.png'),
                pygame.image.load('Img/spritesN/NAD8.png')]

class AtacarDSatiro(AtacarD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesS/SAD1.png'),
                pygame.image.load('Img/spritesS/SAD2.png'),
                pygame.image.load('Img/spritesS/SAD3.png'),
                pygame.image.load('Img/spritesS/SAD4.png'),
                pygame.image.load('Img/spritesS/SAD5.png'),
                pygame.image.load('Img/spritesS/SAD6.png'),
                pygame.image.load('Img/spritesS/SAD7.png'),
                pygame.image.load('Img/spritesS/SAD8.png')]


class AtacarI():
    def get_sprites(self):
        pass

class AtacarIZombi(AtacarI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesZ/ZAI1.png'),
                pygame.image.load('Img/spritesZ/ZAI2.png'),
                pygame.image.load('Img/spritesZ/ZAI3.png'),
                pygame.image.load('Img/spritesZ/ZAI4.png'),
                pygame.image.load('Img/spritesZ/ZAI5.png'),
                pygame.image.load('Img/spritesZ/ZAI6.png'),
                pygame.image.load('Img/spritesZ/ZAI7.png'),
                pygame.image.load('Img/spritesZ/ZAI8.png')]

class AtacarICaballero(AtacarI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesC/CAI1.png'),
                pygame.image.load('Img/spritesC/CAI2.png'),
                pygame.image.load('Img/spritesC/CAI3.png'),
                pygame.image.load('Img/spritesC/CAI4.png'),
                pygame.image.load('Img/spritesC/CAI5.png'),
                pygame.image.load('Img/spritesC/CAI6.png'),
                pygame.image.load('Img/spritesC/CAI7.png'),
                pygame.image.load('Img/spritesC/CAI8.png')]

class AtacarINinja(AtacarI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesN/NAI1.png'),
                pygame.image.load('Img/spritesN/NAI2.png'),
                pygame.image.load('Img/spritesN/NAI3.png'),
                pygame.image.load('Img/spritesN/NAI4.png'),
                pygame.image.load('Img/spritesN/NAI5.png'),
                pygame.image.load('Img/spritesN/NAI6.png'),
                pygame.image.load('Img/spritesN/NAI7.png'),
                pygame.image.load('Img/spritesN/NAI8.png')]

class AtacarISatiro(AtacarI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesS/SAI1.png'),
                pygame.image.load('Img/spritesS/SAI2.png'),
                pygame.image.load('Img/spritesS/SAI3.png'),
                pygame.image.load('Img/spritesS/SAI4.png'),
                pygame.image.load('Img/spritesS/SAI5.png'),
                pygame.image.load('Img/spritesS/SAI6.png'),
                pygame.image.load('Img/spritesS/SAI7.png'),
                pygame.image.load('Img/spritesS/SAI8.png')]


class QuietoD():
    def get_sprites(self):
        pass

class QuietoDZombi(QuietoD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesZ/ZQD1.png'),
                pygame.image.load('Img/spritesZ/ZQD2.png'),
                pygame.image.load('Img/spritesZ/ZQD3.png'),
                pygame.image.load('Img/spritesZ/ZQD4.png'),
                pygame.image.load('Img/spritesZ/ZQD5.png'),
                pygame.image.load('Img/spritesZ/ZQD6.png'),
                pygame.image.load('Img/spritesZ/ZQD7.png'),
                pygame.image.load('Img/spritesZ/ZQD8.png')]

class QuietoDCaballero(QuietoD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesC/CQD1.png'),
                pygame.image.load('Img/spritesC/CQD2.png'),
                pygame.image.load('Img/spritesC/CQD3.png'),
                pygame.image.load('Img/spritesC/CQD4.png'),
                pygame.image.load('Img/spritesC/CQD5.png'),
                pygame.image.load('Img/spritesC/CQD6.png'),
                pygame.image.load('Img/spritesC/CQD7.png'),
                pygame.image.load('Img/spritesC/CQD8.png')]

class QuietoDNinja(QuietoD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesN/NQD1.png'),
                pygame.image.load('Img/spritesN/NQD2.png'),
                pygame.image.load('Img/spritesN/NQD3.png'),
                pygame.image.load('Img/spritesN/NQD4.png'),
                pygame.image.load('Img/spritesN/NQD5.png'),
                pygame.image.load('Img/spritesN/NQD6.png'),
                pygame.image.load('Img/spritesN/NQD7.png'),
                pygame.image.load('Img/spritesN/NQD8.png')]

class QuietoDSatiro(QuietoD):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesS/SQD1.png'),
                pygame.image.load('Img/spritesS/SQD2.png'),
                pygame.image.load('Img/spritesS/SQD3.png'),
                pygame.image.load('Img/spritesS/SQD4.png'),
                pygame.image.load('Img/spritesS/SQD5.png'),
                pygame.image.load('Img/spritesS/SQD6.png'),
                pygame.image.load('Img/spritesS/SQD7.png'),
                pygame.image.load('Img/spritesS/SQD8.png')]


class QuietoI():
    def get_sprites(self):
        pass

class QuietoIZombi(QuietoI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesZ/ZQI1.png'),
                pygame.image.load('Img/spritesZ/ZQI2.png'),
                pygame.image.load('Img/spritesZ/ZQI3.png'),
                pygame.image.load('Img/spritesZ/ZQI4.png'),
                pygame.image.load('Img/spritesZ/ZQI5.png'),
                pygame.image.load('Img/spritesZ/ZQI6.png'),
                pygame.image.load('Img/spritesZ/ZQI7.png'),
                pygame.image.load('Img/spritesZ/ZQI8.png')]

class QuietoICaballero(QuietoI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesC/CQI1.png'),
                pygame.image.load('Img/spritesC/CQI2.png'),
                pygame.image.load('Img/spritesC/CQI3.png'),
                pygame.image.load('Img/spritesC/CQI4.png'),
                pygame.image.load('Img/spritesC/CQI5.png'),
                pygame.image.load('Img/spritesC/CQI6.png'),
                pygame.image.load('Img/spritesC/CQI7.png'),
                pygame.image.load('Img/spritesC/CQI8.png')]

class QuietoINinja(QuietoI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesN/NQI1.png'),
                pygame.image.load('Img/spritesN/NQI2.png'),
                pygame.image.load('Img/spritesN/NQI3.png'),
                pygame.image.load('Img/spritesN/NQI4.png'),
                pygame.image.load('Img/spritesN/NQI5.png'),
                pygame.image.load('Img/spritesN/NQI6.png'),
                pygame.image.load('Img/spritesN/NQI7.png'),
                pygame.image.load('Img/spritesN/NQI8.png')]

class QuietoISatiro(QuietoI):
    def get_sprites(self):
        return [pygame.image.load('Img/spritesS/SQI1.png'),
                pygame.image.load('Img/spritesS/SQI2.png'),
                pygame.image.load('Img/spritesS/SQI3.png'),
                pygame.image.load('Img/spritesS/SQI4.png'),
                pygame.image.load('Img/spritesS/SQI5.png'),
                pygame.image.load('Img/spritesS/SQI6.png'),
                pygame.image.load('Img/spritesS/SQI7.png'),
                pygame.image.load('Img/spritesS/SQI8.png')]