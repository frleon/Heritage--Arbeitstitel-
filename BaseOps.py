# -*- coding: latin-1 -*-

#\x84\x94\x81 = ���	\x8e\x99\x9a = ���

import Image, ImageDraw, PIL.ImageOps
import pickle
from random import *
from cmath import log
import os, sys

import Heritage

import pygame
from pygame.locals import *



'''Da jedes Modul BaseOps importiert, werden Importe nicht eigens definierter Module alle hier eingef�gt.'''

PAPER	 = (255, 255, 127)
INK		 = ( 63, 191,   0)
LIGHTINK = ( 63, 255,   0)
GREY	 = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE	 = (255, 255, 255)
RED	 	 = (255,   0,   0)
GREEN	 = (  0, 255,   0)
BLUE	 = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 127,   0)
PURPLE   = (255,   0, 255)
CYAN	 = (  0, 255, 255)
BLACK    = (  0,   0,   0)
DARKBLUE = (  0,   0, 127)

BFS = 20 # Schriftgr��e, BASEFONTSIZE
FONTTYPE = 'timesnewroman'
MENUSIZE = 256

world = Image.open("Quadrat.bmp")
xsz, ysz = world.size


def outOf(ls):
	'Gibt ein zuf�lliges Element von <ls> zur�ck'
	
	return ls[randint(0, len(ls) - 1)]


def addsafe(ls, element):
	'Fuegt <element> zu <ls> hinzu genau dann, wenn es noch nicht darin vorhanden ist.'
	
	if not element in ls:
		ls.append(element)
		return True
	return False


def progress(now, goal, STEP = 10):
	try:
		if now % (goal / STEP) == 0:
			print str(round(now * 100.0 / goal, 1)) + "%"
			return True
	except ZeroDivisionError:
		pass
	return False


def getNeighbours(point, r = 1, mx = xsz):
	'''Gibt die Moore-Nachbarn eines als Koordinaten interpretierten 2-Tupels zurueck'''
	
	n = []
	x, y = point
	for i in range(max(x - r, 0), min(x + r + 1, mx)):
		for j in range(max(0, y - r), min(y + r + 1, mx)):
			n.append((i, j))
	try:
		n.remove(point)
	except ValueError:
		pass
	return n

def getNeumann(point, mx = xsz):
	'''Gibt die von-Neumann-Nachbarn eines als Koordinaten interpretierten 2-Tupels zur�ck.
	Achtung! Im Gegensatz zur getNeighbours() k�nnen invalide Punkte zur�ckgegeben werden!'''
	
	x, y = point
	re = ((x - 1, y),
		(x + 1, y),
		(x, y - 1),
		(x, y + 1))
	return re
