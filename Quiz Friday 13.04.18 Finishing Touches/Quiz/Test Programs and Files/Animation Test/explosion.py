'''
Welcom to the test code for my Animation
- This code was not used in my game as was ean experiment to try make a gif in the game
- You cant quit properly as I havent added that code to this...
'''
#Import libraries
import pygame #pygame library for all game functions
import random #Random library
import time   #Time Library

#Get/Intitialize all local files for pygame
from pygame.locals import *

#Initialize Pygame
pygame.mixer.pre_init(44100, 16, 2, 4096) #Initializes mixer for click and other sounds
pygame.init() #Pygame Initialize all

#Game Display width and height variables
display_width = 800 #Display Width is 800 pixels
display_height = 600 #Display height is 600 pixels

#Gamedisplay setting
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.DOUBLEBUF, 32) #Initializes/Opens the Display

#Sets Caption at the top of the screen
pygame.display.set_caption("Thor Quizzr Volume 1") 

#Clock (I use for fps)
clock = pygame.time.Clock()
#fps = 120 #Frames Per Second Variable (Clock tick rate)

#Animation Assets
#animation = pygame.image.load("resources/animation/explosion.gif")
scene1 = pygame.image.load("resources/explosion/scene1.jpg")#Scene Load
scene2 = pygame.image.load("resources/explosion/scene2.jpg")#Scene Load
scene3 = pygame.image.load("resources/explosion/scene3.jpg")#Scene Load
scene4 = pygame.image.load("resources/explosion/scene4.jpg")#Scene Load
scene5 = pygame.image.load("resources/explosion/scene5.jpg")#Scene Load
scene6 = pygame.image.load("resources/explosion/scene6.jpg")#Scene Load
scene7 = pygame.image.load("resources/explosion/scene7.jpg")#Scene Load
scene8 = pygame.image.load("resources/explosion/scene8.jpg")#Scene Load
scene9 = pygame.image.load("resources/explosion/scene9.jpg")#Scene Load
scene10 = pygame.image.load("resources/explosion/scene10.jpg")#Scene Load
scene11 = pygame.image.load("resources/explosion/scene11.jpg")#Scene Load
scene12 = pygame.image.load("resources/explosion/scene12.jpg")#Scene Load
scene14 = pygame.image.load("resources/explosion/scene14.jpg")#Scene Load
scene15 = pygame.image.load("resources/explosion/scene15.jpg")#Scene Load
scene16 = pygame.image.load("resources/explosion/scene16.jpg")#Scene Load
scene17 = pygame.image.load("resources/explosion/scene17.jpg")#Scene Load
scene18 = pygame.image.load("resources/explosion/scene18.jpg")#Scene Load
scene19 = pygame.image.load("resources/explosion/scene19.jpg")#Scene Load
scene20 = pygame.image.load("resources/explosion/scene20.jpg")#Scene Load
scene21 = pygame.image.load("resources/explosion/scene21.jpg")#Scene Load
scene22 = pygame.image.load("resources/explosion/scene22.jpg")#Scene Load
scene23 = pygame.image.load("resources/explosion/scene23.jpg")#Scene Load
scene24 = pygame.image.load("resources/explosion/scene24.jpg")#Scene Load
scene25 = pygame.image.load("resources/explosion/scene25.jpg")#Scene Load
scene26 = pygame.image.load("resources/explosion/scene26.jpg")#Scene Load
scene27 = pygame.image.load("resources/explosion/scene27.jpg")#Scene Load

def animation():
    animationplay = True
    while animationplay:
        print(Restart) 
        gameDisplay.blit(scene1, (0,0)
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene2, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene3, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene4, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene5, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene6, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene7, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene8, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene9, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene10, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene11, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene12, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        #gameDisplay.blit(scene13, (0,0))
        #time.sleep(1)
        #pygame.display.update()
        gameDisplay.blit(scene14, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene15, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene16, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene17, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene18, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene19, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene20, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene21, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene22, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene23, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene24, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene25, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene26, (0,0))
        time.sleep(0.1)
        pygame.display.update()
        gameDisplay.blit(scene27, (0,0))
        time.sleep(0.1)
        pygame.display.update()

animation()
   
