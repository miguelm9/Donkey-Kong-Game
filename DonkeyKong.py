import pyxel
from mario import *
from peach import *
from plataformas import *
from escaleras import *
from monofurioso import *
from barriles import *

WIDTH = 224
HEIGHT = 256
FPS = 30

CAPTION = "Donkey Kong Game!"
pyxel.init(WIDTH, HEIGHT, caption=CAPTION, scale=3, fps= 30)
pyxel.load("assets.pyxres")


mario = Mario()
barriles = []


def update():
    print(mario.saltar)
    global x, y, barriles
    for i in range(10):
        if pyxel.frame_count == 60 * i:
            barriles.append("barril" + str(i))
            barriles[i] = BarrilesRodando()
    if pyxel.btnp(pyxel.KEY_SPACE):
        mario.saltar = True
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    mario.x,mario.y = mario.move(mario.x,mario.y,barriles, escaleras)
    for i in range(len(barriles)):
        if len(barriles) == 0:
            pass
        else:
            barriles[i].x, barriles[i].y = barriles[i].moveBarril(barriles[i].x, barriles[i].y)
            print(barriles[i], barriles[i].x, barriles[i].y)

def draw():

    global x,y, barriles
    pyxel.cls(0)

    for i in range(len(escaleras)):
        escaleras[i].drawEscalera()

    drawBarrilesQuietos()
    drawPlataformas()

    peach = Peach(88,56)
    peach.drawPeach()

    monoFurioso = MonoFurioso(64,84)
    monoFurioso.drawMonoFurioso()

    for i in range(len(barriles)):
        if len(barriles) == 0:
            pass
        elif pyxel.frame_count >= 60*i:
            barriles[i].drawBarril(barriles[i].x-12,barriles[i].y-10)
            barriles[i].x, barriles[i].y = barriles[i].moveBarril(barriles[i].x, barriles[i].y)


    mario.x,mario.y = mario.move(mario.x,mario.y,barriles, escaleras)
    if (mario.marioAppear):
        mario.drawMarioRight(mario.x,mario.y)
    elif (not mario.marioAppear):
        mario.drawMarioLeft(mario.x,mario.y)


pyxel.run(update, draw)