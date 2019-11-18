
import pyxel

WIDTH = 160
HEIGHT = 120
CAPTION = "This is an example of moving things in pyxel"

pyxel.init(WIDTH, HEIGHT, caption=CAPTION)
x = 10
y = 10



def move(x, y):
    ''' This function checks if the arrows of the keyboard are pressed and
    updates the x and y accordingly.'''
    # See all the keys at:
    # https://github.com/kitao/pyxel/blob/master/pyxel/__init__.py
    # If the arrows are pressed it updates x or y accordingly
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x >= 150):
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
        if (y >= 110):
            y = 110
        y = y + 1
    return x, y


# To use pyxel we need to define two functions, one will do all the
# calculations needed each frame, the other will paint things on the screen
# They can have any name, but the 'standard' ones are update and draw
def update():
    ''' This function is executed every frame. It invokes the move function
     which updates x and y of the circle'''
    # This marks that x and y are the ones defined at the beginning, but it is
    # not recommended to use it, in a near future we will see how to use object
    # orientation to avoid this
    global x, y
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    else:
        x, y = move(x, y)


def draw():
    ''' This function draws geometrical figures on the screen every turn'''
    # We set the background color, anything on the screen is erased
    # See pyxel documentation for available colors (16)
    # 0 is black
    pyxel.cls(1)
    pyxel.circ(x, y, 10, 10)


# To start the game we invoke the run method with the update and draw functions
pyxel.run(update, draw)