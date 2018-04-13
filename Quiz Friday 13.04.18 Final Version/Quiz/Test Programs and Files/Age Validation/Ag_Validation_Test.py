'''
Age Validation Test Program
This Program Runs the pygame window and asks for user input/user age and checks whether these are correct
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

#Defining Colors (Defined as RGB)
white = (255,255,255) #White
black = (0,0,0,0) #Black
grey = (200,200,100) #Grey
blackgloss = (43,43,43,0) #Glossblack experiment
red = (255,0,0) #Red
orange = (255,128,0) #Orange
yellow = (255,255,0) #Yellow
green = (0,155,0) #Green
blue = (0,100,255) #Blue
pink = (255,0,127) #Pink
purple = (204,0,204) #Purple
brown = (165,42,42) #Brown
lightbrown = (160,82,45) #Light Brown
transparent = (0,0,0,0) #Transparent

#Game Display width and height variables
display_width = 800 #Display Width is 800 pixels
display_height = 600 #Display height is 600 pixels

#Gamedisplay setting
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.DOUBLEBUF, 32) #Initializes/Opens the Display

#Sets Caption at the top of the screen
pygame.display.set_caption("Thor Quizzr Volume 1") 

#Clock (I use for fps)
clock = pygame.time.Clock()
fps = 120 #Frames Per Second Variable (Clock tick rate)

#Fonts for text in game
font = pygame.font.SysFont(None, 25)

#Player age Assets
clickaudio = pygame.mixer.Sound("resources/audio/click.wav") #Click Sound
age_up = pygame.image.load("up.png")#Image Load
age_down = pygame.image.load("down.png")#Image Load
age_banner = pygame.image.load("age_banner.png")#Image Load
ok = pygame.image.load("ok.png")#Image Load
quitimg = pygame.image.load("quit.png")#Image Load
bg = pygame.image.load("background.jpg")#Image Load
player_age = 15 #Starting age = 15

def text_objects(text, color): #This Function Prints Text to the Screen
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
    pygame.display.update() #Updates the Display
    
def age(): #First Function To run AGE - Asks for player age
    global player_age #Makes the player_age variable editable from within the function
    age_input = False #No age has been input
    gameExit = False #Game has not exited

    while not gameExit: #While game is open
        for event in pygame.event.get(): #If Some one click the quit button then quit
            if event.type == pygame.QUIT: #If quit button clicked
                pygame.quit() #Quits
                quit() #Quits

        gameDisplay.blit(bg, (0,0)) #Background #Background#Background image
        gameDisplay.blit(age_banner, (90,0)) #Age banner
        #Up Button
        gameDisplay.blit(age_up, (display_width/2 - 60, display_height/2 - 40)) #Button Text
        age_button(display_width/2 - 60,display_height/2 - 40,120,62, grey, action = 'up') #Button 
        #Down Button
        gameDisplay.blit(age_down, (display_width/2 - 60, display_height/2 + 100))#Image Blit
        age_button(display_width/2 - 60,display_height/2 + 100,120,63, grey, action = 'down')#Button 
        #Age Display
        pygame.draw.rect(gameDisplay, white, [display_width/2 - 60,display_height/2 + 32, 120, 60])#Draws a rectangle
        message_to_screen_age(str(player_age),black) #Actual text
        #Ok Button
        pygame.draw.rect(gameDisplay, white, [display_width/2 - 60, display_height/2 + 170, 120, 60])#Draws a rectangle
        age_button(display_width/2 - 60, display_height/2 + 170, 120, 60, grey, action = 'ok')#Button 
        gameDisplay.blit(ok, (display_width/2 - 60, display_height/2 + 155))#Image Blit
        if player_age > 100: #If player age is greater than 100 set it to 100
            player_age = 100
        elif player_age < 1 or player_age > 100: #Else you cant be 0 to if less than 1 then set to 1
            player_age = 1
        pygame.display.update() #Updates the Display #Updates the display
        clock.tick(fps) #Runs this function at the game FPS value #Runs the function at FPS

def age_button(x,y,width,height,active_color, action = None): # Function for all the buttons to do with age
     cur = pygame.mouse.get_pos() #Gets Cursor Position #Gets mouse Position
     click = pygame.mouse.get_pressed() #Checks for mouse click #Checks if mouse button is pressed
     global player_age #Makes Player age global
     if x + width > cur[0] > x and y + height > cur[1] > y:#Checks if mouse position is over the button #If mouse position is over the button
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height)) #Draw a bigger rectangle to show active
         gameDisplay.blit(age_up, (display_width/2 - 60, display_height/2 - 40)) #Draws image back on top
         gameDisplay.blit(age_down, (display_width/2 - 60, display_height/2 + 100)) #Draws image bakc on top
         
         if click[0] == 1 and action != None: #If Button is clicked and action is not equal to nothing #If click
             if action == "quit": #If the action (button clicked) is quit 
                 pygame.quit() #Quits #quit
                 quit() #Quits #quit
             elif action == "up": #If age up button pressed
                 clickaudio.play() #Plays the Click audio  #Click sound 
                 player_age += 1 #Adds 1 to the planets score #Player age plus 1
                 time.sleep(0.5) #Pauses the game for 0.5 seconds #Sleep for 0.5 to ensure it doesnt change by alot
             elif action == "down":#If age down button pressed
                 clickaudio.play() #Plays the Click audio#Click sound 
                 player_age -= 1 #Player age minus 1
                 time.sleep(0.5) #Pauses the game for 0.5 seconds #Sleep for 0.5 to ensure it doesnt change by alot
             elif  action == "ok": #If ok button is pressed
                 clickaudio.play() #Plays the Click audio#Click sound 
                 age_validation() #Run the age validation function
                
def message_to_screen_age(msg, color): #Prints The Players age to the screen
    textSurf, textRect = text_objects(msg,color) #Text Surface
    textRect = (display_width/2 - 10), (display_height/2 + 50)#Text Rectangle
    gameDisplay.blit(textSurf, textRect) #Puts them on the display

def age_validation(): #Checks if user is able to play
    print("Your age is", player_age) #Prints their age to shell (Testing)
    if player_age >= 10 and player_age <= 18: #If thier age is within the range (10-18)
        print("Congratulation you are eligible to play") #Thier eligible
        val_yes() #Run the Yes function 
    else:
        print("You are not eligable to play but you may still continue") #If thier age is not within the requirements
        val_no() #Run the No function

def val_yes(): #Function to tell the user they are eligible
    gameExit = False #Game Hasnt exited

    while not gameExit: #While it hasnt exited
        for event in pygame.event.get(): #Get events
            if event.type == pygame.QUIT: #If quit button clicked #If quit button
                pygame.quit() #Quits 
                quit() #Quits 
            gameDisplay.blit(bg, (0,0)) #Background 
            message_to_screen_val("You are eligible to play :)", green) #Actual Text
            pygame.draw.rect(gameDisplay, white, [display_width/2 - 60, display_height/2 + 140, 120, 60])#Draws a rectangle
            gameDisplay.blit(ok, (display_width/2 - 65, display_height/2 + 130))#Image Blit
            ok_button(display_width/2 - 60, display_height/2 + 140, 120, 60, grey, action = 'ok')#Button 
            pygame.display.update() #Updates the Display
            

def val_no():
    gameExit = False

    while not gameExit: #While Game Hasnt exited
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If quit button clicked
                pygame.quit() #Quits
                quit() #Quits
            gameDisplay.blit(bg, (0,0)) #Background  
            message_to_screen_val("You are not eligible to play", red)#Actual text
            pygame.draw.rect(gameDisplay, white, [display_width/2 - 60, display_height/2 + 140, 120, 60])#Draws a rectangle
            gameDisplay.blit(ok, (display_width/2 - 65, display_height/2 + 130))
            ok_button(display_width/2 - 60, display_height/2 + 140, 120, 60, grey, action = 'quit')#Button 
            pygame.display.update() #Updates the Display
            
def message_to_screen_val(msg, color): #This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (display_width/2 - 100), (display_height/2)
    gameDisplay.blit(textSurf, textRect)#Image Blit



def ok_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos() #Gets Cursor Position
    click = pygame.mouse.get_pressed() #Checks for mouse click
    global player_age
    if x + width > cur[0] > x and y + height > cur[1] > y:#Checks if mouse position is over the button
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))#Draws a rectangle
        gameDisplay.blit(ok, (display_width/2 - 65, display_height/2 + 130))#Image Blit
        if click[0] == 1 and action != None: #If Button is clicked and action is not equal to nothing
            if action == "quit":
                pygame.quit() #Quits
                quit() #Quits
            if action == "ok":
                clickaudio.play() #Plays the Click audio
                time.sleep(0.1)
                #NOTHING HAPPENS AS THERE IS NO MAIN MENU IN THIS CODE

age()
pygame.quit()
quit()
