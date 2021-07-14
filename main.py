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

    foodX = random.randrange(mainGameAreaXLeft,mainGameAreaXRight)
    foodY = random.randrange(mainGameAreaYTop,mainGameAreaYBottom)

    


    while not EXIT_GAME:
        
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
                    velocityY = -15

                # The below condition will increase the velocity of the snake when user presses the down key
                elif event.key == K_DOWN:
                    velocityX = 0
                    velocityY = 15
                
                # The below condition will increase the velocity of the snake when user presses the up key
                elif event.key == K_RIGHT:
                    velocityX = 15
                    velocityY = 0

                # The below condition will increase the velocity of the snake when user presses the up key
                elif event.key == K_LEFT:
                    velocityX = -15
                    velocityY = 0
        snakeX += velocityX
        time.sleep(0.03)
        snakeY += velocityY
        time.sleep(0.03)

        
            


        SCREEN.blit(mainGameImage,(0,0))
        pygame.draw.rect(SCREEN,red,(foodX,foodY,foodWidth,foodHeight))
        # From here we will start making the snake
        pygame.draw.rect(SCREEN,black,(snakeX,snakeY,snakeWidth,snakeHeight))
        pygame.display.update()
        # snakeX += velocityX
        # snakeY += velocityY
        # pygame.display.update()

                

        """ From here we will start the making the random food """

                # # Creating random coordinates for the area
                
                # foodX = random.randrange(mainGameAreaXLeft,mainGameAreaXRight)
                # foodY = random.randrange(mainGameAreaYTop,mainGameAreaYBottom)

                # pygame.draw.rect(SCREEN,red,(foodX,foodY,foodWidth,foodHeight))
                # pygame.display.update()
        
        
    
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