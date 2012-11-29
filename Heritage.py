# -*- coding: latin-1 -*-


from BaseOps import *
from Family import *
from Geography import *
from WorldGeneration import *
from Initialise import initialise

#Elementar für die Fensterdarstellung
os.environ['SDL_VIDEODRIVER'] = 'windib'

PATH = os.path.abspath(os.curdir)

imList = {}

for phile in os.listdir(PATH + "\\imFiles"):
	if phile[- 4:] == ".bmp":
		imList[phile[: - 4]] = pygame.image.load(phile)


pygame.font.init()
	
FONT = pygame.font.SysFont(FONTTYPE, BFS)

world = Image.open(PATH + "\\imFiles\\Quadrat.bmp")
	
xsz, ysz = world.size

NOW = 0 # Beginn der Zeitlinie in Tagen
FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = xsz # size of window's width in pixels
WINDOWHEIGHT = ysz # size of windows' height in pixels

mapSize = (xsz, ysz)


# DER Spielstand
SAVEGAME = {}



def main(NOW, FPS, WINDOWWIDTH, WINDOWHEIGHT, mapSize):
	
	windowSize = (WINDOWWIDTH + MENUSIZE, WINDOWHEIGHT)
	
	#Person(0, None, None, City((0, 0)))
	
	land = initialise(NOW)
	
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	mapCons = imList["Countries"]
	mapCits = imList["Cities"]
	
	#Default-Mausposition
	mx, my = (0, 0)
	
	menu = None
	mapLoaded = False
		
	oneToOne = imList["Countries"]
	DISPLAY = pygame.display.set_mode((MENUSIZE + xsz, max(ysz, MENUSIZE)), HWSURFACE|DOUBLEBUF|RESIZABLE)
	
	pygame.display.flip()
	pygame.display.set_caption('Il Principe')
	
	firstRun = True
	
	while True:
		DISPLAY.fill(DARKBLUE)
		
		moved = False
		newButton = False
		mouseClickedAt = (0, 0)
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				moved = True
				#mx, my = event.pos
				mx, my = getMousePos(event.pos, mapSize)
		
			elif event.type == MOUSEBUTTONDOWN:
				mouseClickedAt = (0, 0)
			
			elif event.type == MOUSEBUTTONUP:
				mouseClickedAt = event.pos
				newButton = True
			
			elif event.type == VIDEORESIZE or firstRun:
				if not firstRun:
					windowSize = event.size
				mapSize = (max(32, windowSize[0] - MENUSIZE), windowSize[1])
				displaySize = (max(xsz + MENUSIZE, windowSize[0]), max(MENUSIZE, windowSize[1]))
				DISPLAY = pygame.display.set_mode(displaySize, HWSURFACE|DOUBLEBUF|RESIZABLE)
				DISPLAY.fill(DARKBLUE)
				firstRun = False
		
		#Karte resetten
		oneToOne.blit(mapCons, (0, 0))
		
		#Ländergrenzen einzeichnen
		frameArea(oneToOne, mx, my, True, PURPLE, (xsz, ysz))
		frameArea(oneToOne, mx, my, False, ORANGE, (xsz, ysz))
		
		#An Fenstergröße anpassen
		DISPLAY.blit(pygame.transform.scale(oneToOne, mapSize), (0, 0))
		
		#Buttons zeichnen
		btChoice = drawButtons(DISPLAY, windowSize, (displaySize[0] - MENUSIZE / 2, displaySize[1] / 2), mouseClickedAt)
		
		if not btChoice == None:
			button = btChoice
		else:
			newButton = False
		
		if newButton:
			menu = button
			newButton = False
			if menu == "Audienz":
				pass
			elif menu == "Gefolge":
				pass
			elif menu == "Jahrbuch":
				pass
			elif menu == "System":
				system(DISPLAY, FPSCLOCK, displaySize)
		
		'''for i in getNeighbours((mx, my), 3, max(mapSize)):
			if isCity(i):
				here = cityAt(i)
				if moved:
					print str(cityAt(i))'''
					
		pygame.display.update()
		FPSCLOCK.tick(FPS)


def printAt(text, pos, display, highlight = False, colour = INK):
	if highlight:
		colour = LIGHTINK
	font = FONT.render(text, True, colour)
	display.blit(font, pos)


def drawWindow(display, pos, xsz, ysz, colour = PAPER):
	'''Zeichnet ein Fenster mit Rahmen.
	
	VORSICHT: Die Funktion ist nicht sicher, es muss r, g, b < 60 gelten.'''
	
	r, g, b = colour
	framewidth = 7
	colstep = 20
	antiframe = framewidth * 4 - 2
	
	pygame.draw.rect(display, colour, (pos[0], pos[1], xsz, ysz), 0)
	
	for i in range(framewidth):
		darkness = i * colstep
		fPos = (pos[0] + i, pos[1] + i, xsz - 2 * i, ysz - 2 * i)
		pygame.draw.rect(display, (r - darkness, g - darkness, b - darkness / 2), fPos, (framewidth - i) * 2 - 1)
	
	
	darkest = (framewidth - 1) * colstep
	return drawXButton(display, colour, (r - darkest, g - darkest, b - darkest / 2), (pos[0] + xsz - antiframe + framewidth, pos[1] - framewidth), antiframe)
	

def drawXButton(display, bgColour, XColour, pos, size):
	xdist = 3
	pygame.draw.rect(display, XColour, (pos[0], pos[1], size, size), 1)
	pygame.draw.rect(display, bgColour, (pos[0] + 1, pos[1] + 1, size - 2, size - 2), 0)
	
	xa = pos[0] + xdist
	xb = pos[0] + size - xdist
	ya = pos[1] + xdist
	yb = pos[1] + size - xdist
	
	pygame.draw.line(display, XColour, (xa, yb), (xb, ya), 2)
	pygame.draw.line(display, XColour, (xb, yb), (xa, ya), 2)
	
	#Menge der X-sensitiven Punkte bestimmen
	re = []
	for i in range(size):
		for j in range(size):
			re.append((pos[0] + i, pos[1] + j))
	return re
	


def system(display, FPSCLOCK, displaySize):
	savegame = {}
	xsz, ysz = displaySize
	
	#Maximale Anzahl an Spielstände
	NUMSAVES = 5
	
	for i in range(NUMSAVES):
		try:
			fi = open("\\saves\\World%s\\Universe.pcp" % i)
			savegame[i] = pickle.load(fi)
		except IOError:
			savegame[i] = None
	mpos = (0, 0)
	
	#Sub-Eval-Schleife
	
	edge = (xsz / 10, ysz / 10)
	hl = - 1
	clickPos = (- 1, - 1)
	
	while True:
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONUP:
				clickPos = event.pos
			if event.type == MOUSEMOTION:
				mpos = event.pos
		
		markedWorld = (mpos[1] - BFS - edge[1]) / int(BFS * 1.5)
		
		if 0 <= markedWorld < NUMSAVES:
			hl = markedWorld
		
		closeWindow = drawWindow(display, edge, edge[0] * 8, edge[1] * 8)
		artwork = imList["Skull"]
		display.blit(artwork, (edge[0] * 8 - artwork[0], edge[1] * 8 - artwork[1]))
		for i in range(NUMSAVES):
			printAt("Welt" + str(i), (edge[0] + BFS, edge[1] + BFS + i * int(BFS * 1.5)), display, highlight = (i == hl))
		
		if clickPos in closeWindow:
			break
				
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		


def getMousePos(pos, size):
	global WINDOWWIDTH, WINDOWHEIGHT
	
	return (int(pos[0] * (WINDOWWIDTH / float(size[0]))), int(pos[1] * (WINDOWHEIGHT / float(size[1]))))


def getScreenPos(pos, size):
	global WINDOWWIDTH, WINDOWHEIGHT
	
	ls = []
	widthRatio = size[0] / float(WINDOWWIDTH)
	heightRatio = size[1] / float(WINDOWHEIGHT)
	for i in range(int(pos[0] * widthRatio), int((pos[0] + 1) * widthRatio)):
		for j in range(int(pos[1] * heightRatio), int((pos[1] + 1) * heightRatio)):
			ls.append((i, j))
	return ls
	

def getScreenPosCentre(pos, size):
	div0 = WINDOWWIDTH / float(size[0])
	div1 = WINDOWHEIGHT / float(size[1])
	x = int(pos[0] / div0)
	y = int(pos[1] / div1)
	
	return (x, y)
	

def frameArea(DISPLAY, x, y, distMode, colour, size):
	widthRatio = int(size[0] / float(WINDOWWIDTH))
	heightRatio = int(size[1] / float(WINDOWHEIGHT))
	
	if distMode:
		refList = District.dists
	else:
		refList = City.cits
	for i in refList:
		l = i.getLands()
		#if getScreenPosCentre((x, y), size) in l:
		if (x, y) in l:
			b = i.getBorders()
			for j in b:
				jj = getScreenPos(j, size)
				for jjj in jj:
					pygame.draw.aaline(DISPLAY, colour, jjj, jjj)
			if distMode:
				for city in i.realm:
					pos = getScreenPosCentre(city.getPos(), size)
					pygame.draw.rect(DISPLAY, RED, (pos[0] - widthRatio, pos[1] - heightRatio, 3 * widthRatio, 3 * heightRatio), 0)
				pos = getScreenPosCentre(i.cap.getPos(), size)
				pygame.draw.rect(DISPLAY, RED, (pos[0] - 2 * widthRatio, pos[1] - 2 * heightRatio, 5 * widthRatio, 5 * heightRatio), 0)
			else:
				streets = i.getPaths()
				for j in streets:
					pygame.draw.aaline(DISPLAY, BLUE, getScreenPosCentre(i.getPos(), size), getScreenPosCentre(j.goto(i).getPos(), size), max(int(size[0] / float(WINDOWWIDTH)), 1))
					pos = getScreenPosCentre(j.goto(i).getPos(), size)
					pygame.draw.rect(DISPLAY, RED, (pos[0] - widthRatio, pos[1] - heightRatio, 3 * widthRatio, 3 * heightRatio), 0)
				pos = getScreenPosCentre(i.getPos(), size)
				pygame.draw.rect(DISPLAY, colour, (pos[0] - 2 * widthRatio, pos[1] - 2 * heightRatio, 5 * widthRatio, 5 * heightRatio), 0)
			break


def drawButtons(display, windowSize, menuCentre, mouseClickedAt = (0, 0)):
	'''xsz und ysz beziehen sich hier nur auf die Menügröße'''
	
	xsz, ysz = windowSize
	BUTTONSIZE = 128	#Größe der quadratischen .bmp-Dateien
	BUTTONSOURCE = {
	"Audienz"	: (- 1, - 1),
	"Gefolge"	: (- 1, 0),
	"Jahrbuch"	: (0, - 1),
	"System"	: (0, 0)
	}
	
	re = None
	
	for i in BUTTONSOURCE.keys():
		xe, ye = BUTTONSOURCE[i]
		pos = (menuCentre[0] + xe * BUTTONSIZE, menuCentre[1] + ye * BUTTONSIZE)
		antipos = (pos[0] + BUTTONSIZE, pos[1] + BUTTONSIZE)
		
		active = False
		
		if pos[0] < mouseClickedAt[0] < antipos[0]:
			if pos[1] < mouseClickedAt[1] < antipos[1]:
				active = True
		
		if active:
			button = imList[i + "Pressed"]
			pygame.draw.rect(display, DARKBLUE, (pos[0], pos[1], BUTTONSIZE, BUTTONSIZE), 0)
			pos = (pos[0] - 1, pos[1] - 1)
			re = i
		else:
			button = imList[i]
		display.blit(button, pos)
	return re




main(NOW, FPS, WINDOWWIDTH, WINDOWHEIGHT, mapSize)
