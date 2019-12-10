import pyxel
from mario import *
from pauline import *
from plataformas import *
from escaleras import *
from monofurioso import *
from barriles import *

WIDTH = 224
HEIGHT = 256
FPS = 30

CAPTION = "Donkey Kong Game!"
pyxel.init(WIDTH, HEIGHT, caption=CAPTION, scale=3, fps= FPS)
pyxel.load("assets.pyxres")


mario = Mario()
barril = BarrilesRodando()
monoFurioso = MonoFurioso(64, 84)

barriles = []

def update():
    global x, y, barriles

    for i in range(10):
        if pyxel.frame_count == 60 * i:
            barriles.append("barril" + str(i))
            barriles[i] = BarrilesRodando()
    if pyxel.btnp(pyxel.KEY_SPACE):
        mario.saltar = True
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btnp(pyxel.KEY_R):
        return None
    mario.x,mario.y = mario.move(mario.x,mario.y,barriles)
    for i in range(len(barriles)):
        if len(barriles) == 0:
            pass
        else:
            barriles[i].x, barriles[i].y = barriles[i].moveBarril(barriles[i].x, barriles[i].y)


def draw():

    global x,y, barriles, monoAppear

    if (not mario.isMarioVivo()):
        pyxel.rect(0,0,256,260,0)
        pyxel.text(70,110,"GAME OVER",3)
        pyxel.text(70,124,"Insert Coin To Continue",3)
        pyxel.text(70, 117, "Final Score: " + str(mario.getPuntos()), 3)
    elif(mario.hasMarioWon()):
        pyxel.rect(0, 0, 256, 260, 0)
        pyxel.text(70, 110, "NIVEL SUPERADO", 3)
        pyxel.text(70, 124, "Insert Coin To Continue", 3)
        pyxel.text(70, 117, "Final Score: " + str(mario.getBonus()), 3)
    else:
        pyxel.cls(0)

        drawEscenario()
        barril.barrilesAppear(barriles)

        mario.x, mario.y = mario.move(mario.x,mario.y,barriles)
        mario.drawLeftOrRight()
        mono.drawMono()





def drawEscenario():


    mario.drawVidas()
    mario.drawPuntos()

    for i in range(len(escaleras)):
        escaleras[i].drawEscalera()

    barril.drawBarrilesQuietos()
    plataforma = Plataforma()
    plataforma.drawPlataformas()

    peach = Pauline(88, 56)
    peach.drawPauline()


pyxel.run(update, draw)