#Code for My Quiz Game

#Import libraries
import pygame #pygame library for all game functions
import random #Random library
import time   #Time Library

#Get all local files from pygame
from pygame.locals import *

#Initialize Pygame
pygame.init()

#Defining Colors (Defined as RGB)
white = (255,255,255)
black = (0,0,0,0)
grey = (200,200,100)
blackgloss = (43,43,43,0)
red = (255,0,0)
orange = (255,128,0)
yellow = (255,255,0)
green = (0,155,0)
blue = (0,100,255)
pink = (255,0,127)
purple = (204,0,204)
brown = (165,42,42)
lightbrown = (160,82,45)


#Game Display width and height variables
display_width = 800
display_height = 600

#Game Status (For Displaying different screens/levels
gamestatus = 0
global game_status

#Gamedisplay setting
gameDisplay = pygame.display.set_mode((display_width,display_height))

#Sets Caption at the top of the screen
pygame.display.set_caption("Thor Quizzr Volume 1")

#Clock (I use for fps)
clock = pygame.time.Clock()
fps = 60 #Frames Per Second Variable (Clock tick rate)

#Player Name
playerName = "anonymous"

#Game Images & assets
bg = pygame.image.load("resources/images/background.jpg")
bg1 = pygame.image.load("resources/images/background.png")
menubanner = pygame.image.load("resources/images/banner.png")
scorebanner = pygame.image.load("resources/images/scorebanner.png")
settingsbanner = pygame.image.load("resources/images/settingsbanner.png")
#Text
playtext = pygame.image.load("resources/text/play.png")
scoretext = pygame.image.load("resources/text/highscores.png")
settingstext = pygame.image.load("resources/text/settings.png")
quittext = pygame.image.load("resources/text/quit.png")
backtext = pygame.image.load("resources/text/back.png")

#Planets
sun = pygame.image.load("resources/planets/sun.jpg")
#Animation Assets
#animation = pygame.image.load("resources/animation/explosion.gif")
scene1 = pygame.image.load("resources/explosion/scene1.jpg")
scene2 = pygame.image.load("resources/explosion/scene2.jpg")
scene3 = pygame.image.load("resources/explosion/scene3.jpg")
scene4 = pygame.image.load("resources/explosion/scene4.jpg")
scene5 = pygame.image.load("resources/explosion/scene5.jpg")
scene6 = pygame.image.load("resources/explosion/scene6.jpg")
scene7 = pygame.image.load("resources/explosion/scene7.jpg")
scene8 = pygame.image.load("resources/explosion/scene8.jpg")
scene9 = pygame.image.load("resources/explosion/scene9.jpg")
scene10 = pygame.image.load("resources/explosion/scene10.jpg")
scene11 = pygame.image.load("resources/explosion/scene11.jpg")
scene12 = pygame.image.load("resources/explosion/scene12.jpg")
#scene13 = pygame.image.load("resources/explosion/scene13.jpg")
scene14 = pygame.image.load("resources/explosion/scene14.jpg")
scene15 = pygame.image.load("resources/explosion/scene15.jpg")
scene16 = pygame.image.load("resources/explosion/scene16.jpg")
scene17 = pygame.image.load("resources/explosion/scene17.jpg")
scene18 = pygame.image.load("resources/explosion/scene18.jpg")
scene19 = pygame.image.load("resources/explosion/scene19.jpg")
scene20 = pygame.image.load("resources/explosion/scene20.jpg")
scene21 = pygame.image.load("resources/explosion/scene21.jpg")
scene22 = pygame.image.load("resources/explosion/scene22.jpg")
scene23 = pygame.image.load("resources/explosion/scene23.jpg")
scene24 = pygame.image.load("resources/explosion/scene24.jpg")
scene25 = pygame.image.load("resources/explosion/scene25.jpg")
scene26 = pygame.image.load("resources/explosion/scene26.jpg")
scene27 = pygame.image.load("resources/explosion/scene27.jpg")

##def player_name(playerName): #This will currently run in shell, Working on putting into the Game
##     playerName = input("Welcome to ThorQuizzerV1 What is you're name?: ")
##
##     if playerName != "anonymous": #If player has entered a name
##         main_menu()#Go to Main Menu
##     elif playerName == "anonymous":
##         print("Please enter a name")
##         player_name(playerName)
        
#Main Menu Function, Runs if player name is entered
def main_menu():
    menu = True

    while menu:
         for event in pygame.event.get():
              if event.type == pygame.QUIT: #Quits
                   pygame.quit()
                   quit()
                   
              gameDisplay.blit(bg, (0,0))    #Background Img
              gameDisplay.blit(menubanner, (0,0))

              #Play Button
              pygame.draw.rect(gameDisplay, white, [300,200,220,55])
              gameDisplay.blit(playtext, (340,200))
              play_button(280,195,260,65, grey, action = 'play')

              #Settings Button
              pygame.draw.rect(gameDisplay, white, [300,280,220,55])
              gameDisplay.blit(settingstext, (300,280))
              settings_button(280,270,260,75, grey, action = 'settings')
              

              #HighScore Button
              pygame.draw.rect(gameDisplay, white, [300,360,220,55])
              gameDisplay.blit(scoretext, (300,365))
              high_score_button(280,350,260,75, grey, action = 'highscore')

              #Quit Button
              pygame.draw.rect(gameDisplay, white, [300,440,220,55])
              gameDisplay.blit(quittext, (340,440))
              quit_button(280,430,260,75, grey, action = 'quit')

              pygame.display.update()
              
#Play Button
def play_button(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
          pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
          gameDisplay.blit(playtext, (340,200))
          if click[0] == 1 and action != None:
               if action == "quit":
                    pygame.quit()
                    quit()
               elif action == "play":
                   game_loop()
#Settings Button
def settings_button(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(settingstext, (300,280))
         if click[0] == 1 and action != None:
             if action == "quit":
                 pygame.quit()
                 quit()
             elif action == "settings":
                   settings()

#HighScore button
def high_score_button(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(scoretext, (300,365))
         if click[0] == 1 and action != None:
             if action == "quit":
                 pygame.quit()
                 quit()
             elif action == "highscore":
                 high_scores()
         
         
#Quit
def quit_button(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(quittext, (340,440))
         if click[0] == 1 and action != None:
               if action == "quit":
                    pygame.quit()
                    quit()

def back_button(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(backtext, (340,440))
         if click[0] == 1 and action != None:
             if action == "back":
                 main_menu()
def back_button1(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(backtext, (340,440))
         if click[0] == 1 and action != None:
             if action == "back":
                 main_menu()
                 

def settings():
    print("The Settings Function has run")
    gameExit = False #Game Exit is = false

    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameexit is true and while loop will stop running
                gameExit = True
            
        gameDisplay.blit(bg, (0,0))
        gameDisplay.blit(settingsbanner, (0,0))

        #Back Button
        pygame.draw.rect(gameDisplay, white, [300,440,220,55])
        gameDisplay.blit(backtext, (340,440))
        back_button(280,430,260,75, grey, action = 'back')
              
        pygame.display.update()

def animation():
    animationplay = True

    while animationplay:
            gameDisplay.blit(scene1, (0,0))
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
            animationplay = False

    while not animationplay:
        print("animationplay = False")
        game_home()
            
        
        
    
    
def high_scores():
    print("The High Score Function has run")
    gameExit = False #Game Exit is = false

    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameexit is true and while loop will stop running
                gameExit = True
                
        gameDisplay.blit(bg, (0,0))
        gameDisplay.blit(scorebanner, (0,0))

        #Back Button
        pygame.draw.rect(gameDisplay, white, [300,440,220,55])
        gameDisplay.blit(backtext, (340,440))
        back_button1(280,430,260,75, grey, action = 'back') 

        pygame.display.update()       
          


#Gameloop, Mainloop for the game
def game_loop():

    gameExit = False #Game Exit is = false
    animationplay = True
    while not gameExit: #While Game Exit is not = true run everything below
                        #If it is it will escape the while loop and run quit code/gameover code at the bottom
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameexit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
        #time.sleep(2)
        #main_menu()
        while animationplay:
            animation()
            
        pygame.display.update()         #If anything is blit to the display, the display will have to be updated, it will update (fps) times per second
        clock.tick(fps)                 #Each Clocktick will run this loop again that many times per second, Defined by the clocktick variable

def game_home():
    gameExit = False #Game Exit is = false
    print("game home")
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameexit is true and while loop will stop running
                gameExit = True
        
    gameDisplay.blit(bg, (0,0))
    gameDisplay.blit(sun, (20,20))
    pygame.display.update
    clock.tick(fps)
        
main_menu()
game_loop()   #Will run gameloop firstly
pygame.quit() #Will Quit Game if the game_loop is escaped
quit()        #Quit
            
