import pygame
import os

os.environ['SDL_VIDEODRIVER'] = 'windib'

from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((500,500),HWSURFACE|DOUBLEBUF|RESIZABLE)
pic=pygame.image.load("Countries.bmp") #You need an example picture in the same folder as this file!
screen.blit(pygame.transform.scale(pic,(500,500)),(0,0))
pygame.display.flip()
while True:
	for event in pygame.event.get():
		elif event.type==VIDEORESIZE:
			screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
			screen.blit(pygame.transform.scale(pic,event.dict['size']),(0,0))
			pygame.display.flip()
