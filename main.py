import random
import sys
import pygame
from pygame.locals import *
import time

# Creating Global Game Variables

EXIT_GAME = False
FPS = 32 # Frames per second
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # Making the screen


""" From here we will start making the functions that will be used in main game functions """

def showText(text, color, x, y):
    screen_text = font.render(text, True, color)
    SCREEN.blit(screen_text, [x,y])

def drawSnake(screen,color,list,width,height):
     for x,y in list:
        pygame.draw.rect(screen, color, (x, y, width, height))

def drawFood(screen,color,x,y,width,height):
    pygame.draw.rect(screen,color,(x,y,width,height))


""" Here we will end making the functions that will be used in main game functions """

""" From here we will start making the main game functions """


def welcomeScreen():
    """ This function will produce the welcome screen of the game """
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:

                # The below line will detect if user presses the enter key and will run the mainGame() which will intialise the main game window
                if event.key == K_RETURN:
                    mainGame()
                
                # The below line will detect if user presses the Spacebar and will run the instructions() which will intialise the instructions window
                elif event.key == K_SPACE:
                    instructions()

            else:
                SCREEN.blit(welcomeScreenImage,(0,0))
                pygame.display.update()
                FPSCLOCK.tick(FPS)



def mainGame():
    """ This is the main function of the whole game it has the main window in which the main game will run """

    # Initaialising the main velocity and increment variables
    global EXIT_GAME
    global snakeX
    global snakeY
    global velocityX
    global velocityY
    global SCORE
    global highScore

    
    snakeList = []
    snakeLength = 1

    gameOverBool = False

    foodX = random.randint(mainGameAreaXLeft + 30,mainGameAreaXRight - 30)
    foodY = random.randint(mainGameAreaYTop + 30,mainGameAreaYBottom - 30)
    velocityX = 0
    velocityY = 0
    backgroundMusic.play()


    while not EXIT_GAME:

        if gameOverBool:
            SCORE = 0
            backgroundMusic.stop()
            explodeMusic.play()
            time.sleep(0.1)
            snakeX = 120
            snakeY = 240
            velocityX =0
            velocityY = 0
            gameOver()

        else:        
            for event in pygame.event.get():

                # if user clicks on cross button, close the game
                if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                    # pygame.quit()
                    # sys.exit()
                    EXIT_GAME = True
                
                if event.type == KEYDOWN:
                    # The below condition will increase the velocity of the snake when user presses the up key
                    if event.key == K_UP:
                        velocityX = 0
                        velocityY = -2

                    # The below condition will increase the velocity of the snake when user presses the down key
                    elif event.key == K_DOWN:
                        velocityX = 0
                        velocityY = 2
                    
                    # The below condition will increase the velocity of the snake when user presses the up key
                    elif event.key == K_RIGHT:
                        velocityX = 2
                        velocityY = 0

                    # The below condition will increase the velocity of the snake when user presses the up key
                    elif event.key == K_LEFT:
                        velocityX = -2
                        velocityY = 0
                    
                    elif event.key == K_SPACE:
                        pauseGame()

        snakeX += velocityX
        # time.sleep(0.03)
        snakeY += velocityY
        # time.sleep(0.03)

        if abs(snakeX - foodX)<9 and abs(snakeY - foodY)<9:
            foodX = random.randint(mainGameAreaXLeft + 30,mainGameAreaXRight - 30)
            foodY = random.randint(mainGameAreaYTop + 30,mainGameAreaYBottom - 30)
            SCORE += 10
            snakeLength += 5

            
        
        if abs(snakeX - mainGameAreaXLeft)<15 or abs(snakeX - mainGameAreaXRight)<15 or abs(snakeY - mainGameAreaYTop)<10 or abs(snakeY - mainGameAreaYBottom)<20:
            gameOverBool = True

        head = []
        head.append(snakeX)
        head.append(snakeY)
        snakeList.append(head)

        if len(snakeList)>snakeLength:
            del snakeList[0]

        if head in snakeList[:-1]:
            gameOverBool = True
            print("Snake collided with itself")
        

        

        

        

        
            
        scoreScreen = f"Score : {SCORE}"

        SCREEN.blit(mainGameImage,(0,0))
        drawFood(SCREEN, red, foodX, foodY, foodWidth, foodHeight)
        showText(scoreScreen, red, 12, 12)
        # From here we will start making the snake
        drawSnake(SCREEN, black, snakeList , snakeWidth, snakeHeight)
        pygame.display.update()
        # snakeX += velocityX
        # snakeY += velocityY
        # pygame.display.update()
        

                

        """ From here we will start the making the random food """
        
    
    FPSCLOCK.tick(FPS)
    pygame.quit()
    quit()
    
    
    
    
        



def pauseGame():
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    mainGame()
                
                elif event.key == K_SPACE:
                    welcomeScreen()
                
                elif event.key == K_RETURN:
                    SCORE = 0
                    time.sleep(0.1)
                    snakeX = 120
                    snakeY = 240
                    velocityX =0
                    velocityY = 0
                    gameOver()
                
            else:
                SCREEN.blit(pauseImage,(0,0))
                pygame.display.update()

def gameOver():
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    mainGame()
                
                elif event.key == K_SPACE:
                    welcomeScreen()

            else:
                SCREEN.blit(gameOverImage,(0,0))
                pygame.display.update()

def instructions():
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            else:
                SCREEN.blit(instructionsImage,(0,0))
                pygame.display.update()



""" Here we will end making the main game functions """





if __name__ == '__main__':
    # This will be the main point from where our game will start
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Snakes Game') # Setting the title
    SCORE = 0
    high_score_list = [0]
    highScore = high_score_list[0]
    font = pygame.font.SysFont(None, 55)


    """ From here we will start to make variables of colors """
    darkGreen = (13, 74, 40)
    black = (0,0,0)
    red = (217, 7, 10)


    """ From here we will start to make variables that are needed to make the snake and its food """
    snakeX = 120
    snakeY = 240
    snakeWidth = 30
    snakeHeight = 30

    foodWidth = 28
    foodHeight = 28

    """ Velocity variables """
    velocityX = 10
    velocityY = 10

    """ From here we will start making the variables of arena """
    mainGameAreaXLeft = 66
    mainGameAreaXRight = 830

    mainGameAreaYTop = 53
    mainGameAreaYBottom = 540

    """ Music game variables """
    backgroundMusic = pygame.mixer.Sound('gallery/audio/background.mp3')
    beepMusic = pygame.mixer.Sound('gallery/audio/beep.mp3')
    explodeMusic = pygame.mixer.Sound('gallery/audio/explode.mp3')



    """ From Here we will set the images in variables in the game """


    welcomeScreenImage = pygame.image.load("gallery/sprites/welcome_screen_bg.jpg").convert()
    welcomeScreenImage = pygame.transform.scale(welcomeScreenImage, (SCREEN_WIDTH, SCREEN_HEIGHT)) 


    mainGameImage = pygame.image.load("gallery/sprites/main_game_bg.jpg").convert()
    mainGameImage = pygame.transform.scale(mainGameImage, (SCREEN_WIDTH, SCREEN_HEIGHT))

    instructionsImage = pygame.image.load("gallery/sprites/instructions_bg.jpg").convert()
    instructionsImage = pygame.transform.scale(instructionsImage, (SCREEN_WIDTH, SCREEN_HEIGHT))


    pauseImage = pygame.image.load("gallery/sprites/pause_bg.jpg").convert()
    pauseImage = pygame.transform.scale(pauseImage, (SCREEN_WIDTH, SCREEN_HEIGHT))

    gameOverImage = pygame.image.load("gallery/sprites/game_over_bg.jpg").convert()
    gameOverImage = pygame.transform.scale(gameOverImage, (SCREEN_WIDTH, SCREEN_HEIGHT))



    """ From Here we will set the music in variables in the game """

    welcomeScreen()