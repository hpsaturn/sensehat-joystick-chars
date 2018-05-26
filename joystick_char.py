import string
import random

from time import sleep
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

sense = SenseHat()
sense.set_rotation(270)
chars = list(string.ascii_lowercase)
charssize = len(chars)
upchars = list(string.ascii_uppercase)
upcharssize = len(upchars)
char=0
character='a'

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def getChar(pos):
    global char
    global character
    char = min(charssize-1,max(0,pos)) 
    character=chars[char]
    sense.show_letter(character,color)

def getUpChar(pos):
    global char
    global character
    char = min(upcharssize-1,max(0,pos)) 
    character=upchars[char]
    sense.show_letter(character,color)

def pushed_up(event):
    global char
    if event.action != ACTION_RELEASED:
        char=char+1
        getChar(char)

def pushed_down(event):
    global char
    if event.action != ACTION_RELEASED:
        char=char-1
        getChar(char)

def pushed_left(event):
    global char
    if event.action != ACTION_RELEASED:
        char=char+1
        getUpChar(char)

def pushed_right(event):
    global char
    if event.action != ACTION_RELEASED:
        char=char-1
        getUpChar(char)

def pushed_middle(event):
    global color
    global character
    if event.action != ACTION_RELEASED:
        color=random_color()
        sense.show_letter(character,color)

color = random_color()
sense.show_letter(character,color)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle
pause()


