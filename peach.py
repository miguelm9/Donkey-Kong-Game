import pyxel

class Peach:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def drawPeach(self):
        #y-22 debido a la altura del personaje (22px)
        pyxel.blt(self.x,self.y-22,0,7,179,15,22,colkey=0)
