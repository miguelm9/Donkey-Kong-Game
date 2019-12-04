import pyxel
from mario import *
from peach import *
from plataformas import *
from escaleras import *
from monofurioso import *

WIDTH = 224
HEIGHT = 256

CAPTION = "Donkey Kong Game!"
pyxel.init(WIDTH, HEIGHT, caption=CAPTION)
pyxel.load("assets.pyxres")


mario = Mario()


def move(x, y):
    print(x,y)
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1
        mario.marioAppear = True
    elif pyxel.btn(pyxel.KEY_LEFT):
        x = x - 1
        mario.marioAppear = False

    # Programar cuando vayamos a hacer escaleras
    elif pyxel.btn(pyxel.KEY_UP):
        y = y - 3
    elif pyxel.btn(pyxel.KEY_DOWN):
        y = y + 1

    # Comprobar si choca con la plataforma inferior
    if len(listaPlat[0]) > x//16 and y >= listaPlat[0][x//16]:
        y = listaPlat[0][x//16]

    # Comprobar si choca con la plataforma creciente1
    elif len(listaPlat[1]) > x//16 and (listaPlat[1][x//16]+3 >= y >= listaPlat[1][x//16]): #Creciente
        y = listaPlat[1][x//16]
    # Comprobar si choca con la plataforma decreciente1
    elif len(listaPlat[2]) > x//16 and (listaPlat[2][x//16]+3 >= y >= listaPlat[2][x//16]): #Decreciente
        y = listaPlat[2][x//16]

    # Comprobar si choca con la plataforma superior
    elif len(listaPlat[3]) > x//16 and (listaPlat[3][x//16]+3 >= y >= listaPlat[3][x//16]): #
        y = listaPlat[3][x//16]

    # Comprobar si choca con la plataforma creciente2
    elif len(listaPlat[4]) > x // 16 and (listaPlat[4][x // 16] + 3 >= y >= listaPlat[4][x // 16]):
        y = listaPlat[4][x // 16]

    # Comprobar si choca con la plataforma decrecinte2
    elif len(listaPlat[5]) > x // 16 and (listaPlat[5][x // 16] + 3 >= y >= listaPlat[5][x // 16]):  # Superior
        y = listaPlat[5][x // 16]

    y += 1

    return x, y


def update():
    global x, y
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    else:
        mario.x,mario.y = move(mario.x,mario.y)


def draw():
    global x,y
    pyxel.cls(0)

    drawEscaleras()
    drawPlataformas()

    peach = Peach(88,56)
    peach.drawPeach()

    monoFurioso = MonoFurioso(10,53)
    monoFurioso.drawMonoFurioso()

    mario.x,mario.y = move(mario.x,mario.y)
    if (mario.marioAppear):
        mario.drawMarioRight(mario.x,mario.y)
    elif (not mario.marioAppear):
        mario.drawMarioLeft(mario.x,mario.y)

pyxel.run(update, draw)