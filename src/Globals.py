import sys
import pygame as P
import random
from time import sleep
import psutil, os

P.init()
P.font.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0,0,255)
GREEN = (0,255,0)
SKY_BLUE = (230, 247, 247)
OCEAN_BLUE = (0,31,75)
JUNGLE_GREEN = (0,75,42)
CRIMSON = (126, 0, 0)

SPECIAL_KEYS = [P.K_ESCAPE,P.K_BACKSPACE,P.K_TAB,P.K_RETURN,P.K_SPACE]
WORDLIST = []
DEF_LETTER_COLOR = WHITE
DEF_WORD_COLOR = WHITE
MONOSPACE_FONT = "static/Anonymous_Pro.ttf"
SCORE = 0
D_WIDTH  = 640
D_HEIGHT = 480
DEF_DIMENSIONS = (D_WIDTH,D_HEIGHT)
DIFFICULTY_LEVEL = 1
TOP_CENTER = (320,120)
SCREEN_CENTER = (320,240)

openf = []

def make_word_list(wordList='static/wordList.txt'):
	global WORDLIST
	with open(wordList) as f:
		WORDLIST = f.read().splitlines()
	f.close()
	WORDLIST = map(lambda x: x.lower(),WORDLIST)
	return WORDLIST

def draw(gm,label,center):
    label_rect = label.get_rect(center=center)
    gm.screen.blit(label,label_rect)

def draw_letter_list(gm, letters, center):
	num_letters = len(letters)
	if num_letters > 1:
		letter_width = letters[0].get_width()
		total_width = num_letters * letter_width

		x0 = center[0] - (total_width / 2) + (letter_width / 2)
		y = center[1]

		for letter in letters:
			label_rect = letter.label.get_rect(center=(x0, y))
			gm.screen.blit(letter.label, label_rect)
			x0 += letter_width
	elif num_letters == 1:
			gm.screen.blit(letters[0].label, letters[0].label.get_rect(center=center))

def set_difficulty_easy():
	global DIFFICULTY_LEVEL
	DIFFICULTY_LEVEL = 1
	print "Difficulty level is -- {}".format(DIFFICULTY_LEVEL)

def set_difficulty_medium():
	global DIFFICULTY_LEVEL
	DIFFICULTY_LEVEL = 3
	print "Difficulty level is -- {}".format(DIFFICULTY_LEVEL)

def set_difficulty_hard():
	global DIFFICULTY_LEVEL
	DIFFICULTY_LEVEL = 5
	print "Difficulty level is -- {}".format(DIFFICULTY_LEVEL)

def getRandom(inputList):
	return (random.choice(inputList))

def get_random_no_dups(inputList,firstLetters):
	if len(inputList) == len(firstLetters):
		return False

	filtered = filter(lambda x: x[0] not in firstLetters,inputList)
	if len(filtered) == 0:
		return False
	else:
		return random.choice(filtered)

def cleanup(openf):
	p = psutil.Process()
	for i in p.open_files():
		if '.ttf' in i.path and i not in openf:
			try:
				os.close(i.fd)
			except:
				pass
