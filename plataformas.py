import pyxel

listaPlat = [
    [], #lista para la plat inferior
    [0],#lista para las plat creciente1
    [], #lista para las plat decreciente
    [],#lisa para la superior
    [0], #lista para la plat creciente1
    [], #lista para la plat decreciente1
]

def platInferior(x, y):
    o = 1
    for i in range(14):
        if (i > 6):
            pyxel.blt(x + i * 16, y - o, 1, 0, 0, 16, 8,colkey=0)
            o += 1
            if (pyxel.frame_count == 0):
                listaPlat[0].append(y-o)
        else:
            pyxel.blt(x + i * 16, y, 1, 0, 0, 16, 8,colkey=0)
            if (pyxel.frame_count == 0):
                listaPlat[0].append(y)


def platDecreciente(x, y):
    for i in range(13):
        pyxel.blt(x + i * 16, y + i, 1, 0, 0, 16, 8,colkey=0)
        if (pyxel.frame_count == 0):
            listaPlat[2].append(y+i)

def platDecreciente1(x, y):
    for i in range(13):
        pyxel.blt(x + i * 16, y + i, 1, 0, 0, 16, 8,colkey=0)
        if (pyxel.frame_count == 0):
            listaPlat[5].append(y+i)

def platCreciente(x, y):
    for i in range(13):
        pyxel.blt(x + i * 16, y - i, 1, 0, 0, 16, 8,colkey=0)
        if (pyxel.frame_count == 0):
            listaPlat[4].append(y-i)

def platCreciente1(x, y):
    for i in range(13):
        pyxel.blt(x + i * 16, y - i, 1, 0, 0, 16, 8,colkey=0)
        if (pyxel.frame_count == 0):
            listaPlat[1].append(y-i)

def platSuperior(x, y):
    o = 1
    for i in range(13):
        if (i > 8):
            pyxel.blt(x + i * 16, y + o, 1, 0, 0, 16, 8,colkey=0)
            o += 1
            if (pyxel.frame_count == 0):
                listaPlat[3].append(y+o)
        else:
            pyxel.blt(x + i * 16, y, 1, 0, 0, 16, 8,colkey=0)
            if (pyxel.frame_count == 0):
                listaPlat[3].append(y)
def platPeach(x, y):
    o = 0
    for i in range(3):
        pyxel.blt(x + o * 16, y, 1, 0, 0, 16, 8,colkey=0)
        o += 1

def drawPlataformas():
    platInferior(0, 248)
    platDecreciente(0, 208)
    platCreciente(16, 187)
    platDecreciente1(0, 142)
    platCreciente1(16, 121)
    platSuperior(0, 84)
    platPeach(88, 56)