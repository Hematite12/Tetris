import random, copy

from Constants import *

class Board:
    def __init__(self): 
        self.matrix = [[None for x in range(WIDTH)] for y in range(HEIGHT)]
        self.nextPieces = random.sample(PIECES, 7)
        self.pieceType = self.nextPieces[0]
        self.nextPieces = self.nextPieces[1:]
        self.pieceLocs = copy.deepcopy(PIECEPOSITIONS[self.pieceType])
        self.pieceOrigin = copy.deepcopy(PIECEORIGINS[self.pieceType])
        self.gameOver = False
        self.quickFallOver = False
    
    def drawLoc(self, x, y):
        drawPosX = MARGINWIDTH+CELLDIM*x+CELLMARGIN
        drawPosY = MARGINHEIGHT+CELLDIM*y+CELLMARGIN
        cellThickness = CELLDIM-2*CELLMARGIN
        rect(drawPosX,drawPosY,cellThickness,cellThickness,5)
    
    def show(self):
        fill(*GRIDBACKGROUND)
        rect(MARGINWIDTH,MARGINHEIGHT,CELLDIM*WIDTH,CELLDIM*HEIGHT)
        for x in range(WIDTH):
            for y in range(HEIGHT):
                fill(*COLOR_DICTIONARY[self.matrix[y][x]])
                self.drawLoc(x, y)
        if self.pieceType != None:
            fill(*COLOR_GHOST_DICTIONARY[self.pieceType])
            for ghostloc in self.getGhostLocs():
                self.drawLoc(ghostloc[0], ghostloc[1])
            fill(*COLOR_DICTIONARY[self.pieceType])
            for loc in self.pieceLocs:
                self.drawLoc(loc[0], loc[1])
    
    def checkStillFalling(self):
        doneFalling = False
        for loc in self.pieceLocs:
            if loc[1] == HEIGHT - 1:
                doneFalling = True
            elif self.matrix[loc[1]+1][loc[0]] != None:
                doneFalling = True
        return doneFalling
    
    def pieceFall(self, replace=True):
        self.checkCollision()
        if self.gameOver: return
        if self.checkStillFalling():
            self.quickFallOver = True
            if not replace: return
            for loc in self.pieceLocs:
                self.matrix[loc[1]][loc[0]] = self.pieceType
            if len(self.nextPieces) == 0:
                self.nextPieces = random.sample(PIECES, 7)
            self.pieceType = self.nextPieces[0]
            self.nextPieces = self.nextPieces[1:]
            self.pieceLocs = copy.deepcopy(PIECEPOSITIONS[self.pieceType])
            self.pieceOrigin = copy.deepcopy(PIECEORIGINS[self.pieceType])
        elif self.pieceType != None:
            for loc in self.pieceLocs:
                loc[1] = loc[1] + 1
            self.pieceOrigin[1] += 1
        self.checkRows()
    
    def quickFall(self, replace=True):
        self.quickFallOver = False
        while not self.quickFallOver:
            self.pieceFall(replace)
    
    def leftMost(self):
        farthestLeft = False
        for loc in self.pieceLocs:
            if loc[0] == 0:
                farthestLeft = True
            elif self.matrix[loc[1]][loc[0]-1] != None:
                farthestLeft = True
        return farthestLeft
    
    def rightMost(self):
        farthestRight = False
        for loc in self.pieceLocs:
            if loc[0] == WIDTH - 1:
                farthestRight = True
            elif self.matrix[loc[1]][loc[0]+1] != None:
                farthestRight = True
        return farthestRight
    
    def shiftLeft(self):
        if self.pieceType != None and not self.leftMost():
            for loc in self.pieceLocs:
                loc[0] = loc[0] - 1
            self.pieceOrigin[0] -= 1
    
    def shiftRight(self):
        if self.pieceType != None and not self.rightMost():
            for loc in self.pieceLocs:
                loc[0] = loc[0] + 1
            self.pieceOrigin[0] += 1
    
    def checkRows(self):
        for i in range(HEIGHT):
            row = self.matrix[i]
            if None not in row:
                self.matrix=[[None for x in range(WIDTH)]]+\
                self.matrix[:i]+self.matrix[i+1:]
    
    def checkCollision(self):
        for loc in self.pieceLocs:
            if self.matrix[loc[1]][loc[0]] != None:
                self.setGameOver()
                break
    
    def setGameOver(self):
        self.gameOver = True
    
    def inBounds(self):
        for loc in self.pieceLocs:
            if loc[0] < 0 or loc[0] >= WIDTH:
                return False
            if loc[1] < 0 or loc[1] >= HEIGHT:
                return False
            if self.matrix[loc[1]][loc[0]] != None:
                return False
        return True
    
    def moveLeft(self):
        for loc in self.pieceLocs:
            loc[0] = loc[0] - 1
        self.pieceOrigin[0] -= 1
    
    def moveRight(self):
        for loc in self.pieceLocs:
            loc[0] = loc[0] + 1
        self.pieceOrigin[0] += 1
    
    def rotatePieceClockwise(self):
        self.rotatePiece("clockwise")
    
    def rotatePieceCounterClockwise(self):
        self.rotatePiece("counterclockwise")
        
    def rotatePiece(self, dir):
        if self.pieceType == "O": return
        for loc in self.pieceLocs:
            loc[0] -= self.pieceOrigin[0]
            loc[1] -= self.pieceOrigin[1]
            if dir == "clockwise":
                temp = loc[1]
                loc[1] = loc[0]
                loc[0] = -1*temp
            elif dir == "counterclockwise":
                temp = loc[0]
                loc[0] = loc[1]
                loc[1] = -1*temp
            loc[0] += self.pieceOrigin[0]
            loc[1] += self.pieceOrigin[1]
        if not self.inBounds():
            self.moveRight()
            if not self.inBounds():
                self.moveLeft()
                self.moveLeft()
                if not self.inBounds():
                    self.moveRight()
                    if not self.pieceType == "I":
                        if dir == "clockwise":
                            self.rotatePieceCounterClockwise()
                        elif dir == "counterclockwise":
                            self.rotatePieceClockwise()
        if self.pieceType == "I" and not self.inBounds():
            self.moveRight()
            self.moveRight()
            if not self.inBounds():
                self.moveLeft()
                self.moveLeft()
                self.moveLeft()
                self.moveLeft()
                if not self.inBounds():
                    self.moveRight()
                    self.moveRight()
                    if dir == "clockwise":
                        self.rotatePieceCounterClockwise()
                    elif dir == "counterclockwise":
                        self.rotatePieceClockwise()
    
    def getGhostLocs(self):
        self.checkCollision()
        if self.gameOver:
            return []
        tempLocs = copy.deepcopy(self.pieceLocs)
        tempOrigin = copy.deepcopy(self.pieceOrigin)
        self.quickFall(False)
        ghostLocs = self.pieceLocs
        self.pieceLocs = tempLocs
        self.pieceOrigin = tempOrigin
        return ghostLocs
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    