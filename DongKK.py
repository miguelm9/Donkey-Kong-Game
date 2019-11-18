import pyxel

WIDTH = 224
HEIGHT = 256
CAPTION = "Dong King Kong Game!"
pyxel.init(WIDTH, HEIGHT, caption=CAPTION)
pyxel.load("assets.pyxres")

def plataformaBaja (x,y):
    o = 1
    for i in range(14):
        if (i> 6):
            pyxel.blt(x+i * 16, y - o, 1, 0, 0, 16, 8)
            o += 1
        else:
            pyxel.blt(x+i * 16, y, 1, 0, 0, 16, 8)

def platDecreciente (x,y):
    for i in range(13):
        pyxel.blt(x+i * 16, y+i, 1, 0, 0, 16, 8)

def platCreciente (x,y):
    for i in range(13):
        pyxel.blt(x+i * 16, y-i, 1, 0, 0, 16, 8)


def platSuperior (x,y):
    o = 1
    for i in range(13):
        if (i > 6):
            pyxel.blt(x + i * 16, y + o, 1, 0, 0, 16, 8)
            o += 1
        else:
            pyxel.blt(x + i * 16, y, 1, 0, 0, 16, 8)


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(3)
    plataformaBaja(0,248)

    platDecreciente(0,208)
    platCreciente(16,186)

    platDecreciente(0,138)
    platCreciente(16,116)

    platSuperior(0, 70)



pyxel.run(update, draw)