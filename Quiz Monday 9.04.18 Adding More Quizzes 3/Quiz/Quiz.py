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
transparent = (0,0,0,0)
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

#Gamedisplay setting
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.DOUBLEBUF, 32)

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
coming = pygame.image.load("resources/images/coming.png")
smiley = pygame.image.load("resources/images/smiley.png")
#Correct/Wrong/Other
correctimg = pygame.image.load("resources/images/correct.png")
wrongimg = pygame.image.load("resources/images/wrong.png")
trickimg = pygame.image.load("resources/images/trick.jpg")
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
helptext = pygame.image.load("resources/text/help.png")
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
mars_question_1 = pygame.image.load("resources/questions/mars/question1.png")
mars_question_2 = pygame.image.load("resources/questions/mars/question2.png")
mars_question_3 = pygame.image.load("resources/questions/mars/question3.png")
mars_question_4 = pygame.image.load("resources/questions/mars/question4.png")
mars_question_5 = pygame.image.load("resources/questions/mars/question5.png")
#Moon
moon_question_1 = pygame.image.load("resources/questions/moon/question1.png")
###Sun
sun_question_1 = pygame.image.load("resources/questions/sun/question1.png")
sun_question_2 = pygame.image.load("resources/questions/sun/question2.png")
sun_question_3 = pygame.image.load("resources/questions/sun/question3.png")
sun_question_4 = pygame.image.load("resources/questions/sun/question4.png")
sun_question_5 = pygame.image.load("resources/questions/sun/question5.png")
sun_question_6 = pygame.image.load("resources/questions/sun/question6.png")
sun_question_7 = pygame.image.load("resources/questions/sun/question7.png")
sun_question_8 = pygame.image.load("resources/questions/sun/question8.png")
sun_question_9 = pygame.image.load("resources/questions/sun/question9.png")
sun_question_10 = pygame.image.load("resources/questions/sun/question10.png")
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
#Venus
venus_question_1 = pygame.image.load("resources/questions/venus/question1.png")
venus_question_2 = pygame.image.load("resources/questions/venus/question2.png")
venus_question_3 = pygame.image.load("resources/questions/venus/question3.png")
venus_question_4 = pygame.image.load("resources/questions/venus/question4.png")
venus_question_5 = pygame.image.load("resources/questions/venus/question5.png")
venus_question_6 = pygame.image.load("resources/questions/venus/question6.png")
venus_question_7 = pygame.image.load("resources/questions/venus/question7.png")
venus_question_8 = pygame.image.load("resources/questions/venus/question8.png")
venus_question_9 = pygame.image.load("resources/questions/venus/question9.png")
venus_question_10 = pygame.image.load("resources/questions/venus/question10.png")
#Uranus
uranus_question_1 = pygame.image.load("resources/questions/uranus/question1.png")
uranus_question_2 = pygame.image.load("resources/questions/uranus/question2.png")
uranus_question_3 = pygame.image.load("resources/questions/uranus/question3.png")
uranus_question_4 = pygame.image.load("resources/questions/uranus/question4.png")
uranus_question_5 = pygame.image.load("resources/questions/uranus/question5.png")
uranus_question_6 = pygame.image.load("resources/questions/uranus/question6.png")
uranus_question_7 = pygame.image.load("resources/questions/uranus/question7.png")
uranus_question_8 = pygame.image.load("resources/questions/uranus/question8.png")
uranus_question_9 = pygame.image.load("resources/questions/uranus/question9.png")
uranus_question_10 = pygame.image.load("resources/questions/uranus/question10.png")
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

planetsun = pygame.image.load("resources/answers/sun/planet.png")
star = pygame.image.load("resources/answers/sun/star.png")
mean42 = pygame.image.load("resources/answers/sun/42.png")
infinity = pygame.image.load("resources/answers/sun/infinity.png")
apollo11 = pygame.image.load("resources/answers/sun/apollo11.jpg")
atlantis = pygame.image.load("resources/answers/sun/atlantis.jpg")
columbia = pygame.image.load("resources/answers/sun/columbia.jpg")
aresv = pygame.image.load("resources/answers/sun/aresv.png")
saturnv = pygame.image.load("resources/answers/sun/saturnv.png")
elseimg = pygame.image.load("resources/answers/sun/else.png")
james = pygame.image.load("resources/answers/sun/james.png")
collins = pygame.image.load("resources/answers/sun/collins.jpg")
chris = pygame.image.load("resources/answers/sun/chris.png")
armstrong = pygame.image.load("resources/answers/sun/neilarmstrong.png")
num1 = pygame.image.load("resources/answers/sun/1.jpg")
num2 = pygame.image.load("resources/answers/sun/2.jpg")
num3 = pygame.image.load("resources/answers/sun/3.jpg")
num4 = pygame.image.load("resources/answers/sun/4.jpg")
num5 = pygame.image.load("resources/answers/sun/5.jpg")
jupitertxt = pygame.image.load("resources/answers/sun/jupitertxt.jpg")
venustxt = pygame.image.load("resources/answers/sun/venustxt.jpg")
marstxt = pygame.image.load("resources/answers/sun/marstxt.jpg")
earthtxt = pygame.image.load("resources/answers/sun/earthtxt.jpg")
mercurytxt = pygame.image.load("resources/answers/sun/mercurytxt.jpg") 

ball = pygame.image.load("resources/answers/venus/ball.jpg") 
brain = pygame.image.load("resources/answers/venus/brain.jpg") 
bull = pygame.image.load("resources/answers/venus/bull.jpg") 
cheetah = pygame.image.load("resources/answers/venus/cheetahS.jpg") 
email = pygame.image.load("resources/answers/venus/email.png") 
griffin = pygame.image.load("resources/answers/venus/griffin.jpg") 
hammer = pygame.image.load("resources/answers/venus/hammer.png") 
lightning = pygame.image.load("resources/answers/venus/lightning.jpg") 
solar = pygame.image.load("resources/answers/venus/solarsystem.jpg") 
spin = pygame.image.load("resources/answers/venus/spin.png") 
#WYR Answers
L1 = pygame.image.load("resources/answers/moon/L1.png") 
R1 = pygame.image.load("resources/answers/moon/R1.png") 
L2 = pygame.image.load("resources/answers/moon/L2.png") 
R2 = pygame.image.load("resources/answers/moon/R2.png")
L3 = pygame.image.load("resources/answers/moon/L3.png") 
R3 = pygame.image.load("resources/answers/moon/R3.png")
L4 = pygame.image.load("resources/answers/moon/L4.png") 
R4 = pygame.image.load("resources/answers/moon/R4.png")
L5 = pygame.image.load("resources/answers/moon/L5.png") 
R5 = pygame.image.load("resources/answers/moon/R5.png")
L6 = pygame.image.load("resources/answers/moon/L6.png") 
R6 = pygame.image.load("resources/answers/moon/R6.png")
L7 = pygame.image.load("resources/answers/moon/L7.png") 
R7 = pygame.image.load("resources/answers/moon/R7.png")
L8 = pygame.image.load("resources/answers/moon/L8.png") 
R8 = pygame.image.load("resources/answers/moon/R8.png")
L9 = pygame.image.load("resources/answers/moon/L9.png") 
R9 = pygame.image.load("resources/answers/moon/R9.png")
L10 = pygame.image.load("resources/answers/moon/L10.png") 
R10 = pygame.image.load("resources/answers/moon/R10.png")
#Star Wars (Uranus Quiz) Answers
anewhope = pygame.image.load("resources/answers/uranus/anewhope.jpg")
returnofthejedi = pygame.image.load("resources/answers/uranus/returnofthejedi.jpg")
thelastjedi = pygame.image.load("resources/answers/uranus/thelastjedi.jpg")
bb8 = pygame.image.load("resources/answers/uranus/bb8.png")
r2d2 = pygame.image.load("resources/answers/uranus/r2d2.png")
c3po = pygame.image.load("resources/answers/uranus/c3po.jpg")
bud = pygame.image.load("resources/answers/uranus/bud.png")
finn = pygame.image.load("resources/answers/uranus/finn.png")
john = pygame.image.load("resources/answers/uranus/john.png")
kyber = pygame.image.load("resources/answers/uranus/kyber.png")
kybar = pygame.image.load("resources/answers/uranus/kybar.png")
kybur = pygame.image.load("resources/answers/uranus/kybur.png")
kyba = pygame.image.load("resources/answers/uranus/kyba.png")
porg = pygame.image.load("resources/answers/uranus/porg.png")
poru = pygame.image.load("resources/answers/uranus/poru.png")
nova = pygame.image.load("resources/answers/uranus/nova.png")
porgimg = pygame.image.load("resources/answers/uranus/porgimg.png")
falcon = pygame.image.load("resources/answers/uranus/falcon.png")
enterprise = pygame.image.load("resources/answers/uranus/enterprise.jpg")
xwing = pygame.image.load("resources/answers/uranus/xwing.png")
leia = pygame.image.load("resources/answers/uranus/leia.jpg")
luke = pygame.image.load("resources/answers/uranus/luke.jpg")
yoda = pygame.image.load("resources/answers/uranus/yoda.jpg")
anakin = pygame.image.load("resources/answers/uranus/anakin.jpg")
yodu = pygame.image.load("resources/answers/uranus/yodu.png")
yaddle = pygame.image.load("resources/answers/uranus/yaddle.png")
yodan = pygame.image.load("resources/answers/uranus/yodan.png")
yanna = pygame.image.load("resources/answers/uranus/yanna.png")
kyberimg = pygame.image.load("resources/answers/uranus/kyberimg.jpg")
fn2187 = pygame.image.load("resources/answers/uranus/fn2187.jpg")
jedichurch = pygame.image.load("resources/answers/uranus/jedi.jpg")
#Help Menu
help_banner = pygame.image.load("resources/images/helpbanner.png")
help_message = pygame.image.load("resources/images/help.png")
#Player age
age_up = pygame.image.load("resources/images/up.png")
age_down = pygame.image.load("resources/images/down.png")
age_banner = pygame.image.load("resources/images/age_banner.png")
ok = pygame.image.load("resources/images/ok.png")
anyway = pygame.image.load("resources/images/anyway.png")
player_age = 12

def age():
    global player_age
    age_input = False
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bg, (0,0))
        gameDisplay.blit(age_banner, (90,0))
        #Up Button
        gameDisplay.blit(age_up, (display_width/2 - 60, display_height/2 - 40))
        age_button(display_width/2 - 60,display_height/2 - 40,120,62, grey, action = 'up')
        #Down Button
        gameDisplay.blit(age_down, (display_width/2 - 60, display_height/2 + 100))
        age_button(display_width/2 - 60,display_height/2 + 100,120,63, grey, action = 'down')
        #Age Display
        pygame.draw.rect(gameDisplay, white, [display_width/2 - 60,display_height/2 + 32, 120, 60])
        message_to_screen_age(str(player_age),black)
        #Ok Button
        pygame.draw.rect(gameDisplay, white, [display_width/2 - 60, display_height/2 + 170, 120, 60])
        age_button(display_width/2 - 60, display_height/2 + 170, 120, 60, grey, action = 'ok')
        gameDisplay.blit(ok, (display_width/2 - 60, display_height/2 + 155))
        if player_age > 100:
            player_age = 100
        elif player_age < 1 or player_age > 100:
            player_age = 1
        pygame.display.update()
        clock.tick(fps)

def age_button(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     global player_age
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(age_up, (display_width/2 - 60, display_height/2 - 40))
         gameDisplay.blit(age_down, (display_width/2 - 60, display_height/2 + 100))
         
         if click[0] == 1 and action != None:
             if action == "quit":
                 pygame.quit()
                 quit()
             elif action == "up":
                 clickaudio.play()   
                 player_age += 1
                 time.sleep(0.5)
             elif action == "down":
                 clickaudio.play()
                 player_age -= 1
                 time.sleep(0.5)
             elif  action == "ok":
                 clickaudio.play()
                 age_validation()
                
def message_to_screen_age(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (display_width/2 - 10), (display_height/2 + 50)
    gameDisplay.blit(textSurf, textRect)

def age_validation():
    print("Your age is", player_age)
    if player_age >= 10 and player_age <= 18:
        print("Congratulation you are eligible to play")
        val_yes()
    else:
        print("You are not eligable to play but you may still continue")
        val_no()

def val_yes():
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.blit(bg, (0,0))  
            message_to_screen_val("You are eligible to play :)", green)
            pygame.draw.rect(gameDisplay, white, [display_width/2 - 60, display_height/2 + 140, 120, 60])
            gameDisplay.blit(ok, (display_width/2 - 65, display_height/2 + 130))
            ok_button(display_width/2 - 60, display_height/2 + 140, 120, 60, grey, action = 'ok')
            pygame.display.update()
            

def val_no():
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.blit(bg, (0,0))    
            message_to_screen_val("You are not eligible to play", red)
            pygame.draw.rect(gameDisplay, white, [display_width/2 - 60, display_height/2 + 140, 160, 60])
            gameDisplay.blit(anyway, (display_width/2 - 60, display_height/2 + 140))
            continue_button(display_width/2 - 60, display_height/2 + 140, 160, 60, grey, action = 'anyway')
            pygame.display.update()
            
def message_to_screen_val(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (display_width/2 - 100), (display_height/2)
    gameDisplay.blit(textSurf, textRect)

def continue_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global player_age
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        gameDisplay.blit(anyway, (display_width/2 - 60, display_height/2 + 140))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "anyway":
                clickaudio.play()
                main_menu()

def ok_button(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global player_age
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        gameDisplay.blit(ok, (display_width/2 - 65, display_height/2 + 130))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "ok":
                clickaudio.play()
                time.sleep(0.1)
                main_menu()

    
                 
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

              #Help Button
              pygame.draw.rect(gameDisplay,white, [300, 520, 220, 55])
              gameDisplay.blit(helptext, (340,530))
              quit_button(280, 510, 260, 75, grey, action = 'help')
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
         gameDisplay.blit(helptext, (340,530))
         
         if click[0] == 1 and action != None:
               if action == "quit":
                   clickaudio.play()
                   time.sleep(0.5)
                   pygame.quit()
                   quit()
               if action == "help":
                   clickaudio.play()
                   time.sleep(0.5)
                   help_menu()

def back_button(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + width > cur[0] > x and y + height > cur[1] > y:
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
         gameDisplay.blit(backtext, (340,440))
         if click[0] == 1 and action != None:
             clickaudio.play()
             time.sleep(0.5) 
             if action == "back":  
                 main_menu()
             if action == "backtolevels":
                 game_loop()
                 
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

def help_menu():
    print("The High Score Function has run")
    gameExit = False #Game Exit is = false

    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameexit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0))
        gameDisplay.blit(help_banner, (50,0))
        gameDisplay.blit(help_message, (0,0))
        gameDisplay.blit(help_banner, (50,0))
                     
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
            questions_buttons(100,270,150,151, None, action = 'windows1')
            gameDisplay.blit(apple, (325,250))
            questions_buttons(325,250,130,161, None, action = 'apple1')
            gameDisplay.blit(linux, (550,270))
            questions_buttons(550,270,150,166, None, action = 'linux1')
            pygame.display.update()
            
        elif earth_question1_run == True and earth_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_2, (80,50))
            gameDisplay.blit(windows, (100,270))
            questions_buttons(100,270,150,151, None, action = 'windows2')
            gameDisplay.blit(apple, (325,250))
            questions_buttons(325,250,130,161, None, action = 'apple2')
            gameDisplay.blit(linux, (550,270))
            questions_buttons(550,270,150,166, None, action = 'linux2')
            pygame.display.update()
            

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_3, (30,50))
            gameDisplay.blit(windows, (100,270))
            questions_buttons(100,270,150,151, None, action = 'windows3')
            gameDisplay.blit(apple, (325,250))
            questions_buttons(325,250,130,161, None, action = 'apple3')
            gameDisplay.blit(linux, (550,270))
            questions_buttons(550,270,150,166, None, action = 'linux3')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_4, (70,50))
            gameDisplay.blit(true, (225,250))
            questions_buttons(225,250,135,137, None, action = 'true1')
            gameDisplay.blit(false, (425,250))
            questions_buttons(425,250,135,137, None, action = 'false1')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0))  
            gameDisplay.blit(earth_question_5, (-10,50))
            pygame.draw.rect(gameDisplay, red, (25,260,50,50))
            questions_buttons(25,260,50,50, None, action = 'red1')
            pygame.draw.rect(gameDisplay, orange, (125,260,50,50))
            questions_buttons(125,260,50,50, None, action = 'orange1')
            pygame.draw.rect(gameDisplay, yellow, (225,260,50,50))
            questions_buttons(225,260,50,50, None, action = 'yellow1')
            pygame.draw.rect(gameDisplay, green, (325,260,50,50))
            questions_buttons(325,260,50,50, None, action = 'green1')
            pygame.draw.rect(gameDisplay, blue, (425,260,50,50))
            questions_buttons(425,260,50,50, None, action = 'blue1')
            pygame.draw.rect(gameDisplay, pink, (525,260,50,50))
            questions_buttons(525,260,50,50, None, action = 'pink1')
            pygame.draw.rect(gameDisplay, purple, (625,260,50,50))
            questions_buttons(625,260,50,50, None, action = 'purple1')
            pygame.draw.rect(gameDisplay, white, (725,260,50,50))
            questions_buttons(725,260,50,50, None, action = 'white1')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_6, (80,50))
            gameDisplay.blit(vr, (50,200))
            questions_buttons(50,200,225,225, None, action = 'vr')
            gameDisplay.blit(vr1, (287.5,200))
            questions_buttons(287.5,200,225,225, None, action = 'vr1')
            gameDisplay.blit(vr2, (525,200))
            questions_buttons(525,200,225,225, None, action = 'vr2')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_7, (0,50))
            gameDisplay.blit(spacex, (50,170))
            questions_buttons(50,170,225,225, None, action = 'spacex')
            gameDisplay.blit(nasa, (287.5,200))
            questions_buttons(287.5,200,225,225, None, action = 'nasa')
            gameDisplay.blit(apollox, (525,250))
            questions_buttons(525,200,225,95, None, action = 'apollox')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_8, (100,50))
            gameDisplay.blit(windowsos, (100,200))
            questions_buttons(100,200,300,190, None, action = 'windowsos')
            gameDisplay.blit(appleos, (400,200))
            questions_buttons(400,200,300,190, None, action = 'appleos')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == True and earth_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_9, (20,50))
            gameDisplay.blit(spark, (25,180))
            questions_buttons(50,200,300,190, None, action = 'spark')
            gameDisplay.blit(vodafone, (280,200))
            questions_buttons(280,200,300,190, None, action = 'vodafone')
            gameDisplay.blit(degrees2, (550,200))
            questions_buttons(550,200,300,190, None, action = '2degrees')
            gameDisplay.blit(flip, (55,400))
            questions_buttons(55,400,300,190, None, action = 'flip')
            gameDisplay.blit(slingshot, (280,400))
            questions_buttons(280,400,300,190, None, action = 'slingshot')
            gameDisplay.blit(trustpower, (540,400))
            questions_buttons(540,400,300,190, None, action = 'trustpower')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == True and earth_question9_run == True and earth_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(earth_question_10, (20,50)) 
            gameDisplay.blit(yes, (225,250))
            questions_buttons(225,250,135,137, None, action = 'yes1')
            gameDisplay.blit(no, (425,250))
            questions_buttons(425,250,135,137, None, action = 'no1')
            pygame.display.update()

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == True and earth_question9_run == True and earth_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(congratulations, (0,50))
            print("First Score = ", earth_score)
            earth_score = str(earth_score)
            message_to_screen_text_earth("Youre Score:      /10", white)
            message_to_screen_text_earth_score(earth_score, white)
            with open("resources/scores/earthscore.txt", 'r') as f:
                for line in f:
                    print("Earth Score: ", earth_score)
                    print("Earth Read: ", line)
                    int(line)
            
            if earth_score > line:
                print("earth_score > line")
                with open("resources/scores/earthscore.txt", 'w') as f:
                        f.write(earth_score)
                        
            elif earth_score < line:
                print("earth_score is less than line")
                print("ES:", earth_score)
                print("L:", line)
                
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])
            gameDisplay.blit(restarttext, (310,200))
            questions_buttons(280,195,260,65, grey, action = 'restartearth')

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])
            gameDisplay.blit(levelstext, (310,280))
            questions_buttons(280,270,260,75, grey, action = 'levels')

            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])
            gameDisplay.blit(mainmtext, (310,365))
            questions_buttons(280,350,260,75, grey, action = 'mainm')

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])
            gameDisplay.blit(quittext, (340,440))
            questions_buttons(280,430,260,75, grey, action = 'quit')

            pygame.display.update()

def message_to_screen_text_earth(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)
    gameDisplay.blit(textSurf, textRect)

def message_to_screen_text_earth_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)
    gameDisplay.blit(textSurf, textRect)                   
##################################################################################################                
#################################################SUN QUIZ#########################################
##################################################################################################                
def sun_quiz():
    global sun_question1_run
    global sun_question2_run
    global sun_question3_run
    global sun_question4_run
    global sun_question5_run
    global sun_question6_run
    global sun_question7_run
    global sun_question8_run
    global sun_question9_run
    global sun_question10_run
    global sun_end
    global sun_score
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if sun_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(sun_question_1, (170,50)) 
            gameDisplay.blit(star, (150,250))
            questions_buttons(150,250,200,200, None, action = 'star')
            gameDisplay.blit(planetsun, (420,250))
            questions_buttons(400,250,200,200, None, action = 'planet')
            pygame.display.update()
            
        elif sun_question1_run == True and sun_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(sun_question_2, (100,0))
            gameDisplay.blit(armstrong, (80,250))
            questions_buttons(80,250,186,186, None, action = 'armstrong')   
            gameDisplay.blit(collins, (520,250))
            questions_buttons(520,250,220,284, None, action = 'collins')
            gameDisplay.blit(chris, (300,220))
            questions_buttons(300,220,300,200, None, action = 'chris')
            pygame.display.update()
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(sun_question_3, (150,0))
            gameDisplay.blit(apollo11, (20,160))
            questions_buttons(20,160,300,375, None, action = 'apollo11')
            gameDisplay.blit(atlantis, (270,160))
            questions_buttons(275,160,250,375, None, action = 'atlantis')
            gameDisplay.blit(columbia, (520,160))
            questions_buttons(520,160,250,375, None, action = 'columbia')
            pygame.display.update()
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(sun_question_4, (50,0))
            gameDisplay.blit(aresv, (250,115))
            questions_buttons(250,115,100,474, None, action = 'aresv')
            gameDisplay.blit(saturnv, (450,115))
            questions_buttons(450,115,100,474, None, action = 'saturnv')
            pygame.display.update()
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(sun_question_5, (0,0)) 
            gameDisplay.blit(collins, (520,250))
            questions_buttons(520,250,220,284, None, action = 'collins1')
            gameDisplay.blit(james, (60,250))
            questions_buttons(60,250,250,225, None, action = 'james1')  
            gameDisplay.blit(chris, (300,220))
            questions_buttons(300,220,300,200, None, action = 'chris1')
            pygame.display.update()
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(sun_question_6, (20,0))
            gameDisplay.blit(num1, (50,230))
            questions_buttons(50,230,100,20, None, action = 'num1')
            gameDisplay.blit(num2, (200,230))
            questions_buttons(200,230,100,200, None, action = 'num2')
            gameDisplay.blit(num3, (350,230))
            questions_buttons(350,230,100,200, None, action = 'num3')
            gameDisplay.blit(num4, (500,230))
            questions_buttons(500,230,100,200, None, action = 'num4')
            gameDisplay.blit(num5, (650,230))
            questions_buttons(650,230,100,200, None, action = 'num5')
            pygame.display.update()
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == True and sun_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(sun_question_7, (200,0))
            gameDisplay.blit(yes, (225,250))
            questions_buttons(225,250,135,137, None, action = 'yes2')
            gameDisplay.blit(no, (425,250))
            questions_buttons(425,250,135,137, None, action = 'no2')
            pygame.display.update()
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == True and sun_question7_run == True and sun_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(sun_question_8, (50,0))
            gameDisplay.blit(earthtxt, (350,120))
            questions_buttons(350,120,120,130, None, action = 'earthtxt')
            gameDisplay.blit(marstxt, (500,270))
            questions_buttons(500,270,120,130, None, action = 'marstxt')
            gameDisplay.blit(jupitertxt, (200,300))
            questions_buttons(200,270,120,130, None, action = 'jupitertxt')
            gameDisplay.blit(venustxt, (350,450))
            questions_buttons(350,450,120,130, None, action = 'venustxt')
            pygame.display.update()
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == True and sun_question7_run == True and sun_question8_run == True and sun_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(sun_question_9, (50,0))
            gameDisplay.blit(earthtxt, (350,120))
            questions_buttons(350,120,120,130, None, action = 'earthtxt1')
            gameDisplay.blit(marstxt, (500,270))
            questions_buttons(500,270,120,130, None, action = 'marstxt1')
            gameDisplay.blit(mercurytxt, (200,300))
            questions_buttons(200,270,120,130, None, action = 'mercurytxt1')
            gameDisplay.blit(venustxt, (350,450))
            questions_buttons(350,450,120,130, None, action = 'venustxt1')
            pygame.display.update()
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == True and sun_question7_run == True and sun_question8_run == True and sun_question9_run == True and sun_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(sun_question_10, (60,0))
            gameDisplay.blit(infinity, (150,150))
            questions_buttons(150,150,450,185, None, action = 'infinity')
            gameDisplay.blit(elseimg, (400,350))
            questions_buttons(400,350,200,200, None, action = 'elseimg')
            gameDisplay.blit(mean42, (200,350))
            questions_buttons(200,350,200,155, None, action = 'mean42')
            pygame.display.update()
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == True and sun_question7_run == True and sun_question8_run == True and sun_question9_run == True and sun_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(congratulations, (0,50))
            print("First Score = ", sun_score)
            sun_score = str(sun_score)
            message_to_screen_text_sun("Youre Score:      /10", white)
            message_to_screen_text_sun_score(sun_score, white)
            with open("resources/scores/sunscore.txt", 'r') as f:
                for line in f:
                    print("sun Score: ", sun_score)
                    print("sun Read: ", line)
                    int(line)
            
            if sun_score > line:
                print("sun_score > line")
                with open("resources/scores/sunscore.txt", 'w') as f:
                        f.write(sun_score)
                        
            elif sun_score < line:
                print("sun_score is less than line")
                print("ES:", sun_score)
                print("L:", line)
                
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])
            gameDisplay.blit(restarttext, (310,200))
            questions_buttons(280,195,260,65, grey, action = 'restartsun')

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])
            gameDisplay.blit(levelstext, (310,280))
            questions_buttons(280,270,260,75, grey, action = 'levels')


            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])
            gameDisplay.blit(mainmtext, (310,365))
            questions_buttons(280,350,260,75, grey, action = 'mainm')

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])
            gameDisplay.blit(quittext, (340,440))
            questions_buttons(280,430,260,75, grey, action = 'quit')
            pygame.display.update()
        pygame.display.update()
        clock.tick(fps)
def message_to_screen_text_sun(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)
    gameDisplay.blit(textSurf, textRect)

def message_to_screen_text_sun_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)
    gameDisplay.blit(textSurf, textRect)    

def moon_quiz():
    global moon_question1_run
    global moon_question2_run
    global moon_question3_run
    global moon_question4_run
    global moon_question5_run
    global moon_question6_run
    global moon_question7_run
    global moon_question8_run
    global moon_question9_run
    global moon_question10_run
    global moon_end
    global moon_score
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if moon_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L1, (80,180))
            questions_buttons(80,180,327,300, None, action = 'wyrleft1')
            gameDisplay.blit(R1, (400,180))
            questions_buttons(400,180,327,300, None, action = 'wyrright1')
            pygame.display.update()
        elif moon_question1_run == True and moon_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L2, (80,180))
            questions_buttons(80,180,327,300, None, action = 'wyrleft2')
            gameDisplay.blit(R2, (400,180))
            questions_buttons(400,180,327,300, None, action = 'wyrright2')
            pygame.display.update()
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L3, (80,180))
            questions_buttons(80,180,327,300, None, action = 'wyrleft3')
            gameDisplay.blit(R3, (400,180))
            questions_buttons(400,180,327,300, None, action = 'wyrrigh3')
            pygame.display.update()
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L4, (80,180))
            questions_buttons(80,180,327,300, None, action = 'wyrleft4')
            gameDisplay.blit(R4, (400,180))
            questions_buttons(400,180,327,300, None, action = 'wyrright4')
            pygame.display.update()
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L5, (80,180))
            questions_buttons(80,180,327,300, None, action = 'wyrleft5')
            gameDisplay.blit(R5, (400,180))
            questions_buttons(400,180,327,300, None, action = 'wyrright5')
            pygame.display.update()
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L6, (80,180))
            questions_buttons(80,180,327,300, None, action = 'wyrleft6')
            gameDisplay.blit(R6, (400,180))
            questions_buttons(400,180,327,300, None, action = 'wyrright6')
            pygame.display.update()
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == True and moon_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L7, (80,180))
            questions_buttons(80,180,327,300, None, action = 'wyrleft7')
            gameDisplay.blit(R7, (400,180))
            questions_buttons(400,180,327,300, None, action = 'wyrright7')
            pygame.display.update()
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == True and moon_question7_run == True and moon_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L8, (80,180))
            questions_buttons(80,180,327,300, None, action = 'wyrleft8')
            gameDisplay.blit(R8, (400,180))
            questions_buttons(400,180,327,300, None, action = 'wyrright8')
            pygame.display.update()
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == True and moon_question7_run == True and moon_question8_run == True and moon_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L9, (80,180))
            questions_buttons(80,180,327,300, None, action = 'wyrleft9')
            gameDisplay.blit(R9, (400,180))
            questions_buttons(400,180,327,300, None, action = 'wyrright9')
            pygame.display.update()
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == True and moon_question7_run == True and moon_question8_run == True and moon_question9_run == True and moon_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L10, (80,180))
            questions_buttons(80,180,327,300, None, action = 'wyrleft10')
            gameDisplay.blit(R10, (400,180))
            questions_buttons(400,180,327,300, None, action = 'wyrright10')
            pygame.display.update()
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == True and moon_question7_run == True and moon_question8_run == True and moon_question9_run == True and moon_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(welldone, (150,50))
            print("First Score = ", moon_score)
            message_to_screen_text_sun("Youre Score:10/10", white)
            with open("resources/scores/moonscore.txt", 'w') as f:
                f.write('10')
                        
                
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])
            gameDisplay.blit(restarttext, (310,200))
            questions_buttons(280,195,260,65, grey, action = 'restartmoon')

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])
            gameDisplay.blit(levelstext, (310,280))
            questions_buttons(280,270,260,75, grey, action = 'levels')


            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])
            gameDisplay.blit(mainmtext, (310,365))
            questions_buttons(280,350,260,75, grey, action = 'mainm')

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])
            gameDisplay.blit(quittext, (340,440))
            questions_buttons(280,430,260,75, grey, action = 'quit')
            pygame.display.update()
        pygame.display.update()
        clock.tick(fps)

def saturn_quiz():
    global saturn_question1_run
    global saturn_question2_run
    global saturn_question3_run
    global saturn_question4_run
    global saturn_question5_run
    global saturn_question6_run
    global saturn_question7_run
    global saturn_question8_run
    global saturn_question9_run
    global saturn_question10_run
    global saturn_end
    global saturn_score
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if saturn_question1_run == False: #QUESTION 1
            coming_soon()
        elif saturn_question1_run == True and saturn_question2_run == False: #QUESTION 2
            pass
        elif saturn_question1_run == True and saturn_question2_run == True and saturn_question3_run == False: #QUESTION 3
            pass
        elif saturn_question1_run == True and saturn_question2_run == True and saturn_question3_run == True and saturn_question4_run == False: #QUESTION 4       
            pass
        elif saturn_question1_run == True and saturn_question2_run == True and saturn_question3_run == True and saturn_question4_run == True and saturn_question5_run == False: #QUESTION 5
            pass
        elif saturn_question1_run == True and saturn_question2_run == True and saturn_question3_run == True and saturn_question4_run == True and saturn_question5_run == True and saturn_question6_run == False: #QUESTION 6
            pass
        elif saturn_question1_run == True and saturn_question2_run == True and saturn_question3_run == True and saturn_question4_run == True and saturn_question5_run == True and saturn_question6_run == True and saturn_question7_run == False: #QUESTION 7                                                           
            pass
        elif saturn_question1_run == True and saturn_question2_run == True and saturn_question3_run == True and saturn_question4_run == True and saturn_question5_run == True and saturn_question6_run == True and saturn_question7_run == True and saturn_question8_run == False: #QUESTION 8
            pass
        elif saturn_question1_run == True and saturn_question2_run == True and saturn_question3_run == True and saturn_question4_run == True and saturn_question5_run == True and saturn_question6_run == True and saturn_question7_run == True and saturn_question8_run == True and saturn_question9_run == False: #QUESTION 9                         
            pass
        elif saturn_question1_run == True and saturn_question2_run == True and saturn_question3_run == True and saturn_question4_run == True and saturn_question5_run == True and saturn_question6_run == True and saturn_question7_run == True and saturn_question8_run == True and saturn_question9_run == True and saturn_end == False: #QUESTION 10
            pass
        elif saturn_question1_run == True and saturn_question2_run == True and saturn_question3_run == True and saturn_question4_run == True and saturn_question5_run == True and saturn_question6_run == True and saturn_question7_run == True and saturn_question8_run == True and saturn_question9_run == True and saturn_end == True: #QUESTION 10
            pass
        pygame.display.update()
        clock.tick(fps)
########################################################################URANUS QUIZ##########################################################################
def uranus_quiz():
    global uranus_question1_run
    global uranus_question2_run
    global uranus_question3_run
    global uranus_question4_run
    global uranus_question5_run
    global uranus_question6_run
    global uranus_question7_run
    global uranus_question8_run
    global uranus_question9_run
    global uranus_question10_run
    global uranus_end
    global uranus_score
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if uranus_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(uranus_question_1, (100,0))
            gameDisplay.blit(porgimg, (180,300))
            gameDisplay.blit(nova, (100,230))
            questions_buttons(100,230,170,85, None, action = 'nova')
            gameDisplay.blit(poru, (300,230))
            questions_buttons(300,230,170,85, None, action = 'poru')
            gameDisplay.blit(porg, (500,230))
            questions_buttons(500,230,170,85, None, action = 'porg')
            pygame.display.update()    
        elif uranus_question1_run == True and uranus_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(uranus_question_2, (0,0))
            gameDisplay.blit(yoda, (300,300))
            gameDisplay.blit(yodu, (20,230))
            questions_buttons(20,230,170,85, None, action = 'yodu')
            gameDisplay.blit(yaddle, (180,230))
            questions_buttons(180,230,170,85, None, action = 'yaddle')
            gameDisplay.blit(yanna, (380,230))
            questions_buttons(380,230,170,85, None, action = 'yanna')
            gameDisplay.blit(yodan, (570,230))
            questions_buttons(570,230,170,85, None, action = 'yodan')
            pygame.display.update()    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(uranus_question_3, (50,0))
            gameDisplay.blit(kyberimg, (250,400))
            gameDisplay.blit(kybar, (10,200))
            questions_buttons(10,200,390,100, None, action = 'kybar')
            gameDisplay.blit(kybur, (440,200))
            questions_buttons(440,200,390,100, None, action = 'kybur')
            gameDisplay.blit(kyber, (10,300))
            questions_buttons(10,300,390,100, None, action = 'kyber')
            gameDisplay.blit(kyba, (440,300))
            questions_buttons(440,300,390,100, None, action = 'kyba')
            pygame.display.update()    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(uranus_question_4, (100,0))
            gameDisplay.blit(yoda, (20,200))
            questions_buttons(20,200,205,250, None, action = 'yoda1')
            gameDisplay.blit(anakin, (550,200))
            questions_buttons(300,200,250,250, None, action = 'anakin1')
            gameDisplay.blit(luke, (250,200))
            questions_buttons(250,200,280,242, None, action = 'luke1')
            pygame.display.update()    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == False: #QUESTION 5gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(uranus_question_5, (0,0))
            gameDisplay.blit(leia, (30,220))
            questions_buttons(20,220,205,250, None, action = 'leia2')
            gameDisplay.blit(anakin, (520,220))
            questions_buttons(300,220,250,250, None, action = 'anakin2')
            gameDisplay.blit(luke, (220,220))
            questions_buttons(250,220,280,242, None, action = 'luke2')
            pygame.display.update()    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(uranus_question_6, (130,20))
            gameDisplay.blit(anewhope, (100,230))
            questions_buttons(100,230,185,300, None, action = 'anewhope')
            gameDisplay.blit(returnofthejedi, (300,230))
            questions_buttons(300,230,190,300, None, action = 'returnofthejedi')
            gameDisplay.blit(thelastjedi, (500,230))
            questions_buttons(500,230,200,300, None, action = 'thelastjedi')
            pygame.display.update()   
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == True and uranus_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(uranus_question_7, (100,0))
            gameDisplay.blit(c3po, (10,230))
            questions_buttons(10,230,185,300, None, action = 'c3po')
            gameDisplay.blit(bb8, (300,230))
            questions_buttons(300,230,190,300, None, action = 'bb8')
            gameDisplay.blit(r2d2, (550,230))
            questions_buttons(500,230,200,300, None, action = 'r2d2')
            pygame.display.update()    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == True and uranus_question7_run == True and uranus_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(uranus_question_8, (0,0))
            gameDisplay.blit(fn2187, (250,300))
            gameDisplay.blit(bud, (100,230))
            questions_buttons(100,230,170,85, None, action = 'bud')
            gameDisplay.blit(finn, (300,230))
            questions_buttons(300,230,170,85, None, action = 'finn')
            gameDisplay.blit(john, (500,230))
            questions_buttons(500,230,170,85, None, action = 'john')
            pygame.display.update()    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == True and uranus_question7_run == True and uranus_question8_run == True and uranus_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(uranus_question_9, (100,0))
            gameDisplay.blit(xwing, (200,410))
            questions_buttons(200,410,400,225, None, action = 'xwing')
            gameDisplay.blit(falcon, (0,180))
            questions_buttons(0,180,400,225, None, action = 'falcon')
            gameDisplay.blit(enterprise, (400,180))
            questions_buttons(400,180,400,225, None, action = 'enterprise')
            pygame.display.update()    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == True and uranus_question7_run == True and uranus_question8_run == True and uranus_question9_run == True and uranus_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(uranus_question_10, (100,0))
            gameDisplay.blit(jedichurch, (330,150))
            gameDisplay.blit(true, (200,300))
            questions_buttons(200,250,130,130, None, action = 'jedi')
            gameDisplay.blit(false, (450,300))
            questions_buttons(250,400,130,130, None, action = 'jedi')
            pygame.display.update()
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == True and uranus_question7_run == True and uranus_question8_run == True and uranus_question9_run == True and uranus_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(congratulations, (0,50))
            print("First Score = ", uranus_score)
            uranus_score = str(uranus_score)
            message_to_screen_text_uranus("Youre Score:      /10", white)
            message_to_screen_text_uranus_score(uranus_score, white)
            with open("resources/scores/uranusscore.txt", 'r') as f:
                for line in f:
                    print("uranus Score: ", uranus_score)
                    print("uranus Read: ", line)
                    int(line)
            
            if uranus_score > line:
                print("uranus_score > line")
                with open("resources/scores/uranusscore.txt", 'w') as f:
                        f.write(uranus_score)
                        
            elif uranus_score < line:
                print("uranus_score is less than line")
                print("ES:", uranus_score)
                print("L:", line)
                
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])
            gameDisplay.blit(restarttext, (310,200))
            questions_buttons(280,195,260,65, grey, action = 'restarturanus')

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])
            gameDisplay.blit(levelstext, (310,280))
            questions_buttons(280,270,260,75, grey, action = 'levels')


            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])
            gameDisplay.blit(mainmtext, (310,365))
            questions_buttons(280,350,260,75, grey, action = 'mainm')

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])
            gameDisplay.blit(quittext, (340,440))
            questions_buttons(280,430,260,75, grey, action = 'quit')
            pygame.display.update()
            pygame.display.update()    
        pygame.display.update()
        clock.tick(fps)
def message_to_screen_text_uranus(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)
    gameDisplay.blit(textSurf, textRect)

def message_to_screen_text_uranus_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)
    gameDisplay.blit(textSurf, textRect)       

def mercury_quiz():
    global mercury_question1_run
    global mercury_question2_run
    global mercury_question3_run
    global mercury_question4_run
    global mercury_question5_run
    global mercury_question6_run
    global mercury_question7_run
    global mercury_question8_run
    global mercury_question9_run
    global mercury_question10_run
    global mercury_end
    global mercury_score
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if mercury_question1_run == False: #QUESTION 1
            coming_soon()
        elif mercury_question1_run == True and mercury_question2_run == False: #QUESTION 2
            pass
        elif mercury_question1_run == True and mercury_question2_run == True and mercury_question3_run == False: #QUESTION 3
            pass
        elif mercury_question1_run == True and mercury_question2_run == True and mercury_question3_run == True and mercury_question4_run == False: #QUESTION 4       
            pass
        elif mercury_question1_run == True and mercury_question2_run == True and mercury_question3_run == True and mercury_question4_run == True and mercury_question5_run == False: #QUESTION 5
            pass
        elif mercury_question1_run == True and mercury_question2_run == True and mercury_question3_run == True and mercury_question4_run == True and mercury_question5_run == True and mercury_question6_run == False: #QUESTION 6
            pass
        elif mercury_question1_run == True and mercury_question2_run == True and mercury_question3_run == True and mercury_question4_run == True and mercury_question5_run == True and mercury_question6_run == True and mercury_question7_run == False: #QUESTION 7                                                           
            pass
        elif mercury_question1_run == True and mercury_question2_run == True and mercury_question3_run == True and mercury_question4_run == True and mercury_question5_run == True and mercury_question6_run == True and mercury_question7_run == True and mercury_question8_run == False: #QUESTION 8
            pass
        elif mercury_question1_run == True and mercury_question2_run == True and mercury_question3_run == True and mercury_question4_run == True and mercury_question5_run == True and mercury_question6_run == True and mercury_question7_run == True and mercury_question8_run == True and mercury_question9_run == False: #QUESTION 9                         
            pass
        elif mercury_question1_run == True and mercury_question2_run == True and mercury_question3_run == True and mercury_question4_run == True and mercury_question5_run == True and mercury_question6_run == True and mercury_question7_run == True and mercury_question8_run == True and mercury_question9_run == True and mercury_end == False: #QUESTION 10
            pass
        elif mercury_question1_run == True and mercury_question2_run == True and mercury_question3_run == True and mercury_question4_run == True and mercury_question5_run == True and mercury_question6_run == True and mercury_question7_run == True and mercury_question8_run == True and mercury_question9_run == True and mercury_end == True: #QUESTION 10
            pass
        pygame.display.update()
        clock.tick(fps)

def jupiter_quiz():
    global jupiter_question1_run
    global jupiter_question2_run
    global jupiter_question3_run
    global jupiter_question4_run
    global jupiter_question5_run
    global jupiter_question6_run
    global jupiter_question7_run
    global jupiter_question8_run
    global jupiter_question9_run
    global jupiter_question10_run
    global jupiter_end
    global jupiter_score
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = False
 
        if jupiter_question1_run == False: #QUESTION 1
            coming_soon()
        elif jupiter_question1_run == True and jupiter_question2_run == False: #QUESTION 2
            pass
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == False: #QUESTION 3
            pass
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == False: #QUESTION 4       
            pass
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == False: #QUESTION 5
            pass
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == False: #QUESTION 6
            pass
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == True and jupiter_question7_run == False: #QUESTION 7                                                           
            pass
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == True and jupiter_question7_run == True and jupiter_question8_run == False: #QUESTION 8
            pass
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == True and jupiter_question7_run == True and jupiter_question8_run == True and jupiter_question9_run == False: #QUESTION 9                         
            pass
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == True and jupiter_question7_run == True and jupiter_question8_run == True and jupiter_question9_run == True and jupiter_end == False: #QUESTION 10
            pass
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == True and jupiter_question7_run == True and jupiter_question8_run == True and jupiter_question9_run == True and jupiter_end == True: #QUESTION 10
            pass
        pygame.display.update()
        clock.tick(fps)    

############################################################################################################################################################
##########################################################################MARS GENIUS/IDIOT TEST##################################################################################
############################################################################################################################################################        
def mars_quiz():
    global mars_question1_run
    global mars_question2_run
    global mars_question3_run
    global mars_question4_run
    global mars_question5_run
    global mars_question6_run
    global mars_question7_run
    global mars_question8_run
    global mars_question9_run
    global mars_question10_run
    global mars_end
    global mars_score
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if mars_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(mars_question_1, (0,0))
            pygame.draw.rect(gameDisplay, orange, [100,100,160,160])
            questions_buttons(100,100,160,160, orange, action = 'q')
            pygame.draw.rect(gameDisplay, blue, [600,560,10,10])
            questions_buttons(600,560,10,10, blue, action = 'a')
            pygame.draw.rect(gameDisplay, white, [356,100,220,220])
            questions_buttons(356,100,220,220, white, action = 'q')
            pygame.draw.rect(gameDisplay, yellow, [600,287,113,220])
            questions_buttons(600,287,113,220, yellow, action = 'q')
            pygame.draw.rect(gameDisplay, red, [250,350,88,110])
            questions_buttons(250,350,88,110, red, action = 'q')
            pygame.draw.rect(gameDisplay, green, [55,430,70,60])
            questions_buttons(55,430,70,60, green, action = 'q')
            pygame.draw.rect(gameDisplay, pink, [477,467,55,32])
            questions_buttons(477,467,55,32, pink, action = 'q')
            pygame.draw.rect(gameDisplay, blue, [600,145,90,81])
            questions_buttons(600,145,90,81, blue, action = 'q')
            pygame.display.update()
        elif mars_question1_run == True and mars_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(mars_question_2, (0,0))
            questions_buttons(400,20,110,50, transparent, action = 'yesrect')
            gameDisplay.blit(no, (300,200))
            questions_buttons(300,200,140,140, transparent, action = 'norect')
            gameDisplay.blit(no, (100,67))
            questions_buttons(100,67,140,140, transparent, action = 'norect')
            gameDisplay.blit(no, (400,337))
            questions_buttons(400,337,140,140, transparent, action = 'norect')
            gameDisplay.blit(no, (600,24))
            questions_buttons(600,24,140,140, transparent, action = 'norect')
            gameDisplay.blit(no, (45,400))
            questions_buttons(45,400,140,140, transparent, action = 'norect')
            gameDisplay.blit(no, (670,400))
            questions_buttons(670,400,140,140, transparent, action = 'norect')
            pygame.display.update()
        elif mars_question1_run == True and mars_question2_run == True and mars_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(mars_question_3, (0,0))
            #1st Row
            pygame.draw.rect(gameDisplay, red, [75,100,100,100]) and pygame.draw.rect(gameDisplay, red, [225,100,100,100]) and pygame.draw.rect(gameDisplay, red, [375,100,100,100]) and pygame.draw.rect(gameDisplay, red, [525,100,100,100]) and pygame.draw.rect(gameDisplay, red, [675,100,100,100])
            #2nd Row
            pygame.draw.rect(gameDisplay, red, [75,250,100,100]) and pygame.draw.rect(gameDisplay, red, [225,250,100,100]) and pygame.draw.rect(gameDisplay, red, [375,250,100,100]) and pygame.draw.rect(gameDisplay, red, [525,250,100,100]) and pygame.draw.rect(gameDisplay, red, [675,250,100,100])
            #3rd Row
            pygame.draw.rect(gameDisplay, red, [75,400,100,100]) and pygame.draw.rect(gameDisplay, red, [225,400,100,100]) and pygame.draw.rect(gameDisplay, red, [375,400,100,100]) and pygame.draw.rect(gameDisplay, red, [525,400,100,100]) and pygame.draw.rect(gameDisplay, red, [675,400,100,100])
            questions_buttons_idiot_test(75,100,100,100, green, action = 'thered1')
            questions_buttons_idiot_test(75,400,100,100, orange, action = 'thered1')
            questions_buttons_idiot_test(75,250,100,100, yellow, action = 'thered1')
            questions_buttons_idiot_test(225,100,100,100, pink, action = 'thered1')
            questions_buttons_idiot_test(225,400,100,100, yellow, action = 'thered1')
            questions_buttons_idiot_test(225,250,100,100, orange, action = 'thered1')
            questions_buttons_idiot_test(375,100,100,100, purple, action = 'thered1')
            questions_buttons_idiot_test(375,400,100,100, black, action = 'thered1')
            questions_buttons_idiot_test(375,250,100,100, white, action = 'thered1')
            questions_buttons_idiot_test(525,100,100,100, grey, action = 'thered1')
            questions_buttons_idiot_test(525,400,100,100, orange, action = 'thered1')
            questions_buttons_idiot_test(525,250,100,100, brown, action = 'thered1')
            questions_buttons_idiot_test(675,100,100,100, green, action = 'thered1')
            questions_buttons_idiot_test(675,400,100,100, lightbrown, action = 'thered1')
            questions_buttons_idiot_test(675,250,100,100, blue, action = 'theblue1')
            pygame.display.update()
        elif mars_question1_run == True and mars_question2_run == True and mars_question3_run == True and mars_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(mars_question_4, (0,0))
            questions_buttons(540,30,160,40, None, action = 'dontclick') #HERE
            questions_buttons(290,120,120,40, None, action = 'dontclick')#ME
            questions_buttons(250,250,160,40, None, action = 'dontclick') #HERE
            questions_buttons(560,290,120,40, None, action = 'dontclick') #ME
            questions_buttons(140,330,100,40, None, action = 'dontclick') #HERE
            questions_buttons(460,400,100,40, None, action = 'dontclick') #HERE
            questions_buttons(520,550,100,40, None, action = 'dontclick') #HERE
            questions_buttons(620,160,100,40, None, action = 'click')     #HERE  
            pygame.display.update()
        elif mars_question1_run == True and mars_question2_run == True and mars_question3_run == True and mars_question4_run == True and mars_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(mars_question_5, (0,0))
            questions_buttons(0,0,800,600, None, action = 'justclick') 
            pygame.display.update()
        elif mars_question1_run == True and mars_question2_run == True and mars_question3_run == True and mars_question4_run == True and mars_question5_run == True and mars_end == True:
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(congratulations, (0,50))
            print("First Score = ", mars_score)
            mars_score = str(mars_score)
            message_to_screen_text_mars("Youre Score:      /10", white)
            message_to_screen_text_mars_score(mars_score, white)
            with open("resources/scores/marsscore.txt", 'r') as f:
                for line in f:
                    print("mars Score: ", mars_score)
                    print("mars Read: ", line)
                    int(line)
            
            if mars_score > line:
                print("mars_score > line")
                with open("resources/scores/marsscore.txt", 'w') as f:
                        f.write(mars_score)
                        
            elif mars_score < line:
                print("mars_score is less than line")
                print("ES:", mars_score)
                print("L:", line)
        pygame.display.update()
        clock.tick(fps)
def message_to_screen_text_mars(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)
    gameDisplay.blit(textSurf, textRect)

def message_to_screen_text_mars_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)
    gameDisplay.blit(textSurf, textRect)
    
def pluto_quiz():
    global pluto_question1_run
    global pluto_question2_run
    global pluto_question3_run
    global pluto_question4_run
    global pluto_question5_run
    global pluto_question6_run
    global pluto_question7_run
    global pluto_question8_run
    global pluto_question9_run
    global pluto_question10_run
    global pluto_end
    global pluto_score
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if pluto_question1_run == False: #QUESTION 1
            coming_soon()
        elif pluto_question1_run == True and pluto_question2_run == False: #QUESTION 2
            pass
        elif pluto_question1_run == True and pluto_question2_run == True and pluto_question3_run == False: #QUESTION 3
            pass
        elif pluto_question1_run == True and pluto_question2_run == True and pluto_question3_run == True and pluto_question4_run == False: #QUESTION 4       
            pass
        elif pluto_question1_run == True and pluto_question2_run == True and pluto_question3_run == True and pluto_question4_run == True and pluto_question5_run == False: #QUESTION 5
            pass
        elif pluto_question1_run == True and pluto_question2_run == True and pluto_question3_run == True and pluto_question4_run == True and pluto_question5_run == True and pluto_question6_run == False: #QUESTION 6
            pass
        elif pluto_question1_run == True and pluto_question2_run == True and pluto_question3_run == True and pluto_question4_run == True and pluto_question5_run == True and pluto_question6_run == True and pluto_question7_run == False: #QUESTION 7                                                           
            pass
        elif pluto_question1_run == True and pluto_question2_run == True and pluto_question3_run == True and pluto_question4_run == True and pluto_question5_run == True and pluto_question6_run == True and pluto_question7_run == True and pluto_question8_run == False: #QUESTION 8
            pass
        elif pluto_question1_run == True and pluto_question2_run == True and pluto_question3_run == True and pluto_question4_run == True and pluto_question5_run == True and pluto_question6_run == True and pluto_question7_run == True and pluto_question8_run == True and pluto_question9_run == False: #QUESTION 9                         
            pass
        elif pluto_question1_run == True and pluto_question2_run == True and pluto_question3_run == True and pluto_question4_run == True and pluto_question5_run == True and pluto_question6_run == True and pluto_question7_run == True and pluto_question8_run == True and pluto_question9_run == True and pluto_end == False: #QUESTION 10
            pass
        elif pluto_question1_run == True and pluto_question2_run == True and pluto_question3_run == True and pluto_question4_run == True and pluto_question5_run == True and pluto_question6_run == True and pluto_question7_run == True and pluto_question8_run == True and pluto_question9_run == True and pluto_end == True: #QUESTION 10
            pass
        pygame.display.update()
        clock.tick(fps)

#################################VENUS QUIZ#################################
def venus_quiz():
    global venus_question1_run
    global venus_question2_run
    global venus_question3_run
    global venus_question4_run
    global venus_question5_run
    global venus_question6_run
    global venus_question7_run
    global venus_question8_run
    global venus_question9_run
    global venus_question10_run
    global venus_end
    global venus_score
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if venus_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(venus_question_1, (120,10))
            gameDisplay.blit(bull, (220,180))
            gameDisplay.blit(true, (200,450))
            questions_buttons(200,450,130,130, None, action = 'true2')
            gameDisplay.blit(false, (450,450))
            questions_buttons(450,400,130,130, None, action = 'false2')
            pygame.display.update()
        elif venus_question1_run == True and venus_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(venus_question_2, (0,10))
            gameDisplay.blit(brain, (260,180))
            gameDisplay.blit(true, (200,450))
            questions_buttons(200,450,130,130, None, action = 'true3')
            gameDisplay.blit(false, (450,450))
            questions_buttons(450,450,130,130, None, action = 'false3')
            pygame.display.update()
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(venus_question_3, (10,0))
            gameDisplay.blit(email, (250,180))
            gameDisplay.blit(true, (200,450))
            questions_buttons(200,450,130,130, None, action = 'true4')
            gameDisplay.blit(false, (450,450))
            questions_buttons(450,450,130,130, None, action = 'false4')
            pygame.display.update()
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(venus_question_4, (0,10))
            gameDisplay.blit(solar, (180,190))
            gameDisplay.blit(true, (200,450))
            questions_buttons(200,450,130,130, None, action = 'true5')
            gameDisplay.blit(false, (450,450))
            questions_buttons(450,450,130,130, None, action = 'false5')
            pygame.display.update()
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(venus_question_5, (130,10))
            gameDisplay.blit(cheetah, (250,185))
            gameDisplay.blit(true, (200,450))
            questions_buttons(200,450,130,130, None, action = 'true6')
            gameDisplay.blit(false, (450,450))
            questions_buttons(450,450,130,130, None, action = 'false6')
            pygame.display.update()
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(venus_question_6, (50,10))
            gameDisplay.blit(ball, (260,180))
            gameDisplay.blit(true, (200,450))
            questions_buttons(200,450,130,130, None, action = 'true7')
            gameDisplay.blit(false, (450,450))
            questions_buttons(450,450,130,130, None, action = 'false7')
            pygame.display.update()
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == True and venus_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(venus_question_7, (40,10))
            gameDisplay.blit(hammer, (260,170))
            gameDisplay.blit(true, (200,450))
            questions_buttons(200,450,130,130, None, action = 'true8')
            gameDisplay.blit(false, (450,450))
            questions_buttons(450,450,130,130, None, action = 'false8')
            pygame.display.update()
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == True and venus_question7_run == True and venus_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(venus_question_8, (100,10))
            gameDisplay.blit(spin, (270,185))
            gameDisplay.blit(true, (200,450))
            questions_buttons(200,450,130,130, None, action = 'true9')
            gameDisplay.blit(false, (450,450))
            questions_buttons(450,450,130,130, None, action = 'false9')
            pygame.display.update()
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == True and venus_question7_run == True and venus_question8_run == True and venus_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(venus_question_9, (100,10))
            gameDisplay.blit(lightning, (210,185))
            gameDisplay.blit(true, (200,450))
            questions_buttons(200,450,130,130, None, action = 'true10')
            gameDisplay.blit(false, (450,450))
            questions_buttons(450,450,130,130, None, action = 'false10')
            pygame.display.update()
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == True and venus_question7_run == True and venus_question8_run == True and venus_question9_run == True and venus_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(venus_question_10, (100,10))
            gameDisplay.blit(griffin, (310,150))
            gameDisplay.blit(true, (200,450))
            questions_buttons(200,450,130,130, None, action = 'true11')
            gameDisplay.blit(false, (450,450))
            questions_buttons(450,450,130,130, None, action = 'false11')
            pygame.display.update()
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == True and venus_question7_run == True and venus_question8_run == True and venus_question9_run == True and venus_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(congrats, (0,50))
            print("First Score = ", venus_score)
            venus_score = str(venus_score)
            message_to_screen_text_venus("Youre Score:      /10", white)
            message_to_screen_text_venus_score(venus_score, white)
            with open("resources/scores/venusscore.txt", 'r') as f:
                for line in f:
                    print("venus Score: ", venus_score)
                    print("venus Read: ", line)
                    int(line)
                    int(venus_score)
            
            if venus_score > line:
                print("venus_score > line")
                with open("resources/scores/venusscore.txt", 'w') as f:
                    f.write(venus_score)
                        
            elif venus_score < line:
                print("venus_score is less than line")
                print("SS:", venus_score)
                print("L:", line)
                
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])
            gameDisplay.blit(restarttext, (310,200))
            questions_buttons(280,195,260,65, grey, action = 'restartvenus')

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])
            gameDisplay.blit(levelstext, (310,280))
            questions_buttons(280,270,260,75, grey, action = 'levels')


            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])
            gameDisplay.blit(mainmtext, (310,365))
            questions_buttons(280,350,260,75, grey, action = 'mainm')

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])
            gameDisplay.blit(quittext, (340,440))
            questions_buttons(280,430,260,75, grey, action = 'quit')
            pygame.display.update()
        pygame.display.update()
        clock.tick(fps)
def message_to_screen_text_venus(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)
    gameDisplay.blit(textSurf, textRect)

def message_to_screen_text_venus_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)
    gameDisplay.blit(textSurf, textRect)

#################################NEPTUNE QUIZ#################################
def neptune_quiz():
    global neptune_question1_run
    global neptune_question2_run
    global neptune_question3_run
    global neptune_question4_run
    global neptune_question5_run
    global neptune_question6_run
    global neptune_question7_run
    global neptune_question8_run
    global neptune_question9_run
    global neptune_question10_run
    global neptune_end
    global neptune_score
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if neptune_question1_run == False: #QUESTION 1
            coming_soon()
        elif neptune_question1_run == True and neptune_question2_run == False: #QUESTION 2
            pass
        elif neptune_question1_run == True and neptune_question2_run == True and neptune_question3_run == False: #QUESTION 3
            pass
        elif neptune_question1_run == True and neptune_question2_run == True and neptune_question3_run == True and neptune_question4_run == False: #QUESTION 4       
            pass
        elif neptune_question1_run == True and neptune_question2_run == True and neptune_question3_run == True and neptune_question4_run == True and neptune_question5_run == False: #QUESTION 5
            pass
        elif neptune_question1_run == True and neptune_question2_run == True and neptune_question3_run == True and neptune_question4_run == True and neptune_question5_run == True and neptune_question6_run == False: #QUESTION 6
            pass
        elif neptune_question1_run == True and neptune_question2_run == True and neptune_question3_run == True and neptune_question4_run == True and neptune_question5_run == True and neptune_question6_run == True and neptune_question7_run == False: #QUESTION 7                                                           
            pass
        elif neptune_question1_run == True and neptune_question2_run == True and neptune_question3_run == True and neptune_question4_run == True and neptune_question5_run == True and neptune_question6_run == True and neptune_question7_run == True and neptune_question8_run == False: #QUESTION 8
            pass
        elif neptune_question1_run == True and neptune_question2_run == True and neptune_question3_run == True and neptune_question4_run == True and neptune_question5_run == True and neptune_question6_run == True and neptune_question7_run == True and neptune_question8_run == True and neptune_question9_run == False: #QUESTION 9                         
            pass
        elif neptune_question1_run == True and neptune_question2_run == True and neptune_question3_run == True and neptune_question4_run == True and neptune_question5_run == True and neptune_question6_run == True and neptune_question7_run == True and neptune_question8_run == True and neptune_question9_run == True and neptune_end == False: #QUESTION 10
            pass
        elif neptune_question1_run == True and neptune_question2_run == True and neptune_question3_run == True and neptune_question4_run == True and neptune_question5_run == True and neptune_question6_run == True and neptune_question7_run == True and neptune_question8_run == True and neptune_question9_run == True and neptune_end == True: #QUESTION 10
            pass
        pygame.display.update()
        clock.tick(fps)

def correct():
    gameDisplay.fill(green) 
    gameDisplay.blit(correctimg, (250,150))
    pygame.display.update()
    time.sleep(1)

def wrong():
    gameDisplay.fill(red) 
    gameDisplay.blit(wrongimg, (100,0))
    pygame.display.update()
    time.sleep(1)

def trick():
    gameDisplay.blit(trickimg, (0,0))
    pygame.display.update()
    time.sleep(1)

def questions_buttons_idiot_test(x,y,width,height,active_color,action = None):
    global mars_question1_run
    global mars_question2_run
    global mars_question3_run
    global mars_question4_run
    global mars_question5_run
    global mars_question6_run
    global mars_question7_run
    global mars_question8_run
    global mars_question9_run
    global mars_question10_run
    global mars_end
    global mars_score
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "thered1":
                wrong()
                mars_question3_run = True
            if action == "theblue1":
                correct()
                mars_score += 2
                print(mars_score)
                mars_question3_run = True
def questions_buttons(x,y,width,height,active_color, action = None):
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
    global sun_question1_run
    global sun_question2_run
    global sun_question3_run
    global sun_question4_run
    global sun_question5_run
    global sun_question6_run
    global sun_question7_run
    global sun_question8_run
    global sun_question9_run
    global sun_question10_run
    global sun_end
    global sun_score
    global moon_question1_run
    global moon_question2_run
    global moon_question3_run
    global moon_question4_run
    global moon_question5_run
    global moon_question6_run
    global moon_question7_run
    global moon_question8_run
    global moon_question9_run
    global moon_question10_run
    global moon_end
    global moon_score
    global venus_question1_run
    global venus_question2_run
    global venus_question3_run
    global venus_question4_run
    global venus_question5_run
    global venus_question6_run
    global venus_question7_run
    global venus_question8_run
    global venus_question9_run
    global venus_question10_run
    global venus_end
    global venus_score
    global uranus_question1_run
    global uranus_question2_run
    global uranus_question3_run
    global uranus_question4_run
    global uranus_question5_run
    global uranus_question6_run
    global uranus_question7_run
    global uranus_question8_run
    global uranus_question9_run
    global uranus_question10_run
    global uranus_end
    global uranus_score
    global mars_question1_run
    global mars_question2_run
    global mars_question3_run
    global mars_question4_run
    global mars_question5_run
    global mars_end
    global mars_score  
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            clickaudio.play()
            time.sleep(0.5)
            if action == "windows1":
                wrong()
                earth_question1_run = True
            if action == "linux1":
                correct()
                earth_question1_run = True
                earth_score += 1
                print(earth_score)
            if action == "apple1":
                wrong()
                earth_question1_run = True
            if action == "windows2":
                correct()
                earth_question2_run = True
                earth_score += 1
                print(earth_score)
            if action == "linux2":
                wrong()
                earth_question2_run = True
            if action == "apple2":
                wrong()
                earth_question2_run = True
            if action == "windows3":
                wrong()
                earth_question3_run = True
            if action == "linux3":
                wrong()
                earth_question3_run = True
            if action == "apple3":
                correct()
                earth_score += 1
                print(earth_score)
                earth_question3_run = True
            if action == "true1":
                wrong()
                earth_question4_run = True
            if action == "false1":
                correct()
                earth_score += 1
                print(earth_score)
                earth_question4_run = True
            if action == "red1":
                correct()
                earth_score += 1
                print(earth_score)
                earth_question5_run = True
            if action == "orange1" or action == "yellow1" or action == "green1" or action == "blue1" or action == "pink1" or action == "purple1" or action == "white1":
                wrong()
                earth_question5_run = True
            if action == "vr":
                correct()
                earth_score += 1
                print(earth_score)
                earth_question6_run = True
            if action == "vr1" or action == "vr2":
                wrong()
                earth_question6_run = True
            if action == "spacex":
                correct()
                earth_score += 1
                print(earth_score)
                earth_question7_run = True
            if action == "apollox" or action == "nasa":
                wrong()
                earth_question7_run = True
            if action == "windowsos":
                wrong()
                earth_question8_run = True
            if action == "appleos":
                correct()
                earth_score += 1
                print(earth_score)
                earth_question8_run = True
            if action == "flip":
                correct()
                earth_score += 1
                print(earth_score)
                earth_question9_run = True
            if action == "2degrees" or action == "spark" or action == "slingshot" or action == "vodafone" or action == "trustpower":
                wrong()
                earth_question9_run = True
            if action == "yes1" or action == "no1":
                trick()
                earth_score += 1
                print(earth_score)
                earth_end = True
            if action == "restartearth":
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
            if action == "restartsun":
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
                sun_quiz()
            if action == "restartsun":
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
                venus_quiz()
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
                
                main_menu()
            if action == "quit":
                pygame.quit()
                quit()
            if action == "planet":
                wrong()
                sun_question1_run = True
            if action == "star":
                correct()
                sun_score += 1
                print(sun_score)
                sun_question1_run = True

            if action == "armstrong": #Who was first on the moon (Neil 'Armstrong')
                correct()             #Runs the correct() function  
                sun_score += 1        #Adds 1 to the score 
                print(sun_score)      #Prints score to shell 
                sun_question2_run = True #Sets this question to have run
            if action == "chris":
                wrong()
                sun_question2_run = True
            if action == "collins":
                wrong()
                sun_question2_run = True

            if action == "apollo11":
                correct()
                sun_score += 1
                print(sun_score)
                sun_question3_run = True
            if action == "atlantis":
                wrong()
                sun_question3_run = True
            if action == "columbia":
                wrong()
                sun_question3_run = True
            if action == "saturnv":
                correct()
                sun_score += 1
                print(sun_score)
                sun_question4_run = True
            if action == "aresv":
                wrong()
                sun_question4_run = True
            if action == "james1":
                correct()
                sun_score += 1
                print(sun_score)
                sun_question5_run = True
            if action == "collins1":
                wrong()
                sun_question5_run = True
            if action == "chris1":
                wrong()
                sun_question5_run = True
            if action == 'num1' or action == 'num3' or action == 'num4' or action == 'num5':
                wrong()
                sun_question6_run = True
            if action == "num2":
                correct()
                sun_score += 1
                print(sun_score)
                sun_question6_run = True
            if action == "yes2":
                correct()
                sun_score += 1
                print(sun_score)
                sun_question7_run = True
            if action == "no2":
                wrong()
                sun_question7_run = True
            if action == "jupitertxt":
                correct()
                sun_score += 1
                print(sun_score)
                sun_question8_run = True
            if action == "earthtxt" or action == "marstxt" or action == "venustxt":
                wrong()
                sun_question8_run = True
            if action == "mercurytxt1":
                correct()
                sun_score += 1
                print(sun_score)
                sun_question9_run = True
            if action == "earthtxt1" or action == "marstxt1" or action == "venustxt1":
                wrong()
                sun_question9_run = True
                sun_end = True
            if action == "infinity" or action == "mean42" or action == "elseimg":
                trick()
                sun_score += 1
                print(sun_score)
                sun_question10_run = True
                sun_end = True

            if action == "wyrleft1" or action == "wyrright1":
                trick()
                moon_score += 1
                print(moon_score)
                moon_question1_run = True
            if action == "wyrleft2" or action == "wyrright2":
                trick()
                moon_score += 1
                print(moon_score)
                moon_question2_run = True
            if action == "wyrleft3" or action == "wyrright3":
                trick()
                moon_score += 1
                print(moon_score)
                moon_question3_run = True
            if action == "wyrleft4" or action == "wyrright4":
                trick()
                moon_score += 1
                print(moon_score)
                moon_question4_run = True
            if action == "wyrleft5" or action == "wyrright5":
                trick()
                moon_score += 1
                print(moon_score)
                moon_question5_run = True
            if action == "wyrleft6" or action == "wyrright6":
                trick()
                moon_score += 1
                print(moon_score)
                moon_question6_run = True
            if action == "wyrleft7" or action == "wyrright7":
                trick()
                moon_score += 1
                print(moon_score)
                moon_question7_run = True
            if action == "wyrleft8" or action == "wyrright8":
                trick()
                moon_score += 1
                print(moon_score)
                moon_question8_run = True
            if action == "wyrleft9" or action == "wyrright9":
                trick()
                moon_score += 1
                print(moon_score)
                moon_question9_run = True
            if action == "wyrleft10" or action == "wyrright10":
                trick()
                moon_score += 1
                print(moon_score)
                moon_end = True

            if action == "true2":
                wrong()
                venus_question1_run = True
            if action == "false2":
                correct()
                venus_score += 1
                print(venus_score)
                venus_question1_run = True
            if action == "true3":
                wrong()
                venus_question2_run = True
            if action == "false3":
                correct()
                venus_score += 1
                print(venus_score)
                venus_question2_run = True
            if action == "false4":
                wrong()
                venus_question3_run = True
            if action == "true4":
                correct()
                venus_score += 1
                print(venus_score)
                venus_question3_run = True
            if action == "true5":
                wrong()
                venus_question4_run = True
            if action == "false5":
                correct()
                venus_score += 1
                print(venus_score)
                venus_question4_run = True
            if action == "true6":
                wrong()
                venus_question5_run = True
            if action == "false6":
                correct()
                venus_score += 1
                print(venus_score)
                venus_question5_run = True
            if action == "false7":
                wrong()
                venus_question6_run = True
            if action == "true7":
                correct()
                venus_score += 1
                print(venus_score)
                venus_question6_run = True
            if action == "false8":
                wrong()
                venus_question7_run = True
            if action == "true8":
                correct()
                venus_score += 1
                print(venus_score)
                venus_question7_run = True
            if action == "false9":
                wrong()
                venus_question8_run = True
            if action == "true9":
                correct()
                venus_score += 1
                print(venus_score)
                venus_question8_run = True
            if action == "true10":
                wrong()
                venus_question9_run = True
            if action == "false10":
                correct()
                venus_score += 1
                print(venus_score)
                venus_question9_run = True
            if action == "false11":
                wrong()
                venus_question10_run = True
                venus_end = True
            if action == "true11":
                correct()
                venus_score += 1
                print(venus_score)
                venus_question10_run = True
                venus_end = True

            if action == 'nova' or action == 'poru':
                wrong()
                uranus_question1_run = True
            if action == 'porg':
                correct()
                uranus_score += 1
                print(uranus_score)
                uranus_question1_run = True

            if action == 'yodu' or action == 'yanna' or action == "yodan":
                wrong()
                uranus_question2_run = True
            if action == 'yaddle':
                correct()
                uranus_score += 1
                print(uranus_score)
                uranus_question2_run = True
            if action == 'kyba' or action == 'kybar' or action == "kybur":
                wrong()
                uranus_question3_run = True
            if action == 'kyber':
                correct()
                uranus_score += 1
                print(uranus_score)
                uranus_question3_run = True
            if action == 'luke1' or action == 'yoda1':
                wrong()
                uranus_question4_run = True
            if action == 'anakin1':
                correct()
                uranus_score += 1
                print(uranus_score)
                uranus_question4_run = True

            if action == 'luke2' or action == 'yoda2':
                wrong()
                uranus_question5_run = True
            if action == 'leia2':
                correct()
                uranus_score += 1
                print(uranus_score)
                uranus_question5_run = True
            if action == 'anewhope' or action == 'thelastjedi':
                wrong()
                uranus_question6_run = True
            if action == 'returnofthejedi':
                correct()
                uranus_score += 1
                print(uranus_score)
                uranus_question6_run = True
            if action == 'r2d2' or action == 'c3po':
                wrong()
                uranus_question7_run = True
            if action == 'bb8':
                correct()
                uranus_score += 1
                print(uranus_score)
                uranus_question7_run = True
            if action == 'bud' or action == 'john':
                wrong()
                uranus_question8_run = True
            if action == 'finn':
                correct()
                uranus_score += 1
                print(uranus_score)
                uranus_question8_run = True
            if action == 'enterprise' or action == 'xwing':
                wrong()
                uranus_question9_run = True
            if action == 'falcon':
                correct()
                uranus_score += 1
                print(uranus_score)
                uranus_question9_run = True
            if action == 'jedi':
                trick()
                uranus_score += 1
                print(uranus_score)
                uranus_question10_run = True
                uranus_end = True
            if action == 'a':
                correct()
                mars_score += 2
                print(mars_score)
                mars_question1_run = True
            if action == 'q':
                wrong()
                mars_question1_run = True
            if action == 'yesrect':
                correct()
                mars_score += 2
                print(mars_score)
                mars_question2_run = True
            if action == 'norect':
                wrong()
                mars_question2_run = True
            if action == 'click':
                correct()
                mars_score += 2
                print(mars_score)
                mars_question4_run = True
            if action == 'dontclick':
                wrong()
                mars_question4_run = True
            if action == "justclick":
                correct()
                mars_score += 2
                print(mars_score)
                mars_question5_run = True
                mars_end = True

def coming_soon():
    gameDisplay.blit(bg, (0,0))
    gameDisplay.blit(coming, (100,0))
    gameDisplay.blit(smiley, (220,90))
    pygame.draw.rect(gameDisplay, white, [300,440,220,55])
    gameDisplay.blit(backtext, (340,440))
    back_button(280,430,260,75, grey, action = 'backtolevels')
age()#Checks user age
game_loop()   #Will run gameloop firstly
pygame.quit() #Will Quit Game if the game_loop is escaped
quit()        #Quit
