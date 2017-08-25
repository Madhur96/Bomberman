'''
    This file contains bomber class definition and its working
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
from suplement import *


class Bomber(object):
    '''docstring for Bomber'''
    '''You can get idea of most functions just by their names.'''

    def __init__(self):
        self.shape = [['B', 'B',  'B',  'B'], ['B',  'B',  'B',  'B']]
        self.position = [2, 2]
        self.lives = 2
        self.existance = 1
        #defining the initials for bomber man like shape, lives
        #The existance property checks whether the character is alive of dead at a moment and calls the function accordingly

    def SetPosition(self, x, y):
        self.position = [x, y]

    def GetPosition(self):
        return self.position

    def GetLives(self):
        return self.lives

    def SetLives(self, num):
        self.lives = num

    def SetExistance(self, x):
        self.existance = x

    def Make_Bomber(self):
    #creating/drawing the bomberman at [x, y] co-ordinate
        if self.existance:
            [x, y] = self.GetPosition()
            if a[y][x] != ' ':
                pass
            else:
                for i in range(4):
                    a[y][i + x] = self.shape[0][i]
                    a[y + 1][i + x] = self.shape[1][i]

    def Remove_Bomber(self):
    #removing/erasing character from its original position
        [x, y] = self.GetPosition()
        for i in range(4):
            a[y][i + x] = ' '
            a[y + 1][i + x] = ' '

    #defining the movemont features for character(s)
    def Move_Right(self):
        flag = 1
        [x, y] = self.GetPosition()
        if(a[y][x+4] == 'X' or a[y][x+4] == '/'):
            flag = 0
        if flag:
            self.SetPosition(x+4, y)
        else:
            self.SetPosition(x, y)
            return 1

    def Move_Left(self):
        flag = 1
        [x, y] = self.GetPosition()
        if(a[y][x-4] == 'X' or a[y][x-4] == '/'):
            flag = 0
        if flag:
            self.SetPosition(x-4, y)
        else:
            self.SetPosition(x, y)
            return 1

    def Move_Up(self):
        flag = 1
        [x, y] = self.GetPosition()

        if(a[y-2][x] == 'X' or a[y-2][x] == '/'):
            flag = 0
        if flag:
            self.SetPosition(x, y-2)
        else:
            self.SetPosition(x, y)
            return 1

    def Move_Down(self):
        flag = 1
        [x, y] = self.GetPosition()
        if(a[y+2][x] == 'X' or a[y+2][x] == '/'):
            flag = 0
        if flag:
            self.SetPosition(x, y+2)
        else:
            self.SetPosition(x, y)
            return 1

    def Death(self):
        self.SetExistance(0)

    def Respawn(self):
        self.SetPosition(2, 2)
        self.SetExistance(1)

'''
    Class definition DONE!
'''
