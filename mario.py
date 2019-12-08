import pyxel
from plataformas import *
from escaleras import *
from monofurioso import *
from peach import *

mono = MonoFurioso(64,84)
peach = Peach(88,56)

barrilesDescartados = []

class Mario:
    def __init__(self):
        self.x = 4
        self.y = 240

        self.marioAppear = True
        self.saltar = False
        self.s = 1
        self.vidas = 3
        self.vivo = True
        self.wins = False
        self.puntos = -100


    def getX(self):
        return self.x
    def getY (self):
        return self.y
    def drawMarioRight(self,x,y):
        pyxel.blt(x-8, y-16, 1, 16, 0, -15, 16, colkey=0)
    def drawMarioLeft(self,x,y):
        pyxel.blt(x-8, y-16, 1, 16, 0, 15, 16, colkey=0)

    def muerteMario(self):
        x,y = 4,240
        self.marioAppear = True

        return x,y

    def move(self,x, y, barriles, escaleras):

        if x >= 220:
            x = 220
        if x<=2:
            x= 2

        if peach.x+25 >= x >= peach.x-10 and peach.y == y:
            self.wins = True

        for i in range(len(barriles)):
            if len(barriles) == 0:
                pass
            elif ((barriles[i].x + 6 >= x >= barriles[i].x - 6) and (barriles[i].y +5 >= y >= barriles[i].y-5)):
                pass
                self.quedanVidas()
                return self.muerteMario()
            elif (barriles[i].y > y and not barrilesDescartados.__contains__(barriles[i])):
                print(self.puntos)
                self.puntos += 100
                barrilesDescartados.append(barriles[i])


        if pyxel.btn(pyxel.KEY_RIGHT):
            x = x + 1
            self.marioAppear = True
        elif pyxel.btn(pyxel.KEY_LEFT):
            x = x - 1
            self.marioAppear = False

        if self.saltar:
            if self.s < 10:
                y -= 3
                self.s += 1
            elif self.s < 20 and self.s >= 10:
                self.s += 1
                y += 0
            elif self.s == 20:
                self.s = 0
                self.saltar = False
        if pyxel.btn(pyxel.KEY_UP):
            for i in range(len(escaleras)):
                if escaleras[i].x < x < escaleras[i].x+8: #and escaleras[i].y+escaleras[i].h*4+8 < y+16 < escaleras[i].y+8: #Las 3 escaleras largas del centro no funcionan.
                    y -= 1

        # elif pyxel.btn(pyxel.KEY_DOWN):
            # y = y + 1

        # Comprobar si choca con la plataforma inferior
        if len(listaPlat[0]) > x // 16 and y >= listaPlat[0][x // 16]:
            y = listaPlat[0][x // 16]
            saltar = True

        # Comprobar si choca con la plataforma creciente1
        elif len(listaPlat[1]) > x // 16 and (listaPlat[1][x // 16] + 3 >= y >= listaPlat[1][x // 16]):  # Creciente
            y = listaPlat[1][x // 16]

        # Comprobar si choca con la plataforma decreciente1
        elif len(listaPlat[2]) > x // 16 and (listaPlat[2][x // 16] + 3 >= y >= listaPlat[2][x // 16]):  # Decreciente
            y = listaPlat[2][x // 16]

        # Comprobar si choca con la plataforma superior
        elif len(listaPlat[3]) > x // 16 and (listaPlat[3][x // 16] + 3 >= y >= listaPlat[3][x // 16]):  #
            y = listaPlat[3][x // 16]

        # Comprobar si choca con la plataforma creciente2
        elif len(listaPlat[4]) > x // 16 and (listaPlat[4][x // 16] + 3 >= y >= listaPlat[4][x // 16]):
            y = listaPlat[4][x // 16]

        # Comprobar si choca con la plataforma decrecinte2
        elif len(listaPlat[5]) > x // 16 and (listaPlat[5][x // 16] + 3 >= y >= listaPlat[5][x // 16]):  # Superior
            y = listaPlat[5][x // 16]

        #Comprobar si choca con la plataforma de la princesa
        if len(listaPlat[6]) > x // 16 and (listaPlat[6][x // 16] + 3 >= y >= listaPlat[6][x // 16]):
            y = listaPlat[6][x//16]-1

        y += 1

        return x, y

    def quedanVidas(self):
        if (self.vidas > 0):
            self.vidas -= 1
            return True
        elif (self.vidas == 0):
            self.vivo = False
            return False
        else:
            print("Wtf")
