'''
    This file contains bomb class definition and its working
    Also a README is specified that contains all salient features of the implementation.
'''

from __future__ import print_function
import signal
import copy
import sys
import time
from random import randint
import os
from termcolor import colored

'''Importing modules from other files'''
from bomber import *
from suplement import *


class Bomb(Bomber):
    '''docstring for Bomb'''
    '''The bomb class "inherits"  the features of Bomber Class like setPositon ,getPosition etc'''

    def __init__(self, x, y):
        self.position = [x, y]
        self.shape = [['<',  ' ',  ' ',  '>'], ['<',  ' ',  ' ',  '>']]
        self.time = 4
        self.status = 0
        self.planted = 1
        #defining the initials for bomb man like shape, time to go off
        #The planted property checks if the bomb has been planted yet and checks that bombCount doesn't become more than 1

    def Make_Bomb(self):
        if self.status == 1:
            [x, y] = self.GetPosition()
            self.planted = 0
            for i in range(4):
                a[y][i + x] = self.shape[0][i]
                a[y+1][i + x] = self.shape[1][i]

    def GetTime(self):
        return self.time

    def SetTime(self, time):
        self.time = time
        self.shape = [['<', chr(48 + self.time), chr(48 + self.time), '>'], ['<', chr(48 + self.time), chr(48 + self.time), '>']]

    def Explosion(self, x, y, sy):
        #makes the explosion of symbol sy
        if a[y][x] != 'X':
            for i in range(4):
                a[y][x + i] = sy
                a[y + 1][x + i] = sy

    def Remove_Bomb(self):
        #After explosion the bomb is removed and its values are reset
        [x, y] = self.GetPosition()
        for i in range(4):
            a[y][i + x] = ' '
            a[y+1][i+x] = ' '
        self.SetTime(4)
        self.status = 0
        self.planted = 1

    def Explode(self, sy):
        self.time = self.SetTime(self.time-1)
        [x, y] = self.GetPosition()
        self.Explosion(x + 4, y, sy)
        self.Explosion(x - 4, y, sy)
        self.Explosion(x, y - 2, sy)
        self.Explosion(x, y + 2, sy)


'''
    Class definition DONE!
'''
