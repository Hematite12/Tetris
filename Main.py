from Constants import *
from Board import *

def setup():
    global b, paused
    size(CANVASWIDTH, CANVASHEIGHT)
    background(*BACKGROUND)
    b = Board()
    paused = False

def draw():
    background(*BACKGROUND)
    b.show()
    if frameCount%(60//DROPSPEED)==0 and not b.gameOver and not paused:
        b.pieceFall()

def keyPressed():
    global b, paused
    if not b.gameOver:
        if keyCode == UP:
            b.rotatePieceClockwise()
        if keyCode == LEFT:
            b.shiftLeft()
        if keyCode == RIGHT:
            b.shiftRight()
        if keyCode == DOWN:
            b.pieceFall()
        if key == " ":
            b.quickFall()
        if key == "p":
            paused = not paused
    if key == ENTER:
        b = Board()