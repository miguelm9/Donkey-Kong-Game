import pyxel

def escalera(x, y, h):
    for i in range(h):
        pyxel.blt(x, y - 4 - i * 4, 1, 0, 8, 8, 4,colkey=0)


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