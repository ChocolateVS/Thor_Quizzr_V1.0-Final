'''
Welcome to the File Opening Test Program
This Program open a file an reads it and if the value read
is less than earth_earth score it will be written to the file
This is a SHELL Test and does not a use pygame window

'''
import random
import time
import pygame

def loop():
    loopexit = False #Loop Exit is False
    while not loopexit: #While the loop hasnt exit
        earth_score = random.randrange(0,11) #Earth Score is equal to a value between 1 and 11
        print("The New Random Value is: ", earth_score)
        with open("earthscore.txt", 'r') as f: #Opens this file for reading
            for old_score in f:
                print("Current Reading in file is: ", old_score)
                int(earth_score)
                int(old_score)
            
        if earth_score > old_score:
            print("The Old Score is less than the Random value")
            with open("earthscore.txt", 'w') as f: #Opens this file for writing
                f.write(earth_score)
                print("New Score: ", earth_score)
                    
        elif earth_score < old_score:
            print("The value is less than earth_score")
            print("Random Value", earth_score)
            print("Old Score", old_score)
            print(" ")
        time.sleep(2) #Delay 2 seconds
 
loop()
quit()
    
    




