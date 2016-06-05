# SASQUATCH MOUNTAIN
# CPSC 386
# Team: Bright Light Sasquatch Squad!! (Extreme Force)

import pygame, random
pygame.init()

class PlayerObj():
    def __init__(self, name, pieceimage, faceimage): # Add faceimage and pieceimage
            self.face = faceimage
            self.piece = pieceimage
            self.coords = []
            self.pos = 0 #Position in map[]
            self.finished = False
            self.score = 0
            self.roundsCompleted = 1
            self.name = name
            
    def getName(self):
        return "Player " + str(self.name)
    
##    def move(self, steps, direction):
##            if direction:
##                    self.pos += steps
##            else:
##                    if pos >= len(map):
##                            self.finished = true
##                            pos = endPos
##                    elif pos < 0:
##                            pos = 0
##                    else:
##                            pos = 0
##    
##    def rollDice(self):
##            n = random.randint(1,10)
##            self.face = n
##    #corresponding to the face
##
##    def getDice(self):
##            return self.face
##
##    def get_image(self):
##            return self.face
##
##    def set_score(self, score):
##            self.score+=score
##
##    def get_score(self):
##            return self.score
##
##    def currentPosition(self):
##            return self.pos
##
##    def makeCompleted(self):
##            self.finished = true
##
##    def isFinished(self):
##            return self.finished
##
##    def set_roundsCompleted(self, numRound):
##            self.roundsCompleted = numRound
##
##    def get_roundsCompleted(self):
##            return self.roundsCompleted
