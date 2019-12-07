import pyxel
escaleras = []

class Escalera:
    def __init__(self,x,y,h):
        self.x = x
        self.y = y
        self.h = h
    def drawEscalera(self):
        for i in range(self.h):
            pyxel.blt(self.x, self.y - 4 - i * 4, 1, 0, 8, 8, 4,colkey=0)

escaleras.append(Escalera(64, 84, 14))
escaleras.append(Escalera(80, 84, 14))
escaleras.append(Escalera(128, 84, 5))
escaleras.append(Escalera(88, 96, 1))
escaleras.append(Escalera(88, 120, 4))
escaleras.append(Escalera(32, 144, 4))
escaleras.append(Escalera(72, 148, 6))
escaleras.append(Escalera(64, 160, 2))
escaleras.append(Escalera(64, 184, 2))
escaleras.append(Escalera(32, 212, 5))
escaleras.append(Escalera(80, 248, 2))
escaleras.append(Escalera(80, 224, 1))
escaleras.append(Escalera(96, 216, 7))
escaleras.append(Escalera(112, 184, 7))
escaleras.append(Escalera(184, 244, 5))
escaleras.append(Escalera(184, 180, 5))
escaleras.append(Escalera(168, 152, 2))
escaleras.append(Escalera(168, 128, 2))
escaleras.append(Escalera(184, 112, 5))