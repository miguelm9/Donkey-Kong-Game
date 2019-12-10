import pyxel
from plataformas import *
from escaleras import *
from monofurioso import *
from pauline import *

mono = MonoFurioso(64, 84)
pauline = Pauline(88, 56)

barrilesDescartados = []


class Mario:
    def __init__(self):
        self.x = 4
        self.y = 240

        self.__marioAppear = True  # Boolean para controlar que Mario se dibuje hacia la izquierda o hacia la derecha
        self.saltar = False
        self.__salto = 1
        self.__vidas = 3
        self.__vivo = True  # Boolean para checkear que Mario se ha quedado sin vidas
        self.__wins = False  # Boolean para checkear que Mario ha llegado a la plataforma de la princesa
        self.__puntos = 0
        self.__gravedad = True
        self.__bonus = 5000

    def drawMarioRight(self, x, y):  # Metodo para dibujar a Mario mirando hacia la izquierda
        pyxel.blt(x - 8, y - 16, 1, 16, 0, -15, 16, colkey=0)

    def drawMarioRunningRight(self,x,y):
        if (pyxel.frame_count % 5 == 0):
            pyxel.blt(x - 8, y - 16, 0, 29, 32, -16, 16, colkey=0)
        else:
            #pyxel.blt(x - 8, y - 16, 0, 53, 32, -16, 16, colkey=0)
            pyxel.blt(x - 8, y - 16, 1, 16, 0, -15, 16, colkey=0)


    def drawMarioRunningLeft(self,x,y):
        if (pyxel.frame_count % 5 == 0):
            pyxel.blt(x - 8, y - 16, 0, 29, 32, 16, 16, colkey=0)
        else:
            #pyxel.blt(x - 8, y - 16, 0, 53, 32, 16, 16, colkey=0)
            pyxel.blt(x - 8, y - 16, 1, 16, 0, 15, 16, colkey=0)

    def drawMarioLeft(self, x, y):  # Metodo para dibujar a Mario mirando hacia la izquierda
        pyxel.blt(x - 8, y - 16, 1, 16, 0, 15, 16, colkey=0)

    def isMarioVivo(self):
        return self.__vivo
        # Estos dos metodos nos permiten hacer privados los atributos Vivo y Wins

    def hasMarioWon(self):
        return self.__wins

    def muerteMario(self):  # Metodo para cuando Mario es golpeado por un barril
        self.quedanVidas()
        x, y = 4, 240
        self.__marioAppear = True

        return x, y

    def getPuntos(self):
        return self.__puntos
    def getBonus(self):
        return self.__puntos + self.__bonus
    def move(self, x, y, barriles):

        if x >= 220:  # Para que no se salga por la derecha de la pantalla
            x = 220
        if x <= 2:  # Para que no se salga por la izquierda de la pantalla
            x = 2

        if pauline.x + 25 >= x >= pauline.x - 10 and pauline.y == y:
            self.__wins = True

        for i in range(len(barriles)):
            if len(barriles) == 0:
                pass
            elif ((barriles[i].x + 6 >= x >= barriles[i].x - 6) and (barriles[i].y + 5 >= y >= barriles[i].y - 5)):
                barrilesDescartados.append(barriles[i])
                return self.muerteMario()
            elif (barriles[i].y - 10 >= y >= barriles[i].y - 25 and not barrilesDescartados.__contains__(barriles[i])):
                if (self.__vivo and not self.__wins):
                    self.__puntos += 100
                barrilesDescartados.append(barriles[i])


        x,y = self.teclas(x,y)
        x,y = self.chocaPlataformas(x,y)

        if self.__gravedad == True:
            y += 1

        return x, y

    def quedanVidas(self):
        if (self.__vidas > 0):
            self.__vidas -= 1
            return True
        elif (self.__vidas == 0):
            self.__vivo = False
            return False
        else:
            print("Wtf")

    def drawVidas(self):
        for i in range(self.__vidas):
            pyxel.blt(10 + 10 * i, 10, 0, 131, 8, 8, 8)  # Imagen vidas de mario

    def drawPuntos(self):
        pyxel.blt(165, 28, 0, 181, 100, 43, 19)  # Para los puntos de mario
        pyxel.text(10, 20, "Score: " + str(self.__puntos), 6)
        if pyxel.frame_count % 60 == 0 and self.__vivo and self.__wins == False and pyxel.frame_count <= 3000: #De 5000 ptos a 0 ptos. El Bonus decrece con cada barril (60 frames), decrece a 0 en 3000 frames
             self.__bonus -= 100
        pyxel.text(179, 37, str(self.__bonus), 6)

    def drawLeftOrRight(self):
        if (self.__marioAppear):
            self.drawMarioRight(self.x, self.y)
        elif (not self.__marioAppear):
            self.drawMarioLeft(self.x, self.y)


    def teclas(self,x,y):
        if pyxel.btn(pyxel.KEY_RIGHT):
            x = x + 1
            self.__marioAppear = True
            self.drawMarioRunningRight(x,y)
        elif pyxel.btn(pyxel.KEY_LEFT):
            x = x - 1
            self.__marioAppear = False
            self.drawMarioRunningLeft(x,y)

        if self.saltar:
            if self.__salto < 10:
                y -= 3
                self.__salto += 1
            elif self.__salto < 20 and self.__salto >= 10:
                self.__salto += 1
                y += 0
            elif self.__salto == 20:
                self.__salto = 0
                self.saltar = False

        if pyxel.btn(pyxel.KEY_UP):
            for i in range(len(escaleras)):
                if escaleras[i].x <= x <= escaleras[i].x + 8 and escaleras[i].y - escaleras[i].h * 4 - 8 <= y <= \
                        escaleras[i].y + 1:
                    self.__gravedad = False
                    self.saltar = False
                    y -= 2
                else:
                    self.__gravedad = True
        if pyxel.btn(pyxel.KEY_DOWN):
            for i in range(len(escaleras)):
                if escaleras[i].x <= x <= escaleras[i].x + 8 and escaleras[i].y - escaleras[i].h * 4 - 32 <= y <= \
                        escaleras[i].y + 16:
                    print("HOLAA")
                    y += 2.00001
                else:
                    self.__gravedad = True

        else:
            if (self.__marioAppear):
                self.drawMarioRight(x,y)
            else:
                self.drawMarioLeft(x,y)
        return x,y

    def chocaPlataformas(self,x,y):
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

        # Comprobar si choca con la plataforma de la princesa
        if len(listaPlat[6]) > x // 16 and (listaPlat[6][x // 16] + 3 >= y >= listaPlat[6][x // 16]):
            y = listaPlat[6][x // 16] - 1

        return x,y