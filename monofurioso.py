import pyxel

class MonoFurioso ():
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__monoAppear = 0
    def drawMonoCenter(self):
        pyxel.blt(self.__x-40,self.__y-31,0,8,213,40,31, colkey=0)
    def drawMonoRight(self):
        pyxel.blt(self.__x-43,self.__y-31,0,53,58,-43,31, colkey=0)
    def drawMonoLeft(self):
        pyxel.blt(self.__x-43,self.__y-31,0,53,58,43,31, colkey=0)

    def drawMono(self):
        if pyxel.frame_count % 60 == 0:
            self.__monoAppear = 1
        elif pyxel.frame_count % 60 == 20:
            self.__monoAppear = 2
        elif pyxel.frame_count % 60 == 40:
            self.__monoAppear = 3

        if self.__monoAppear == 1:
            self.drawMonoRight()
        elif self.__monoAppear == 2:
            self.drawMonoLeft()
        elif self.__monoAppear == 3:
            self.drawMonoCenter()