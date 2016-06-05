# SASQUATCH MOUNTAIN
# CPSC 386
# Team: Bright Light Sasquatch Squad!! (Extreme Force)

import os, pygame, random, time
from pygame.locals import *
import PlayerObj

pygame.init()

###################################### FUNCTIONS ###############################################
#Function to display the background image
def refreshBG():
        #load image file and rescale it to fit screen size
        background = pygame.image.load("bg.png")
        background = pygame.transform.scale(background, size)
        #get rectangular area of image
        rect = background.get_rect()
        #render image
        screen.blit(background, rect)
        
#Function to update current UI
def refreshUI():
        refreshBG()
        y1 = 0
        x=50
        for i in range(0, numPlayers):
                #display players' info
                getText(player[i].getName() + ", Score: " + str(player[i].score), white, 30, (0, y1))
                #display players' pieces on the starting location
                piece = pygame.image.load(player[i].piece)
                piece = pygame.transform.scale(piece, (35, 35))
                screen.blit(piece, player[i].coords[player[i].pos])
                #display face that are corresponding to each player
                face = pygame.image.load(player[i].face)
                face = pygame.transform.scale(face, (60, 60))
                screen.blit(face, (0, y1+20))
                
                piece = pygame.image.load(player[i].piece)
                piece = pygame.transform.scale(piece, (60, 60))
                screen.blit(piece, (x, y1+20))
                y1 += 100
                #display instruction
                getText("Press LEFT to move backward" , orange, 28, (width-290, 0))
                getText("Press RIGHT to move forward" , orange, 28, (width-290, 28))
                getText("Press SPACE to end turn" , orange, 28, (width-290, 56))
                #TODO: Refresh sasquatch pieces and images
                if sasquatchOut:
                        sasquatch = pygame.image.load("sq.png")
                        sasquatch = pygame.transform.scale(sasquatch, (50, 50))
                        screen.blit(sasquatch, sascoords[saspos])
                
#Check if game is done
def isGameDone():
        gameDone = True
        for i in range (0, numPlayers):
                if not player[i].finished:
                        gameDone = False

        return gameDone

#Function to render text with its color, size and location
def getText(text, color, sizeText, location):
    front = pygame.font.SysFont(None, sizeText)
    title = front.render(text, True, color)
    screen.blit(title, location)

#Function to display game instruction and prompt user for number of players
def welcome():
    getText("Sasquatch Mountain", black, 60, (220,30))
    getText("Goal: Climb the mountain as high as you can with the most points!", black, 25, (155,80))
    getText("Land on green squares and earn 1-3 points!", black, 25, (235, 100))
    getText("Land on red squares and lose 1-3 points!", black, 25, (245, 120))
    
    #draw a rectangular shape 'rect(Surface, color, Rect, thickness=0)'
    #Rect = ((coordinates x y of upper left hand corner), rect width, rect height)
    pygame.draw.rect(screen, orange, (325, 360, 200, 80), 0)
    
    getText("Press 2 for two players", white, 20, (345, 365))
    getText("Press 3 for three players", white, 20, (345, 385))
    getText("Press 4 for four players", white, 20, (345, 405))
    getText("Press ESC to quit game", white, 20, (345, 425))
    
    #display all texts
    pygame.display.flip()


#Function to get the input of user for number of players and create player list based on that number
def getPlayers():
    playersCounted = False
    global turns
    global numPlayers
    while not playersCounted:
        for event in pygame.event.get():
        #terminate if user press x button on the left corner
            if event.type == pygame.QUIT:
                os._exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    os._exit(0)
                if event.key == pygame.K_2:
                    numPlayers = 2
                    turns = [0,1]
                    playersCounted = True
                if event.key == pygame.K_3:
                    numPlayers = 3
                    turns = [0, 1, 2]
                    playersCounted = True
                if event.key == pygame.K_4:
                    numPlayers = 4
                    turns = [0, 1, 2, 3]
                    playersCounted = True

def endTurn():
        global space2Continue
        global turnFinished
                
        while space2Continue:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                os._exit(0)
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                        os._exit(0)
                                if event.key == K_SPACE:
                                        turnFinished = True
                                        space2Continue = False

#Function to shuffle players' turn order
def shuffle():
        #display shuffling message
        refreshBG()
        getText("Shuffling players' turn order...", white, 30, (265, 395))
        pygame.display.flip()
        pygame.time.delay(500)

        #Decide turn order
        random.shuffle(turns)

        #create player list
        for i in range(0, numPlayers):
                x = PlayerObj.PlayerObj(turns[i]+1, "p" + str(i+1) + ".png", "f" + str(i+1) + ".png")
                player.append(x)
                
        #Display players' turn order
        refreshBG()
        getText("Players' order", white, 30, (340, 370))
        x=255
        for i in range(0, numPlayers):
                getText(player[i].getName() + " " , white, 25, (x, 400))
                x=x+80
        pygame.display.flip()

#Set piece coordinates
def setPieceCoords():
        for i in range(0, numPlayers):
                for j in range (0, 11):
                        player[i].coords.append((725-(j*65), 585+(i*20)))
                for j in range (0, 9):
                        player[i].coords.append(((j*65)+140, 455+(i*20)))
                for j in range (0, 5):
                        player[i].coords.append((530-(j*65), 315+(i*20)))
                for j in range(0, 3):
                        player[i].coords.append(((j*65)+340, 250+(i*20)))
                for j in range(0, 3):
                        player[i].coords.append((465-(j*65), 185+(i*20)))
                for j in range(0, 3):
                        player[i].coords.append(((j*65)+335, 115+(i*20)))

        for j in range (0, 11):
                sascoords.append((725-(j*65), 585))
        for j in range (0, 9):
                sascoords.append((140+(j*65), 455))
        for j in range (0, 5):
                sascoords.append((530-(j*65), 315))
        for j in range(0, 3):
                sascoords.append((340+(j*65), 250))
        for j in range(0, 3):
                sascoords.append((465-(j*65), 185))
        for j in range(0, 3):
                sascoords.append((335+(j*65), 115))

def getDice(n):
        dice = pygame.image.load("dice" + str(n) + ".bmp")
        dice = pygame.transform.scale(dice, (30, 30))
        screen.blit(dice, (410, 45))
        getText("Rolled", black, 25, (405, 25))
        pygame.display.flip()
                
###################################### INITIALIZATION ###############################################
#set application's name
pygame.display.set_caption('Sasquatch Mountain')

#set colors
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
orange = (120, 60, 0)

#set screen size
width = 850
height = 700
size = (width, height)
screen = pygame.display.set_mode(size)

#number of Players
numPlayers = 0

#Create player list
player = []

#list for shuffling players' turn order
turns = []

#Tile color map (34 spaces total)
#2 = start ; 3 = finish ; 0 = green ; 1 = red 
map = [2,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,0,3]

#Initialize game vars
gameDone = False
gameRound = 1
sasquatchOut = False
saspos = 0
space2Continue = False #starts off; set to True when waiting for user input
sascoords = []

###################################### MAIN ###############################################

#display background image
refreshBG()
pygame.display.flip()

#display welcome message and ask user for number of players
welcome()

#generate player list based on user's input
getPlayers()

#shuffle players' turn order
shuffle()

#set each player's piece coordinates
setPieceCoords()

#START GAME LOOP
while not gameDone:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        os._exit(0)
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                os._exit(0)
                        
        #Refresh interface
        refreshUI()
        
        #Release sasquatch
        if gameRound == 2:
                sasquatchOut = True
                saspos = 0
                getText("The sasquatch is coming!", red, 60, (180, 320))
                pygame.display.flip()
                time.sleep(1.5)
                refreshUI()
                pygame.display.flip()
                
        print(player)
        for i in range (0, numPlayers):
                if not player[i].finished:
                        #display a player's turn
                        refreshUI()
                        getText(player[i].getName() + "'s turn!", black, 25, (365, 10))
                        pygame.display.flip()
                                                
                        #handle input from that player
                        turnFinished = False
                        while not turnFinished:
                                for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                                os._exit(0)
                                        if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_ESCAPE:
                                                        os._exit(0)
                                                #If going forward
                                                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                                                        n = random.randint(1,6)
                                                        
                                                        #get the dice face the player got
                                                        getDice(n)
                                                        
                                                        #get the number of spaces and the moving direction
                                                        #Set piece location with p#coords in relation to player's pos
                                                        if (event.key==pygame.K_RIGHT):
                                                                getText("Going " + str(n) + " space forward!", black, 20, (345, 75))
                                                                player[i].pos += n
                                                        else:
                                                                if player[i].pos == 0:
                                                                        player[i].finished = True
                                                                        getText("Player " + str(turns[i]+1) + " fell off the mountain and cannot move anymore!", red, 36, (95, 360))
                                                                        pygame.display.flip()
                                                                        space2Continue = True
                                                                        endTurn()
                                                                        continue
                                        
                                                                getText("Going " + str(n) + " space backward!", black, 20, (345, 75))
                                                                player[i].pos -= n

                                                        
                                                        #Check for passing start or sasquatch
                                                        if player[i].pos <= 0:
                                                                player[i].pos = 0
                                                        if player[i].pos <= saspos:
                                                                player[i].finished = True
                                                                player[i].roundsCompleted = gameRound
                                                                getText("Got mauled and cannot move anymore!", red, 25, (260, 115))
                                                                
                                                        #Check for passing end
                                                        if player[i].pos >= 33:
                                                                player[i].pos = 33
                                                                player[i].finished = True
                                                                player[i].roundsCompleted = gameRound
                                                                refreshUI()
                                                                getText(player[i].getName() + " reached the end!", black, 20, (340, 30))
                                                        
                                                        #Update score
                                                        m = random.randint(1,3)
                                                        if map[player[i].pos] == 1:
                                                                player[i].score -= m
                                                                getText("Land on red space, lost " + str(m) + " points!",  black, 20, (310, 90))
                                                        else:
                                                                player[i].score += m
                                                                getText("Land on green space, gained " + str(m) + " points!", black, 20, (300, 90))
                                                                
                                                        #display everything to the screen
                                                        pygame.display.flip()
                                                        #End turn
                                                        space2Continue = True
                                                        endTurn()

        refreshUI()
        winner = player[0]
        soleSurvivor = False
        #Check winner and/or decide tiebreaker
        if isGameDone():
                
                #winningScore = player[0].score
                #leastRounds = player[0].roundsCompleted
                tieBreaker = False
                for i in range(1, numPlayers):
                        #Check for highest points
                        if player[i].score > winner.score:
                                winner = player[i]
                                #winningScore = player[i].score
                        #Check for quickest finish if tie exists
                        else:
                                if player[i].score == winner.score:
                                        tieBreaker = True
                                        if player[i].roundsCompleted < winner.roundsCompleted:
                                                winner = player[i]
                                                #leastRounds = player[i].roundsCompleted
                #Display winner
                refreshUI()
                if tieBreaker:
                        getText(winner.getName() + " won with " + str(winner.score) + " points and finishing sooner!", red, 36, (140, 300))
                else:
                        getText(winner.getName() + " won with " + str(winner.score) + " points!", red, 36, (260, 320))
                getText("Hit ESC to exit", red, 25, (360, 360))
                pygame.display.flip()
                space2Continue = True
                while space2Continue:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        os._exit(0)
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                                os._exit(0)                
                
        #If game not done, proceed with sasquatch's turn
        else:
                if (gameRound >=2):
                        getText("Sasquatch's turn!", black, 25, (365, 10))
                        pygame.display.flip()
                        pygame.time.delay(500)
                        n=random.randint(1, 3)
                        getDice(n)
                        getText("Going " + str(n) + " space forward!", black, 20, (355, 75))
                        pygame.display.flip()
                        saspos += n
                        pygame.time.delay(300)
                        
                        #check if any players got mauled
                        for i in range(0, numPlayers):
                                if player[i].pos <= saspos and not player[i].finished:
                                        player[i].finished = True
                                        refreshUI()
                                        getText(player[i].getName() + " got mauled and cannot move anymore!", red, 36, (180, 100))
                                        pygame.display.flip()


        #Advance game round
        gameRound += 1
        
#END GAME LOOP
