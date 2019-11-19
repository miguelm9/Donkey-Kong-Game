import pyxel

WIDTH = 224
HEIGHT = 256
x = 200
y = 230

CAPTION = "Donkey Kong Game!"
pyxel.init(WIDTH, HEIGHT, caption=CAPTION)
pyxel.load("assets.pyxres")

class Mario:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY (self):
        return self.y

    def marioAppear(self):
        pyxel.blt(x, y, 1, 16, 0, -15, 16, colkey=0)

    def drawMarioRight(self,x,y):
        pyxel.blt(x, y, 1, 16, 0, -15, 16, colkey=0)
    def drawMarioLeft(self,x,y):
        pyxel.blt(x, y, 1, 16, 0, 15, 16, colkey=0)

mario = Mario(y, y)

def platInferior(x, y):
    o = 1
    for i in range(14):
        if (i > 6):
            pyxel.blt(x + i * 16, y - o, 1, 0, 0, 16, 8)
            o += 1
        else:
            pyxel.blt(x + i * 16, y, 1, 0, 0, 16, 8)
def platDecreciente(x, y):
    for i in range(13):
        pyxel.blt(x + i * 16, y + i, 1, 0, 0, 16, 8)
def platCreciente(x, y):
    for i in range(13):
        pyxel.blt(x + i * 16, y - i, 1, 0, 0, 16, 8)
def platSuperior(x, y):
    o = 1
    for i in range(13):
        if (i > 8):
            pyxel.blt(x + i * 16, y + o, 1, 0, 0, 16, 8)
            o += 1
        else:
            pyxel.blt(x + i * 16, y, 1, 0, 0, 16, 8)
def platPeach(x, y):
    o = 0
    for i in range(3):
        pyxel.blt(x + o * 16, y, 1, 0, 0, 16, 8)
        o += 1
def escalera(x, y, h):
    for i in range(h):
        pyxel.blt(x, y - 4 - i * 4, 1, 0, 8, 8, 4)

def move(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1
        mario.drawMarioRight(x,y)
    elif pyxel.btn(pyxel.KEY_LEFT):
        x = x - 1
        mario.drawMarioLeft(x,y)
    elif pyxel.btn(pyxel.KEY_UP):
        y = y - 1
    elif pyxel.btn(pyxel.KEY_DOWN):
        y = y + 1
    return x, y

def update():
    global x, y
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    else:
        x,y = move(x,y)


def drawEscaleras():
    escalera(64, 84, 14)
    escalera(80, 84, 14)
    escalera(128, 84, 5)
    escalera(88, 96, 1)
    escalera(88, 120, 4)
    escalera(32, 144, 4)
    escalera(72, 148, 6)
    escalera(64, 160, 2)
    escalera(64, 184, 2)
    escalera(32, 212, 5)
    escalera(80, 248, 2)
    escalera(80, 224, 1)
    escalera(96, 216, 7)
    escalera(112, 184, 7)
    escalera(184, 244, 5)
    escalera(184, 180, 5)
    escalera(168, 152, 2)
    escalera(168, 128, 2)
    escalera(184, 112, 5)
def drawPlataformas():
    # Plataformas
    platInferior(0, 248)
    platDecreciente(0, 208)
    platCreciente(16, 187)
    platDecreciente(0, 142)
    platCreciente(16, 121)
    platSuperior(0, 84)
    platPeach(88, 56)



def draw():
    global x,y
    ##################
    pyxel.cls(3)
    drawEscaleras()
    drawPlataformas()
    ##################

    x,y = move(x,y)
    mario.marioAppear()



pyxel.run(update, draw)