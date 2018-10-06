'''
    This is the main working code that inherits the classes from the
    enemy.py + bomb.py + bomber.py + suplement.py and uses them with an object instantiated
'''


from __future__ import print_function
import signal
import copy
import sys
import time
from random import randint
import os
from termcolor import colored

''' importing classes and their functions in the main file'''
from bomber import Bomber
from bomb import Bomb
from enemy import Enemy
from suplement import *


#-----------------------------------------------------------------------------------------------

global enemy_flag
enemy_flag = 1

global brick_flag
brick_flag = 1
#Two flags to keep a check on exsitance of the bricks and enemies


def Make_Walls():
    ''' The function generates the wall on the screen at a regular interval of 4x2 block'''
    for x in range(h):
        for y in range(w):
            if ((y-2) % 8 == 4 or (y-2) % 8 == 5 or (y-2) % 8 == 6 or (y-2) % 8 == 7):
                a[x][y] = 'X'
            if ((x) % 4 == 2 or (x) % 4 == 3):
                a[x][y] = ' '
            if (x == 0 or x == 1 or x == h-1 or x == h-2):
                a[x][y] = 'X'
            if (y == 0 or y == 1 or y == w-1 or y == w-2):
                a[x][y] = 'X'


def Make_Bricks():
    '''The function when called creates a brick randomly on the board (if possible) '''

    brick = [['/' for x in range(2)] for y in range(4)]
    bx = randint(2, 37)
    by = randint(2, 77)
    if (by % 4 == 2 and bx % 2 == 0):

        if(a[bx][by] == ' ' and a[bx][by + 1] == ' '):
            a[bx][by] = '/'
            a[bx][by + 1] = '/'
            a[bx][by + 2] = '/'
            a[bx][by + 3] = '/'
            a[bx + 1][by + 1] = '/'
            a[bx + 1][by + 2] = '/'
            a[bx + 1][by + 3] = '/'
            a[bx + 1][by] = '/'
            global brick_flag
            brick_flag = 0

        else:
            global brick_flag
            brick_flag = 1

    else:
        global brick_flag
        brick_flag = 1


#-----------------------------------------------------------------------------------------------------------------
''' Creating objects from their classes '''

bomber1 = Bomber()
bomb1 = Bomb(2, 2)
bomb1.status = 0

enemy1 = Enemy()
enemy2 = Enemy()

#-------------------------------------------------------------------------------------------------------------------
'''creating 2 enemies at random place on the board '''

global enemy_flag
enemy_flag = 0
enemy1.Make_Enemy()
while(enemy_flag):
    enemy1.Make_Enemy()
enemy2.Make_Enemy()
while(enemy_flag):
    enemy2.Make_Enemy()

#----------------------------------------------------------------------------------------------------------------------


def Make_All():
    '''The most important function , it prints the whole board , score and Lives left when called'''

    bomber1.Make_Bomber()
    os.system('tput reset')
    for x in range(h):
        for y in range(w):
            if a[x][y] == '/':
                print(colored(a[x][y], 'yellow'), end='')

            elif a[x][y] == 'B':
                print(colored(a[x][y], 'blue'), end='')

            elif a[x][y] == 'E':
                print(colored(a[x][y], 'red'), end='')

            elif a[x][y] == '*':
                print(colored(a[x][y], 'green'), end='')

            else:
                print(a[x][y], end='')
        print()
    print("Lives : ", bomber1.GetLives())
    print('score : ', score)
#-------------------------------------------------------------------------------------------------------------------

Make_Walls()
Make_All()


def Create_brick():
    ''' Some line of code to create bricks as they can only be created after creation of board '''
    for i in range(22):
        global brick_flag
        brick_flag = 0
        Make_Bricks()
        while(brick_flag):
            Make_Bricks()

Create_brick()
#----------------------------------------------------------------------------------------------------------------


def Intersection():
    ''' The code checks the intersection of position of enemy and the bomberman'''

    en = enemy1.GetPosition()
    bb = bomber1.GetPosition()
    en2 = enemy2.GetPosition()
    if ((en[0] == bb[0]) and (en[1] == bb[1]) and not enemy1.IsDead()):
        return 1

    if ((en2[0] == bb[0]) and (en2[1] == bb[1]) and not enemy2.IsDead()):
        return 1

#------------------------------------------------------------------------------------------------------------------------


'''The infinite loop , the main frame changer per move '''

while(1):

    inp = input_to()
    #printing of enemies on board
    enemy1.Remove_Enemy()
    enemy1.Movement()
    enemy1.GetPosition()
    enemy1.Make_Bomber()
    enemy2.Remove_Enemy()
    enemy2.Movement()
    enemy2.GetPosition()
    enemy2.Make_Bomber()

    #defining responses on key pressing
    if(inp == 'q'):
        sys.exit(0)

    if(inp == 'd'):
        bomber1.Remove_Bomber()
        bomber1.Move_Right()

    if(inp == 'a'):
        bomber1.Remove_Bomber()
        bomber1.Move_Left()

    if(inp == 's'):
        bomber1.Remove_Bomber()
        bomber1.Move_Down()

    if(inp == 'w'):
        bomber1.Remove_Bomber()
        bomber1.Move_Up()

    if(inp == 'b'):
        [p, q] = bomber1.GetPosition()
        if bomb1.planted:
            bomb1.SetPosition(p, q)

            bomb1.status = 1
            bomb1.planted = 0
            bomb1.Make_Bomb()

    en = enemy1.GetPosition()
    bb = bomber1.GetPosition()
    en2 = enemy2.GetPosition()
    if bomb1.status == 1:
        bomb1.SetTime(bomb1.GetTime()-1)
        bomb1.Make_Bomb()
        #calling bomb explosion
        if bomb1.GetTime() == 1:
            bomb1.status = 2
            bomb1.Explode('*')
            r = bomb1.GetPosition()
            # checking if any of enemy or bomberman himself collides with the bomb explosion
            if ((r[0] == en[0] and r[1] == en[1])
              or
               (r[0] + 4 == en[0] and r[1] == en[1])
              or
               (r[0] - 4 == en[0] and r[1]==en[1])
              or
               (r[0] == en[0] and r[1] - 2 == en[1])
              or
               (r[0] == en[0] and r[1] + 2 == en[1])): 
                if not enemy1.IsDead():
                    enemy1.Death()
                    score += 100

            if ((r[0] == en2[0] and r[1] == en2[1])
               or
               (r[0]+4 == en2[0] and r[1] == en2[1])
               or
               (r[0]-4 == en2[0] and r[1]==en2[1]) 
               or
               (r[0] == en2[0] and r[1]-2 == en2[1])  
               or 
               (r[0] == en2[0] and r[1]+2 == en2[1])): 
                if not enemy2.IsDead():
                    enemy2.Death()
                    score+=100

            if ((r[0] == bb[0] and r[1] == bb[1])  
                or 
                (r[0]+4 == bb[0] and r[1] ==bb[1])  
                or 
                (r[0]-4 == bb[0] and r[1]==bb[1]) 
                or 
                (r[0] ==bb[0] and r[1]-2 == bb[1])  
                or 
                (r[0] == bb[0] and r[1]+2 ==bb[1])): 
                bomber1.Death()
                l= bomber1.GetLives()
                bomber1.SetLives(l-1)
                bomber1.Respawn()
            bomb1.SetTime(2)

    if bomb1.status == 2:
        bomb1.SetTime(bomb1.GetTime()-1)        
        if bomb1.GetTime() == 0:
            bomb1.Explode(' ')
            bomb1.Remove_Bomb()

    l= bomber1.GetLives()

    if Intersection():
        bomber1.Death()
        bomber1.SetLives(l-1)           
        bomber1.Respawn()

    l = bomber1.GetLives()
    if (l == 0):
        Make_All()
        time.sleep(2)
        Make_All()

        print("Game Over")
        sys.exit(0)

    Make_All()

    if(enemy1.IsDead() and enemy2.IsDead()):
        Make_All()
        time.sleep(2)
        print("\n***You Won***\n")
        sys.exit(0)
