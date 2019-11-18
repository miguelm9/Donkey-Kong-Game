# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:48:02 2019

@author: Angel Garcia Olaya PLG-UC3M
@version: 1.0
Example of using graphics in pyxel
"""

import pyxel

x = 10
y = 10
WIDTH = 250
HEIGHT = 250
CAPTION = "This is an example of images in pyxel"

# The first thing to do is to create the screen, see API for more parameters
pyxel.init(WIDTH, HEIGHT, caption=CAPTION)
# Loading the pyxres file, it has a 16x16 cat in (0,0) in bank 0
pyxel.load("assets/jump_game.pyxres")
# Loading a 16x16 spaceship at bank 0 in (17,0)
pyxel.image(0).load(17, 0, "assets/cat_16x16.png")
pyxel.image(1).load(17,21, "assets/Ship.png")
def move (x,y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x >= WIDTH):
            x = 150
        x = x + 1
    elif pyxel.btn(pyxel.KEY_LEFT):
        if (x <= 10):
            x = 10
        x = x - 1
    elif pyxel.btn(pyxel.KEY_UP):
        if (y <= 10):
            y = 10
        y = y - 1
    elif pyxel.btn(pyxel.KEY_DOWN):
        if (y >= HEIGHT):
            y = 110
        y = y + 1

    return x,y


# To use pyxel we need to define two functions, one will do all the
# calculations needed each frame, the other will paint things on the screen
# They can have any name, but the 'standard' ones are update and draw
def update():
    ''' This function is executed every frame. Now it only checks if the user
    pressed Q to finish'''
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    else:
        move(x,y)

def draw():
    global x,y
    ''' This function draws graphics from the image bank'''
    pyxel.cls(3)

    #GATO 1
    b = pyxel.frame_count % pyxel.width
    #pyxel.blt(b, 10, 0, 33, 0, 16, 16, colkey=7)

    x, y = move(x, y)
    pyxel.blt(x,y,1,20,26, 16,16,colkey=0)

    pyxel.blt(b, 30, 0, 17, 0, 16, 16, colkey=5)
    # A space ship, we can use an additional parameter to specify which is the
    # background color of the image (notice the difference with previous one)

    #Gato 2



# To start the game we invoke the run method with the update and draw functions
pyxel.run(update, draw)