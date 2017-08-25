'''
    This file contains enemy class definition and its working
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

'''Importing features from other files'''
from bomber import *
from suplement import *


class Enemy(Bomber):
    '''docstring for Enemy'''
    '''The enemy class "inherits"  the features of Bomber Class like death ,movement etc'''
    def __init__(self):
        self.shape = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]
        self.position = [2, 10]
        self.count = 2
        self.existance = 1
        #defining the initials for  enemy like shape, position

    def Random(self, num):
        #generates a random number and on the basis of num generated the enemy decides a random direction to move
        if(self.existance):
            if num == 0:
                return self.Move_Up()
            if num == 1:
                return self.Move_Down()
            if num == 2:
                return self.Move_Left()
            if num == 3:
                return self.Move_Right()

    def Movement(self):
        # The movement part for the enemy is decided by this function , it takes care that if given direction has a wall then not to go
        if(self.existance):
            flag = 1
            arr = []
            while flag:
                num = randint(0, 4)
                t = self.Random(num)
                if (t != 1 and num not in arr):
                    flag = 0
                else:
                    arr.append(num)

    def Make_Enemy(self):
        #Helps in making (mind not printing) of enemy at a random location
        ex = randint(2, 37)
        ey = randint(2, 77)
        if(ey % 4 == 2 and ex % 2 == 0):

            if(a[ex][ey] == ' ' and a[ex][ey + 1] == ' '):
                a[ex][ey] = 'E'
                a[ex][ey+1] = 'E'
                a[ex][ey+2] = 'E'
                a[ex][ey+3] = 'E'
                a[ex+1][ey+1] = 'E'
                a[ex+1][ey+2] = 'E'
                a[ex+1][ey+3] = 'E'
                a[ex+1][ey] = 'E'
                global enemy_flag
                enemy_flag = 0
                self.SetPosition(ey, ex)

            else:
                global enemy_flag
                enemy_flag = 1

        else:
            global enemy_flag
            enemy_flag = 1

    def Remove_Enemy(self):
        [x, y] = self.GetPosition()
        for i in range(4):
            a[y][i + x] = ' '
            a[y+1][i + x] = ' '

    def IsDead(self):
        #Just a flag function used to check if enemy is dead or not
        if (not self.existance):
            return 1
        return 0

'''
    Class definition DONE!
'''
