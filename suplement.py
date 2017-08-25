from __future__ import print_function
import signal
import copy
import sys
import time
from random import randint
import os
from termcolor import colored

'''The File has additional settings regarding frames and timeout'''


class GetchUnix:
    '''docstring for Enemy'''
    '''The function allows us to generate an output as soon as it has an input rather than waiting for an enter'''
    def __init__(self):
        import tty

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
getch = GetchUnix()


class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):
    '''The function creates a timeout of 1 unit '''
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

#---------------------------------------------------------------------------------------------------------
'''Some initials for the the board purpose'''
w, h = 80, 42
a = [[' ' for x in range(w)] for y in range(h)]
score = 0
