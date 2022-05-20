#-----------------------------------------------------------------------
# File : drumPi.py
#
# Programmer: Hugo Davalos
#
# Program #: The main script for my drum machine
#
# Due Date: 04/18/22
#
# Course: EGRE 347, Spring 2022
# 
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: Contains the menu, the button input, and implementation for the drum machine
#
#-----------------------------------------------------------------------

#used for sleep function
import time

#for keyboard input
import tty, sys, termios
filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)

#Pygame displays a message everytime you import, this chunk of code supresses that
import os
from xml.dom import pulldom
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame 

#contains my class for the drumkit
import drumkit
from drumkit import dkit

#pin constants
BLUE = 27
RED = 24
YELLOW = 5
GREEN = 16

#Import GPIO 
import RPi.GPIO as GPIO
GPIO.setwarnings(False) #disables warnings
GPIO.setmode(GPIO.BCM)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

pygame.init() 
pygame.mixer.init() #initializes the mixer

vinp = False #checks to make sure user input correct option
menu = False
kit_name = ""
Running = True

kit = dkit()

#blink LED twice
def blink2x(PIN):
    GPIO.output(PIN,1)
    time.sleep(0.5)
    GPIO.output(PIN,0)
    time.sleep(0.5)
    GPIO.output(PIN,1)
    time.sleep(0.5)
    GPIO.output(PIN,0)



print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("   Welcome to DrumPi 0.1.1!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

kit_LED = 0 #will show user what mode they're in with LED

# loop to run drum machine
while Running == True:
    menu = False #menu sentinel
    GPIO.output(GREEN,1)
    GPIO.output(BLUE,0)
    GPIO.output(YELLOW,0)
    GPIO.output(RED,0)
    

    while vinp == False: 
        print("Please select kit.") 
        print("Enter \"A\" for acoustic kit, enter \"E\" for electronic kit, or enter \"Q\" to quit: ") 
        kit_LED = 0
        kit_select = input()
        if kit_select == 'A' or kit_select == 'a':
            #acoustic kit, loads from acous_kit file 
            kit.set_acous()
            vinp = True
            kit_name = "Acoustic"
            GPIO.output(YELLOW,1)
        elif kit_select == 'E' or kit_select == 'e':
            #electric kit, loads from elec_kit file
            kit.set_elec()
            blink2x(BLUE)
            vinp = True
            kit_name = "Electronic"
            GPIO.output(BLUE,0)
        elif kit_select == 'Q' or kit_select == 'q':
            blink2x(RED)
            blink2x(RED)
            menu = True
            vinp = True
            Running = False
        else:
            print("[invalid input]")
            vinp = False
    
    
    GPIO.output(GREEN,0)


    if menu == False:
        print("\nloading...\n") #not actually loading anything, but I felt it made the program look better
        time.sleep(1)

        print("-----------------------------------------------------")
        print(f'\tYou have chosen the {kit_name} drum kit!')
        print("If you'd like to go back to the main menu, press 'q'.")
        print("-----------------------------------------------------")    
    
    while menu == False:
        key = 0
        key=sys.stdin.read(1)[0]
        if key == 'a':
            kit.kick.play()
        if key == 's':
            kit.snare.play()
        if key == 't':
            kit.chihat.play()
        if key == 'y':
            kit.ohihat.play()
        if key == 'u':
            kit.ride.play()
        if key == 'g':
            kit.crash.play()
        if key == 'f':
            kit.flrtom.play()
        if key == 'q':
            menu = True
            vinp = False

GPIO.output(RED,0)
GPIO.output(GREEN,0)
GPIO.output(YELLOW,0)
GPIO.output(BLUE,0)
GPIO.cleanup()

print("       --------------")
print("       |  Goodbye!  |")
print("       --------------")

    
