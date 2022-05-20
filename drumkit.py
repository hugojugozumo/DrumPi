#-----------------------------------------------------------------------
# File : drumkit.py
#
# Programmer: Hugo Davalos
#
# Program #: Defines the drum kit class and methods for setting sounds 
#
# Due Date: 05/01/22
#
# Course: EGRE 347, Spring 2022
# 
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: Uses pygame's mixer to set the sounds for each element of the kit
# makes my main.py code a lot less cluttered
#
#-----------------------------------------------------------------------


#Pygame displays a message everytime you import, this chunk of code supresses that
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame 

# Description of Pygame mixer:
#   Each sound is loaded onto the pygame "mixer" object and a "sound" object 
#   This means that each sound is sent to a master track to be mixed with other incoming sounds before being played
#   I chose the pygame library for this reason specifically
#   In all other libraries, if a sound was triggered, all other sounds would have to "wait in line" for the current sound to finish playing 
#   (i.e "playsound" and python's native sound player)

class dkit:

    #hopefully we never actually get here, but just in case, I have it play a little error sound
    def __init__(self):
        self.kick = pygame.mixer.Sound('error.wav')
        self.snare = pygame.mixer.Sound('error.wav')
        self.chihat = pygame.mixer.Sound('error.wav')
        self.ohihat = pygame.mixer.Sound('error.wav')
        self.flrtom = pygame.mixer.Sound('error.wav')
        self.ride = pygame.mixer.Sound('error.wav')
        self.crash = pygame.mixer.Sound('error.wav')

    #sets the electric kit sounds
    def set_elec(self):
        self.dkkick = pygame.mixer.Sound('elec_kick.wav')
        self.snare = pygame.mixer.Sound('elec_snare.wav')
        self.chihat = pygame.mixer.Sound('elec_high_closed.wav')
        self.ohihat = pygame.mixer.Sound('elec_open_hat.wav')
        self.flrtom = pygame.mixer.Sound('tom_elec.wav')
        self.ride = pygame.mixer.Sound('elec_ride.wav')
        self.crash = pygame.mixer.Sound('crash_elec.wav')

    #sets the acoustic kit sounds
    def set_acous(self):
        self.kick = pygame.mixer.Sound('Kick.wav')
        self.snare = pygame.mixer.Sound('snare.wav')
        self.chihat = pygame.mixer.Sound('closed_high_hat.wav')
        self.ohihat = pygame.mixer.Sound('open_high_hat.wav')
        self.flrtom = pygame.mixer.Sound('floortom.wav')
        self.ride = pygame.mixer.Sound('ride.wav')
        self.crash = pygame.mixer.Sound('crash.wav')