import pyxel

class MonoFurioso ():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def drawMonoFurioso (self):
        pyxel.blt(self.x,self.y,0,6,58,38,31,colkey=0)

#(6,58) hasta (,)
