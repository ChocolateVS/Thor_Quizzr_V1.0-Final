###################################################################THOR QUIZZR VERSION 1.0##############################################################

'''
WELCOME TO MY QUIZ CODE PLEASE ENJOY READING ALL 3200 ISH LINES BELOW.... HAVE FUN..... OR NOT.... :)

BY THE WAY QUIZZR IS PURPOSLY MISPELT 

This has taken me a total of probably about 90 - 100 (or more) hours from The Beginning of March to Friday (April) 12/04/18
(It was FUN although not all this time was fully dedicated to this verion)

Took me about 3 hours to fully comment!!!!

OPEN SOURCE, ROWAN THORLEY 

WILL BE UPDATING AND ADDING TO MY WEBSITE AT 'https://rowansblog.tk' at the games section the website is NOT currently active
ALSO GOING TO BE CHANGING QUESTION METHOD TO LISTS IN STEAD OF VARIABLES AND FUNCTIONS

Features
- Working Settings Menu with FPS, SOUND, Tutorial & Controls (Coming Soon)
- High Score Menu
- 7 Functioning Quizzes (4 in Progress)
- Help Menu
- Level Select Menu - With Player Movement
- You can fly through the sides (and appear on the other side) in the levels menu
- Must be a certain age to play
- FULLY COMMENTED :)
- OPEN SOURCE

Coming Soon
- 4 extra quizzes and Updates on current quizzes
- Online Version
- Tutorial
- Controls Setup
- Better Quiz Structure
- Random Question Order
- A quiz that takes random question's from all other quizzes!!!
- File to reset all scored, or an in game function to do so
- Major BUG Fixes

Things to know
- Test Programs, You can find my test programs in the Test Programs and FIles Folder (Same Directory as this quiz file)
- There is an excel spreadsheet located in the same directory as this quiz containing my tests/results for test programs

- Age range is 10 - 18 years 

- In pygame it is not possible to make text inputs without phenomenal amounts of code so I apologize for the lack of these

- Please dont mark me down on not commenting some of these as its just a waste of time) :)
- Also I have talked to my dads programmers and they said it is NOT necessary to comment some of these things becuase
they are extremly obvious and arent needed because programmers are easily able to figure them out. :)

- Global Variables - Anything that has 'global' before it Makes that varible editable from within that function
- Loading Images - pygame.image.load() loads images to the game
- Question_Run Variables - Anything that has a planetname_question_run is used for running question (Pretty Self Explanatory)
- Print - Print prints things to the display
- BLITTING IMAGES - Anywhere there is a gameDisplay.blit(image, (x,y) it means an image is being blit to the screen
BUTTONS - All buttons are set out like this the_button_function_name(x,y,width,height, active_color, action)

ACTUAL TEXT ON THE DISPLAY - (This is quite tricky as pygame doesnt have a built in function for text blitting, this is why i have used mostly images)
- For things Like Scores, all mesages are set out like this message_to_screen_something(the text or variable, color)
Rhis Runs a function taking the variable of you message and the color.

- All buttons will have a #Buttons Comment
- All blits will have a #Blit Comment
- All Actual Text will have a #Actual Text Comment
- All Prints Will have a #Prints To Shell Comment
- All lines with 'pygame.image.load ' Will have an #Image Load Comment
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

#Get Settings
with open('resources/files/fps.txt', 'r') as f: #Opens this file for reading #Opens Frames Per Second File
    fps = int(f.read(3)) #Frames Per Second is equal to what it reads from the file
    print("FPS = ", fps) #Prints The FPS

with open('resources/files/tutorial.txt', 'r') as g: #Opens Tutorial File
    tutorial = g.read() #Sets tutorial to whats in te file (ON/OFF)
    print("Tutorial = ", tutorial) #Prints whether Tutorial is on or off

with open('resources/files/sound.txt', 'r') as s: #Opens Sound File
    sound = s.read() #Sets Sound to what it reads from the file
    print("Sound = ", sound,"%") #Prints Sound
    
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

#Fonts for text in game
font = pygame.font.SysFont(None, 25)

#Player varibles for levels screen
playerName = "anonymous" #Player Name
player_speed = 5
################################################GAME ASSETS##################################################
#Sound
clickaudio = pygame.mixer.Sound("resources/audio/click.wav") #Click Sound
#Settings assests (PLEASE DONT MAKE ME COMMENT ALL THESE)
controls = pygame.image.load("resources/images/controls.png")#Image Load
credits1 = pygame.image.load("resources/images/credits.png")#Image Load
fpsimg = pygame.image.load("resources/images/fps.png")#Image Load
sound = pygame.image.load("resources/images/sound.png")#Image Load
tutorial = pygame.image.load("resources/images/tutorial.png")#Image Load
fpsimage1 = pygame.image.load("resources/text/30.png")#Image Load
fpsimage2 = pygame.image.load("resources/text/60.png")#Image Load
fpsimage3 = pygame.image.load("resources/text/120.png")#Image Load
on = pygame.image.load("resources/text/on.png")#Image Load
off = pygame.image.load("resources/text/off.png")#Image Load
sound1 = pygame.image.load("resources/text/25.png")#Image Load
sound2 = pygame.image.load("resources/text/50.png")#Image Load
sound3 = pygame.image.load("resources/text/75.png")#Image Load
sound4 = pygame.image.load("resources/text/100.png")#Image Load
#Edit Button
edit = pygame.image.load("resources/images/edit.png")#Image Load
#Game Images & assets
bg = pygame.image.load("resources/images/background.jpg")#Image Load
bg1 = pygame.image.load("resources/images/background.png")#Image Load
menubanner = pygame.image.load("resources/images/banner.png")#Image Load
scorebanner = pygame.image.load("resources/images/scorebanner.png")#Image Load
settingsbanner = pygame.image.load("resources/images/settingsbanner.png")#Image Load
player = pygame.image.load("resources/images/player.png")#Image Load
coming = pygame.image.load("resources/images/coming.png")#Image Load
smiley = pygame.image.load("resources/images/smiley.png")#Image Load
#Correct/Wrong/Other
correctimg = pygame.image.load("resources/images/correct.png")#Image Load
wrongimg = pygame.image.load("resources/images/wrong.png")#Image Load
trickimg = pygame.image.load("resources/images/trick.jpg")#Image Load
#Text On Planets
earth_text = pygame.image.load("resources/text/earth.png")#Image Load
mars_text = pygame.image.load("resources/text/mars.png")#Image Load
pluto_text = pygame.image.load("resources/text/pluto.png")#Image Load
moon_text = pygame.image.load("resources/text/moon.png")#Image Load
sun_text = pygame.image.load("resources/text/sun.png")#Image Load
neptune_text = pygame.image.load("resources/text/neptune.png")#Image Load
mercury_text = pygame.image.load("resources/text/mercury.png")#Image Load
jupiter_text = pygame.image.load("resources/text/jupiter.png")#Image Load
uranus_text = pygame.image.load("resources/text/uranus.png")#Image Load
venus_text = pygame.image.load("resources/text/venus.png")#Image Load
saturn_text = pygame.image.load("resources/text/saturn.png")#Image Load
#Text
playtext = pygame.image.load("resources/text/play.png")#Image Load
scoretext = pygame.image.load("resources/text/highscores.png")#Image Load
settingstext = pygame.image.load("resources/text/settings.png")#Image Load
quittext = pygame.image.load("resources/text/quit.png")#Image Load
helptext = pygame.image.load("resources/text/help.png")#Image Load
mainmtext = pygame.image.load("resources/text/mainm.png")#Image Load
levelstext = pygame.image.load("resources/text/levels.png")#Image Load
restarttext = pygame.image.load("resources/text/restart.png")#Image Load
backtext = pygame.image.load("resources/text/back.png")#Image Load
quizzes = pygame.image.load("resources/text/quizzes.png")#Image Load
welldone = pygame.image.load("resources/text/welldone.png") #Image Load
greatjob = pygame.image.load("resources/text/great.png")#Image Load
congrats = pygame.image.load("resources/text/congrats2.png")#Image Load
congratulations = pygame.image.load("resources/text/congrats.png")#Image Load

#Planets
sun = pygame.image.load("resources/planets/sun.jpg")#Image Load
moon = pygame.image.load("resources/planets/moon.jpg")#Image Load
earth = pygame.image.load("resources/planets/earth.jpg")#Image Load
mars = pygame.image.load("resources/planets/mars.jpg")#Image Load
venus = pygame.image.load("resources/planets/venus.jpg")#Image Load
uranus = pygame.image.load("resources/planets/uranus.jpg")#Image Load
neptune = pygame.image.load("resources/planets/neptune.jpg")#Image Load
pluto = pygame.image.load("resources/planets/pluto.jpg")#Image Load
jupiter = pygame.image.load("resources/planets/jupiter.jpg")#Image Load
saturn = pygame.image.load("resources/planets/saturn.jpg")#Image Load
mercury = pygame.image.load("resources/planets/mercury.jpg")#Image Load

###########################Questions Assests######################
#The game Uses images for EVERYTHING including the questions becuase I found it easer than text in this language#
#Some Quizzes are still coming so they are commented#
#Earth
earth_question_1 = pygame.image.load("resources/questions/earth/question1.png")#Image Load
earth_question_2 = pygame.image.load("resources/questions/earth/question2.png")#Image Load
earth_question_3 = pygame.image.load("resources/questions/earth/question3.png")#Image Load
earth_question_4 = pygame.image.load("resources/questions/earth/question4.png")#Image Load
earth_question_5 = pygame.image.load("resources/questions/earth/question5.png")#Image Load
earth_question_6 = pygame.image.load("resources/questions/earth/question6.png")#Image Load
earth_question_7 = pygame.image.load("resources/questions/earth/question7.png")#Image Load
earth_question_8 = pygame.image.load("resources/questions/earth/question8.png")#Image Load
earth_question_9 = pygame.image.load("resources/questions/earth/question9.png")#Image Load
earth_question_10 = pygame.image.load("resources/questions/earth/question10.png")#Image Load
#Mars
mars_question_1 = pygame.image.load("resources/questions/mars/question1.png")#Image Load
mars_question_2 = pygame.image.load("resources/questions/mars/question2.png")#Image Load
mars_question_3 = pygame.image.load("resources/questions/mars/question3.png")#Image Load
mars_question_4 = pygame.image.load("resources/questions/mars/question4.png")#Image Load
mars_question_5 = pygame.image.load("resources/questions/mars/question5.png")#Image Load
#Moon
moon_question_1 = pygame.image.load("resources/questions/moon/question1.png")#Image Load
###Sun
sun_question_1 = pygame.image.load("resources/questions/sun/question1.png")#Image Load
sun_question_2 = pygame.image.load("resources/questions/sun/question2.png")#Image Load
sun_question_3 = pygame.image.load("resources/questions/sun/question3.png")#Image Load
sun_question_4 = pygame.image.load("resources/questions/sun/question4.png")#Image Load
sun_question_5 = pygame.image.load("resources/questions/sun/question5.png")#Image Load
sun_question_6 = pygame.image.load("resources/questions/sun/question6.png")#Image Load
sun_question_7 = pygame.image.load("resources/questions/sun/question7.png")#Image Load
sun_question_8 = pygame.image.load("resources/questions/sun/question8.png")#Image Load
sun_question_9 = pygame.image.load("resources/questions/sun/question9.png")#Image Load
sun_question_10 = pygame.image.load("resources/questions/sun/question10.png")#Image Load
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
#Jupiter
jupiter_question_1 = pygame.image.load("resources/questions/jupiter/question1.png")#Image Load
jupiter_question_2 = pygame.image.load("resources/questions/jupiter/question2.png")#Image Load
jupiter_question_3 = pygame.image.load("resources/questions/jupiter/question3.png")#Image Load
jupiter_question_4 = pygame.image.load("resources/questions/jupiter/question4.png")#Image Load
jupiter_question_5 = pygame.image.load("resources/questions/jupiter/question5.png")#Image Load
jupiter_question_6 = pygame.image.load("resources/questions/jupiter/question6.png")#Image Load
jupiter_question_7 = pygame.image.load("resources/questions/jupiter/question7.png")#Image Load
jupiter_question_8 = pygame.image.load("resources/questions/jupiter/question8.png")#Image Load
jupiter_question_9 = pygame.image.load("resources/questions/jupiter/question9.png")#Image Load
jupiter_question_10 = pygame.image.load("resources/questions/jupiter/question10.png")#Image Load
#Venus
venus_question_1 = pygame.image.load("resources/questions/venus/question1.png")#Image Load
venus_question_2 = pygame.image.load("resources/questions/venus/question2.png")#Image Load
venus_question_3 = pygame.image.load("resources/questions/venus/question3.png")#Image Load
venus_question_4 = pygame.image.load("resources/questions/venus/question4.png")#Image Load
venus_question_5 = pygame.image.load("resources/questions/venus/question5.png")#Image Load
venus_question_6 = pygame.image.load("resources/questions/venus/question6.png")#Image Load
venus_question_7 = pygame.image.load("resources/questions/venus/question7.png")#Image Load
venus_question_8 = pygame.image.load("resources/questions/venus/question8.png")#Image Load
venus_question_9 = pygame.image.load("resources/questions/venus/question9.png")#Image Load
venus_question_10 = pygame.image.load("resources/questions/venus/question10.png")#Image Load
#Uranus
uranus_question_1 = pygame.image.load("resources/questions/uranus/question1.png")#Image Load
uranus_question_2 = pygame.image.load("resources/questions/uranus/question2.png")#Image Load
uranus_question_3 = pygame.image.load("resources/questions/uranus/question3.png")#Image Load
uranus_question_4 = pygame.image.load("resources/questions/uranus/question4.png")#Image Load
uranus_question_5 = pygame.image.load("resources/questions/uranus/question5.png")#Image Load
uranus_question_6 = pygame.image.load("resources/questions/uranus/question6.png")#Image Load
uranus_question_7 = pygame.image.load("resources/questions/uranus/question7.png")#Image Load
uranus_question_8 = pygame.image.load("resources/questions/uranus/question8.png")#Image Load
uranus_question_9 = pygame.image.load("resources/questions/uranus/question9.png")#Image Load
uranus_question_10 = pygame.image.load("resources/questions/uranus/question10.png")#Image Load
###Mercury
##mercury_question_1 = pygame.image.load("resources/questions/mercury/question1.png")#Image Load
##mercury_question_2 = pygame.image.load("resources/questions/mercury/question2.png")#Image Load
##mercury_question_3 = pygame.image.load("resources/questions/mercury/question3.png")#Image Load
##mercury_question_4 = pygame.image.load("resources/questions/mercury/question4.png")#Image Load
##mercury_question_5 = pygame.image.load("resources/questions/mercury/question5.png")#Image Load
##mercury_question_6 = pygame.image.load("resources/questions/mercury/question6.png")#Image Load
##mercury_question_7 = pygame.image.load("resources/questions/mercury/question7.png")#Image Load
##mercury_question_8 = pygame.image.load("resources/questions/mercury/question8.png")#Image Load
##mercury_question_9 = pygame.image.load("resources/questions/mercury/question9.png")#Image Load
##mercury_question_10 = pygame.image.load("resources/questions/mercury/question10.png")#Image Load
###Neptune
##neptune_question_1 = pygame.image.load("resources/questions/neptune/question1.png")#Image Load
##neptune_question_2 = pygame.image.load("resources/questions/neptune/question2.png")#Image Load
##neptune_question_3 = pygame.image.load("resources/questions/neptune/question3.png")#Image Load
##neptune_question_4 = pygame.image.load("resources/questions/neptune/question4.png")#Image Load
##neptune_question_5 = pygame.image.load("resources/questions/neptune/question5.png")#Image Load
##neptune_question_6 = pygame.image.load("resources/questions/neptune/question6.png")#Image Load
##neptune_question_7 = pygame.image.load("resources/questions/neptune/question7.png")#Image Load
##neptune_question_8 = pygame.image.load("resources/questions/neptune/question8.png")#Image Load
##neptune_question_9 = pygame.image.load("resources/questions/neptune/question9.png")#Image Load
##neptune_question_10 = pygame.image.load("resources/questions/neptune/question10.png")#Image Load

#Answers
true = pygame.image.load("resources/answers/earth/true.png")#Image Load
false = pygame.image.load("resources/answers/earth/false.png")#Image Load
yes = pygame.image.load("resources/answers/earth/yes.png")#Image Load
no = pygame.image.load("resources/answers/earth/no.png")#Image Load
windows = pygame.image.load("resources/answers/earth/windows.png")#Image Load
apple = pygame.image.load("resources/answers/earth/apple.png")#Image Load
linux = pygame.image.load("resources/answers/earth/linux.png")#Image Load
windowsos = pygame.image.load("resources/answers/earth/windowsos.jpg")#Image Load
appleos = pygame.image.load("resources/answers/earth/appleos.jpg")#Image Load
spark = pygame.image.load("resources/answers/earth/spark.png")#Image Load
vodafone = pygame.image.load("resources/answers/earth/vodafone.png")#Image Load
degrees2 = pygame.image.load("resources/answers/earth/2degrees.png")#Image Load
trustpower = pygame.image.load("resources/answers/earth/trustpower.png")#Image Load
slingshot = pygame.image.load("resources/answers/earth/slingshot.png")#Image Load
flip = pygame.image.load("resources/answers/earth/flip.png")#Image Load
nasa = pygame.image.load("resources/answers/earth/nasa.png")#Image Load
spacex = pygame.image.load("resources/answers/earth/spacex.png")#Image Load
apollox = pygame.image.load("resources/answers/earth/apollox.png")#Image Load
vr = pygame.image.load("resources/answers/earth/vr.png")#Image Load
vr1 = pygame.image.load("resources/answers/earth/vr1.png")#Image Load
vr2 = pygame.image.load("resources/answers/earth/vr2.jpg")#Image Load

planetsun = pygame.image.load("resources/answers/sun/planet.png")#Image Load
star = pygame.image.load("resources/answers/sun/star.png")#Image Load
mean42 = pygame.image.load("resources/answers/sun/42.png")#Image Load
infinity = pygame.image.load("resources/answers/sun/infinity.png")#Image Load
apollo11 = pygame.image.load("resources/answers/sun/apollo11.jpg")#Image Load
atlantis = pygame.image.load("resources/answers/sun/atlantis.jpg")#Image Load
columbia = pygame.image.load("resources/answers/sun/columbia.jpg")#Image Load
aresv = pygame.image.load("resources/answers/sun/aresv.png")#Image Load
saturnv = pygame.image.load("resources/answers/sun/saturnv.png")#Image Load
elseimg = pygame.image.load("resources/answers/sun/else.png")#Image Load
james = pygame.image.load("resources/answers/sun/james.png")#Image Load
collins = pygame.image.load("resources/answers/sun/collins.jpg")#Image Load
chris = pygame.image.load("resources/answers/sun/chris.png")#Image Load
armstrong = pygame.image.load("resources/answers/sun/neilarmstrong.png")#Image Load
num1 = pygame.image.load("resources/answers/sun/1.jpg")#Image Load
num2 = pygame.image.load("resources/answers/sun/2.jpg")#Image Load
num3 = pygame.image.load("resources/answers/sun/3.jpg")#Image Load
num4 = pygame.image.load("resources/answers/sun/4.jpg")#Image Load
num5 = pygame.image.load("resources/answers/sun/5.jpg")#Image Load
jupitertxt = pygame.image.load("resources/answers/sun/jupitertxt.jpg")#Image Load
venustxt = pygame.image.load("resources/answers/sun/venustxt.jpg")#Image Load
marstxt = pygame.image.load("resources/answers/sun/marstxt.jpg")#Image Load
earthtxt = pygame.image.load("resources/answers/sun/earthtxt.jpg")#Image Load
mercurytxt = pygame.image.load("resources/answers/sun/mercurytxt.jpg")#Image Load

ball = pygame.image.load("resources/answers/venus/ball.jpg")#Image Load 
brain = pygame.image.load("resources/answers/venus/brain.jpg")#Image Load 
bull = pygame.image.load("resources/answers/venus/bull.jpg") #Image Load
cheetah = pygame.image.load("resources/answers/venus/cheetahS.jpg") #Image Load
email = pygame.image.load("resources/answers/venus/email.png") #Image Load
griffin = pygame.image.load("resources/answers/venus/griffin.jpg") #Image Load
hammer = pygame.image.load("resources/answers/venus/hammer.png") #Image Load
lightning = pygame.image.load("resources/answers/venus/lightning.jpg")#Image Load 
solar = pygame.image.load("resources/answers/venus/solarsystem.jpg") #Image Load
spin = pygame.image.load("resources/answers/venus/spin.png") #Image Load
#WYR Answers
L1 = pygame.image.load("resources/answers/moon/L1.png") #Image Load
R1 = pygame.image.load("resources/answers/moon/R1.png") #Image Load
L2 = pygame.image.load("resources/answers/moon/L2.png") #Image Load
R2 = pygame.image.load("resources/answers/moon/R2.png") #Image Load
L3 = pygame.image.load("resources/answers/moon/L3.png") #Image Load
R3 = pygame.image.load("resources/answers/moon/R3.png") #Image Load
L4 = pygame.image.load("resources/answers/moon/L4.png") #Image Load
R4 = pygame.image.load("resources/answers/moon/R4.png") #Image Load
L5 = pygame.image.load("resources/answers/moon/L5.png") #Image Load
R5 = pygame.image.load("resources/answers/moon/R5.png") #Image Load
L6 = pygame.image.load("resources/answers/moon/L6.png") #Image Load
R6 = pygame.image.load("resources/answers/moon/R6.png") #Image Load
L7 = pygame.image.load("resources/answers/moon/L7.png") #Image Load
R7 = pygame.image.load("resources/answers/moon/R7.png") #Image Load
L8 = pygame.image.load("resources/answers/moon/L8.png") #Image Load
R8 = pygame.image.load("resources/answers/moon/R8.png") #Image Load
L9 = pygame.image.load("resources/answers/moon/L9.png") #Image Load
R9 = pygame.image.load("resources/answers/moon/R9.png") #Image Load
L10 = pygame.image.load("resources/answers/moon/L10.png") #Image Load
R10 = pygame.image.load("resources/answers/moon/R10.png") #Image Load
#Star Wars (Uranus Quiz) Answers
anewhope = pygame.image.load("resources/answers/uranus/anewhope.jpg")#Image Load
returnofthejedi = pygame.image.load("resources/answers/uranus/returnofthejedi.jpg")#Image Load
thelastjedi = pygame.image.load("resources/answers/uranus/thelastjedi.jpg")#Image Load
bb8 = pygame.image.load("resources/answers/uranus/bb8.png")#Image Load
r2d2 = pygame.image.load("resources/answers/uranus/r2d2.png")#Image Load
c3po = pygame.image.load("resources/answers/uranus/c3po.jpg")#Image Load
bud = pygame.image.load("resources/answers/uranus/bud.png")#Image Load
finn = pygame.image.load("resources/answers/uranus/finn.png")#Image Load
john = pygame.image.load("resources/answers/uranus/john.png")#Image Load
kyber = pygame.image.load("resources/answers/uranus/kyber.png")#Image Load
kybar = pygame.image.load("resources/answers/uranus/kybar.png")#Image Load
kybur = pygame.image.load("resources/answers/uranus/kybur.png")#Image Load
kyba = pygame.image.load("resources/answers/uranus/kyba.png")#Image Load
porg = pygame.image.load("resources/answers/uranus/porg.png")#Image Load
poru = pygame.image.load("resources/answers/uranus/poru.png")#Image Load
nova = pygame.image.load("resources/answers/uranus/nova.png")#Image Load
porgimg = pygame.image.load("resources/answers/uranus/porgimg.png")#Image Load
falcon = pygame.image.load("resources/answers/uranus/falcon.png")#Image Load
enterprise = pygame.image.load("resources/answers/uranus/enterprise.jpg")#Image Load
xwing = pygame.image.load("resources/answers/uranus/xwing.png")#Image Load
leia = pygame.image.load("resources/answers/uranus/leia.jpg")#Image Load
luke = pygame.image.load("resources/answers/uranus/luke.jpg")#Image Load
yoda = pygame.image.load("resources/answers/uranus/yoda.jpg")#Image Load
anakin = pygame.image.load("resources/answers/uranus/anakin.jpg")#Image Load
yodu = pygame.image.load("resources/answers/uranus/yodu.png")#Image Load
yaddle = pygame.image.load("resources/answers/uranus/yaddle.png")#Image Load
yodan = pygame.image.load("resources/answers/uranus/yodan.png")#Image Load
yanna = pygame.image.load("resources/answers/uranus/yanna.png")#Image Load
kyberimg = pygame.image.load("resources/answers/uranus/kyberimg.jpg")#Image Load
fn2187 = pygame.image.load("resources/answers/uranus/fn2187.jpg")#Image Load
jedichurch = pygame.image.load("resources/answers/uranus/jedi.jpg")#Image Load

africa = pygame.image.load("resources/answers/jupiter/africa.jpg")#Image Load
america = pygame.image.load("resources/answers/jupiter/america.png")#Image Load
asia = pygame.image.load("resources/answers/jupiter/asia.png")#Image Load
argon = pygame.image.load("resources/answers/jupiter/argon.jpg")#Image Load
silver = pygame.image.load("resources/answers/jupiter/silver.png")#Image Load
gold = pygame.image.load("resources/answers/jupiter/gold.png")#Image Load
noway = pygame.image.load("resources/answers/jupiter/noway.png")#Image Load
#noto = pygame.image.load("resources/answers/jupiter/not.jpg")#Image Load
nope = pygame.image.load("resources/answers/jupiter/nope.jpg")#Image Load
albert = pygame.image.load("resources/answers/jupiter/albert.jpg")#Image Load
thomas = pygame.image.load("resources/answers/jupiter/thomas.jpg")#Image Load
ben = pygame.image.load("resources/answers/jupiter/ben.jpg") #Image Load
dodec1 = pygame.image.load("resources/answers/jupiter/shape1.png")#Image Load
dodec2 = pygame.image.load("resources/answers/jupiter/dodec.jpg")#Image Load
dodec3 = pygame.image.load("resources/answers/jupiter/dodec.png")#Image Load
george = pygame.image.load("resources/answers/jupiter/george.jpg")#Image Load
jfk = pygame.image.load("resources/answers/jupiter/jfk.jpg")#Image Load
hillary = pygame.image.load("resources/answers/jupiter/hillary.jpg")#Image Load
hdmi = pygame.image.load("resources/answers/jupiter/hdmi.png")#Image Load
sata = pygame.image.load("resources/answers/jupiter/sata.png")#Image Load
ide = pygame.image.load("resources/answers/jupiter/ide.png")#Image Load
cricket = pygame.image.load("resources/answers/jupiter/cricket.png")#Image Load
basketball = pygame.image.load("resources/answers/jupiter/basketball.png")#Image Load
soccer = pygame.image.load("resources/answers/jupiter/soccer.png")#Image Load
canada = pygame.image.load("resources/answers/jupiter/turkeyflag.png")#Image Load
peru = pygame.image.load("resources/answers/jupiter/peruflag.png")#Image Load
turkey = pygame.image.load("resources/answers/jupiter/turkeyflag.png")#Image Load
#Help Menu Assets
help_banner = pygame.image.load("resources/images/helpbanner.png")#Image Load
help_message = pygame.image.load("resources/images/help.png")#Image Load
#Player age Assets 
age_up = pygame.image.load("resources/images/up.png")#Image Load
age_down = pygame.image.load("resources/images/down.png")#Image Load
age_banner = pygame.image.load("resources/images/age_banner.png")#Image Load
ok = pygame.image.load("resources/images/ok.png")#Image Load
anyway = pygame.image.load("resources/images/anyway.png")#Image Load
player_age = 15 #Start age = 15

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
            pygame.draw.rect(gameDisplay, white, [display_width/2 - 60, display_height/2 + 140, 160, 60])#Draws a rectangle
            gameDisplay.blit(ok, (display_width/2 - 60, display_height/2 + 140))#Image Blit
            ok_button(display_width/2 - 60, display_height/2 + 140, 160, 60, grey, action = 'quit')#Button 
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
                main_menu() #Runs the main_menu() Function

    
                 
#Main Menu Function
def main_menu(): #Runs the main_menu() function
    menu = True #Menu is true
    while menu: #While menu Is True
         for event in pygame.event.get(): #Get Events
              if event.type == pygame.QUIT: #If quit button clicked #Quits
                   pygame.quit() #Quits
                   quit() #Quits
              gameDisplay.blit(bg, (0,0)) #Background 
              gameDisplay.blit(menubanner, (0,0))#Image Blit
              #Play Button
              pygame.draw.rect(gameDisplay, white, [300,200,220,55])#Draws a rectangle
              gameDisplay.blit(playtext, (340,200))#Image Blit
              main_menu_buttons(280,195,260,65, grey, action = 'play')#Button 

              #Settings Button
              pygame.draw.rect(gameDisplay, white, [300,280,220,55])#Draws a rectangle
              gameDisplay.blit(settingstext, (300,280))#Image Blit
              main_menu_buttons(280,270,260,75, grey, action = 'settings')#Button 


              #HighScore Button
              pygame.draw.rect(gameDisplay, white, [300,360,220,55])#Draws a rectangle
              gameDisplay.blit(scoretext, (300,365))#Image Blit
              main_menu_buttons(280,350,260,75, grey, action = 'highscore')#Button 

              #Quit Button
              pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
              gameDisplay.blit(quittext, (340,440))#Image Blit
              main_menu_buttons(280,430,260,75, grey, action = 'quit')#Button 

              #Help Button
              pygame.draw.rect(gameDisplay,white, [300, 520, 220, 55])#Draws a rectangle
              gameDisplay.blit(helptext, (340,530))#Image Blit
              main_menu_buttons(280, 510, 260, 75, grey, action = 'help')#Button 
              pygame.display.update() #Updates the Display


#Menu Buttons
def main_menu_buttons(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos() #Gets Cursor Position
     click = pygame.mouse.get_pressed() #Checks for mouse click
     if x + width > cur[0] > x and y + height > cur[1] > y:#Checks if mouse position is over the button
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))#Draws a rectangle
         gameDisplay.blit(quittext, (340,440))#Image Blit
         gameDisplay.blit(helptext, (340,530))#Image Blit
         gameDisplay.blit(scoretext, (300,365))#Image Blit
         gameDisplay.blit(settingstext, (300,280))#Image Blit
         gameDisplay.blit(playtext, (340,200))#Image Blit
         if click[0] == 1 and action != None: #If Button is clicked and action is not equal to nothing
             if action == "quit":
                 clickaudio.play() #Plays the Click audio
                 time.sleep(0.5) #Pauses the game for 0.5 seconds
                 pygame.quit() #Quits
                 quit() #Quits
             if action == "help":
                 clickaudio.play() #Plays the Click audio
                 time.sleep(0.5) #Pauses the game for 0.5 seconds
                 help_menu()  
             elif action == "play":
                 clickaudio.play() #Plays the Click audio
                 time.sleep(0.5) #Pauses the game for 0.5 seconds
                 game_loop()
             elif action == "settings":
                 clickaudio.play() #Plays the Click audio
                 time.sleep(0.5) #Pauses the game for 0.5 seconds
                 settings()
             elif action == "highscore":
                 clickaudio.play() #Plays the Click audio
                 time.sleep(0.5) #Pauses the game for 0.5 seconds  
                 high_scores()

def back_button(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos() #Gets Cursor Position
     click = pygame.mouse.get_pressed() #Checks for mouse click
     if x + width > cur[0] > x and y + height > cur[1] > y:#Checks if mouse position is over the button
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))#Draws a rectangle
         gameDisplay.blit(backtext, (340,440))#Image Blit
         if click[0] == 1 and action != None: #If Button is clicked and action is not equal to nothing
             clickaudio.play() #Plays the Click audio
             time.sleep(0.5) #Pauses the game for 0.5 seconds 
             if action == "back":  
                 main_menu() #Runs the main_menu() Function
             if action == "backtolevels":
                 game_loop()
                 
def back_button1(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos() #Gets Cursor Position
     click = pygame.mouse.get_pressed() #Checks for mouse click
     if x + width > cur[0] > x and y + height > cur[1] > y:#Checks if mouse position is over the button
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))#Draws a rectangle
         gameDisplay.blit(backtext, (340,440))#Image Blit
         if click[0] == 1 and action != None: #If Button is clicked and action is not equal to nothing
             if action == "back":
                 clickaudio.play() #Plays the Click audio
                 time.sleep(0.5) #Pauses the game for 0.5 seconds
                 main_menu() #Runs the main_menu() Function

def settings_buttons(x,y,width,height,active_color, action = None):
     cur = pygame.mouse.get_pos() #Gets Cursor Position
     click = pygame.mouse.get_pressed() #Checks for mouse click
     if x + width > cur[0] > x and y + height > cur[1] > y:#Checks if mouse position is over the button
         pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))#Draws a rectangle
         gameDisplay.blit(fpsimage1, (420,210))#Image Blit
         gameDisplay.blit(on, (420,310))#Image Blit
         gameDisplay.blit(off, (500,310))#Image Blit
         gameDisplay.blit(edit, (480,370))#Image Blit
         gameDisplay.blit(sound4, (660,260))#Image Blit
         gameDisplay.blit(fpsimage2, (500,210))#Image Blit
         gameDisplay.blit(fpsimage3, (580,210))#Image Blit
         gameDisplay.blit(sound1, (420,260))#Image Blit
         gameDisplay.blit(sound2, (500,260))#Image Blit
         gameDisplay.blit(sound3, (580,260))#Image Blit
         if click[0] == 1 and action != None: #If Button is clicked and action is not equal to nothing
             clickaudio.play() #Plays the Click audio
             time.sleep(0.5) #Pauses the game for 0.5 seconds
             if action == "30_fps":
                 print("FPS = 30")
                 with open('resources/files/fps.txt', 'w') as t:
                     t.write('30')
             if action == "on":
                 print("Tutorial On")
                 with open('resources/files/tutorial.txt', 'w') as t:
                     t.write('ON')
             if action == "off":
                 print("Tutorial Off")
                 with open('resources/files/tutorial.txt', 'w') as t:
                     t.write('OFF')
             if action == "60_fps":
                 print("FPS = 60")
                 with open('resources/files/fps.txt', 'w') as t:
                     t.write('60')           
             if action == "120_fps":
                 print("FPS = 120")
                 with open('resources/files/fps.txt', 'w') as t:
                     t.write('120')
             if action == "sound_25":
                 print("Sound = 25%")
                 with open('resources/files/sound.txt', 'w') as t:
                     t.write('25')
             if action == "sound_50":
                 print("Sound = 50%")
                 with open('resources/files/sound.txt', 'w') as t:
                     t.write('50')
             if action == "sound_75":
                 print("Sound = 75%")
                 with open('resources/files/sound.txt', 'w') as t:
                     t.write('75')                
             if action == "sound_100":
                 print("Sound = 100%")
                 with open('resources/files/sound.txt', 'w') as t:
                     t.write('100')      
             if action == "edit_controls":
                 print("Coming Soon!!! Current controls are WASD or LEFT, RIGHT, UP and DOWN")      
def text_objects(text, color): #This Function Prints Text to the Screen
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
    pygame.display.update() #Updates the Display    
def message_to_screen_earth(msg,color): #This Function Prints Text to the Screen
    textSurf, textRect = text_objects(msg,color)
    textRect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)#Image Blit
    pygame.display.update() #Updates the Display
def message_to_screen_high_score(msg,color): #This Function Prints Text to the Screen
    textSurf, textRect = text_objects(msg,color)
    textRect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)#Image Blit
    pygame.display.update() #Updates the Display  
def settings():
    print("The Settings Function has run")
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked
                gameExit = True #Escaps this loop
        gameDisplay.blit(bg, (0,0)) #Background
        gameDisplay.blit(settingsbanner, (0,0))#Image Blit
        #Back Button
        pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
        gameDisplay.blit(backtext, (340,440))#Image Blit
        back_button(280,430,260,75, grey, action = 'back') #Button      
        gameDisplay.blit(fpsimg, (250,200))#Image Blit
        gameDisplay.blit(sound, (250,250))#Image Blit
        gameDisplay.blit(tutorial, (250,300))#Image Blit
        gameDisplay.blit(controls, (250,350))#Image Blit
        with open('resources/files/fps.txt', 'r') as f: #Opens this file for reading
            fpsread = int(f.read(3))
            print("FPS = ", fps)
        with open('resources/files/tutorial.txt', 'r') as f: #Opens this file for reading
            tutorialread = str(f.read(3))
            print("Tutorial = ", tutorial)
        with open('resources/files/sound.txt', 'r') as f: #Opens this file for reading
            soundread = int(f.read(3))
            print("Sound = ", sound,"%")
        if fpsread == 30:
            pygame.draw.rect(gameDisplay, blue, (420,220,75,40))#Draws a rectangle
        if fpsread == 60:
            pygame.draw.rect(gameDisplay, blue, (500,220,75,40))#Draws a rectangle
        if fpsread == 120:
            pygame.draw.rect(gameDisplay, blue, (580,220,95,40))#Draws a rectangle
        if soundread == 25:
            pygame.draw.rect(gameDisplay, blue, (420,270,75,40))#Draws a rectangle
        if soundread == 50:
            pygame.draw.rect(gameDisplay, blue, (500,270,75,40))#Draws a rectangle 
        if soundread == 75:
            pygame.draw.rect(gameDisplay, blue, (580,270,75,40))#Draws a rectangle
        if soundread == 100:
            pygame.draw.rect(gameDisplay, blue, (660,270,95,40))#Draws a rectangle
        if tutorialread == 'ON':
            pygame.draw.rect(gameDisplay, blue, (420,320,75,40))#Draws a rectangle
        if tutorialread == 'OFF':
            pygame.draw.rect(gameDisplay, blue, (500,320,95,40))#Draws a rectangle 
        #30fps :)
        gameDisplay.blit(fpsimage1, (420,210))#Image Blit
        settings_buttons(420,220,75,40, grey, action = '30_fps')#Button     
        #60fps :)
        gameDisplay.blit(fpsimage2, (500,210))#Image Blit
        settings_buttons(500,220,75,40, grey, action = '60_fps')#Button        
        #120fps :)
        gameDisplay.blit(fpsimage3, (580,210))#Image Blit
        settings_buttons(580,220,95,40, grey, action = '120_fps')#Button       
        #25%
        gameDisplay.blit(sound1, (420,260))#Image Blit
        settings_buttons(420,270,75,40, grey, action = 'sound_25')#Button       
        #50%
        gameDisplay.blit(sound2, (500,260))#Image Blit
        settings_buttons(500,270,75,40, grey, action = 'sound_50')#Button    
        #75%
        gameDisplay.blit(sound3, (580,260))#Image Blit
        settings_buttons(580,270,75,40, grey, action = 'sound_75')#Button      
        #100%
        gameDisplay.blit(sound4, (660,260))#Image Blit
        settings_buttons(660,270,95,40, grey, action = 'sound_100')#Button    
        #On
        gameDisplay.blit(on, (420,310))#Image Blit
        settings_buttons(420,320,75,40, grey, action = 'on')#Button   
        #OFF
        gameDisplay.blit(off, (500,310))#Image Blit
        settings_buttons(500,320,95,40, grey, action = 'off')#Button  
        #Controls
        gameDisplay.blit(edit, (480,370))#Image Blit
        settings_buttons(480,370,40,40, grey, action = 'edit_controls')#Button   
        #Back Button
        gameDisplay.blit(backtext, (340,440))#Image Blit
        back_button(280,430,260,75, grey, action = 'back')#Button
        pygame.display.update() #Updates the Display


def high_scores(): #HIGH SCORES
    print("The High Score Function has run") #FOR TESTING PURPOSES
    gameExit = False #Game Exit is = false
    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameexit is true and while loop will stop running
                gameExit = True
        gameDisplay.blit(bg, (0,0)) #Background
        gameDisplay.blit(scorebanner, (0,0))#Image Blit
        gameDisplay.blit(quizzes, (257,209))#Image Blit
        with open("resources/scores/earthscore.txt") as f: 
            for line in f:
                message_to_screen_earth1(line, white)#Actual text             
        with open("resources/scores/marsscore.txt") as f:
            for line in f:
                message_to_screen_mars1(line, white)#Actual text           
        with open("resources/scores/moonscore.txt") as f:
            for line in f:
                message_to_screen_moon1(line, white)#Actual text      
        with open("resources/scores/saturnscore.txt") as f:
            for line in f:
                message_to_screen_saturn1(line, white)#Actual text          
        with open("resources/scores/venusscore.txt") as f:
            for line in f:
                message_to_screen_venus1(line, white)#Actual text   
        with open("resources/scores/mercuryscore.txt") as f:
            for line in f:
                message_to_screen_mercury1(line, "/10", white)#Actual text               
        with open("resources/scores/plutoscore.txt") as f:
            for line in f:
                message_to_screen_pluto1(line, white)#Actual text          
        with open("resources/scores/neptunescore.txt") as f:
            for line in f:
                message_to_screen_neptune1(line, white)#Actual text          
        with open("resources/scores/jupiterscore.txt") as f:
            for line in f:
                message_to_screen_jupiter1(line, white)#Actual text        
        with open("resources/scores/uranusscore.txt") as f:
            for line in f:
                message_to_screen_uranus1(line, white)#Actual text        
        with open("resources/scores/sunscore.txt") as f:
            for line in f:
                message_to_screen_sun1(line, white)#Actual text                
        #Back Button
        pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
        gameDisplay.blit(backtext, (340,440))#Image Blit
        back_button1(280,430,260,75, grey, action = 'back')#Button
        pygame.display.update() #Updates the Display

def help_menu():
    print("The High Score Function has run")
    gameExit = False #Game Exit is = false

    while not gameExit: #While Game Exit is not = true run everything below
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameexit is true and while loop will stop running
                gameExit = True

        gameDisplay.blit(bg, (0,0)) #Background
        gameDisplay.blit(help_banner, (50,0))#Image Blit
        gameDisplay.blit(help_message, (0,0))#Image Blit
        gameDisplay.blit(help_banner, (50,0))#Image Blit
                     
        #Back Button
        pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
        gameDisplay.blit(backtext, (340,440))#Image Blit
        back_button1(280,430,260,75, grey, action = 'back')#Button
        pygame.display.update() #Updates the Display

def message_to_screen_earth1(msg, color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (210)
    gameDisplay.blit(textSurf, textRect)#Image Blit
def message_to_screen_mars1(msg,color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (230)
    gameDisplay.blit(textSurf, textRect)#Image Blit
def message_to_screen_moon1(msg,color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (250)
    gameDisplay.blit(textSurf, textRect)#Image Blit
def message_to_screen_saturn1(msg,color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (270)
    gameDisplay.blit(textSurf, textRect)#Image Blit
def message_to_screen_venus1(msg,color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (290)
    gameDisplay.blit(textSurf, textRect)#Image Blit
def message_to_screen_mercury1(msg, msg1, color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (310)
    gameDisplay.blit(textSurf, textRect)#Image Blit
def message_to_screen_pluto1(msg,color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (330)
    gameDisplay.blit(textSurf, textRect)#Image Blit
def message_to_screen_neptune1(msg,color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (350)
    gameDisplay.blit(textSurf, textRect)#Image Blit
def message_to_screen_jupiter1(msg,color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (370)
    gameDisplay.blit(textSurf, textRect)#Image Blit
def message_to_screen_uranus1(msg,color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (390)
    gameDisplay.blit(textSurf, textRect)#Image Blit
def message_to_screen_sun1(msg,color):#This Function Prints Text to the screen
    textSurf, textRect = text_objects(msg,color)
    textRect = (550), (410)
    gameDisplay.blit(textSurf, textRect)#Image Blit
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
    while not gameExit: #While Game Exit is not equal to true run everything below
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameexit is true and while loop will stop running
                gameExit = True
        gameDisplay.blit(bg, (0,0)) #Background 
        gameDisplay.blit(sun, (sun_x,sun_y)) #Image Blit
        gameDisplay.blit(mars, (mars_x,mars_y))#Image Blit
        gameDisplay.blit(saturn, (saturn_x,saturn_y))#Image Blit
        gameDisplay.blit(venus, (venus_x,venus_y))#Image Blit
        gameDisplay.blit(uranus, (uranus_x,uranus_y))#Image Blit
        gameDisplay.blit(earth, (earth_x,earth_y))#Image Blit
        gameDisplay.blit(jupiter, (jupiter_x,jupiter_y))#Image Blit
        gameDisplay.blit(mercury, (mercury_x,mercury_y))#Image Blit
        gameDisplay.blit(neptune, (neptune_x,neptune_y))#Image Blit
        gameDisplay.blit(moon, (moon_x,moon_y))#Image Blit
        gameDisplay.blit(pluto, (pluto_x,pluto_y))#Image Blit
        #Player Movement
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked
                gameExit = True #Quit
            if event.type == pygame.KEYDOWN: #If Event key press (Same applies for all other movement)
                if event.key == pygame.K_a: #If the key is a
                    x_change = -player_speed #Go Left
                    y_change = 0 #Y is constant other wise you would move diagonally
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
        if player_x >= display_width: #If the ufo goes off the screen he is moved to the opposite side
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
            gameDisplay.blit(sun_text, (65,75))#Image Blit
            planet_buttons(60,40,130,121, None, action = 'sun') #Button    
        #Mars Crossover
        if player_x >= mars_x and player_x <= mars_x + 120 and player_y >= mars_y and player_y <= mars_y + 118:
            gameDisplay.blit(mars_text, (255,65))#Image Blit
            planet_buttons(250,20,120,118, None, action = 'mars')#Button
        #Saturn Crossover
        if player_x >= saturn_x and player_x <= saturn_x + 200 and player_y >= saturn_y and player_y <= saturn_y + 136:
            gameDisplay.blit(saturn_text, (650,120))#Image Blit
            planet_buttons(560,20,200,136, None, action = 'saturn')#Button
        #Venus Crossover
        if player_x >= venus_x and player_x <= venus_x + 120 and player_y >= venus_y and player_y <= venus_y + 118:
            gameDisplay.blit(venus_text, (645,235))#Image Blit
            planet_buttons(640,200,120,128, None, action = 'venus')  #Button   
        #Uranus Crossover
        if player_x >= uranus_x and player_x <= uranus_x + 120 and player_y >= uranus_y and player_y <= uranus_y + 118:
            gameDisplay.blit(uranus_text, (10,170))#Image Blit
            planet_buttons(20,200,120,128, None, action = 'uranus')#Button
        #Earth Crossover
        if player_x >= earth_x and player_x <= earth_x + 120 and player_y >= earth_y and player_y <= earth_y + 128:
            gameDisplay.blit(earth_text, (335,200))#Image Blit
            planet_buttons(display_width/2.4,display_height/2.5,120,128, None, action = 'earth') #Button          
        #Jupiter Crossover
        if player_x >= jupiter_x and player_x <= jupiter_x + 120 and player_y >= jupiter_y and player_y <= jupiter_y + 122:
            gameDisplay.blit(jupiter_text, (20,345))#Image Blit
            planet_buttons(40,380,120,122, None, action = 'jupiter')#Button
        #Mercury Crossover
        if player_x >= mercury_x and player_x <= mercury_x + 120 and player_y >= mercury_y and player_y <= mercury_y + 122:
            gameDisplay.blit(mercury_text, (605,350))#Image Blit
            planet_buttons(620,380,120,122, None, action = 'mercury')#Button 
        #Neptune Crossover
        if player_x >= neptune_x and player_x <= neptune_x + 120 and player_y >= neptune_y and player_y <= neptune_y + 119:
            gameDisplay.blit(neptune_text, (180,385))#Image Blit
            planet_buttons(200,430,120,119, None, action = 'neptune')#Button
        #Moon Crossover
        if player_x >= moon_x and player_x <= moon_x + 120 and player_y >= moon_y and player_y <= moon_y + 125:
            gameDisplay.blit(moon_text, (430,60))#Image Blit
            planet_buttons(430,20,120,125, None, action = 'moon')#Button
        #Pluto Crossover
        if player_x >= pluto_x and player_x <= pluto_x + 120 and player_y >= pluto_y and player_y <= pluto_y + 121:
            gameDisplay.blit(pluto_text, (457,470))#Image Blit
            planet_buttons(450,430,120,121, None, action = 'pluto')#Button
        player_x += x_change
        player_y += y_change
        ufo(player_x,player_y)
        pygame.display.update() #Updates the Display         #If anything is blit to the display, the display will have to be updated, it will update (fps) times per second
        clock.tick(fps) #Runs this function at the game FPS value                 #Each Clocktick will run this loop again that many times per second, Defined by the clocktick variable
def planet_buttons(x,y,width,height,active_color, action = None):
    cur = pygame.mouse.get_pos() #Gets Cursor Position
    click = pygame.mouse.get_pressed() #Checks for mouse click
    if x + width > cur[0] > x and y + height > cur[1] > y:#Checks if mouse position is over the button
        if click[0] == 1 and action != None: #If Button is clicked and action is not equal to nothing
            clickaudio.play() #Plays the Click audio
            time.sleep(0.5) #Pauses the game for 0.5 seconds
            if action == "earth":
                earth_quiz()
            if action == "sun":
                sun_quiz()
            if action == "mars":
                mars_quiz()
            if action == "moon":
                moon_quiz()
            if action == "venus":
                venus_quiz()
            if action == "neptune":
                neptune_quiz()
            if action == "jupiter":
                jupiter_quiz()
            if action == "mercury":
                mercury_quiz()
            if action == "uranus":
                uranus_quiz()
            if action == "pluto":
                pluto_quiz()
            if action == "saturn":
                saturn_quiz()
def ufo(player_x,player_y):
    gameDisplay.blit(player,(player_x,player_y))#Image Blit
########################################################################THE QUIZZES################################################################################
earth_question1_run = False #Sets this question run to False
earth_question2_run = False #Sets this question run to False
earth_question3_run = False #Sets this question run to False
earth_question4_run = False #Sets this question run to False
earth_question5_run = False #Sets this question run to False
earth_question6_run = False #Sets this question run to False
earth_question7_run = False #Sets this question run to False
earth_question8_run = False #Sets this question run to False
earth_question9_run = False #Sets this question run to False
earth_question10_run = False #Sets this question run to False
earth_end = False
earth_score = 0 #Sets this Quizzes Score to 0
sun_question1_run = False #Sets this question run to False
sun_question2_run = False #Sets this question run to False
sun_question3_run = False #Sets this question run to False
sun_question4_run = False #Sets this question run to False
sun_question5_run = False #Sets this question run to False
sun_question6_run = False #Sets this question run to False
sun_question7_run = False #Sets this question run to False
sun_question8_run = False #Sets this question run to False
sun_question9_run = False #Sets this question run to False
sun_question10_run = False #Sets this question run to False
sun_end = False
sun_score = 0 #Sets this Quizzes Score to 0
moon_question1_run = False #Sets this question run to False
moon_question2_run = False #Sets this question run to False
moon_question3_run = False #Sets this question run to False
moon_question4_run = False #Sets this question run to False
moon_question5_run = False #Sets this question run to False
moon_question6_run = False #Sets this question run to False
moon_question7_run = False #Sets this question run to False
moon_question8_run = False #Sets this question run to False
moon_question9_run = False #Sets this question run to False
moon_question10_run = False #Sets this question run to False
moon_end = False
moon_score = 0 #Sets this Quizzes Score to 0
mars_question1_run = False #Sets this question run to False
mars_question2_run = False #Sets this question run to False
mars_question3_run = False #Sets this question run to False
mars_question4_run = False #Sets this question run to False
mars_question5_run = False #Sets this question run to False
mars_question6_run = False #Sets this question run to False
mars_question7_run = False #Sets this question run to False
mars_question8_run = False #Sets this question run to False
mars_question9_run = False #Sets this question run to False
mars_question10_run = False #Sets this question run to False
mars_end = False
mars_score = 0 #Sets this Quizzes Score to 0
saturn_question1_run = False #Sets this question run to False
saturn_question2_run = False #Sets this question run to False
saturn_question3_run = False #Sets this question run to False
saturn_question4_run = False #Sets this question run to False
saturn_question5_run = False #Sets this question run to False
saturn_question6_run = False #Sets this question run to False
saturn_question7_run = False #Sets this question run to False
saturn_question8_run = False #Sets this question run to False
saturn_question9_run = False #Sets this question run to False
saturn_question10_run = False #Sets this question run to False
saturn_end = False
saturn_score = 0 #Sets this Quizzes Score to 0
jupiter_question1_run = False #Sets this question run to False
jupiter_question2_run = False #Sets this question run to False
jupiter_question3_run = False #Sets this question run to False
jupiter_question4_run = False #Sets this question run to False
jupiter_question5_run = False #Sets this question run to False
jupiter_question6_run = False #Sets this question run to False
jupiter_question7_run = False #Sets this question run to False
jupiter_question8_run = False #Sets this question run to False
jupiter_question9_run = False #Sets this question run to False
jupiter_question10_run = False #Sets this question run to False
jupiter_end = False
jupiter_score = 0 #Sets this Quizzes Score to 0
neptune_question1_run = False #Sets this question run to False
neptune_question2_run = False #Sets this question run to False
neptune_question3_run = False #Sets this question run to False
neptune_question4_run = False #Sets this question run to False
neptune_question5_run = False #Sets this question run to False
neptune_question6_run = False #Sets this question run to False
neptune_question7_run = False #Sets this question run to False
neptune_question8_run = False #Sets this question run to False
neptune_question9_run = False #Sets this question run to False
neptune_question10_run = False #Sets this question run to False
neptune_end = False
neptune_score = 0 #Sets this Quizzes Score to 0
uranus_question1_run = False #Sets this question run to False
uranus_question2_run = False #Sets this question run to False
uranus_question3_run = False #Sets this question run to False
uranus_question4_run = False #Sets this question run to False
uranus_question5_run = False #Sets this question run to False
uranus_question6_run = False #Sets this question run to False
uranus_question7_run = False #Sets this question run to False
uranus_question8_run = False #Sets this question run to False
uranus_question9_run = False #Sets this question run to False
uranus_question10_run = False #Sets this question run to False
uranus_end = False
uranus_score = 0 #Sets this Quizzes Score to 0
venus_question1_run = False #Sets this question run to False
venus_question2_run = False #Sets this question run to False
venus_question3_run = False #Sets this question run to False
venus_question4_run = False #Sets this question run to False
venus_question5_run = False #Sets this question run to False
venus_question6_run = False #Sets this question run to False
venus_question7_run = False #Sets this question run to False
venus_question8_run = False #Sets this question run to False
venus_question9_run = False #Sets this question run to False
venus_question10_run = False #Sets this question run to False
venus_end = False
venus_score = 0 #Sets this Quizzes Score to 0
pluto_question1_run = False #Sets this question run to False
pluto_question2_run = False #Sets this question run to False
pluto_question3_run = False #Sets this question run to False
pluto_question4_run = False #Sets this question run to False
pluto_question5_run = False #Sets this question run to False
pluto_question6_run = False #Sets this question run to False
pluto_question7_run = False #Sets this question run to False
pluto_question8_run = False #Sets this question run to False
pluto_question9_run = False #Sets this question run to False
pluto_question10_run = False #Sets this question run to False
pluto_end = False
pluto_score = 0 #Sets this Quizzes Score to 0
mercury_question1_run = False #Sets this question run to False
mercury_question2_run = False #Sets this question run to False
mercury_question3_run = False #Sets this question run to False
mercury_question4_run = False #Sets this question run to False
mercury_question5_run = False #Sets this question run to False
mercury_question6_run = False #Sets this question run to False
mercury_question7_run = False #Sets this question run to False
mercury_question8_run = False #Sets this question run to False
mercury_question9_run = False #Sets this question run to False
mercury_question10_run = False #Sets this question run to False
mercury_end = False
mercury_score = 0 #Sets this Quizzes Score to 0
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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True

        if earth_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(earth_question_1, (20,50))#Image Blit
            gameDisplay.blit(windows, (100,270))#Image Blit
            questions_buttons(100,270,150,151, None, action = 'windows1')#Button
            gameDisplay.blit(apple, (325,250))#Image Blit
            questions_buttons(325,250,130,161, None, action = 'apple1')#Button
            gameDisplay.blit(linux, (550,270))#Image Blit
            questions_buttons(550,270,150,166, None, action = 'linux1')#Button
            pygame.display.update() #Updates the Display
            
        elif earth_question1_run == True and earth_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(earth_question_2, (80,50))#Image Blit
            gameDisplay.blit(windows, (100,270))#Image Blit
            questions_buttons(100,270,150,151, None, action = 'windows2')#Button
            gameDisplay.blit(apple, (325,250))#Image Blit
            questions_buttons(325,250,130,161, None, action = 'apple2')#Button
            gameDisplay.blit(linux, (550,270))#Image Blit
            questions_buttons(550,270,150,166, None, action = 'linux2')#Button
            pygame.display.update() #Updates the Display
            

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(earth_question_3, (30,50))#Image Blit
            gameDisplay.blit(windows, (100,270))#Image Blit
            questions_buttons(100,270,150,151, None, action = 'windows3')#Button
            gameDisplay.blit(apple, (325,250))#Image Blit
            questions_buttons(325,250,130,161, None, action = 'apple3')#Button
            gameDisplay.blit(linux, (550,270))#Image Blit
            questions_buttons(550,270,150,166, None, action = 'linux3')#Button
            pygame.display.update() #Updates the Display

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(earth_question_4, (70,50))#Image Blit
            gameDisplay.blit(true, (225,250))#Image Blit
            questions_buttons(225,250,135,137, None, action = 'true1')#Button
            gameDisplay.blit(false, (425,250))#Image Blit
            questions_buttons(425,250,135,137, None, action = 'false1')#Button
            pygame.display.update() #Updates the Display

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0)) #Background #Background 
            gameDisplay.blit(earth_question_5, (-10,50))#Image Blit
            pygame.draw.rect(gameDisplay, red, (25,260,50,50))#Draws a rectangle
            questions_buttons(25,260,50,50, None, action = 'red1')#Button
            pygame.draw.rect(gameDisplay, orange, (125,260,50,50))#Draws a rectangle
            questions_buttons(125,260,50,50, None, action = 'orange1')#Button
            pygame.draw.rect(gameDisplay, yellow, (225,260,50,50))#Draws a rectangle
            questions_buttons(225,260,50,50, None, action = 'yellow1')#Button
            pygame.draw.rect(gameDisplay, green, (325,260,50,50))#Draws a rectangle
            questions_buttons(325,260,50,50, None, action = 'green1')#Button
            pygame.draw.rect(gameDisplay, blue, (425,260,50,50))#Draws a rectangle
            questions_buttons(425,260,50,50, None, action = 'blue1')#Button
            pygame.draw.rect(gameDisplay, pink, (525,260,50,50))#Draws a rectangle
            questions_buttons(525,260,50,50, None, action = 'pink1')#Button
            pygame.draw.rect(gameDisplay, purple, (625,260,50,50))#Draws a rectangle
            questions_buttons(625,260,50,50, None, action = 'purple1')#Button
            pygame.draw.rect(gameDisplay, white, (725,260,50,50))#Draws a rectangle
            questions_buttons(725,260,50,50, None, action = 'white1')#Button
            pygame.display.update() #Updates the Display

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(earth_question_6, (80,50))#Image Blit
            gameDisplay.blit(vr, (50,200))#Image Blit
            questions_buttons(50,200,225,225, None, action = 'vr')#Button
            gameDisplay.blit(vr1, (287.5,200))#Image Blit
            questions_buttons(287.5,200,225,225, None, action = 'vr1')#Button
            gameDisplay.blit(vr2, (525,200))#Image Blit
            questions_buttons(525,200,225,225, None, action = 'vr2')#Button
            pygame.display.update() #Updates the Display

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(earth_question_7, (0,50))#Image Blit
            gameDisplay.blit(spacex, (50,170))#Image Blit
            questions_buttons(50,170,225,225, None, action = 'spacex')#Button
            gameDisplay.blit(nasa, (287.5,200))#Image Blit
            questions_buttons(287.5,200,225,225, None, action = 'nasa')#Button
            gameDisplay.blit(apollox, (525,250))#Image Blit
            questions_buttons(525,200,225,95, None, action = 'apollox')#Button
            pygame.display.update() #Updates the Display

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(earth_question_8, (100,50))#Image Blit
            gameDisplay.blit(windowsos, (100,200))#Image Blit
            questions_buttons(100,200,300,190, None, action = 'windowsos')#Button
            gameDisplay.blit(appleos, (400,200))#Image Blit
            questions_buttons(400,200,300,190, None, action = 'appleos')#Button
            pygame.display.update() #Updates the Display

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == True and earth_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(earth_question_9, (20,50))#Image Blit
            gameDisplay.blit(spark, (25,180))#Image Blit
            questions_buttons(50,200,300,190, None, action = 'spark')#Button
            gameDisplay.blit(vodafone, (280,200))#Image Blit
            questions_buttons(280,200,300,190, None, action = 'vodafone')#Button
            gameDisplay.blit(degrees2, (550,200))#Image Blit
            questions_buttons(550,200,300,190, None, action = '2degrees')#Button
            gameDisplay.blit(flip, (55,400))#Image Blit
            questions_buttons(55,400,300,190, None, action = 'flip')#Button
            gameDisplay.blit(slingshot, (280,400))#Image Blit
            questions_buttons(280,400,300,190, None, action = 'slingshot')#Button
            gameDisplay.blit(trustpower, (540,400))#Image Blit
            questions_buttons(540,400,300,190, None, action = 'trustpower')#Button
            pygame.display.update() #Updates the Display

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == True and earth_question9_run == True and earth_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(earth_question_10, (20,50)) 
            gameDisplay.blit(yes, (225,250))#Image Blit
            questions_buttons(225,250,135,137, None, action = 'yes1')#Button
            gameDisplay.blit(no, (425,250))#Image Blit
            questions_buttons(425,250,135,137, None, action = 'no1')#Button
            pygame.display.update() #Updates the Display

        elif earth_question1_run == True and earth_question2_run == True and earth_question3_run == True and earth_question4_run == True and earth_question5_run == True and earth_question6_run == True and earth_question7_run == True and earth_question8_run == True and earth_question9_run == True and earth_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(congratulations, (0,50))#Image Blit
            print("First Score = ", earth_score) #Prints the current score for this quiz
            earth_score = str(earth_score) #Prints the current score for this quiz
            message_to_screen_text_earth("Youre Score:      /10", white) #Actual text
            message_to_screen_text_earth_score(earth_score, white) #Actual text
            with open("resources/scores/earthscore.txt", 'r') as f: #Opens this file for reading
                for line in f:
                    print("Earth Score: ", earth_score) #Prints the current score for this quiz
                    print("Earth Read: ", line)
                    int(line)
            
            if earth_score > line:
                print("earth_score > line")
                with open("resources/scores/earthscore.txt", 'w') as f: #Opens this file for writing
                        f.write(earth_score) #Prints the current score for this quiz
                        
            elif earth_score < line:
                print("earth_score is less than line")
                print("ES:", earth_score) #Prints the current score for this quiz
                print("L:", line)
                
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])#Draws a rectangle
            gameDisplay.blit(restarttext, (310,200))#Image Blit
            questions_buttons(280,195,260,65, grey, action = 'restartearth')#Button

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])#Draws a rectangle
            gameDisplay.blit(levelstext, (310,280))#Image Blit
            questions_buttons(280,270,260,75, grey, action = 'levels')#Button

            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])#Draws a rectangle
            gameDisplay.blit(mainmtext, (310,365))#Image Blit
            questions_buttons(280,350,260,75, grey, action = 'mainm')#Button

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
            gameDisplay.blit(quittext, (340,440))#Image Blit
            questions_buttons(280,430,260,75, grey, action = 'quit')#Button

            pygame.display.update() #Updates the Display

def message_to_screen_text_earth(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)
    gameDisplay.blit(textSurf, textRect)#Image Blit

def message_to_screen_text_earth_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)
    gameDisplay.blit(textSurf, textRect)  #Image Blit                 
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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if sun_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(sun_question_1, (170,50))#Image Blit 
            gameDisplay.blit(star, (150,250))#Image Blit
            questions_buttons(150,250,200,200, None, action = 'star')#Button
            gameDisplay.blit(planetsun, (420,250))#Image Blit
            questions_buttons(400,250,200,200, None, action = 'planet')#Button
            pygame.display.update() #Updates the Display
            
        elif sun_question1_run == True and sun_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(sun_question_2, (100,0))
            gameDisplay.blit(armstrong, (80,250))#Image Blit
            questions_buttons(80,250,186,186, None, action = 'armstrong') #Button  
            gameDisplay.blit(collins, (520,250))#Image Blit
            questions_buttons(520,250,220,284, None, action = 'collins')#Button
            gameDisplay.blit(chris, (300,220))#Image Blit
            questions_buttons(300,220,300,200, None, action = 'chris')#Button
            pygame.display.update() #Updates the Display
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(sun_question_3, (150,0))
            gameDisplay.blit(apollo11, (20,160))#Image Blit
            questions_buttons(20,160,300,375, None, action = 'apollo11')#Button
            gameDisplay.blit(atlantis, (270,160))#Image Blit
            questions_buttons(275,160,250,375, None, action = 'atlantis')#Button
            gameDisplay.blit(columbia, (520,160))#Image Blit
            questions_buttons(520,160,250,375, None, action = 'columbia')#Button
            pygame.display.update() #Updates the Display
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(sun_question_4, (50,0))#Image Blit
            gameDisplay.blit(aresv, (250,115))#Image Blit
            questions_buttons(250,115,100,474, None, action = 'aresv')#Button
            gameDisplay.blit(saturnv, (450,115))#Image Blit
            questions_buttons(450,115,100,474, None, action = 'saturnv')#Button
            pygame.display.update() #Updates the Display
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(sun_question_5, (0,0)) 
            gameDisplay.blit(collins, (520,250))#Image Blit
            questions_buttons(520,250,220,284, None, action = 'collins1')#Button
            gameDisplay.blit(james, (60,250))#Image Blit
            questions_buttons(60,250,250,225, None, action = 'james1') #Button 
            gameDisplay.blit(chris, (300,220))#Image Blit
            questions_buttons(300,220,300,200, None, action = 'chris1')#Button
            pygame.display.update() #Updates the Display
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(sun_question_6, (20,0))
            gameDisplay.blit(num1, (50,230))#Image Blit
            questions_buttons(50,230,100,20, None, action = 'num1')#Button
            gameDisplay.blit(num2, (200,230))#Image Blit
            questions_buttons(200,230,100,200, None, action = 'num2')#Button
            gameDisplay.blit(num3, (350,230))#Image Blit
            questions_buttons(350,230,100,200, None, action = 'num3')#Button
            gameDisplay.blit(num4, (500,230))#Image Blit
            questions_buttons(500,230,100,200, None, action = 'num4')#Button
            gameDisplay.blit(num5, (650,230))#Image Blit
            questions_buttons(650,230,100,200, None, action = 'num5')#Button
            pygame.display.update() #Updates the Display
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == True and sun_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(sun_question_7, (200,0))
            gameDisplay.blit(yes, (225,250))#Image Blit
            questions_buttons(225,250,135,137, None, action = 'yes2')#Button
            gameDisplay.blit(no, (425,250))#Image Blit
            questions_buttons(425,250,135,137, None, action = 'no2')#Button
            pygame.display.update() #Updates the Display
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == True and sun_question7_run == True and sun_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(sun_question_8, (50,0))#Image Blit
            gameDisplay.blit(earthtxt, (350,120))#Image Blit
            questions_buttons(350,120,120,130, None, action = 'earthtxt')#Button
            gameDisplay.blit(marstxt, (500,270))#Image Blit
            questions_buttons(500,270,120,130, None, action = 'marstxt')#Button
            gameDisplay.blit(jupitertxt, (200,300))#Image Blit
            questions_buttons(200,270,120,130, None, action = 'jupitertxt')#Button
            gameDisplay.blit(venustxt, (350,450))#Image Blit
            questions_buttons(350,450,120,130, None, action = 'venustxt')#Button
            pygame.display.update() #Updates the Display
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == True and sun_question7_run == True and sun_question8_run == True and sun_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(sun_question_9, (50,0))#Image Blit
            gameDisplay.blit(earthtxt, (350,120))#Image Blit
            questions_buttons(350,120,120,130, None, action = 'earthtxt1')#Button
            gameDisplay.blit(marstxt, (500,270))#Image Blit
            questions_buttons(500,270,120,130, None, action = 'marstxt1')#Button
            gameDisplay.blit(mercurytxt, (200,300))#Image Blit
            questions_buttons(200,270,120,130, None, action = 'mercurytxt1')#Button
            gameDisplay.blit(venustxt, (350,450))#Image Blit
            questions_buttons(350,450,120,130, None, action = 'venustxt1')#Button
            pygame.display.update() #Updates the Display
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == True and sun_question7_run == True and sun_question8_run == True and sun_question9_run == True and sun_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(sun_question_10, (60,0))#Image Blit
            gameDisplay.blit(infinity, (150,150))#Image Blit
            questions_buttons(150,150,450,185, None, action = 'infinity')#Button
            gameDisplay.blit(elseimg, (400,350))#Image Blit
            questions_buttons(400,350,200,200, None, action = 'elseimg')#Button
            gameDisplay.blit(mean42, (200,350))#Image Blit
            questions_buttons(200,350,200,155, None, action = 'mean42')#Button
            pygame.display.update() #Updates the Display
            
        elif sun_question1_run == True and sun_question2_run == True and sun_question3_run == True and sun_question4_run == True and sun_question5_run == True and sun_question6_run == True and sun_question7_run == True and sun_question8_run == True and sun_question9_run == True and sun_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(congratulations, (0,50))#Image Blit
            print("First Score = ", sun_score) #Prints the current score for this quiz
            sun_score = str(sun_score) #Prints the current score for this quiz
            message_to_screen_text_sun("Youre Score:      /10", white) #Actual text
            message_to_screen_text_sun_score(sun_score, white) #Actual text
            with open("resources/scores/sunscore.txt", 'r') as f: #Opens this file for reading
                for line in f:
                    print("sun Score: ", sun_score) #Prints the current score for this quiz
                    print("sun Read: ", line)
                    int(line)
            
            if sun_score > line:
                print("sun_score > line")
                with open("resources/scores/sunscore.txt", 'w') as f: #Opens this file for writing
                        f.write(sun_score) #Prints the current score for this quiz
                        
            elif sun_score < line:
                print("sun_score is less than line")
                print("ES:", sun_score) #Prints the current score for this quiz
                print("L:", line)
                
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])#Draws a rectangle
            gameDisplay.blit(restarttext, (310,200))#Image Blit
            questions_buttons(280,195,260,65, grey, action = 'restartsun')#Button

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])#Draws a rectangle
            gameDisplay.blit(levelstext, (310,280))#Image Blit
            questions_buttons(280,270,260,75, grey, action = 'levels')#Button


            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])#Draws a rectangle
            gameDisplay.blit(mainmtext, (310,365))#Image Blit
            questions_buttons(280,350,260,75, grey, action = 'mainm')#Button

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
            gameDisplay.blit(quittext, (340,440))#Image Blit
            questions_buttons(280,430,260,75, grey, action = 'quit')#Button
            pygame.display.update() #Updates the Display
        pygame.display.update() #Updates the Display
        clock.tick(fps) #Runs this function at the game FPS value
def message_to_screen_text_sun(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)
    gameDisplay.blit(textSurf, textRect)#Image Blit

def message_to_screen_text_sun_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)
    gameDisplay.blit(textSurf, textRect) #Image Blit   

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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if moon_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L1, (80,180))#Image Blit
            questions_buttons(80,180,327,300, None, action = 'wyrleft1')#Button
            gameDisplay.blit(R1, (400,180))#Image Blit
            questions_buttons(400,180,327,300, None, action = 'wyrright1')#Button
            pygame.display.update() #Updates the Display
        elif moon_question1_run == True and moon_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L2, (80,180))#Image Blit
            questions_buttons(80,180,327,300, None, action = 'wyrleft2')#Button
            gameDisplay.blit(R2, (400,180))#Image Blit
            questions_buttons(400,180,327,300, None, action = 'wyrright2')#Button
            pygame.display.update() #Updates the Display
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L3, (80,180))#Image Blit
            questions_buttons(80,180,327,300, None, action = 'wyrleft3')#Button
            gameDisplay.blit(R3, (400,180))#Image Blit
            questions_buttons(400,180,327,300, None, action = 'wyrrigh3')#Button
            pygame.display.update() #Updates the Display
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L4, (80,180))#Image Blit
            questions_buttons(80,180,327,300, None, action = 'wyrleft4')#Button
            gameDisplay.blit(R4, (400,180))#Image Blit
            questions_buttons(400,180,327,300, None, action = 'wyrright4')#Button
            pygame.display.update() #Updates the Display
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L5, (80,180))#Image Blit
            questions_buttons(80,180,327,300, None, action = 'wyrleft5')#Button
            gameDisplay.blit(R5, (400,180))#Image Blit
            questions_buttons(400,180,327,300, None, action = 'wyrright5')#Button
            pygame.display.update() #Updates the Display
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L6, (80,180))#Image Blit
            questions_buttons(80,180,327,300, None, action = 'wyrleft6')#Button
            gameDisplay.blit(R6, (400,180))#Image Blit
            questions_buttons(400,180,327,300, None, action = 'wyrright6')#Button
            pygame.display.update() #Updates the Display
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == True and moon_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L7, (80,180))#Image Blit
            questions_buttons(80,180,327,300, None, action = 'wyrleft7')#Button
            gameDisplay.blit(R7, (400,180))#Image Blit
            questions_buttons(400,180,327,300, None, action = 'wyrright7')#Button
            pygame.display.update() #Updates the Display
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == True and moon_question7_run == True and moon_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L8, (80,180))#Image Blit
            questions_buttons(80,180,327,300, None, action = 'wyrleft8')#Button
            gameDisplay.blit(R8, (400,180))#Image Blit
            questions_buttons(400,180,327,300, None, action = 'wyrright8')#Button
            pygame.display.update() #Updates the Display
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == True and moon_question7_run == True and moon_question8_run == True and moon_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L9, (80,180))#Image Blit
            questions_buttons(80,180,327,300, None, action = 'wyrleft9')#Button
            gameDisplay.blit(R9, (400,180))#Image Blit
            questions_buttons(400,180,327,300, None, action = 'wyrright9')#Button
            pygame.display.update() #Updates the Display
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == True and moon_question7_run == True and moon_question8_run == True and moon_question9_run == True and moon_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(moon_question_1, (70,20))
            gameDisplay.blit(L10, (80,180))#Image Blit
            questions_buttons(80,180,327,300, None, action = 'wyrleft10')#Button
            gameDisplay.blit(R10, (400,180))#Image Blit
            questions_buttons(400,180,327,300, None, action = 'wyrright10')#Button
            pygame.display.update() #Updates the Display
        elif moon_question1_run == True and moon_question2_run == True and moon_question3_run == True and moon_question4_run == True and moon_question5_run == True and moon_question6_run == True and moon_question7_run == True and moon_question8_run == True and moon_question9_run == True and moon_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(welldone, (150,50))#Image Blit
            print("First Score = ", moon_score) #Prints the current score for this quiz
            message_to_screen_text_sun("Youre Score:10/10", white) #Actual text
            with open("resources/scores/moonscore.txt", 'w') as f: #Opens this file for writing
                f.write('10')
                        
                
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])#Draws a rectangle
            gameDisplay.blit(restarttext, (310,200))#Image Blit
            questions_buttons(280,195,260,65, grey, action = 'restartmoon')#Button

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])#Draws a rectangle
            gameDisplay.blit(levelstext, (310,280))#Image Blit
            questions_buttons(280,270,260,75, grey, action = 'levels')#Button


            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])#Draws a rectangle
            gameDisplay.blit(mainmtext, (310,365))#Image Blit
            questions_buttons(280,350,260,75, grey, action = 'mainm')#Button

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
            gameDisplay.blit(quittext, (340,440))#Image Blit
            questions_buttons(280,430,260,75, grey, action = 'quit')#Button
            pygame.display.update() #Updates the Display
        pygame.display.update() #Updates the Display
        clock.tick(fps) #Runs this function at the game FPS value

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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
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
        pygame.display.update() #Updates the Display
        clock.tick(fps) #Runs this function at the game FPS value
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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if uranus_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(uranus_question_1, (100,0))
            gameDisplay.blit(porgimg, (180,300))#Image Blit
            gameDisplay.blit(nova, (100,230))#Image Blit
            questions_buttons(100,230,170,85, None, action = 'nova')#Button
            gameDisplay.blit(poru, (300,230))#Image Blit
            questions_buttons(300,230,170,85, None, action = 'poru')#Button
            gameDisplay.blit(porg, (500,230))#Image Blit
            questions_buttons(500,230,170,85, None, action = 'porg')#Button
            pygame.display.update() #Updates the Display    
        elif uranus_question1_run == True and uranus_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(uranus_question_2, (0,0))#Image Blit
            gameDisplay.blit(yoda, (300,300))#Image Blit
            gameDisplay.blit(yodu, (20,230))#Image Blit
            questions_buttons(20,230,170,85, None, action = 'yodu')#Button
            gameDisplay.blit(yaddle, (180,230))#Image Blit
            questions_buttons(180,230,170,85, None, action = 'yaddle')#Button
            gameDisplay.blit(yanna, (380,230))#Image Blit
            questions_buttons(380,230,170,85, None, action = 'yanna')#Button
            gameDisplay.blit(yodan, (570,230))#Image Blit
            questions_buttons(570,230,170,85, None, action = 'yodan')#Button
            pygame.display.update() #Updates the Display    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(uranus_question_3, (50,0))#Image Blit
            gameDisplay.blit(kyberimg, (250,400))#Image Blit
            gameDisplay.blit(kybar, (10,200))#Image Blit
            questions_buttons(10,200,390,100, None, action = 'kybar')#Button
            gameDisplay.blit(kybur, (440,200))#Image Blit
            questions_buttons(440,200,390,100, None, action = 'kybur')#Button
            gameDisplay.blit(kyber, (10,300))#Image Blit
            questions_buttons(10,300,390,100, None, action = 'kyber')#Button
            gameDisplay.blit(kyba, (440,300))#Image Blit
            questions_buttons(440,300,390,100, None, action = 'kyba')#Button
            pygame.display.update() #Updates the Display    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(uranus_question_4, (100,0))#Image Blit
            gameDisplay.blit(yoda, (20,200))#Image Blit
            questions_buttons(20,200,205,250, None, action = 'yoda1')#Button
            gameDisplay.blit(anakin, (550,200))#Image Blit
            questions_buttons(300,200,250,250, None, action = 'anakin1')#Button
            gameDisplay.blit(luke, (250,200))#Image Blit
            questions_buttons(250,200,280,242, None, action = 'luke1')#Button
            pygame.display.update() #Updates the Display    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == False: #QUESTION 5gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(uranus_question_5, (0,0))#Image Blit
            gameDisplay.blit(leia, (30,220))#Image Blit
            questions_buttons(20,220,205,250, None, action = 'leia2')#Button
            gameDisplay.blit(anakin, (520,220))#Image Blit
            questions_buttons(300,220,250,250, None, action = 'anakin2')#Button
            gameDisplay.blit(luke, (220,220))#Image Blit
            questions_buttons(250,220,280,242, None, action = 'luke2')#Button
            pygame.display.update() #Updates the Display    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(uranus_question_6, (130,20))#Image Blit
            gameDisplay.blit(anewhope, (100,230))#Image Blit
            questions_buttons(100,230,185,300, None, action = 'anewhope')#Button
            gameDisplay.blit(returnofthejedi, (300,230))#Image Blit
            questions_buttons(300,230,190,300, None, action = 'returnofthejedi')#Button
            gameDisplay.blit(thelastjedi, (500,230))#Image Blit
            questions_buttons(500,230,200,300, None, action = 'thelastjedi')#Button
            pygame.display.update() #Updates the Display   
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == True and uranus_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(uranus_question_7, (100,0))#Image Blit
            gameDisplay.blit(c3po, (10,230))#Image Blit
            questions_buttons(10,230,185,300, None, action = 'c3po')#Button
            gameDisplay.blit(bb8, (300,230))#Image Blit
            questions_buttons(300,230,190,300, None, action = 'bb8')#Button
            gameDisplay.blit(r2d2, (550,230))#Image Blit
            questions_buttons(500,230,200,300, None, action = 'r2d2')#Button
            pygame.display.update() #Updates the Display    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == True and uranus_question7_run == True and uranus_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(uranus_question_8, (0,0))#Image Blit
            gameDisplay.blit(fn2187, (250,300))#Image Blit
            gameDisplay.blit(bud, (100,230))#Image Blit
            questions_buttons(100,230,170,85, None, action = 'bud')#Button
            gameDisplay.blit(finn, (300,230))#Image Blit
            questions_buttons(300,230,170,85, None, action = 'finn')#Button
            gameDisplay.blit(john, (500,230))#Image Blit
            questions_buttons(500,230,170,85, None, action = 'john')#Button
            pygame.display.update() #Updates the Display    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == True and uranus_question7_run == True and uranus_question8_run == True and uranus_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(uranus_question_9, (100,0))#Image Blit
            gameDisplay.blit(xwing, (200,410))#Image Blit
            questions_buttons(200,410,400,225, None, action = 'xwing')#Button
            gameDisplay.blit(falcon, (0,180))#Image Blit
            questions_buttons(0,180,400,225, None, action = 'falcon')#Button
            gameDisplay.blit(enterprise, (400,180))#Image Blit
            questions_buttons(400,180,400,225, None, action = 'enterprise')#Button
            pygame.display.update() #Updates the Display    
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == True and uranus_question7_run == True and uranus_question8_run == True and uranus_question9_run == True and uranus_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(uranus_question_10, (100,0))#Image Blit
            gameDisplay.blit(jedichurch, (330,150))#Image Blit
            gameDisplay.blit(true, (200,300))#Image Blit
            questions_buttons(200,250,130,130, None, action = 'jedi')#Button
            gameDisplay.blit(false, (450,300))#Image Blit
            questions_buttons(250,400,130,130, None, action = 'jedi')#Button
            pygame.display.update() #Updates the Display
        elif uranus_question1_run == True and uranus_question2_run == True and uranus_question3_run == True and uranus_question4_run == True and uranus_question5_run == True and uranus_question6_run == True and uranus_question7_run == True and uranus_question8_run == True and uranus_question9_run == True and uranus_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(congratulations, (0,50))#Image Blit
            print("First Score = ", uranus_score) #Prints the current score for this quiz
            uranus_score = str(uranus_score) #Prints the current score for this quiz
            message_to_screen_text_uranus("Youre Score:      /10", white) #Actual text
            message_to_screen_text_uranus_score(uranus_score, white) #Actual text
            with open("resources/scores/uranusscore.txt", 'r') as f: #Opens this file for reading
                for line in f:
                    print("uranus Score: ", uranus_score) #Prints the current score for this quiz
                    print("uranus Read: ", line)
                    int(line)
            
            if uranus_score > line:
                print("uranus_score > line")
                with open("resources/scores/uranusscore.txt", 'w') as f: #Opens this file for writing
                        f.write(uranus_score) #Prints the current score for this quiz
                        
            elif uranus_score < line:
                print("uranus_score is less than line")
                print("ES:", uranus_score) #Prints the current score for this quiz
                print("L:", line)
                
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])#Draws a rectangle
            gameDisplay.blit(restarttext, (310,200))#Image Blit
            questions_buttons(280,195,260,65, grey, action = 'restarturanus')#Button

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])#Draws a rectangle
            gameDisplay.blit(levelstext, (310,280))#Image Blit
            questions_buttons(280,270,260,75, grey, action = 'levels')#Button


            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])#Draws a rectangle
            gameDisplay.blit(mainmtext, (310,365))#Image Blit
            questions_buttons(280,350,260,75, grey, action = 'mainm')#Button

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
            gameDisplay.blit(quittext, (340,440))#Image Blit
            questions_buttons(280,430,260,75, grey, action = 'quit')#Button
            pygame.display.update() #Updates the Display
            pygame.display.update() #Updates the Display    
        pygame.display.update() #Updates the Display
        clock.tick(fps) #Runs this function at the game FPS value
def message_to_screen_text_uranus(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)
    gameDisplay.blit(textSurf, textRect)#Image Blit

def message_to_screen_text_uranus_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)
    gameDisplay.blit(textSurf, textRect)#Image Blit     

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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
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
        pygame.display.update() #Updates the Display
        clock.tick(fps) #Runs this function at the game FPS value
############################################################################################################################################################
#####################################################JUPITERERERERERERERERERERERERERERERERERE##################################################################################
############################################################################################################################################################ 
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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = False
 
        if jupiter_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(jupiter_question_1, (125,0))#Image Blit
            gameDisplay.blit(albert, (50,320))#Image Blit
            questions_buttons(50,320,438,278, None, action = 'albert')#Button
            gameDisplay.blit(ben, (200,150))#Image Blit
            questions_buttons(200,150,400,151, None, action = 'ben')#Button
            gameDisplay.blit(thomas, (550,320))#Image Blit
            questions_buttons(550,320,200,278, None, action = 'thomas')#Button
            pygame.display.update() #Updates the Display
        elif jupiter_question1_run == True and jupiter_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(jupiter_question_2, (0,0))#Image Blit
            gameDisplay.blit(argon, (50,200))#Image Blit
            questions_buttons(200,200,438,278, None, action = 'argon')#Button
            gameDisplay.blit(gold, (200,200))#Image Blit
            questions_buttons(400,200,400,151, None, action = 'gold')#Button
            gameDisplay.blit(silver, (550,200))#Image Blit
            questions_buttons(550,200,200,278, None, action = 'silver')#Button
            pygame.display.update() #Updates the Display
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(jupiter_question_3, (100,0))#Image Blit
            gameDisplay.blit(num1, (50,230))#Image Blit
            questions_buttons(50,230,100,20, None, action = 'gamma1')#Button
            gameDisplay.blit(num2, (200,230))#Image Blit
            questions_buttons(200,230,100,200, None, action = 'gamma2')#Button
            gameDisplay.blit(num3, (350,230))#Image Blit
            questions_buttons(350,230,100,200, None, action = 'gamma3')#Button
            gameDisplay.blit(num4, (500,230))#Image Blit
            questions_buttons(500,230,100,200, None, action = 'gamma4')#Button
            gameDisplay.blit(num5, (650,230))#Image Blit
            questions_buttons(650,230,100,200, None, action = 'gamma5')#Button
            pygame.display.update() #Updates the Display
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(jupiter_question_4, (0,0))#Image Blit
            pygame.display.update() #Updates the Display
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(jupiter_question_5, (0,0))#Image Blit
            pygame.display.update() #Updates the Display
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(jupiter_question_6, (0,0))#Image Blit
            pygame.display.update() #Updates the Display
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == True and jupiter_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(jupiter_question_7, (0,0))#Image Blit
            pygame.display.update() #Updates the Display
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == True and jupiter_question7_run == True and jupiter_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(jupiter_question_8, (0,0))#Image Blit
            pygame.display.update() #Updates the Display
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == True and jupiter_question7_run == True and jupiter_question8_run == True and jupiter_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(jupiter_question_9, (0,0))#Image Blit
            pygame.display.update() #Updates the Display
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == True and jupiter_question7_run == True and jupiter_question8_run == True and jupiter_question9_run == True and jupiter_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(jupiter_question_10, (0,0))#Image Blit
            pygame.display.update() #Updates the Display
        elif jupiter_question1_run == True and jupiter_question2_run == True and jupiter_question3_run == True and jupiter_question4_run == True and jupiter_question5_run == True and jupiter_question6_run == True and jupiter_question7_run == True and jupiter_question8_run == True and jupiter_question9_run == True and jupiter_end == True: #QUESTION 10
            pass
        pygame.display.update() #Updates the Display
        clock.tick(fps) #Runs this function at the game FPS value    

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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if mars_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(mars_question_1, (0,0))#Image Blit
            pygame.draw.rect(gameDisplay, orange, [100,100,160,160])#Draws a rectangle
            questions_buttons(100,100,160,160, orange, action = 'q')#Button
            pygame.draw.rect(gameDisplay, blue, [600,560,10,10])#Draws a rectangle
            questions_buttons(600,560,10,10, blue, action = 'a')#Button
            pygame.draw.rect(gameDisplay, white, [356,100,220,220])#Draws a rectangle
            questions_buttons(356,100,220,220, white, action = 'q')#Button
            pygame.draw.rect(gameDisplay, yellow, [600,287,113,220])#Draws a rectangle
            questions_buttons(600,287,113,220, yellow, action = 'q')#Button
            pygame.draw.rect(gameDisplay, red, [250,350,88,110])#Draws a rectangle
            questions_buttons(250,350,88,110, red, action = 'q')#Button
            pygame.draw.rect(gameDisplay, green, [55,430,70,60])#Draws a rectangle
            questions_buttons(55,430,70,60, green, action = 'q')#Button
            pygame.draw.rect(gameDisplay, pink, [477,467,55,32])#Draws a rectangle
            questions_buttons(477,467,55,32, pink, action = 'q')#Button
            pygame.draw.rect(gameDisplay, blue, [600,145,90,81])#Draws a rectangle
            questions_buttons(600,145,90,81, blue, action = 'q')#Button
            pygame.display.update() #Updates the Display
        elif mars_question1_run == True and mars_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(mars_question_2, (0,0))#Image Blit
            questions_buttons(400,20,110,50, transparent, action = 'yesrect')#Button
            gameDisplay.blit(no, (300,200))#Image Blit
            questions_buttons(300,200,140,140, transparent, action = 'norect')#Button
            gameDisplay.blit(no, (100,67))#Image Blit
            questions_buttons(100,67,140,140, transparent, action = 'norect')#Button
            gameDisplay.blit(no, (400,337))#Image Blit
            questions_buttons(400,337,140,140, transparent, action = 'norect')#Button
            gameDisplay.blit(no, (600,24))#Image Blit
            questions_buttons(600,24,140,140, transparent, action = 'norect')#Button
            gameDisplay.blit(no, (45,400))#Image Blit
            questions_buttons(45,400,140,140, transparent, action = 'norect')#Button
            gameDisplay.blit(no, (670,400))#Image Blit
            questions_buttons(670,400,140,140, transparent, action = 'norect')#Button
            pygame.display.update() #Updates the Display
        elif mars_question1_run == True and mars_question2_run == True and mars_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(mars_question_3, (0,0))#Image Blit
            #1st Row
            pygame.draw.rect(gameDisplay, red, [75,100,100,100]) and pygame.draw.rect(gameDisplay, red, [225,100,100,100]) and pygame.draw.rect(gameDisplay, red, [375,100,100,100]) and pygame.draw.rect(gameDisplay, red, [525,100,100,100]) and pygame.draw.rect(gameDisplay, red, [675,100,100,100])
            #2nd Row
            pygame.draw.rect(gameDisplay, red, [75,250,100,100]) and pygame.draw.rect(gameDisplay, red, [225,250,100,100]) and pygame.draw.rect(gameDisplay, red, [375,250,100,100]) and pygame.draw.rect(gameDisplay, red, [525,250,100,100]) and pygame.draw.rect(gameDisplay, red, [675,250,100,100])
            #3rd Row
            pygame.draw.rect(gameDisplay, red, [75,400,100,100]) and pygame.draw.rect(gameDisplay, red, [225,400,100,100]) and pygame.draw.rect(gameDisplay, red, [375,400,100,100]) and pygame.draw.rect(gameDisplay, red, [525,400,100,100]) and pygame.draw.rect(gameDisplay, red, [675,400,100,100])
            questions_buttons_idiot_test(75,100,100,100, green, action = 'thered1')#Button
            questions_buttons_idiot_test(75,400,100,100, orange, action = 'thered1')#Button
            questions_buttons_idiot_test(75,250,100,100, yellow, action = 'thered1')#Button
            questions_buttons_idiot_test(225,100,100,100, pink, action = 'thered1')#Button
            questions_buttons_idiot_test(225,400,100,100, yellow, action = 'thered1')#Button
            questions_buttons_idiot_test(225,250,100,100, orange, action = 'thered1')#Button
            questions_buttons_idiot_test(375,100,100,100, purple, action = 'thered1')#Button
            questions_buttons_idiot_test(375,400,100,100, black, action = 'thered1')#Button
            questions_buttons_idiot_test(375,250,100,100, white, action = 'thered1')#Button
            questions_buttons_idiot_test(525,100,100,100, grey, action = 'thered1')#Button
            questions_buttons_idiot_test(525,400,100,100, orange, action = 'thered1')#Button
            questions_buttons_idiot_test(525,250,100,100, brown, action = 'thered1')#Button
            questions_buttons_idiot_test(675,100,100,100, green, action = 'thered1')#Button
            questions_buttons_idiot_test(675,400,100,100, lightbrown, action = 'thered1')#Button
            questions_buttons_idiot_test(675,250,100,100, blue, action = 'theblue1')#Button
            pygame.display.update() #Updates the Display
        elif mars_question1_run == True and mars_question2_run == True and mars_question3_run == True and mars_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(mars_question_4, (0,0))#Image Blit
            questions_buttons(540,30,160,40, None, action = 'dontclick') #Button
            questions_buttons(290,120,120,40, None, action = 'dontclick')#Button
            questions_buttons(250,250,160,40, None, action = 'dontclick')#Button
            questions_buttons(560,290,120,40, None, action = 'dontclick')#Button
            questions_buttons(140,330,100,40, None, action = 'dontclick')#Button
            questions_buttons(460,400,100,40, None, action = 'dontclick')#Button
            questions_buttons(520,550,100,40, None, action = 'dontclick')#Button
            questions_buttons(620,160,100,40, None, action = 'click')#Button
            pygame.display.update() #Updates the Display
        elif mars_question1_run == True and mars_question2_run == True and mars_question3_run == True and mars_question4_run == True and mars_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(mars_question_5, (0,0))#Image Blit
            questions_buttons(0,0,800,600, None, action = 'justclick') 
            pygame.display.update() #Updates the Display
        elif mars_question1_run == True and mars_question2_run == True and mars_question3_run == True and mars_question4_run == True and mars_question5_run == True and mars_end == True:
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(congratulations, (0,50))#Image Blit
            print("First Score = ", mars_score) #Prints the current score for this quiz
            mars_score = str(mars_score) #Prints the current score for this quiz
            message_to_screen_text_mars("Youre Score:      /10", white) #Actual text
            message_to_screen_text_mars_score(mars_score, white) #Actual text
            with open("resources/scores/marsscore.txt", 'r') as f: #Opens this file for reading
                for line in f:
                    print("mars Score: ", mars_score) #Prints the current score for this quiz
                    print("mars Read: ", line)
                    int(line)
            
            if mars_score > line:
                print("mars_score > line")
                with open("resources/scores/marsscore.txt", 'w') as f: #Opens this file for writing
                        f.write(mars_score) #Prints the current score for this quiz
                        
            elif mars_score < line:
                print("mars_score is less than line")
                print("ES:", mars_score) #Prints the current score for this quiz
                print("L:", line)
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])#Draws a rectangle
            gameDisplay.blit(restarttext, (310,200))#Image Blit
            questions_buttons(280,195,260,65, grey, action = 'restartmars')#Button
            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])#Draws a rectangle
            gameDisplay.blit(levelstext, (310,280))#Image Blit
            questions_buttons(280,270,260,75, grey, action = 'levels')#Button
            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])#Draws a rectangle
            gameDisplay.blit(mainmtext, (310,365))#Image Blit
            questions_buttons(280,350,260,75, grey, action = 'mainm')#Button
            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
            gameDisplay.blit(quittext, (340,440))#Image Blit
            questions_buttons(280,430,260,75, grey, action = 'quit')#Button
            pygame.display.update() #Updates the Display
        pygame.display.update() #Updates the Display
        clock.tick(fps) #Runs this function at the game FPS value
def message_to_screen_text_mars(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)#Image Blit
    gameDisplay.blit(textSurf, textRect)

def message_to_screen_text_mars_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)#Image Blit
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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
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
        pygame.display.update() #Updates the Display
        clock.tick(fps) #Runs this function at the game FPS value

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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
                gameExit = True
 
        if venus_question1_run == False: #QUESTION 1
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(venus_question_1, (120,10))#Image Blit
            gameDisplay.blit(bull, (220,180))#Image Blit
            gameDisplay.blit(true, (200,450))#Image Blit
            questions_buttons(200,450,130,130, None, action = 'true2')#Button
            gameDisplay.blit(false, (450,450))#Image Blit
            questions_buttons(450,400,130,130, None, action = 'false2')#Button
            pygame.display.update() #Updates the Display
        elif venus_question1_run == True and venus_question2_run == False: #QUESTION 2
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(venus_question_2, (0,10))#Image Blit
            gameDisplay.blit(brain, (260,180))#Image Blit
            gameDisplay.blit(true, (200,450))#Image Blit
            questions_buttons(200,450,130,130, None, action = 'true3')#Button
            gameDisplay.blit(false, (450,450))#Image Blit
            questions_buttons(450,450,130,130, None, action = 'false3')#Button
            pygame.display.update() #Updates the Display
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == False: #QUESTION 3
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(venus_question_3, (10,0))#Image Blit
            gameDisplay.blit(email, (250,180))#Image Blit
            gameDisplay.blit(true, (200,450))#Image Blit
            questions_buttons(200,450,130,130, None, action = 'true4')#Button
            gameDisplay.blit(false, (450,450))#Image Blit
            questions_buttons(450,450,130,130, None, action = 'false4')#Button
            pygame.display.update() #Updates the Display
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == False: #QUESTION 4       
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(venus_question_4, (0,10))#Image Blit
            gameDisplay.blit(solar, (180,190))#Image Blit
            gameDisplay.blit(true, (200,450))#Image Blit
            questions_buttons(200,450,130,130, None, action = 'true5')#Button
            gameDisplay.blit(false, (450,450))#Image Blit
            questions_buttons(450,450,130,130, None, action = 'false5')#Button
            pygame.display.update() #Updates the Display
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == False: #QUESTION 5
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(venus_question_5, (130,10))#Image Blit
            gameDisplay.blit(cheetah, (250,185))#Image Blit
            gameDisplay.blit(true, (200,450))#Image Blit
            questions_buttons(200,450,130,130, None, action = 'true6')#Button
            gameDisplay.blit(false, (450,450))#Image Blit
            questions_buttons(450,450,130,130, None, action = 'false6')#Button
            pygame.display.update() #Updates the Display
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == False: #QUESTION 6
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(venus_question_6, (50,10))#Image Blit
            gameDisplay.blit(ball, (260,180))#Image Blit
            gameDisplay.blit(true, (200,450))#Image Blit
            questions_buttons(200,450,130,130, None, action = 'true7')#Button
            gameDisplay.blit(false, (450,450))#Image Blit
            questions_buttons(450,450,130,130, None, action = 'false7')#Button
            pygame.display.update() #Updates the Display
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == True and venus_question7_run == False: #QUESTION 7                                                           
            gameDisplay.blit(bg, (0,0)) #Background#Image Blit
            gameDisplay.blit(venus_question_7, (40,10))
            gameDisplay.blit(hammer, (260,170))#Image Blit
            gameDisplay.blit(true, (200,450))#Image Blit
            questions_buttons(200,450,130,130, None, action = 'true8')#Button
            gameDisplay.blit(false, (450,450))#Image Blit
            questions_buttons(450,450,130,130, None, action = 'false8')#Button
            pygame.display.update() #Updates the Display
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == True and venus_question7_run == True and venus_question8_run == False: #QUESTION 8
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(venus_question_8, (100,10))#Image Blit
            gameDisplay.blit(spin, (270,185))#Image Blit
            gameDisplay.blit(true, (200,450))#Image Blit
            questions_buttons(200,450,130,130, None, action = 'true9')#Button
            gameDisplay.blit(false, (450,450))#Image Blit
            questions_buttons(450,450,130,130, None, action = 'false9')#Button
            pygame.display.update() #Updates the Display
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == True and venus_question7_run == True and venus_question8_run == True and venus_question9_run == False: #QUESTION 9                         
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(venus_question_9, (100,10))#Image Blit
            gameDisplay.blit(lightning, (210,185))#Image Blit
            gameDisplay.blit(true, (200,450))#Image Blit
            questions_buttons(200,450,130,130, None, action = 'true10')#Button
            gameDisplay.blit(false, (450,450))#Image Blit
            questions_buttons(450,450,130,130, None, action = 'false10')#Button
            pygame.display.update() #Updates the Display
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == True and venus_question7_run == True and venus_question8_run == True and venus_question9_run == True and venus_end == False: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(venus_question_10, (100,10))#Image Blit
            gameDisplay.blit(griffin, (310,150))#Image Blit
            gameDisplay.blit(true, (200,450))#Image Blit
            questions_buttons(200,450,130,130, None, action = 'true11')#Button
            gameDisplay.blit(false, (450,450))#Image Blit
            questions_buttons(450,450,130,130, None, action = 'false11')#Button
            pygame.display.update() #Updates the Display
        elif venus_question1_run == True and venus_question2_run == True and venus_question3_run == True and venus_question4_run == True and venus_question5_run == True and venus_question6_run == True and venus_question7_run == True and venus_question8_run == True and venus_question9_run == True and venus_end == True: #QUESTION 10
            gameDisplay.blit(bg, (0,0)) #Background
            gameDisplay.blit(congrats, (0,50))#Image Blit
            print("First Score = ", venus_score) #Prints the current score for this quiz
            venus_score = str(venus_score) #Prints the current score for this quiz
            message_to_screen_text_venus("Youre Score:      /10", white) #Actual text
            message_to_screen_text_venus_score(venus_score, white) #Actual text
            with open("resources/scores/venusscore.txt", 'r') as f: #Opens this file for reading
                for line in f:
                    print("venus Score: ", venus_score) #Prints the current score for this quiz
                    print("venus Read: ", line)
                    int(line)
                    int(venus_score) #Prints the current score for this quiz
            
            if venus_score > line:
                print("venus_score > line")
                with open("resources/scores/venusscore.txt", 'w') as f: #Opens this file for writing
                    f.write(venus_score) #Prints the current score for this quiz
                        
            elif venus_score < line:
                print("venus_score is less than line")
                print("SS:", venus_score) #Prints the current score for this quiz
                print("L:", line)
                
            #Restart Button
            pygame.draw.rect(gameDisplay, white, [300,200,220,55])#Draws a rectangle
            gameDisplay.blit(restarttext, (310,200))#Image Blit
            questions_buttons(280,195,260,65, grey, action = 'restartvenus')#Button

            #Levels Button
            pygame.draw.rect(gameDisplay, white, [300,280,220,55])#Draws a rectangle
            gameDisplay.blit(levelstext, (310,280))#Image Blit
            questions_buttons(280,270,260,75, grey, action = 'levels')#Button


            #MainMenu Button
            pygame.draw.rect(gameDisplay, white, [300,360,220,55])#Draws a rectangle
            gameDisplay.blit(mainmtext, (310,365))#Image Blit
            questions_buttons(280,350,260,75, grey, action = 'mainm')#Button

            #Quit Button
            pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
            gameDisplay.blit(quittext, (340,440))#Image Blit
            questions_buttons(280,430,260,75, grey, action = 'quit')#Button
            pygame.display.update() #Updates the Display
        pygame.display.update() #Updates the Display
        clock.tick(fps) #Runs this function at the game FPS value
def message_to_screen_text_venus(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (320),(150)
    gameDisplay.blit(textSurf, textRect)#Image Blit

def message_to_screen_text_venus_score(msg, color):
    textSurf, textRect = text_objects(msg,color)
    textRect = (435),(150)
    gameDisplay.blit(textSurf, textRect)#Image Blit

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
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #If quit button clicked #If Someone clicks the QUIT (X) button gameExit is true and while loop will stop running
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
        pygame.display.update() #Updates the Display
        clock.tick(fps) #Runs this function at the game FPS value

def correct(): #Runs Correct Function:
    gameDisplay.fill(green) 
    gameDisplay.blit(correctimg, (250,150))#Image Blit
    pygame.display.update() #Updates the Display
    time.sleep(1) #Pauses the game for 1 seconds

def wrong(): #Runs Wrong Function:
    gameDisplay.fill(red) 
    gameDisplay.blit(wrongimg, (100,0))#Image Blit
    pygame.display.update() #Updates the Display
    time.sleep(1) #Pauses the game for 1 seconds

def trick(): #Runs trick Function:
    gameDisplay.blit(trickimg, (0,0))#Image Blit
    pygame.display.update() #Updates the Display
    time.sleep(1) #Pauses the game for 1 seconds

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
    cur = pygame.mouse.get_pos() #Gets Cursor Position
    click = pygame.mouse.get_pressed() #Checks for mouse click
    if x + width > cur[0] > x and y + height > cur[1] > y:#Checks if mouse position is over the button
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height)) #Draws a rectangle
        if click[0] == 1 and action != None: #If Button is clicked and action is not equal to nothing
            clickaudio.play() #Plays the Click audio
            time.sleep(0.5) #Pauses the game for 0.5 seconds
            if action == "thered1":
                wrong() #Runs Wrong Function
                mars_question3_run = True #Sets this question to have run
            if action == "theblue1":
                correct() #Runs Correct Function
                mars_score += 2 #Adds 2 to the planets score becuase each question is worth 2 in this quiz
                print(mars_score) #Prints the current score for this quiz
                mars_question3_run = True #Sets this question to have run
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
    cur = pygame.mouse.get_pos() #Gets Cursor Position
    click = pygame.mouse.get_pressed() #Checks for mouse click
    if x + width > cur[0] > x and y + height > cur[1] > y:#Checks if mouse position is over the button
        if click[0] == 1 and action != None: #If Button is clicked and action is not equal to nothing
            clickaudio.play() #Plays the Click audio
            time.sleep(0.5) #Pauses the game for 0.5 seconds
            if action == "windows1":
                wrong() #Runs Wrong Function
                earth_question1_run = True #Sets this question to have run
            if action == "linux1":
                correct() #Runs Correct Function
                earth_question1_run = True #Sets this question to have run
                earth_score += 1 #Adds 1 to the planets score
                print(earth_score) #Prints the current score for this quiz
            if action == "apple1":
                wrong() #Runs Wrong Function
                earth_question1_run = True #Sets this question to have run
            if action == "windows2":
                correct() #Runs Correct Function
                earth_question2_run = True #Sets this question to have run
                earth_score += 1 #Adds 1 to the planets score
                print(earth_score) #Prints the current score for this quiz
            if action == "linux2":
                wrong() #Runs Wrong Function
                earth_question2_run = True #Sets this question to have run
            if action == "apple2":
                wrong() #Runs Wrong Function
                earth_question2_run = True #Sets this question to have run
            if action == "windows3":
                wrong() #Runs Wrong Function
                earth_question3_run = True #Sets this question to have run
            if action == "linux3":
                wrong() #Runs Wrong Function
                earth_question3_run = True #Sets this question to have run
            if action == "apple3":
                correct() #Runs Correct Function
                earth_score += 1 #Adds 1 to the planets score
                print(earth_score) #Prints the current score for this quiz
                earth_question3_run = True #Sets this question to have run
            if action == "true1":
                wrong() #Runs Wrong Function
                earth_question4_run = True #Sets this question to have run
            if action == "false1":
                correct() #Runs Correct Function
                earth_score += 1 #Adds 1 to the planets score
                print(earth_score) #Prints the current score for this quiz
                earth_question4_run = True #Sets this question to have run
            if action == "red1":
                correct() #Runs Correct Function
                earth_score += 1 #Adds 1 to the planets score
                print(earth_score) #Prints the current score for this quiz
                earth_question5_run = True #Sets this question to have run
            if action == "orange1" or action == "yellow1" or action == "green1" or action == "blue1" or action == "pink1" or action == "purple1" or action == "white1":
                wrong() #Runs Wrong Function
                earth_question5_run = True #Sets this question to have run
            if action == "vr":
                correct() #Runs Correct Function
                earth_score += 1 #Adds 1 to the planets score
                print(earth_score) #Prints the current score for this quiz
                earth_question6_run = True #Sets this question to have run
            if action == "vr1" or action == "vr2":
                wrong() #Runs Wrong Function
                earth_question6_run = True #Sets this question to have run
            if action == "spacex":
                correct() #Runs Correct Function
                earth_score += 1 #Adds 1 to the planets score
                print(earth_score) #Prints the current score for this quiz
                earth_question7_run = True #Sets this question to have run
            if action == "apollox" or action == "nasa":
                wrong() #Runs Wrong Function
                earth_question7_run = True #Sets this question to have run
            if action == "windowsos":
                wrong() #Runs Wrong Function
                earth_question8_run = True #Sets this question to have run
            if action == "appleos":
                correct() #Runs Correct Function
                earth_score += 1 #Adds 1 to the planets score
                print(earth_score) #Prints the current score for this quiz
                earth_question8_run = True #Sets this question to have run
            if action == "flip":
                correct() #Runs Correct Function
                earth_score += 1 #Adds 1 to the planets score
                print(earth_score) #Prints the current score for this quiz
                earth_question9_run = True #Sets this question to have run
            if action == "2degrees" or action == "spark" or action == "slingshot" or action == "vodafone" or action == "trustpower":
                wrong() #Runs Wrong Function
                earth_question9_run = True #Sets this question to have run
            if action == "yes1" or action == "no1":
                trick() #Runs trick Function
                earth_score += 1 #Adds 1 to the planets score
                print(earth_score) #Prints the current score for this quiz
                earth_end = True
            if action == "restartearth":
                earth_question1_run = False #Sets this question run to False
                earth_question2_run = False #Sets this question run to False
                earth_question3_run = False #Sets this question run to False
                earth_question4_run = False #Sets this question run to False
                earth_question5_run = False #Sets this question run to False
                earth_question6_run = False #Sets this question run to False
                earth_question7_run = False #Sets this question run to False
                earth_question8_run = False #Sets this question run to False
                earth_question9_run = False #Sets this question run to False
                earth_question10_run = False #Sets this question run to False
                earth_end = False
                earth_score = 0 #Sets this Quizzes Score to 0
                earth_quiz()
            if action == "restartsun":
                sun_question1_run = False #Sets this question run to False
                sun_question2_run = False #Sets this question run to False
                sun_question3_run = False #Sets this question run to False
                sun_question4_run = False #Sets this question run to False
                sun_question5_run = False #Sets this question run to False
                sun_question6_run = False #Sets this question run to False
                sun_question7_run = False #Sets this question run to False
                sun_question8_run = False #Sets this question run to False
                sun_question9_run = False #Sets this question run to False
                sun_question10_run = False #Sets this question run to False
                sun_end = False
                sun_score = 0 #Sets this Quizzes Score to 0
                sun_quiz()
            if action == "restartvenus":
                venus_question1_run = False #Sets this question run to False
                venus_question2_run = False #Sets this question run to False
                venus_question3_run = False #Sets this question run to False
                venus_question4_run = False #Sets this question run to False
                venus_question5_run = False #Sets this question run to False
                venus_question6_run = False #Sets this question run to False
                venus_question7_run = False #Sets this question run to False
                venus_question8_run = False #Sets this question run to False
                venus_question9_run = False #Sets this question run to False
                venus_question10_run = False #Sets this question run to False
                venus_end = False
                venus_score = 0 #Sets this Quizzes Score to 0
                venus_quiz()
            if action == "restartmars":
                mars_question1_run = False #Sets this question run to False
                mars_question2_run = False #Sets this question run to False
                mars_question3_run = False #Sets this question run to False
                mars_question4_run = False #Sets this question run to False
                mars_question5_run = False #Sets this question run to False
                mars_question6_run = False #Sets this question run to False
                mars_question7_run = False #Sets this question run to False
                mars_question8_run = False #Sets this question run to False
                mars_question9_run = False #Sets this question run to False
                mars_question10_run = False #Sets this question run to False
                mars_end = False
                mars_score = 0 #Sets this Quizzes Score to 0
                mars_quiz()
            if action == "levels":
                earth_question1_run = False #Sets this question run to False
                earth_question2_run = False #Sets this question run to False
                earth_question3_run = False #Sets this question run to False
                earth_question4_run = False #Sets this question run to False
                earth_question5_run = False #Sets this question run to False
                earth_question6_run = False #Sets this question run to False
                earth_question7_run = False #Sets this question run to False
                earth_question8_run = False #Sets this question run to False
                earth_question9_run = False #Sets this question run to False
                earth_question10_run = False #Sets this question run to False
                earth_end = False
                earth_score = 0 #Sets this Quizzes Score to 0
                venus_question1_run = False #Sets this question run to False
                venus_question2_run = False #Sets this question run to False
                venus_question3_run = False #Sets this question run to False
                venus_question4_run = False #Sets this question run to False
                venus_question5_run = False #Sets this question run to False
                venus_question6_run = False #Sets this question run to False
                venus_question7_run = False #Sets this question run to False
                venus_question8_run = False #Sets this question run to False
                venus_question9_run = False #Sets this question run to False
                venus_question10_run = False #Sets this question run to False
                venus_end = False
                venus_score = 0 #Sets this Quizzes Score to 0
                sun_question1_run = False #Sets this question run to False
                sun_question2_run = False #Sets this question run to False
                sun_question3_run = False #Sets this question run to False
                sun_question4_run = False #Sets this question run to False
                sun_question5_run = False #Sets this question run to False
                sun_question6_run = False #Sets this question run to False
                sun_question7_run = False #Sets this question run to False
                sun_question8_run = False #Sets this question run to False
                sun_question9_run = False #Sets this question run to False
                sun_question10_run = False #Sets this question run to False
                sun_end = False
                sun_score = 0 #Sets this Quizzes Score to 0
                game_loop()
            if action == "mainm":
                earth_question1_run = False #Sets this question run to False
                earth_question2_run = False #Sets this question run to False
                earth_question3_run = False #Sets this question run to False
                earth_question4_run = False #Sets this question run to False
                earth_question5_run = False #Sets this question run to False
                earth_question6_run = False #Sets this question run to False
                earth_question7_run = False #Sets this question run to False
                earth_question8_run = False #Sets this question run to False
                earth_question9_run = False #Sets this question run to False
                earth_question10_run = False #Sets this question run to False
                earth_end = False
                earth_score = 0 #Sets this Quizzes Score to 0
                sun_question1_run = False #Sets this question run to False
                sun_question2_run = False #Sets this question run to False
                sun_question3_run = False #Sets this question run to False
                sun_question4_run = False #Sets this question run to False
                sun_question5_run = False #Sets this question run to False
                sun_question6_run = False #Sets this question run to False
                sun_question7_run = False #Sets this question run to False
                sun_question8_run = False #Sets this question run to False
                sun_question9_run = False #Sets this question run to False
                sun_question10_run = False #Sets this question run to False
                sun_end = False
                sun_score = 0 #Sets this Quizzes Score to 0
                
                main_menu() #Runs the main_menu() Function
            if action == "quit":
                pygame.quit() #Quits
                quit() #Quits
            if action == "planet":
                wrong() #Runs Wrong Function
                sun_question1_run = True #Sets this question to have run
            if action == "star":
                correct() #Runs Correct Function
                sun_score += 1 #Adds 1 to the planets score
                print(sun_score) #Prints the current score for this quiz
                sun_question1_run = True #Sets this question to have run

            if action == "armstrong": #Who was first on the moon (Neil 'Armstrong')
                correct() #Runs Correct Function             #Runs the correct() #Runs Correct Function function  
                sun_score += 1 #Adds 1 to the planets score        #Adds 1 to the score 
                print(sun_score) #Prints the current score for this quiz      
                sun_question2_run = True #Sets this question to have run #Sets this question to have run
            if action == "chris":
                wrong() #Runs Wrong Function
                sun_question2_run = True #Sets this question to have run
            if action == "collins":
                wrong() #Runs Wrong Function
                sun_question2_run = True #Sets this question to have run

            if action == "apollo11":
                correct() #Runs Correct Function
                sun_score += 1 #Adds 1 to the planets score
                print(sun_score) #Prints the current score for this quiz
                sun_question3_run = True #Sets this question to have run
            if action == "atlantis":
                wrong() #Runs Wrong Function
                sun_question3_run = True #Sets this question to have run
            if action == "columbia":
                wrong() #Runs Wrong Function
                sun_question3_run = True #Sets this question to have run
            if action == "saturnv":
                correct() #Runs Correct Function
                sun_score += 1 #Adds 1 to the planets score
                print(sun_score) #Prints the current score for this quiz
                sun_question4_run = True #Sets this question to have run
            if action == "aresv":
                wrong() #Runs Wrong Function
                sun_question4_run = True #Sets this question to have run
            if action == "james1":
                correct() #Runs Correct Function
                sun_score += 1 #Adds 1 to the planets score
                print(sun_score) #Prints the current score for this quiz
                sun_question5_run = True #Sets this question to have run
            if action == "collins1":
                wrong() #Runs Wrong Function
                sun_question5_run = True #Sets this question to have run
            if action == "chris1":
                wrong() #Runs Wrong Function
                sun_question5_run = True #Sets this question to have run
            if action == 'num1' or action == 'num3' or action == 'num4' or action == 'num5':
                wrong() #Runs Wrong Function
                sun_question6_run = True #Sets this question to have run
            if action == "num2":
                correct() #Runs Correct Function
                sun_score += 1 #Adds 1 to the planets score
                print(sun_score) #Prints the current score for this quiz
                sun_question6_run = True #Sets this question to have run
            if action == "yes2":
                correct() #Runs Correct Function
                sun_score += 1 #Adds 1 to the planets score
                print(sun_score) #Prints the current score for this quiz
                sun_question7_run = True #Sets this question to have run
            if action == "no2":
                wrong() #Runs Wrong Function
                sun_question7_run = True #Sets this question to have run
            if action == "jupitertxt":
                correct() #Runs Correct Function
                sun_score += 1 #Adds 1 to the planets score
                print(sun_score) #Prints the current score for this quiz
                sun_question8_run = True #Sets this question to have run
            if action == "earthtxt" or action == "marstxt" or action == "venustxt":
                wrong() #Runs Wrong Function
                sun_question8_run = True #Sets this question to have run
            if action == "mercurytxt1":
                correct() #Runs Correct Function
                sun_score += 1 #Adds 1 to the planets score
                print(sun_score) #Prints the current score for this quiz
                sun_question9_run = True #Sets this question to have run
            if action == "earthtxt1" or action == "marstxt1" or action == "venustxt1":
                wrong() #Runs Wrong Function
                sun_question9_run = True #Sets this question to have run
                sun_end = True
            if action == "infinity" or action == "mean42" or action == "elseimg":
                trick() #Runs trick Function
                sun_score += 1 #Adds 1 to the planets score
                print(sun_score) #Prints the current score for this quiz
                sun_question10_run = True #Sets this question to have run
                sun_end = True
            if action == "wyrleft1" or action == "wyrright1":
                trick() #Runs trick Function
                moon_score += 1 #Adds 1 to the planets score
                print(moon_score) #Prints the current score for this quiz
                moon_question1_run = True #Sets this question to have run
            if action == "wyrleft2" or action == "wyrright2":
                trick() #Runs trick Function
                moon_score += 1 #Adds 1 to the planets score
                print(moon_score) #Prints the current score for this quiz
                moon_question2_run = True #Sets this question to have run
            if action == "wyrleft3" or action == "wyrright3":
                trick() #Runs trick Function
                moon_score += 1 #Adds 1 to the planets score
                print(moon_score) #Prints the current score for this quiz
                moon_question3_run = True #Sets this question to have run
            if action == "wyrleft4" or action == "wyrright4":
                trick() #Runs trick Function
                moon_score += 1 #Adds 1 to the planets score
                print(moon_score) #Prints the current score for this quiz
                moon_question4_run = True #Sets this question to have run
            if action == "wyrleft5" or action == "wyrright5":
                trick() #Runs trick Function
                moon_score += 1 #Adds 1 to the planets score
                print(moon_score) #Prints the current score for this quiz
                moon_question5_run = True #Sets this question to have run
            if action == "wyrleft6" or action == "wyrright6":
                trick() #Runs trick Function
                moon_score += 1 #Adds 1 to the planets score
                print(moon_score) #Prints the current score for this quiz
                moon_question6_run = True #Sets this question to have run
            if action == "wyrleft7" or action == "wyrright7":
                trick() #Runs trick Function
                moon_score += 1 #Adds 1 to the planets score
                print(moon_score) #Prints the current score for this quiz
                moon_question7_run = True #Sets this question to have run
            if action == "wyrleft8" or action == "wyrright8":
                trick() #Runs trick Function
                moon_score += 1 #Adds 1 to the planets score
                print(moon_score) #Prints the current score for this quiz
                moon_question8_run = True #Sets this question to have run
            if action == "wyrleft9" or action == "wyrright9":
                trick() #Runs trick Function
                moon_score += 1 #Adds 1 to the planets score
                print(moon_score) #Prints the current score for this quiz
                moon_question9_run = True #Sets this question to have run
            if action == "wyrleft10" or action == "wyrright10":
                trick() #Runs trick Function
                moon_score += 1 #Adds 1 to the planets score
                print(moon_score) #Prints the current score for this quiz
                moon_end = True

            if action == "true2":
                wrong() #Runs Wrong Function
                venus_question1_run = True #Sets this question to have run
            if action == "false2":
                correct() #Runs Correct Function
                venus_score += 1 #Adds 1 to the planets score
                print(venus_score) #Prints the current score for this quiz
                venus_question1_run = True #Sets this question to have run
            if action == "true3":
                wrong() #Runs Wrong Function
                venus_question2_run = True #Sets this question to have run
            if action == "false3":
                correct() #Runs Correct Function
                venus_score += 1 #Adds 1 to the planets score
                print(venus_score) #Prints the current score for this quiz
                venus_question2_run = True #Sets this question to have run
            if action == "false4":
                wrong() #Runs Wrong Function
                venus_question3_run = True #Sets this question to have run
            if action == "true4":
                correct() #Runs Correct Function
                venus_score += 1 #Adds 1 to the planets score
                print(venus_score) #Prints the current score for this quiz
                venus_question3_run = True #Sets this question to have run
            if action == "true5":
                wrong() #Runs Wrong Function
                venus_question4_run = True #Sets this question to have run
            if action == "false5":
                correct() #Runs Correct Function
                venus_score += 1 #Adds 1 to the planets score
                print(venus_score) #Prints the current score for this quiz
                venus_question4_run = True #Sets this question to have run
            if action == "true6":
                wrong() #Runs Wrong Function
                venus_question5_run = True #Sets this question to have run
            if action == "false6":
                correct() #Runs Correct Function
                venus_score += 1 #Adds 1 to the planets score
                print(venus_score) #Prints the current score for this quiz
                venus_question5_run = True #Sets this question to have run
            if action == "false7":
                wrong() #Runs Wrong Function
                venus_question6_run = True #Sets this question to have run
            if action == "true7":
                correct() #Runs Correct Function
                venus_score += 1 #Adds 1 to the planets score
                print(venus_score) #Prints the current score for this quiz
                venus_question6_run = True #Sets this question to have run
            if action == "false8":
                wrong() #Runs Wrong Function
                venus_question7_run = True #Sets this question to have run
            if action == "true8":
                correct() #Runs Correct Function
                venus_score += 1 #Adds 1 to the planets score
                print(venus_score) #Prints the current score for this quiz
                venus_question7_run = True #Sets this question to have run
            if action == "false9":
                wrong() #Runs Wrong Function
                venus_question8_run = True #Sets this question to have run
            if action == "true9":
                correct() #Runs Correct Function
                venus_score += 1 #Adds 1 to the planets score
                print(venus_score) #Prints the current score for this quiz
                venus_question8_run = True #Sets this question to have run
            if action == "true10":
                wrong() #Runs Wrong Function
                venus_question9_run = True #Sets this question to have run
            if action == "false10":
                correct() #Runs Correct Function
                venus_score += 1 #Adds 1 to the planets score
                print(venus_score) #Prints the current score for this quiz
                venus_question9_run = True #Sets this question to have run
            if action == "false11":
                wrong() #Runs Wrong Function
                venus_question10_run = True #Sets this question to have run
                venus_end = True
            if action == "true11":
                correct() #Runs Correct Function
                venus_score += 1 #Adds 1 to the planets score
                print(venus_score) #Prints the current score for this quiz
                venus_question10_run = True #Sets this question to have run
                venus_end = True

            if action == 'nova' or action == 'poru':
                wrong() #Runs Wrong Function
                uranus_question1_run = True #Sets this question to have run
            if action == 'porg':
                correct() #Runs Correct Function
                uranus_score += 1 #Adds 1 to the planets score
                print(uranus_score) #Prints the current score for this quiz
                uranus_question1_run = True #Sets this question to have run

            if action == 'yodu' or action == 'yanna' or action == "yodan":
                wrong() #Runs Wrong Function
                uranus_question2_run = True #Sets this question to have run
            if action == 'yaddle':
                correct() #Runs Correct Function
                uranus_score += 1 #Adds 1 to the planets score
                print(uranus_score) #Prints the current score for this quiz
                uranus_question2_run = True #Sets this question to have run
            if action == 'kyba' or action == 'kybar' or action == "kybur":
                wrong() #Runs Wrong Function
                uranus_question3_run = True #Sets this question to have run
            if action == 'kyber':
                correct() #Runs Correct Function
                uranus_score += 1 #Adds 1 to the planets score
                print(uranus_score) #Prints the current score for this quiz
                uranus_question3_run = True #Sets this question to have run
            if action == 'luke1' or action == 'yoda1':
                wrong() #Runs Wrong Function
                uranus_question4_run = True #Sets this question to have run
            if action == 'anakin1':
                correct() #Runs Correct Function
                uranus_score += 1 #Adds 1 to the planets score
                print(uranus_score) #Prints the current score for this quiz
                uranus_question4_run = True #Sets this question to have run

            if action == 'luke2' or action == 'yoda2':
                wrong() #Runs Wrong Function
                uranus_question5_run = True #Sets this question to have run
            if action == 'leia2':
                correct() #Runs Correct Function
                uranus_score += 1 #Adds 1 to the planets score
                print(uranus_score) #Prints the current score for this quiz
                uranus_question5_run = True #Sets this question to have run
            if action == 'anewhope' or action == 'thelastjedi':
                wrong() #Runs Wrong Function
                uranus_question6_run = True #Sets this question to have run
            if action == 'returnofthejedi':
                correct() #Runs Correct Function
                uranus_score += 1 #Adds 1 to the planets score
                print(uranus_score) #Prints the current score for this quiz
                uranus_question6_run = True #Sets this question to have run
            if action == 'r2d2' or action == 'c3po':
                wrong() #Runs Wrong Function
                uranus_question7_run = True #Sets this question to have run
            if action == 'bb8':
                correct() #Runs Correct Function
                uranus_score += 1 #Adds 1 to the planets score
                print(uranus_score) #Prints the current score for this quiz
                uranus_question7_run = True #Sets this question to have run
            if action == 'bud' or action == 'john':
                wrong() #Runs Wrong Function
                uranus_question8_run = True #Sets this question to have run
            if action == 'finn':
                correct() #Runs Correct Function
                uranus_score += 1 #Adds 1 to the planets score
                print(uranus_score) #Prints the current score for this quiz
                uranus_question8_run = True #Sets this question to have run
            if action == 'enterprise' or action == 'xwing':
                wrong() #Runs Wrong Function
                uranus_question9_run = True #Sets this question to have run
            if action == 'falcon':
                correct() #Runs Correct Function
                uranus_score += 1 #Adds 1 to the planets score
                print(uranus_score) #Prints the current score for this quiz
                uranus_question9_run = True #Sets this question to have run
            if action == 'jedi':
                trick() #Runs trick Function
                uranus_score += 1 #Adds 1 to the planets score
                print(uranus_score) #Prints the current score for this quiz
                uranus_question10_run = True #Sets this question to have run
                uranus_end = True
            if action == 'a':
                correct() #Runs Correct Function
                mars_score += 2 #Adds 2 to the planets score becuase each question is worth 2 in this quiz
                print(mars_score) #Prints the current score for this quiz
                mars_question1_run = True #Sets this question to have run
            if action == 'q':
                wrong() #Runs Wrong Function
                mars_question1_run = True #Sets this question to have run
            if action == 'yesrect':
                correct() #Runs Correct Function
                mars_score += 2 #Adds 2 to the planets score becuase each question is worth 2 in this quiz
                print(mars_score) #Prints the current score for this quiz
                mars_question2_run = True #Sets this question to have run
            if action == 'norect':
                wrong() #Runs Wrong Function
                mars_question2_run = True #Sets this question to have run
            if action == 'click':
                correct() #Runs Correct Function
                mars_score += 2 #Adds 2 to the planets score becuase each question is worth 2 in this quiz
                print(mars_score) #Prints the current score for this quiz
                mars_question4_run = True #Sets this question to have run
            if action == 'dontclick':
                wrong() #Runs Wrong Function
                mars_question4_run = True #Sets this question to have run
            if action == "justclick":
                correct() #Runs Correct Function
                mars_score += 2 #Adds 2 to the planets score becuase each question is worth 2 in this quiz
                print(mars_score) #Prints the current score for this quiz
                mars_question5_run = True #Sets this question to have run
                mars_end = True
            if action == 'albert' or action == 'ben':
                wrong() #Runs Wrong Function
                jupiter_question1_run = True #Sets this question to have run
            if action == "thomas":
                correct() #Runs Correct Function
                jupiter_score += 1 #Adds 1 to the planets score
                print(jupiter_score) #Prints the current score for this quiz
                jupiter_question1_run = True #Sets this question to have run
            if action == 'silver' or action == 'argon':
                wrong() #Runs Wrong Function
                jupiter_question2_run = True #Sets this question to have run
            if action == "gold":
                correct() #Runs Correct Function
                jupiter_score += 1 #Adds 1 to the planets score
                print(jupiter_score) #Prints the current score for this quiz
                jupiter_question2_run = True #Sets this question to have run
            if action == 'gamma1' or action == 'gamma2' or action == 'gamma4' or action == 'gamma5':
                wrong() #Runs Wrong Function
                jupiter_question3_run = True #Sets this question to have run
            if action == "gamma3":
                correct() #Runs Correct Function
                jupiter_score += 1 #Adds 1 to the planets score
                print(jupiter_score) #Prints the current score for this quiz
                jupiter_question3_run = True #Sets this question to have run
def coming_soon(): #If The quiz is Coming Soon
    gameDisplay.blit(bg, (0,0)) #Background
    gameDisplay.blit(coming, (100,0))#Image Blit
    gameDisplay.blit(smiley, (220,90))#Image Blit
    pygame.draw.rect(gameDisplay, white, [300,440,220,55])#Draws a rectangle
    gameDisplay.blit(backtext, (340,440))#Image Blit
    back_button(280,430,260,75, grey, action = 'backtolevels')#Button
age()#Checks user age
game_loop()   #Will run gameloop firstly
pygame.quit() #Quits #Will Quit Game if the game_loop is escaped
quit() #Quits        
