import pyxel

class Mario:
    def __init__(self):
        self.x = 4
        self.y = 240
        self.marioAppear = True
    def getX(self):
        return self.x
    def getY (self):
        return self.y
    def drawMarioRight(self,x,y):
        pyxel.blt(x-8, y-16, 1, 16, 0, -15, 16, colkey=0)
    def drawMarioLeft(self,x,y):
        pyxel.blt(x-8, y-16, 1, 16, 0, 15, 16, colkey=0)
#    def gravedad(self):
#       self.y = self.y+1

