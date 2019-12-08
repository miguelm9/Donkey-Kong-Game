import pyxel
from plataformas import *
from mario import *

class BarrilesRodando():
    def __init__(self):
        self.x = 68
        self.y = 82

    def drawBarril(self,x,y):
        pyxel.blt(x,y,0,107,106,12,10,colkey=0)


    def moveBarril (self,x,y):

        if(x < 0):
            x = 68
            y = 82
            barrilesDescartados.remove(self)

        # Comprobar si choca con la plataforma inferior
        elif len(listaPlat[0]) > x // 16 and y >= listaPlat[0][x // 16]:
            y = listaPlat[0][x // 16]
            x -= 1

        # Comprobar si choca con la plataforma creciente1
        elif len(listaPlat[1]) > x // 16 and (listaPlat[1][x // 16] + 3 >= y >= listaPlat[1][x // 16]):  # Creciente
            y = listaPlat[1][x // 16]
            x -= 1

        # Comprobar si choca con la plataforma decreciente1
        elif len(listaPlat[2]) > x // 16 and (listaPlat[2][x // 16] + 3 >= y >= listaPlat[2][x // 16]):  # Decreciente
            y = listaPlat[2][x // 16]
            x += 1

        # Comprobar si choca con la plataforma superior
        elif len(listaPlat[3]) > x // 16 and (listaPlat[3][x // 16] + 3 >= y >= listaPlat[3][x // 16]):  #
            y = listaPlat[3][x // 16]
            x += 1

        # Comprobar si choca con la plataforma creciente2
        elif len(listaPlat[4]) > x // 16 and (listaPlat[4][x // 16] + 3 >= y >= listaPlat[4][x // 16]):
            y = listaPlat[4][x // 16]
            x -= 1

        # Comprobar si choca con la plataforma decrecinte2
        elif len(listaPlat[5]) > x // 16 and (listaPlat[5][x // 16] + 3 >= y >= listaPlat[5][x // 16]):  # Superior
            y = listaPlat[5][x // 16]
            x += 1


        y += 2

        return x,y


def drawBarrilesQuietos():
    pyxel.blt(0,84-32,0,12,103,10,16, colkey=0)
    pyxel.blt(10,84-32,0,12,103,10,16, colkey=0)
    pyxel.blt(0,84-16,0,12,103,10,16, colkey=0)
    pyxel.blt(10,84-16,0,12,103,10,16, colkey=0)