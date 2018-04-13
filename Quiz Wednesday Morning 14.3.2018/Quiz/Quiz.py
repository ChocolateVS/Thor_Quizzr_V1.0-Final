#Code for My Quiz Game

#Import libraries
import pygame #pygame library for all game functions
import random #Random library
import time   #Time Library

#Get all local files from pygame
from pygame.locals import *

#Initialize Pygame
pygame.mixer.pre_init(44100, 16, 2, 4096)
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

#Score
score = 0

#Get Settings
with open('resources/files/fps.txt', 'r') as f:
    fps = int(f.read(3))
    print("FPS = ", fps)

with open('resources/files/tutorial.txt', 'r') as g:
    tutorial = g.read()
    print("Tutorial = ", tutorial)

with open('resources/files/sound.txt', 'r') as s:
    sound = s.read()
    print("Sound = ", sound,"%")
    
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
#fps = 120 #Frames Per Second Variable (Clock tick rate)

#Font
font = pygame.font.SysFont(None, 25)

#Player
playerName = "anonymous" #Player Name
player_speed = 5

#Sound
clickaudio = pygame.mixer.Sound("resources/audio/click.wav")
#Settings
controls = pygame.image.load("resources/images/controls.png")
credits1 = pygame.image.load("resources/images/credits.png")
fpsimg = pygame.image.load("resources/images/fps.png")
sound = pygame.image.load("resources/images/sound.png")
tutorial = pygame.image.load("resources/images/tutorial.png")
fpsimage1 = pygame.image.load("resources/text/30.png")
fpsimage2 = pygame.image.load("resources/text/60.png")
fpsimage3 = pygame.image.load("resources/text/120.png")
on = pygame.image.load("resources/text/on.png")
off = pygame.image.load("resources/text/off.png")
sound1 = pygame.image.load("resources/text/25.png")
sound2 = pygame.image.load("resources/text/50.png")
sound3 = pygame.image.load("resources/text/75.png")
sound4 = pygame.image.load("resources/text/100.png")
#Edit Button
edit = pygame.image.load("resources/images/edit.png")

#Game Images & assets
bg = pygame.image.load("resources/images/background.jpg")
bg1 = pygame.image.load("resources/images/background.png")
menubanner = pygame.image.load("resources/images/banner.png")
scorebanner = pygame.image.load("resources/images/scorebanner.png")
settingsbanner = pygame.image.load("resources/images/settingsbanner.png")
player = pygame.image.load("resources/images/player.png")

#Text On Planets
earth_text = pygame.image.load("resources/text/earth.png")
mars_text = pygame.image.load("resources/text/mars.png")
pluto_text = pygame.image.load("resources/text/pluto.png")
moon_text = pygame.image.load("resources/text/moon.png")
sun_text = pygame.image.load("resources/text/sun.png")
neptune_text = pygame.image.load("resources/text/neptune.png")
mercury_text = pygame.image.load("resources/text/mercury.png")
jupiter_text = pygame.image.load("resources/text/jupiter.png")
uranus_text = pygame.image.load("resources/text/uranus.png")
venus_text = pygame.image.load("resources/text/venus.png")
saturn_text = pygame.image.load("resources/text/saturn.png")

#Text
playtext = pygame.image.load("resources/text/play.png")
scoretext = pygame.image.load("resources/text/highscores.png")
settingstext = pygame.image.load("resources/text/settings.png")
quittext = pygame.image.load("resources/text/quit.png")
mainmtext = pygame.image.load("resources/text/mainm.png")
levelstext = pygame.image.load("resources/text/levels.png")
restarttext = pygame.image.load("resources/text/restart.png")
backtext = pygame.image.load("resources/text/back.png")
quizzes = pygame.image.load("resources/text/quizzes.png")
welldone = pygame.image.load("resources/text/welldone.png") 
greatjob = pygame.image.load("resources/text/great.png")
congrats = pygame.image.load("resources/text/congrats2.png")
congratulations = pygame.image.load("resources/text/congrats.png")

#Planets
sun = pygame.image.load("resources/planets/sun.jpg")
moon = pygame.image.load("resources/planets/moon.jpg")
earth = pygame.image.load("resources/planets/earth.jpg")
mars = pygame.image.load("resources/planets/mars.jpg")
venus = pygame.image.load("resources/planets/venus.jpg")
uranus = pygame.image.load("resources/planets/uranus.jpg")
neptune = pygame.image.load("resources/planets/neptune.jpg")
pluto = pygame.image.load("resources/planets/pluto.jpg")
jupiter = pygame.image.load("resources/planets/jupiter.jpg")
saturn = pygame.image.load("resources/planets/saturn.jpg")
mercury = pygame.image.load("resources/planets/mercury.jpg")

#Questions
#Earth
earth_question_1 = pygame.image.load("resources/questions/earth/question1.png")
earth_question_2 = pygame.image.load("resources/questions/earth/question2.png")
earth_question_3 = pygame.image.load("resources/questions/earth/question3.png")
earth_question_4 = pygame.image.load("resources/questions/earth/question4.png")
earth_question_5 = pygame.image.load("resources/questions/earth/question5.png")
earth_question_6 = pygame.image.load("resources/questions/earth/question6.png")
earth_question_7 = pygame.image.load("resources/questions/earth/question7.png")
earth_question_8 = pygame.image.load("resources/questions/earth/question8.png")
earth_question_9 = pygame.image.load("resources/questions/earth/question9.png")
earth_question_10 = pygame.image.load("resources/questions/earth/question10.png")
#Mars
##mars_question_1 = pygame.image.load("resources/questions/mars/question1.png")
##mars_question_2 = pygame.image.load("resources/questions/mars/question2.png")
##mars_question_3 = pygame.image.load("resources/questions/mars/question3.png")
##mars_question_4 = pygame.image.load("resources/questions/mars/question4.png")
##mars_question_5 = pygame.image.load("resources/questions/mars/question5.png")
##mars_question_6 = pygame.image.load("resources/questions/mars/question6.png")
##mars_question_7 = pygame.image.load("resources/questions/mars/question7.png")
##mars_question_8 = pygame.image.load("resources/questions/mars/question8.png")
##mars_question_9 = pygame.image.load("resources/questions/mars/question9.png")
##mars_question_10 = pygame.image.load("resources/questions/mars/question10.png")
###Moon
##moon_question_1 = pygame.image.load("resources/questions/moon/question1.png")
##moon_question_2 = pygame.image.load("resources/questions/moon/question2.png")
##moon_question_3 = pygame.image.load("resources/questions/moon/question3.png")
##moon_question_4 = pygame.image.load("resources/questions/moon/question4.png")
##moon_question_5 = pygame.image.load("resources/questions/moon/question5.png")
##moon_question_6 = pygame.image.load("resources/questions/moon/question6.png")
##moon_question_7 = pygame.image.load("resources/questions/moon/question7.png")
##moon_question_8 = pygame.image.load("resources/questions/moon/question8.png")
##moon_question_9 = pygame.image.load("resources/questions/moon/question9.png")
##moon_question_10 = pygame.image.load("resources/questions/moon/question10.png")
###Sun
##sun_question_1 = pygame.image.load("resources/questions/sun/question1.png")
##sun_question_2 = pygame.image.load("resources/questions/sun/question2.png")
##sun_question_3 = pygame.image.load("resources/questions/sun/question3.png")
##sun_question_4 = pygame.image.load("resources/questions/sun/question4.png")
##sun_question_5 = pygame.image.load("resources/questions/sun/question5.png")
##sun_question_6 = pygame.image.load("resources/questions/sun/question6.png")
##sun_question_7 = pygame.image.load("resources/questions/sun/question7.png")
##sun_question_8 = pygame.image.load("resources/questions/sun/question8.png")
##sun_question_9 = pygame.image.load("resources/questions/sun/question9.png")
##sun_question_10 = pygame.image.load("resources/questions/sun/question10.png")
###Pluto
##pluto_question_1 = pygame.image.load("resources/questions/pluto/question1.png")
##pluto_question_2 = pygame.image.load("resources/questions/pluto/question2.png")
##pluto_question_3 = pygame.image.load("resources/questions/pluto/question3.png")
##pluto_question_4 = pygame.image.load("resources/questions/pluto/question4.png")
##pluto_question_5 = pygame.image.load("resources/questions/pluto/question5.png")
##pluto_question_6 = pygame.image.load("resources/questions/pluto/question6.png")
##pluto_question_7 = pygame.image.load("resources/questions/pluto/question7.png")
##pluto_question_8 = pygame.image.load("resources/questions/pluto/question8.png")
##pluto_question_9 = pygame.image.load("resources/questions/pluto/question9.png")
##pluto_question_10 = pygame.image.load("resources/questions/pluto/question10.png")
###Saturn
##saturn_question_1 = pygame.image.load("resources/questions/saturn/question1.png")
##saturn_question_2 = pygame.image.load("resources/questions/saturn/question2.png")
##saturn_question_3 = pygame.image.load("resources/questions/saturn/question3.png")
##saturn_question_4 = pygame.image.load("resources/questions/saturn/question4.png")
##saturn_question_5 = pygame.image.load("resources/questions/saturn/question5.png")
##saturn_question_6 = pygame.image.load("resources/questions/saturn/question6.png")
##saturn_question_7 = pygame.image.load("resources/questions/saturn/question7.png")
##saturn_question_8 = pygame.image.load("resources/questions/saturn/question8.png")
##saturn_question_9 = pygame.image.load("resources/questions/saturn/question9.png")
##saturn_question_10 = pygame.image.load("resources/questions/saturn/question10.png")
###Jupiter
##jupiter_question_1 = pygame.image.load("resources/questions/jupiter/question1.png")
##jupiter_question_2 = pygame.image.load("resources/questions/jupiter/question2.png")
##jupiter_question_3 = pygame.image.load("resources/questions/jupiter/question3.png")
##jupiter_question_4 = pygame.image.load("resources/questions/jupiter/question4.png")
##jupiter_question_5 = pygame.image.load("resources/questions/jupiter/question5.png")
##jupiter_question_6 = pygame.image.load("resources/questions/jupiter/question6.png")
##jupiter_question_7 = pygame.image.load("resources/questions/jupiter/question7.png")
##jupiter_question_8 = pygame.image.load("resources/questions/jupiter/question8.png")
##jupiter_question_9 = pygame.image.load("resources/questions/jupiter/question9.png")
##jupiter_question_10 = pygame.image.load("resources/questions/jupiter/question10.png")
###Venus
##venus_question_1 = pygame.image.load("resources/questions/venus/question1.png")
##venus_question_2 = pygame.image.load("resources/questions/venus/question2.png")
##venus_question_3 = pygame.image.load("resources/questions/venus/question3.png")
##venus_question_4 = pygame.image.load("resources/questions/venus/question4.png")
##venus_question_5 = pygame.image.load("resources/questions/venus/question5.png")
##venus_question_6 = pygame.image.load("resources/questions/venus/question6.png")
##venus_question_7 = pygame.image.load("resources/questions/venus/question7.png")
##venus_question_8 = pygame.image.load("resources/questions/venus/question8.png")
##venus_question_9 = pygame.image.load("resources/questions/venus/question9.png")
##venus_question_10 = pygame.image.load("resources/questions/mars/question10.png")
###Uranus
##uranus_question_1 = pygame.image.load("resources/questions/uranus/question1.png")
##uranus_question_2 = pygame.image.load("resources/questions/uranus/question2.png")
##uranus_question_3 = pygame.image.load("resources/questions/uranus/question3.png")
##uranus_question_4 = pygame.image.load("resources/questions/uranus/question4.png")
##uranus_question_5 = pygame.image.load("resources/questions/uranus/question5.png")
##uranus_question_6 = pygame.image.load("resources/questions/uranus/question6.png")
##uranus_question_7 = pygame.image.load("resources/questions/uranus/question7.png")
##uranus_question_8 = pygame.image.load("resources/questions/uranus/question8.png")
##uranus_question_9 = pygame.image.load("resources/questions/uranus/question9.png")
##uranus_question_10 = pygame.image.load("resources/questions/uranus/question10.png")
###Mercury
##mercury_question_1 = pygame.image.load("resources/questions/mercury/question1.png")
##mercury_question_2 = pygame.image.load("resources/questions/mercury/question2.png")
##mercury_question_3 = pygame.image.load("resources/questions/mercury/question3.png")
##mercury_question_4 = pygame.image.load("resources/questions/mercury/question4.png")
##mercury_question_5 = pygame.image.load("resources/questions/mercury/question5.png")
##mercury_question_6 = pygame.image.load("resources/questions/mercury/question6.png")
##mercury_question_7 = pygame.image.load("resources/questions/mercury/question7.png")
##mercury_question_8 = pygame.image.load("resources/questions/mercury/question8.png")
##mercury_question_9 = pygame.image.load("resources/questions/mercury/question9.png")
##mercury_question_10 = pygame.image.load("resources/questions/mercury/question10.png")
###Neptune
##neptune_question_1 = pygame.image.load("resources/questions/neptune/question1.png")
##neptune_question_2 = pygame.image.load("resources/questions/neptune/question2.png")
##neptune_question_3 = pygame.image.load("resources/questions/neptune/question3.png")
##neptune_question_4 = pygame.image.load("resources/questions/neptune/question4.png")
##neptune_question_5 = pygame.image.load("resources/questions/neptune/question5.png")
##neptune_question_6 = pygame.image.load("resources/questions/neptune/question6.png")
##neptune_question_7 = pygame.image.load("resources/questions/neptune/question7.png")
##neptune_question_8 = pygame.image.load("resources/questions/neptune/question8.png")
##neptune_question_9 = pygame.image.load("resources/questions/neptune/question9.png")
##neptune_question_10 = pygame.image.load("resources/questions/neptune/question10.png")

#Answers
true = pygame.image.load("resources/answers/earth/true.png")
false = pygame.image.load("resources/answers/earth/false.png")
yes = pygame.image.load("resources/answers/earth/yes.png")
no = pygame.image.load("resources/answers/earth/no.png")
windows = pygame.image.load("resources/answers/earth/windows.png")
apple = pygame.image.load("resources/answers/earth/apple.png")
linux = pygame.image.load("resources/answers/earth/linux.png")
windowsos = pygame.image.load("resources/answers/earth/windowsos.jpg")
appleos = pygame.image.load("resources/answers/earth/appleos.jpg")
spark = pygame.image.load("resources/answers/earth/spark.png")
vodafone = pygame.image.load("resources/answers/earth/vodafone.png")
degrees2 = pygame.image.load("resources/answers/earth/2degrees.png")
trustpower = pygame.image.load("resources/answers/earth/trustpower.png")
slingshot = pygame.image.load("resources/answers/earth/slingshot.png")
flip = pygame.image.load("resources/answers/earth/flip.png")
nasa = pygame.image.load("resources/answers/earth/nasa.png")
spacex = pygame.image.load("resources/answers/earth/spacex.png")
apollox = pygame.image.load("resources/answers/earth/apollox.png")
vr = pygame.image.load("resources/answers/earth/vr.png")
vr1 = pygame.image.load("resources/answers/earth/vr1.png")
vr2 = pygame.image.load("resources/answers/earth/vr2.jpg")
#Main Menu Function
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
                   clickaudio.play()
                   time.sleep(0.5)
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
                   clickaudio.play()
                   time.sleep(0.5)
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
                 clickaudio.play()
                 time.sleep(0.5)  
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
                    clickaudio.play()
                    time.sleep(0.5)
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
                 clickaudio.play()
                 time.sleep(0.5) 
                 main_menu()
                 
def back_button1(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(backtext, (340,440))
         if click[0] == 1 and action != None:
             if action == "back":
                 clickaudio.play()
                 time.sleep(0.5)
                 main_menu()

def tutorial_on(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(on, (420,310))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5)
             if action == "on":
                 print("Tutorial On")
                 with open('resources/files/tutorial.txt', 'w') as t:
                     t.write('ON')
                
def tutorial_off(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(off, (500,310))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5)
             if action == "off":
                 print("Tutorial Off")
                 with open('resources/files/tutorial.txt', 'w') as t:
                     t.write('OFF')

def fps_30(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(fpsimage1, (420,210))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5)
             if action == "30_fps":
                 print("FPS = 30")
                 with open('resources/files/fps.txt', 'w') as t:
                     t.write('30')
                 

def fps_60(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(fpsimage2, (500,210))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5)
             if action == "60_fps":
                 print("FPS = 60")
                 with open('resources/files/fps.txt', 'w') as t:
                     t.write('60')

def fps_120(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(fpsimage3, (580,210))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5)
             if action == "120_fps":
                 print("FPS = 120")
                 with open('resources/files/fps.txt', 'w') as t:
                     t.write('120')

def sound_25(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(sound1, (420,260))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5)
             if action == "sound_25":
                 print("Sound = 25%")
                 with open('resources/files/sound.txt', 'w') as t:
                     t.write('25')

def sound_50(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(sound2, (500,260))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5)
             if action == "sound_50":
                 print("Sound = 50%")
                 with open('resources/files/sound.txt', 'w') as t:
                     t.write('50')

def sound_75(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(sound3, (580,260))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5)
             if action == "sound_75":
                 print("Sound = 75%")
                 with open('resources/files/sound.txt', 'w') as t:
                     t.write('75')

def sound_100(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(sound4, (660,260))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5)
             if action == "sound_100":
                 print("Sound = 100%")
                 with open('resources/files/sound.txt', 'w') as t:
                     t.write('100')

def edit_controls(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(edit, (480,370))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5)
             if action == "edit_controls":
                 print("Coming Soon!!! Current controls are WASD or LEFT, RIGHT, UP and DOWN")
                
def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
    pygame.display.update()
    
def message_to_screen_earth(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

def message_to_screen_high_score(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    
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
        
        gameDisplay.blit(fpsimg, (250,200))
        gameDisplay.blit(sound, (250,250))
        gameDisplay.blit(tutorial, (250,300))
        gameDisplay.blit(controls, (250,350))

        with open('resources/files/fps.txt', 'r') as f:
            fpsread = int(f.read(3))
            print("FPS = ", fps)

        with open('resources/files/tutorial.txt', 'r') as f:
            tutorialread = str(f.read(3))
            print("Tutorial = ", tutorial)

        with open('resources/files/sound.txt', 'r') as f:
            soundread = int(f.read(3))
            print("Sound = ", sound,"%")

        if fpsread == 30:
            pygame.draw.rect(gameDisplay, blue, (420,220,75,40))

        if fpsread == 60:
            pygame.draw.rect(gameDisplay, blue, (500,220,75,40))

        if fpsread == 120:
            pygame.draw.rect(gameDisplay, blue, (580,220,95,40))
        
        if soundread == 25:
            pygame.draw.rect(gameDisplay, blue, (420,270,75,40))

        if soundread == 50:
            pygame.draw.rect(gameDisplay, blue, (500,270,75,40)) 

        if soundread == 75:
            pygame.draw.rect(gameDisplay, blue, (580,270,75,40))

        if soundread == 100:
            pygame.draw.rect(gameDisplay, blue, (660,270,95,40))

        if tutorialread == 'ON':
            pygame.draw.rect(gameDisplay, blue, (420,320,75,40))

        if tutorialread == 'OFF':
            pygame.draw.rect(gameDisplay, blue, (500,320,95,40))
            
        #30fps :)
        gameDisplay.blit(fpsimage1, (420,210))
        fps_30(420,220,75,40, grey, action = '30_fps')
        
        #60fps :)
        gameDisplay.blit(fpsimage2, (500,210))
        fps_60(500,220,75,40, grey, action = '60_fps')
        
        #120fps :)
        gameDisplay.blit(fpsimage3, (580,210))
        fps_120(580,220,95,40, grey, action = '120_fps')
        
        #25%
        gameDisplay.blit(sound1, (420,260))
        sound_25(420,270,75,40, grey, action = 'sound_25')
        
        #50%
        gameDisplay.blit(sound2, (500,260))
        sound_50(500,270,75,40, grey, action = 'sound_50')
        
        #75%
        gameDisplay.blit(sound3, (580,260))
        sound_75(580,270,75,40, grey, action = 'sound_75')
        
        #100%
        gameDisplay.blit(sound4, (660,260))
        sound_100(660,270,95,40, grey, action = 'sound_100')
        
        #On
        gameDisplay.blit(on, (420,310))
        tutorial_on(420,320,75,40, grey, action = 'on')
        
        #OFF
        gameDisplay.blit(off, (500,310))
        tutorial_off(500,320,95,40, grey, action = 'off')
        
        #Controls
        gameDisplay.blit(edit, (480,370))
        edit_controls(480,370,40,40, grey, action = 'edit_controls')
        
        #Back Button
        gameDisplay.blit(backtext, (340,440))
        back_button(280,430,260,75, grey, action = 'back')

        pygame.display.update()


def high_scores():
    print("The High Score Function has run")
    gameExit = False #Game Exit is = false

    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameexit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
        gameDisplay.blit(scorebanner, (0,0))
        gameDisplay.blit(quizzes, (257,209))
        with open("resources/scores/earthscore.txt") as f:
            for line in f:
                message_to_screen_earth1(line, white) 
                
        with open("resources/scores/marsscore.txt") as f:
            for line in f:
                message_to_screen_mars1(line, white)
                
        with open("resources/scores/moonscore.txt") as f:
            for line in f:
                message_to_screen_moon1(line, white)
                
        with open("resources/scores/saturnscore.txt") as f:
            for line in f:
                message_to_screen_saturn1(line, white)
                
        with open("resources/scores/venusscore.txt") as f:
            for line in f:
                message_to_screen_venus1(line, white)
                
        with open("resources/scores/mercuryscore.txt") as f:
            for line in f:
                message_to_screen_mercury1(line, "/10", white)
                
        with open("resources/scores/plutoscore.txt") as f:
            for line in f:
                message_to_screen_pluto1(line, white)
                
        with open("resources/scores/neptunescore.txt") as f:
            for line in f:
                message_to_screen_neptune1(line, white)
                
        with open("resources/scores/jupiterscore.txt") as f:
            for line in f:
                message_to_screen_jupiter1(line, white)
                
        with open("resources/scores/uranusscore.txt") as f:
            for line in f:
                message_to_screen_uranus1(line, white)
                
        with open("resources/scores/sunscore.txt") as f:
            for line in f:
                message_to_screen_sun1(line, white)

                     
        #Back Button
        pygame.draw.rect(gameDisplay, white, [300,440,220,55])
        gameDisplay.blit(backtext, (340,440))
        back_button1(280,430,260,75, grey, action = 'back')
        pygame.display.update()
        



def message_to_screen_earth1(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (210)
    gameDisplay.blit(textSurf, textRect)
    

def message_to_screen_mars1(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (230)
    gameDisplay.blit(textSurf, textRect)
    

def message_to_screen_moon1(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (250)
    gameDisplay.blit(textSurf, textRect)
    

def message_to_screen_saturn1(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (270)
    gameDisplay.blit(textSurf, textRect)
    

def message_to_screen_venus1(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (290)
    gameDisplay.blit(textSurf, textRect)
    

def message_to_screen_mercury1(msg, msg1, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (310)
    gameDisplay.blit(textSurf, textRect)
    

def message_to_screen_pluto1(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (330)
    gameDisplay.blit(textSurf, textRect)
    

def message_to_screen_neptune1(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (350)
    gameDisplay.blit(textSurf, textRect)
   

def message_to_screen_jupiter1(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (370)
    gameDisplay.blit(textSurf, textRect)
    

def message_to_screen_uranus1(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (390)
    gameDisplay.blit(textSurf, textRect)
  

def message_to_screen_sun1(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (410)
    gameDisplay.blit(textSurf, textRect)

     
#Gameloop, Mainloop for the game
def game_loop():

    gameExit = False #Game Exit is = false
    player_x = 370
    player_y = 185

    x_change = 0
    y_change = 0

    #Planet Locations
    sun_x = 60
    sun_y = 40
    mars_x = 250
    mars_y = 20
    saturn_x = 560
    saturn_y = 20
    venus_x = 640
    venus_y = 200
    uranus_x = 20
    uranus_y = 200
    earth_x = display_width/2.4
    earth_y = display_height/2.5
    jupiter_x = 40
    jupiter_y = 380
    mercury_x = 620
    mercury_y = 380
    neptune_x = 200
    neptune_y = 430
    moon_x = 430
    moon_y = 20
    pluto_x = 450
    pluto_y = 430

    #animation()
    while not gameExit: #While Game Exit is not = true run everything below
                        #If it is it will escape the while loop and run quit code/gameover code at the bottom

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameexit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
        #print(player_x,player_y) 
        gameDisplay.blit(sun, (sun_x,sun_y))
        gameDisplay.blit(mars, (mars_x,mars_y))
        gameDisplay.blit(saturn, (saturn_x,saturn_y))
        gameDisplay.blit(venus, (venus_x,venus_y))
        gameDisplay.blit(uranus, (uranus_x,uranus_y))
        gameDisplay.blit(earth, (earth_x,earth_y))
        gameDisplay.blit(jupiter, (jupiter_x,jupiter_y))
        gameDisplay.blit(mercury, (mercury_x,mercury_y))
        gameDisplay.blit(neptune, (neptune_x,neptune_y))
        gameDisplay.blit(moon, (moon_x,moon_y))
        gameDisplay.blit(pluto, (pluto_x,pluto_y))

        #Player Movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -player_speed
                    y_change = 0
                elif event.key == pygame.K_d:
                    x_change = player_speed
                    y_change = 0
                elif event.key == pygame.K_w:
                    y_change = -player_speed
                    x_change = 0
                elif event.key == pygame.K_s:
                    y_change = player_speed
                    x_change = 0
                if event.key == pygame.K_LEFT:
                    x_change = -player_speed
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = player_speed
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -player_speed
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = player_speed
                    x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_change = 0

                elif event.key == pygame.K_d:
                    x_change = 0

                elif event.key == pygame.K_w:
                    y_change = 0

                elif event.key == pygame.K_s:
                    y_change = 0

                if event.key == pygame.K_LEFT:
                    x_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = 0

                elif event.key == pygame.K_UP:
                    y_change = 0

                elif event.key == pygame.K_DOWN:
                    y_change = 0

        #Boundaries
        #if player_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
        if player_x >= display_width:
            player_x = 0
        if player_x < 0:
            player_x = 800
        if player_y >= display_height:
            player_y = 0
        if player_y < 0:
            player_y = 600

        #Crossover - Collisions
        #Sun Crossover
        if player_x >= sun_x and player_x <= sun_x + 130 and player_y >= sun_y and player_y <= sun_y + 121:
            gameDisplay.blit(sun_text, (65,75))
            sun_button(60,40,130,121, None, action = 'sun')
            
        #Mars Crossover
        if player_x >= mars_x and player_x <= mars_x + 120 and player_y >= mars_y and player_y <= mars_y + 118:
            gameDisplay.blit(mars_text, (255,65))
            mars_button(250,20,120,118, None, action = 'mars')
        #Saturn Crossover
        if player_x >= saturn_x and player_x <= saturn_x + 200 and player_y >= saturn_y and player_y <= saturn_y + 136:
            gameDisplay.blit(saturn_text, (650,120))
            saturn_button(560,20,200,136, None, action = 'saturn')

        #Venus Crossover
        if player_x >= venus_x and player_x <= venus_x + 120 and player_y >= venus_y and player_y <= venus_y + 118:
            gameDisplay.blit(venus_text, (645,235))
            venus_button(640,200,120,128, None, action = 'venus')
            
        #Uranus Crossover
        if player_x >= uranus_x and player_x <= uranus_x + 120 and player_y >= uranus_y and player_y <= uranus_y + 118:
            gameDisplay.blit(uranus_text, (10,170))
            uranus_button(20,200,120,128, None, action = 'uranus')

        #Earth Crossover
        if player_x >= earth_x and player_x <= earth_x + 120 and player_y >= earth_y and player_y <= earth_y + 128:
            gameDisplay.blit(earth_text, (335,200))
            earth_button(display_width/2.4,display_height/2.5,120,128, None, action = 'earth')
            
        #Jupiter Crossover
        if player_x >= jupiter_x and player_x <= jupiter_x + 120 and player_y >= jupiter_y and player_y <= jupiter_y + 122:
            gameDisplay.blit(jupiter_text, (20,345))
            jupiter_button(40,380,120,122, None, action = 'jupiter')

        #Mercury Crossover
        if player_x >= mercury_x and player_x <= mercury_x + 120 and player_y >= mercury_y and player_y <= mercury_y + 122:
            gameDisplay.blit(mercury_text, (605,350))
            mercury_button(620,380,120,122, None, action = 'mercury')
            
        #Neptune Crossover
        if player_x >= neptune_x and player_x <= neptune_x + 120 and player_y >= neptune_y and player_y <= neptune_y + 119:
            gameDisplay.blit(neptune_text, (180,385))
            neptune_button(200,430,120,119, None, action = 'neptune')

        #Moon Crossover
        if player_x >= moon_x and player_x <= moon_x + 120 and player_y >= moon_y and player_y <= moon_y + 125:
            gameDisplay.blit(moon_text, (430,60))
            moon_button(430,20,120,125, None, action = 'moon')

        #Pluto Crossover
        if player_x >= pluto_x and player_x <= pluto_x + 120 and player_y >= pluto_y and player_y <= pluto_y + 121:
            gameDisplay.blit(pluto_text, (457,470))
            pluto_button(450,430,120,121, None, action = 'pluto')

        player_x += x_change
        player_y += y_change
        ufo(player_x,player_y)
        pygame.display.update()         #If anything is blit to the display, the display will have to be updated, it will update (fps) times per second
        clock.tick(fps)                 #Each Clocktick will run this loop again that many times per second, Defined by the clocktick variable

def earth_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "earth":
                earth_quiz()

def sun_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "sun":
                sun_quiz()

def mars_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "mars":
                mars_quiz()


def moon_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "moon":
                moon_quiz()

def venus_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "venus":
                venus_quiz()

def neptune_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "neptune":
                neptune_quiz()

def jupiter_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "jupiter":
                jupiter_quiz()

def mercury_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "mercury":
                mercury_quiz()

def uranus_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "uranus":
                uranus_quiz()

def pluto_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "pluto":
                pluto_quiz()

def saturn_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "saturn":
                saturn_quiz()


def game_home():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True


        pygame.display.update
        clock.tick(fps)

def ufo(player_x,player_y):
    gameDisplay.blit(player,(player_x,player_y))

def print_things(player_x,player_y):
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        #print(player_x,player_y)
        pygame.display.update
        clock.tick(10)


########################################################################THE QUIZZES################################################################################
##################################EARTH QUIZ####################################
earth_question1_run = False
earth_question2_run = False
earth_question3_run = False
earth_question4_run = False
earth_question5_run = False
earth_question6_run = False
earth_question7_run = False
earth_question8_run = False
earth_question9_run = False
earth_question10_run = False
earth_end = False
earth_score = 0

sun_question1_run = False
sun_question2_run = False
sun_question3_run = False
sun_question4_run = False
sun_question5_run = False
sun_question6_run = False
sun_question7_run = False
sun_question8_run = False
sun_question9_run = False
sun_question10_run = False
sun_end = False
sun_score = 0

moon_question1_run = False
moon_question2_run = False
moon_question3_run = False
moon_question4_run = False
moon_question5_run = False
moon_question6_run = False
moon_question7_run = False
moon_question8_run = False
moon_question9_run = False
moon_question10_run = False
moon_end = False
moon_score = 0

mars_question1_run = False
mars_question2_run = False
mars_question3_run = False
mars_question4_run = False
mars_question5_run = False
mars_question6_run = False
mars_question7_run = False
mars_question8_run = False
mars_question9_run = False
mars_question10_run = False
mars_end = False
mars_score = 0

saturn_question1_run = False
saturn_question2_run = False
saturn_question3_run = False
saturn_question4_run = False
saturn_question5_run = False
saturn_question6_run = False
saturn_question7_run = False
saturn_question8_run = False
saturn_question9_run = False
saturn_question10_run = False
saturn_end = False
saturn_score = 0

jupiter_question1_run = False
jupiter_question2_run = False
jupiter_question3_run = False
jupiter_question4_run = False
jupiter_question5_run = False
jupiter_question6_run = False
jupiter_question7_run = False
jupiter_question8_run = False
jupiter_question9_run = False
jupiter_question10_run = False
jupiter_end = False
jupiter_score = 0

neptune_question1_run = False
neptune_question2_run = False
neptune_question3_run = False
neptune_question4_run = False
neptune_question5_run = False
neptune_question6_run = False
neptune_question7_run = False
neptune_question8_run = False
neptune_question9_run = False
neptune_question10_run = False
neptune_end = False
neptune_score = 0

uranus_question1_run = False
uranus_question2_run = False
uranus_question3_run = False
uranus_question4_run = False
uranus_question5_run = False
uranus_question6_run = False
uranus_question7_run = False
uranus_question8_run = False
uranus_question9_run = False
uranus_question10_run = False
uranus_end = False
uranus_score = 0

venus_question1_run = False
venus_question2_run = False
venus_question3_run = False
venus_question4_run = False
venus_question5_run = False
venus_question6_run = False
venus_question7_run = False
venus_question8_run = False
venus_question9_run = False
venus_question10_run = False
venus_end = False
venus_score = 0

pluto_question1_run = False
pluto_question2_run = False
pluto_question3_run = False
pluto_question4_run = False
pluto_question5_run = False
pluto_question6_run = False
pluto_question7_run = False
pluto_question8_run = False
pluto_question9_run = False
pluto_question10_run = False
pluto_end = False
pluto_score = 0

mercury_question1_run = False
mercury_question2_run = False
mercury_question3_run = False
mercury_question4_run = False
mercury_question5_run = False
mercury_question6_run = False
mercury_question7_run = False
mercury_question8_run = False
mercury_question9_run = False
mercury_question10_run = False
mercury_end = False
mercury_score = 0


def earth_quiz():
    global earth_question1_run
    global earth_question2_run
    global earth_question3_run
    global earth_question4_run
    global earth_question5_run
    global earth_question6_run
    global earth_question7_run
    global earth_question8_run
    global earth_question9_run
    global earth_question10_run
    global earth_end
    global earth_score
    
    gameExit = False #Game Exit is = false 
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        if earth_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_1, (20,50))
            gameDisplay.blit(windows, (100,270))
            earth_questions_buttons(100,270,150,151, None, action = 'windows1')
            gameDisplay.blit(apple, (325,250))
            earth_questions_buttons(325,250,130,161, None, action = 'apple1')
            gameDisplay.blit(linux, (550,270))
            earth_questions_buttons(550,270,150,166, None, action = 'linux1')
            pygame.display.update()
            
        elif earth_question1_run == True and earth_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_2, (80,50))
            gameDisplay.blit(windows, (100,270))
            earth_questions_buttons(100,270,150,151, None, action = 'windows2')
            gameDisplay.blit(apple, (325,250))
            earth_questions_buttons(325,250,130,161, None, action = 'apple2')
            gameDisplay.blit(linux, (550,270))
            earth_questions_buttons(550,270,150,166, None, action = 'linux2')
            pygame.display.update()
            

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_3, (30,50))
            gameDisplay.blit(windows, (100,270))
            earth_questions_buttons(100,270,150,151, None, action = 'windows3')
            gameDisplay.blit(apple, (325,250))
            earth_questions_buttons(325,250,130,161, None, action = 'apple3')
            gameDisplay.blit(linux, (550,270))
            earth_questions_buttons(550,270,150,166, None, action = 'linux3')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_4, (70,50))
            gameDisplay.blit(true, (225,250))
            earth_questions_buttons(225,250,135,137, None, action = 'true1')
            gameDisplay.blit(false, (425,250))
            earth_questions_buttons(425,250,135,137, None, action = 'false1')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0))  
            gameDisplay.blit(earth_question_5, (-10,50))
            pygame.draw.rect(gameDisplay, red, (25,260,50,50))
            earth_questions_buttons(25,260,50,50, None, action = 'red1')
            pygame.draw.rect(gameDisplay, orange, (125,260,50,50))
            earth_questions_buttons(125,260,50,50, None, action = 'orange1')
            pygame.draw.rect(gameDisplay, yellow, (225,260,50,50))
            earth_questions_buttons(225,260,50,50, None, action = 'yellow1')
            pygame.draw.rect(gameDisplay, green, (325,260,50,50))
            earth_questions_buttons(325,260,50,50, None, action = 'green1')
            pygame.draw.rect(gameDisplay, blue, (425,260,50,50))
            earth_questions_buttons(425,260,50,50, None, action = 'blue1')
            pygame.draw.rect(gameDisplay, pink, (525,260,50,50))
            earth_questions_buttons(525,260,50,50, None, action = 'pink1')
            pygame.draw.rect(gameDisplay, purple, (625,260,50,50))
            earth_questions_buttons(625,260,50,50, None, action = 'purple1')
            pygame.draw.rect(gameDisplay, white, (725,260,50,50))
            earth_questions_buttons(725,260,50,50, None, action = 'white1')
            
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_6, (80,50))
            gameDisplay.blit(vr, (50,200))
            earth_questions_buttons(50,200,225,225, None, action = 'vr')
            gameDisplay.blit(vr1, (287.5,200))
            earth_questions_buttons(287.5,200,225,225, None, action = 'vr1')
            gameDisplay.blit(vr2, (525,200))
            earth_questions_buttons(525,200,225,225, None, action = 'vr2')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_7, (0,50))
            gameDisplay.blit(spacex, (50,170))
            earth_questions_buttons(50,170,225,225, None, action = 'spacex')
            gameDisplay.blit(nasa, (287.5,200))
            earth_questions_buttons(287.5,200,225,225, None, action = 'nasa')
            gameDisplay.blit(apollox, (525,250))
            earth_questions_buttons(525,200,225,95, None, action = 'apollox')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_8, (100,50))
            gameDisplay.blit(windowsos, (100,200))
            earth_questions_buttons(100,200,300,190, None, action = 'windowsos')
            gameDisplay.blit(appleos, (400,200))
            earth_questions_buttons(400,200,300,190, None, action = 'appleos')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == True and earth_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_9, (20,50))
            gameDisplay.blit(spark, (25,180))
            earth_questions_buttons(50,200,300,190, None, action = 'spark')
            gameDisplay.blit(vodafone, (280,200))
            earth_questions_buttons(280,200,300,190, None, action = 'vodafone')
            gameDisplay.blit(degrees2, (550,200))
            earth_questions_buttons(550,200,300,190, None, action = '2degrees')
            gameDisplay.blit(flip, (55,400))
            earth_questions_buttons(55,400,300,190, None, action = 'flip')
            gameDisplay.blit(slingshot, (280,400))
            earth_questions_buttons(280,400,300,190, None, action = 'slingshot')
            gameDisplay.blit(trustpower, (540,400))
            earth_questions_buttons(540,400,300,190, None, action = 'trustpower')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == True and earth_question9_run == True and earth_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_10, (20,50)) 
            gameDisplay.blit(yes, (225,250))
            earth_questions_buttons(225,250,135,137, None, action = 'yes1')
            gameDisplay.blit(no, (425,250))
            earth_questions_buttons(425,250,135,137, None, action = 'no1')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == True and earth_question9_run == True and earth_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(congratulations, (0,50))
            earth_score = str(earth_score)
            message_to_screen_text_earth("Youre Score:     /10", white)
            message_to_screen_text_earth_score(earth_score, white)

            with open('resources/scores/earthscore.txt', 'r') as f:
                for line in f:  
                    print("Final Score", earth_score)
                    earth_score = int(earth_score) 
                    earth_score = line
                    if line > earth_score:
                        print("It didnt work")
                    if earth_score > line:
                        earth_score = line
                        earth_score = str(earth_score)
                        with open("resources/scores/earthscore.txt",'w') as f:
                            print("The score is being written to the file as: ", earth_score)
                            f.write(earth_score)
                    
                
                   
            
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])
            gameDisplay.blit(restarttext, (310,200))
            earth_questions_buttons(280,195,260,65, grey, action = 'restart')

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])
            gameDisplay.blit(levelstext, (310,280))
            earth_questions_buttons(280,270,260,75, grey, action = 'levels')


            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])
            gameDisplay.blit(mainmtext, (310,365))
            earth_questions_buttons(280,350,260,75, grey, action = 'mainm')

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])
            gameDisplay.blit(quittext, (340,440))
            earth_questions_buttons(280,430,260,75, grey, action = 'quit')

            pygame.display.update()

def message_to_screen_text_earth(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)
    gameDisplay.blit(textSurf, textRect)

def message_to_screen_text_earth_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)
    gameDisplay.blit(textSurf, textRect)
    
def earth_questions_buttons(x,y,width,height,active_color, action = None):
    global earth_question1_run
    global earth_question2_run
    global earth_question3_run
    global earth_question4_run
    global earth_question5_run
    global earth_question6_run
    global earth_question7_run
    global earth_question8_run
    global earth_question9_run
    global earth_question10_run
    global earth_end
    global earth_score

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "windows1":
                gameDisplay.fill(red)
                time.sleep(1)
                earth_question1_run = True
            if action == "linux1":
                gameDisplay.fill(green)
                earth_question1_run = True
                earth_score += 1
                print(earth_score)
            if action == "apple1":
                gameDisplay.fill(red)
                earth_question1_run = True

            if action == "windows2":
                gameDisplay.fill(green)
                earth_question2_run = True
                earth_score += 1
                print(earth_score)
            if action == "linux2":
                gameDisplay.fill(red)
                earth_question2_run = True
            if action == "apple2":
                gameDisplay.fill(red)
                earth_question2_run = True

            if action == "windows3":
                gameDisplay.fill(red)
                earth_question3_run = True
            if action == "linux3":
                gameDisplay.fill(red)
                earth_question3_run = True
            if action == "apple3":
                gameDisplay.fill(green)
                earth_score += 1
                print(earth_score)
                earth_question3_run = True

            if action == "true1":
                gameDisplay.fill(red)
                earth_question4_run = True
            if action == "false1":
                gameDisplay.fill(green)
                earth_score += 1
                print(earth_score)
                earth_question4_run = True

            if action == "red1":
                gameDisplay.fill(green)
                earth_score += 1
                print(earth_score)
                earth_question5_run = True
            if action == "orange1" or action == "yellow1" or action == "green1" or action == "blue1" or action == "pink1" or action == "purple1" or action == "white1":
                gameDisplay.fill(red)
                earth_question5_run = True

            if action == "vr":
                gameDisplay.fill(green)
                earth_score += 1
                print(earth_score)
                earth_question6_run = True
            if action == "vr1" or action == "vr2":
                gameDisplay.fill(red)
                earth_question6_run = True

            if action == "spacex":
                gameDisplay.fill(green)
                earth_score += 1
                print(earth_score)
                earth_question7_run = True
            if action == "apollox" or action == "nasa":
                gameDisplay.fill(red)
                earth_question7_run = True

            if action == "windowsos":
                gameDisplay.fill(red)
                earth_question8_run = True
            if action == "appleos":
                gameDisplay.fill(green)
                earth_score += 1
                print(earth_score)
                earth_question8_run = True

            if action == "flip":
                gameDisplay.fill(green)
                earth_score += 1
                print(earth_score)
                earth_question9_run = True
            if action == "2degrees" or action == "spark" or action == "slingshot" or action == "vodafone" or action == "trustpower":
                gameDisplay.fill(red)
                earth_question9_run = True

            if action == "yes1" or action == "no1":
                gameDisplay.fill(blue)
                earth_score += 1
                print(earth_score)
                earth_end = True

            if action == "restart":
                earth_question1_run = False
                earth_question2_run = False
                earth_question3_run = False
                earth_question4_run = False
                earth_question5_run = False
                earth_question6_run = False
                earth_question7_run = False
                earth_question8_run = False
                earth_question9_run = False
                earth_question10_run = False
                earth_end = False
                earth_score = 0
                earth_quiz()
                
            if action == "levels":
                earth_question1_run = False
                earth_question2_run = False
                earth_question3_run = False
                earth_question4_run = False
                earth_question5_run = False
                earth_question6_run = False
                earth_question7_run = False
                earth_question8_run = False
                earth_question9_run = False
                earth_question10_run = False
                earth_end = False
                earth_score = 0
                game_loop()
    
            if action == "mainm":
                earth_question1_run = False
                earth_question2_run = False
                earth_question3_run = False
                earth_question4_run = False
                earth_question5_run = False
                earth_question6_run = False
                earth_question7_run = False
                earth_question8_run = False
                earth_question9_run = False
                earth_question10_run = False
                earth_end = False
                earth_score = 0
                main_menu()
 
            if action == "quit":
                earth_question1_run = False
                earth_question2_run = False
                earth_question3_run = False
                earth_question4_run = False
                earth_question5_run = False
                earth_question6_run = False
                earth_question7_run = False
                earth_question8_run = False
                earth_question9_run = False
                earth_question10_run = False
                earth_end = False
                earth_score = 0
                pygame.quit()
                quit()

                
####################SUN QUIZ#############################        
def sun_quiz():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
         
        pygame.display.update()
        clock.tick(fps)

def moon_quiz():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
         
        pygame.display.update()
        clock.tick(fps)

def saturn_quiz():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
         
        pygame.display.update()
        clock.tick(fps)

def uranus_quiz():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
         
        pygame.display.update()
        clock.tick(fps)

def mercury_quiz():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
         
        pygame.display.update()
        clock.tick(fps)

def jupiter_quiz():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
         
        pygame.display.update()
        clock.tick(fps)

def mars_quiz():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
         
        pygame.display.update()
        clock.tick(fps)

def pluto_quiz():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
         
        pygame.display.update()
        clock.tick(fps)

def venus_quiz():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
         
        pygame.display.update()
        clock.tick(fps)

def neptune_quiz():
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
         
        pygame.display.update()
        clock.tick(fps)


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

##def animation():
##    animationplay = True
##
##    if animationplay:
##        print(animationplay)
##        gameDisplay.blit(scene1, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene2, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene3, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene4, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene5, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene6, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene7, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene8, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene9, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene10, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene11, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene12, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        #gameDisplay.blit(scene13, (0,0))
##        #time.sleep(1)
##        #pygame.display.update()
##        gameDisplay.blit(scene14, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene15, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene16, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene17, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene18, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene19, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene20, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene21, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene22, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene23, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene24, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene25, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene26, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        gameDisplay.blit(scene27, (0,0))
##        time.sleep(0.1)
##        pygame.display.update()
##        animationplay = False
##    elif animationplay == False:
##        game_loop()      

main_menu()
game_loop()   #Will run gameloop firstly
pygame.quit() #Will Quit Game if the game_loop is escaped
quit()        #Quit
