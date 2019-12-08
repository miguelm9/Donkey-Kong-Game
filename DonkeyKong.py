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

def draw():

    global x,y, barriles



    if (not mario.vivo):
        pyxel.rect(0,0,256,260,0)
        pyxel.text(70,110,"GAME OVER",3)
        pyxel.text(70,117,"Insert Coin To Continue",3)
    elif(mario.wins):
        pyxel.rect(0, 0, 256, 260, 0)
        pyxel.text(70, 110, "NIVEL SUPERADO", 3)
        pyxel.text(70, 117, "Insert Coin To Continue", 3)
    else:
        pyxel.cls(0)


        if (mario.vidas == 3):
            pyxel.blt(10, 10, 0, 131, 8, 8, 8)  # Imagen vidas de mario
            pyxel.blt(20, 10, 0, 131, 8, 8, 8)  # Imagen vidas de mario
            pyxel.blt(30, 10, 0, 131, 8, 8, 8)  # Imagen vidas de mario
        elif (mario.vidas == 2):
            pyxel.blt(10, 10, 0, 131, 8, 8, 8)  # Imagen vidas de mario
            pyxel.blt(20, 10, 0, 131, 8, 8, 8)  # Imagen vidas de mario
        elif(mario.vidas == 1):
            pyxel.blt(10, 10, 0, 131, 8, 8, 8)  # Imagen vidas de mario
        else:
            pass
        
        '''
        pyxel.rect(158,4,150,10,3)
        pyxel.text(220, 6, str(mario.vidas), 6)
        pyxel.text(160,6,"Vidas de Mario: ",6)
        '''
        pyxel.blt(165, 28, 0, 181, 100, 43, 19)

        if (mario.puntos == -100):
            pyxel.text(185, 37, "0", 6)
        else:
            pyxel.text(182, 37, str(mario.puntos), 6)

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