# -*- coding: latin-1 -*-

#\x84\x94\x81 = ���	\x8e\x99\x9a = ���


from BaseOps import *


def strMapSize(QLS):
	try:
		return (u"Punktu�s", "Unspielbar", "Subatomar", "Mikroskopisch", "Staubk�rnchen", "Winzig", "Liliput", "Sehr klein", "Klein", "Mittel", u"Gro�", "XXL")[QLS]
	except:
		return u"KEINK�SEMEHRFEHLER"


def wDraw(world, field):
	for i in range(len(field)):
		for j in range(len(field[0])):
			c = 255 * field[i][j]
			world.putpixel((i, j), (c, c, c))
	return world
	
	
def processPixel(w, x, y, r):
	
	base = 0
	black = 0
	choice = (
		(x - r, y - r),
		(x - r, y),
		(x - r, y + r),
		(x, y - r),
		(x, y + r),
		(x + r, y - r),
		(x + r, y),
		(x + r, y + r)
		)
	for i in choice:
		try:
			if w.getpixel((i[0], i[1])) == BLACK:
				black += 1
			base += 1
		except IndexError:
			pass

	if randint(0, base * 2 - 1) <= black * 2:
		return BLACK
	elif r <= 2 and black > base / 2:
		return BLACK
	else:
		return WHITE

def processField(f, x, y, r):
	
	base = 0
	black = 0
	choice = (
		(x - r, y - r),
		(x - r, y),
		(x - r, y + r),
		(x, y - r),
		(x, y + r),
		(x + r, y - r),
		(x + r, y),
		(x + r, y + r)
		)
	for i in choice:
		try:
			if f[i[0]][i[1]] == 0:
				black += 1
			base += 1
		except IndexError:
			pass

	if randint(0, base * 2 - 1) <= black * 2:
		return 0
	elif r <= 2 and black > base / 2:
		return 0
	else:
		return 1

def rectangle(pic, edges, colour, random = 100):
	'''Zeichnet ein Rechteck.'''
	
	if random == 100:
		for i in range(edges[0], edges[2]):
			for j in range(edges[1], edges[3]):
				pic.putpixel((i, j), colour)
	else:
		for i in range(edges[0], edges[2]):
			for j in range(edges[1], edges[3]):
				if randint(0, 100) < random:
					pic.putpixel((i, j), processPixel(pic, i, j, 1))

def rectanglify(field, edges, bit = 1, random = 100):
	'''Zeichnet ein Rechteck.'''
	
	if random == 100:
		for i in range(edges[0], edges[2]):
			for j in range(edges[1], edges[3]):
				field[i][j] = bit
	else:
		for i in range(edges[0], edges[2]):
			for j in range(edges[1], edges[3]):
				if randint(0, 100) < random:
					field[i][j] = processField(field, i, j, 1)

def frame(pic, thickness, colour, random = 100):
	'''�berschreibt den Bildrand mit einem Rahmen'''
	
	xsz = pic.size[0]
	ysz = pic.size[1]
	rectangle(pic, (0, 0, xsz, thickness), colour, random)
	rectangle(pic, (0, thickness, thickness, ysz), colour, random)
	rectangle(pic, (xsz - thickness - 1, thickness, xsz, ysz), colour, random)
	rectangle(pic, (thickness, ysz - thickness - 1, xsz - thickness - 1, ysz), colour, random)

def framify(field, thickness, bit = 1, random = 100):
	'''�berschreibt den Bildrand mit einem Rahmen'''
	
	xsz = len(field)
	ysz = len(field[1])
	rectanglify(field, (0, 0, xsz, thickness), bit, random)
	rectanglify(field, (0, thickness, thickness, ysz), bit, random)
	rectanglify(field, (xsz - thickness - 1, thickness, xsz, ysz), bit, random)
	rectanglify(field, (thickness, ysz - thickness - 1, xsz - thickness - 1, ysz), bit, random)

def interframe(pic, thickness, colour):
	'''Zeichnet einen weichen Rahmen'''
	
	for i in range(thickness):
		frame(pic, thickness - i, colour, i * 100 / thickness)
		
def interframify(field, thickness, bit = 1):
	'''Zeichnet einen weichen Rahmen'''
	
	for i in range(thickness):
		framify(field, thickness - i, bit, i * 100 / thickness)
		
def do(field, QUADRATLOGSIZE, xsz, ysz):
	'''Mainmethode f�r erste Blaupause'''
	
	field2 = field[:]
	
	for i in range(QUADRATLOGSIZE - 2, - 1, - 1):
		print str(round(100.0 - i * 100.0 / (QUADRATLOGSIZE - 2), 1)) + "%"
		q = 2 ** (QUADRATLOGSIZE - i)
		r = 2 ** i
		for j in range(0, q):
			for k in range(0, q):
				s = processField(field, j * r, k * r, r)
				rectanglify(field2, (j * r, k * r, (j + 1) * r, (k + 1) * r), s)
		for m, j in enumerate(field2):
			for n, k in enumerate(j):
				field2[m][n] = (k + 1) % 2
		field = field2[:]
	black = 0
	for i in field:
		black += sum(i)
	if sum > xsz ** 2 / 2:
		for m, j in enumerate(field2):
			for n, k in enumerate(j):
				field2[m][n] = (k + 1) % 2
	interframify(field, 32)
	return field
	

def paint(field, field2, point):
	n = getNeighbours(point, 1)
	base = 0
	black = 0
	for i in n:
		if field[i[0]][i[1]] == 0:
			black += 1
	base = len(n)
	if  black > base / 4:
		field2[point[0]][point[1]] = 0
	else:
		field2[point[0]][point[1]] = 1


def fill(field, p, bit, mx = 127):
	last = field[p[0]][p[1]]
	if last == bit:
		return field
	l = len(field)
	todo = []
	frontline = [p]
	c = 0
	
	while frontline:
		c += 1
		if c > mx:
			return field
		i = frontline.pop()
		try:
			f = field[i[0]][i[1]]
		except IndexError:
			continue
		if (not i in todo) and f == last:
			todo.append(i)
			frontline += [
				(i[0] - 1, i[1]),
				(i[0] + 1, i[1]),
				(i[0], i[1] - 1),
				(i[0], i[1] + 1)
				]
	for i in todo:
		field[i[0]][i[1]] = bit
	return field


def generateWorld(world, QLS, xsz, ysz, save):
	field = list(list(0 for i in range(ysz)) for i in range(xsz))
	
	for i in range(xsz / 2):
		for j in range(ysz / 2):
			field[i][j] = 1
	
	for i in range(xsz / 2, xsz):
		for j in range(ysz / 2, ysz):
			field[i][j] = 1


	print "Drawing Blueprint..."
	
	
	blueprint = do(field, QLS, xsz, ysz)
	
	for m, j in enumerate(blueprint):
		for n, k in enumerate(j):
			blueprint[m][n] = (k + 1) % 2
	
	s1 = wDraw(world, blueprint)
	
	s1.save("\\saves\\World%s\\World.bmp") % save
	print "Welt gespeichert."
	
	field = blueprint[:]


	print "Smoothening points..."

	field2 = list(list(0 for i in range(ysz)) for i in range(xsz))
	
	for i in range(xsz):
		progress(i, xsz, 32)
		for j in range(ysz):
			paint(field, field2, (i, j))
	
	field = field2[:]

	
	print "Filling spots..."
	
	
	for i in range(32, xsz - 31, 4):
		progress(i, xsz, 32)
		for j in range(32, ysz - 31, 4):
			if field[i][j] == 1:
				field = fill(field, (i, j), 0, randint(16, xsz))
			else:
				field = fill(field, (i, j), 1, randint(16, xsz))
	
	print "Creating Sketch..."
	
	wDraw(world, field)
	
	world.save("\\saves\\World%s\\WorldS.bmp") % save
	
	return field
