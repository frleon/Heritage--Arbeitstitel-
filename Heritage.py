# -*- coding: latin-1 -*-

#\x84\x94\x81 = äöü	\x8e\x99\x9a = ÄÖÜ

import Image, ImageDraw, PIL.ImageOps
import pickle
from random import *
from cmath import log

QUADRATLOGSIZE = 7


world = Image.open("Quadrat.bmp")						#Fuer Algorithmus 3

asz = 0										#A1-2: 1
bsz = 0										#A1-2: 1
xsz = world.size[0]								#A1-2: ... - 2
ysz = world.size[1]								#A1-2: ... - 2

QUADRATLOGSIZE = int(abs(log(xsz, 2)))
print QUADRATLOGSIZE




cities0 = ["Neu", "Bruch", "Borg", "Mos", "Par", "Ober", "Nieder", "Unter", "Nord", "West", "Ost", "Rom", "Sar", "Franken", "Myr", "Win", "Ry", "Alt", "Alten"]
cities1 = ["en", "in", "horn", "lott", "sang", "sel", "lau", "bil", "der", "er", "schild", "hal", "bel", "ter", "ling"]
cities2 = ["burg", "dorf", "berg", "stadt", "burg", "dorf", "berg", "stadt", "burg", "dorf", "berg", "stadt", "walde", "ter", "en", "horst", "hausen", "sal", "stedt", "mar", "furt", "furt", "stein", "stein", "stein", "fels", "fels", "bach", "bach"]

male0 = ["Jo", "Lu", "Hein", "Pe", "Theo", "An", "Bern", "Her", "Wil", "Cas", "Ger", "Hen", "Fried", "Ge", "Her", "Chris", "Cle", "Kle", "Mar", "Mi", "Phil", "Tho", "Wal", "Wer", "Bal", "Diet", "Fer", "Gus", "Kas", "Mat", "Ot", "Au" "Fe", "Gun", "Hel", "Hu", "Kon", "Lud", "Mo", "Nor", "Ro", "Ru", "Se", "Vol", "Wil", "Al", "An", "Ben", "Ber", "Bru", "Bur", "Cas", "Da", "El", "Eng", "Er", "Gis", "Gott", "Gre", "Han", "Ha", "Ig", "Ja", "Leo", "Le", "Lo", "Lud", "Mag", "Man", "Ma", "Mar", "Mar", "Na", "Nik", "Rein", "Rich", "Ro", "Sieg", "Till", "Tim", "Wolf", "Dom"]
male1 = ["hann", "kas", "rich", "sef", "ter", "dor", "o", "ton", "hard", "mann", "helm", "par", "dolf", "hard", "rich", "han", "nes", "org", "bert", "toph", "mens", "tin", "cha", "el", "ber", "hard", "fried", "ther", "mut", "seph", "mas", "ter", "ner", "fons", "fred", "dre", "as", "tha", "sar", "di", "nand", "tav", "bert", "an", "nes", "par", "thi", "as", "to", "o", "gust", "hold", "lix", "tus", "rad", "wig", "ritz", "bas", "ti", "an", "fan", "ker", "fried", "li", "ton", "loys", "i", "us", "dre", "to", "nius", "no", "nard", "dus", "tolt", "no", "an", "ni", "el", "der", "du", "ard", "gon", "mar", "mil", "el", "rik", "win", "ver", "ard", "ver", "har", "dus", "ard", "rit", "lieb", "gor", "do", "rald", "gen", "man", "nus", "natz", "kob", "nik", "a", "chim", "do", "kus", "se", "fus", "on", "renz", "ger", "nus", "nu", "el", "co", "kus", "xi", "mi", "li", "an", "po", "le", "on", "las", "hold", "bin", "ma", "nus", "do", "rus", "we", "gang"]
female0 = ["Ma", "An", "Ca", "Mar", "Jo", "Ag", "Em", "Hil", "Fran", "Ka", "The", "Wil", "Mar", "Irm", "So", "Chris", "Cla", "Ri", "Bar", "Ju", "Ro", "Ur", "Ber", "Frie", "Hed", "Kla", "Li", "Pau", "Pe", "Si", "As", "Cle", "El", "Ga", "Gre", "Gret", "Hen", "Il", "Kor", "Lu", "Mar", "Ma", "Ot", "San", "Sieg", "Sig", "Ste", "Su", "The", "Wil", "Han", "Mi", "Ja", "Min", "Al", "Ang", "An", "Au", "Be", "Bern", "Bir", "Bri", "Ca", "Clau", "Dag", "Da", "De", "Di", "El", "Er", "Fer", "Flo", "Gi", "Gu", "Gun", "Han", "Hed", "He", "Hel", "Her", "Hil", "Ing", "Ir", "Jen", "Jes", "Ka", "Kris", "La", "Lie", "Li", "Lo", "Lu", "Mag", "Mar", "Mecht", "Min", "Mi", "Mo", "Ni", "Pe", "Pi", "Rein", "Re", "Ro", "Sa", "Sy", "Tes", "The", "To", "Ve", "Vi", "An", "Ran"]
female1 = ["ri", "a", "na", "li", "sa", "beth", "tha", "ri", "na", "trud", "ga", "re", "the", "han", "na", "nes", "ma", "de", "gard", "zis", "ka", "da", "re", "si", "a", "hel", "mi", "ga", "re", "tha", "gard", "phi", "ti", "na", "ra", "ta", "ba", "ra", "tel", "ti", "ne", "mi", "li", "a", "su", "la", "ta", "va", "de", "ri", "ke", "se", "la", "wig", "ra", "sa", "tra", "bil", "la", "loi", "si", "a", "trid", "nar", "di", "ne", "men", "ke", "ri", "e", "le", "ta", "ri", "et", "ta", "se", "se", "fa", "du", "cia", "da", "le", "na", "got", "rie", "thil", "de", "tild", "ti", "li", "dra", "lin", "de", "grid", "fa", "nie", "san", "re", "hel", "mi", "ny", "ma", "na", "ga", "tha", "loy", "drea", "ge", "mie", "gus", "ro", "mar", "ana", "del", "traud", "nore", "nan", "ren", "tru", "trud", "drun", "del", "ga", "tha", "lo", "na", "grid", "ris", "ma", "sol", "fer", "tin", "ris", "pol", "sel", "beth", "hild", "am", "gi", "hil", "na", "te", "bi", "phie", "bil", "sa", "o", "do", "ra", "ni", "te", "ro", "ni", "ka", "vi", "en", "ne"]

surnames0 = ["Mar", "Ju", "Mer", "Sa", "Ve", "Val", "Bar", "Es", "Tul", "Ar", "Mal", "Tar", "Mor", "Bel", "Flor", "Lan", "Har", "Star", "Car", "Al", "Mul"]
surnames1 = ["ra", "the", "on", "ter", "mont", "ly", "ryn", "mor", "rent", "ron", "nis", "te", "mi", "si", "us", "ri", "son", "fa"]


def outOf(ls):
	'Gibt ein zufaelliges Element von <ls> zurueck'
	
	return ls[randint(0, len(ls) - 1)]

def genGiven(sex):
	'Vornamen erzeugen'
	
	if sex == 0:
		re = outOf(male0)
		while True:
			re += outOf(male1)
			if randint(0, 11) > 0:
				break
	elif sex == 1:
		re = outOf(female0)
		while True:
			re += outOf(female1)
			if randint(0, 5) > 0:
				break
	else:
		0/0
	return re

def genSurname():
	'Nachnamen erzeugen'
	
	re = outOf(surnames0)
	while True:
		re += outOf(surnames1)
		if randint(0, 5) > 0:
			break
	return re

def genCityName():
	'Stadtnamen erzeugen'
	
	re = ""
	if randint(0, 9) == 0:
		re += outOf(["St. ", "Bad "])
	re += outOf(cities0)
	while True:
		if randint(0, 1) < 1 or len(re) > 16:
			break
		re += outOf(cities1)
	if randint(0, 9) > 0:
		re += outOf(cities2)
	return re




def progress(now, goal, STEP = 10):
	if now % (goal / STEP) == 0:
		print str(round(now * 100.0 / goal, 1)) + "%"

def clean():
	for i in range(asz, xsz + 1):
		for j in range(bsz, ysz + 1):
			n = getNeighbours((i, j))
			change = True
			for k in n:
				if world.getpixel(k) == (255, 255, 255):
					change = False
					break
			if change:
				world.putpixel((i, j), (0, 0, 0))

def getNeighbours(point, r = 1, mx = 1024):
	n = []
	for i in range(max(- r, 0), min(r + 1, mx)):
		for j in range(max(0, - r), min(r + 1, mx)):
			n.append((point[0] + i, point[1] + j))
	n.remove(point)
	return n

def getNeumann(point):
	n = [
		(point[0] - 1, point[1]),
		(point[0], point[1] - 1),
		(point[0], point[1] + 1),
		(point[0] + 1, point[1])
		]
	return n

def wDraw(world, field):
	for i in range(xsz):
		for j in range(ysz):
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
			if w.getpixel((i[0], i[1])) == (0, 0, 0):
				black += 1
			base += 1
		except IndexError:
			pass

	if randint(0, base * 2 - 1) <= black * 2:
		return (0, 0, 0)
	elif r <= 2 and black > base / 2:
		return (0, 0, 0)
	else:
		return (255, 255, 255)

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
	'''Überschreibt den Bildrand mit einem Rahmen'''
	
	xsz = pic.size[0]
	ysz = pic.size[1]
	rectangle(pic, (0, 0, xsz, thickness), colour, random)
	rectangle(pic, (0, thickness, thickness, ysz), colour, random)
	rectangle(pic, (xsz - thickness - 1, thickness, xsz, ysz), colour, random)
	rectangle(pic, (thickness, ysz - thickness - 1, xsz - thickness - 1, ysz), colour, random)

def framify(field, thickness, bit = 1, random = 100):
	'''Überschreibt den Bildrand mit einem Rahmen'''
	
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
	

field = list(list(0 for i in range(ysz)) for i in range(xsz))

for i in range(xsz / 2):
	for j in range(ysz / 2):
		field[i][j] = 1

for i in range(xsz / 2, xsz):
	for j in range(ysz / 2, ysz):
		field[i][j] = 1

def do(field):
	global world
	
	field2 = field[:]
	
	for i in range(QUADRATLOGSIZE - 2, - 1, - 1):
		print str(round(100.0 - i * 100.0 / (QUADRATLOGSIZE - 2), 1)) + "%"
		q = 2 ** (QUADRATLOGSIZE - i)
		r = 2 ** i
		for j in range(0, q):
			for k in range(0, q):
				s = processField(field, j * r, k * r, r)
				rectanglify(field2, (j * r, k * r, (j + 1) * r, (k + 1) * r), s)
		#wDraw(world, field)
		#world.show()
		for m, j in enumerate(field2):
			for n, k in enumerate(j):
				field2[m][n] = (k + 1) % 2
		field = field2[:]
		#wDraw(world, field)
		#world.show()
	black = 0
	for i in field:
		black += sum(i)
	if sum > xsz ** 2 / 2:
		for m, j in enumerate(field2):
			for n, k in enumerate(j):
				field2[m][n] = (k + 1) % 2
	interframify(field, 32)
	'''for m, j in enumerate(field):
		for n, k in enumerate(j):
			field[m][n] = (k + 1) % 2'''
	return field

print "Drawing Blueprint..."

'''do(world)'''

blueprint = do(field)

for m, j in enumerate(blueprint):
	for n, k in enumerate(j):
		blueprint[m][n] = (k + 1) % 2

s1 = wDraw(world, blueprint)

s1.save("World.bmp")
print "Welt gespeichert."

field = blueprint[:]

def paint(field, point):
	n = getNeighbours(point, 2)
	base = 0
	black = 0
	for i in n:
		base += 1
		try:
			if field[i[0]][i[1]] == 0:
				black += 1
		except IndexError:
			base -= 1
	if  black > base / 2:
		field[point[0]][point[1]] = 0
	else:
		field[point[0]][point[1]] = 1

def fill(field, p, bit, mx = 127):
	#print p
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

print "Smoothening points..."

for i in range(xsz):
	progress(i, xsz, 32)
	for j in range(ysz):
		paint(field, (i, j))

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

world.save("WorldS.bmp")




#~~~~~~~Countries~~~~~~~~~~~~



XSZ = 1024

class City(object):
	cits = []
	
	def __init__(self, pos, isCap = False, void = False):
		global XSZ
		
		self.pos = pos
		self.lands = []
		self.name = genCityName()
		if not void:
			City.cits.append(self)
			if not isCap:
				for i in range(0, XSZ + 1, XSZ / 32):
					posCap = self.yieldCap(i)
					if not type(posCap) == type(None):
						self.cap = posCap
						self.cap.addToRealm(self)
						self.district = self.cap.getDistrict()
						self.people = []
						self.ruler = []
						break
	
	def appointRuler(self, person):
		self.ruler = person
	
	def getRuler(self):
		return self.ruler
	
	def addToLands(self, pointOrList):
		if type(pointOrList) == type(()):
			self.lands.append(pointOrList)
		else:
			self.lands += pointOrList
		self.district.addToArea(pointOrList)
	
	def eucDist(self, point):
		return (self.pos[0] - point[0]) ** 2 + (self.pos[1] - point[1]) ** 2
	
	def __eq__(self, other):
		return self.pos == other.pos
	
	def getCap(self):
		return self.cap
	
	def yieldCap(self, dist, xsz = 1024, ysz = 1024):
		qa = self.pos[0] - dist
		qb = self.pos[0] + dist
		ra = self.pos[1] - dist
		rb = self.pos[1] + dist
		re = []
		for i in Capital.caps:
			p = i.getPos()
			if qa <= p[0] <= qb:
				if ra <= p[1] <= rb:
					re.append((self.eucDist(p), i))
		if re:
			return min(re)[1]
		else:
			return None
		
	def getDistrict(self):
		return self.district
	
	def getPos(self):
		return self.pos
	
	def __str__(self):
		return self.name
		


class Capital(City):
	num = 0
	caps = []
	
	def __init__(self, pos, void = False):
		super(Capital, self).__init__(pos, True, void)
		if not void:
			self.district = District(self, Capital.num)
			Capital.num += 1
			Capital.caps.append(self)
			self.realm = []
	
	def addToRealm(self, city):
		self.realm.append(city)
		self.district.addToRealm(city)


def isCity(pos):
	for i in City.cits:
		if i.getPos() == pos:
			return True
	return False


class District():
	dists = []
	
	def __init__(self, cap, num):
		self.cap = cap
		self.num = num
		self.area = []
		self.colour = (randint(0, 63), randint(128, 255), randint(128, 255))
		self.realm = [cap]
		District.dists.append(self)
	
	def addToRealm(self, city):
		self.realm.append(city)
	
	def addToArea(self, pointOrList):
		if type(pointOrList) == type(()):
			self.area.append(pointOrList)
		else:
			self.area += pointOrList
	
	def getColour(self):
		return self.colour




black = []

for i in range(xsz):
	for j in range(ysz):
		if field[i][j] == 0:
			black.append((i, j))

lb = len(black)

print lb, "Quadratkilometer"

print "Processing capitals..."


while len(Capital.caps) < 3:
	for i in range(lb / 1000):
		coord = (randint(1, xsz - 2), randint(1, ysz - 2))
		if coord in black:
			Capital(coord)

lc = len(Capital.caps)

print lc, "Hauptstaedte\n\nProcessing cities"



for i in range(lb / 50):
	progress(i, lb / 50, 18)
	coord = (randint(0, xsz - 1), randint(0, ysz - 1))
	if coord in black:
		if isCity(coord):
			continue
		n = getNeighbours(coord)
		for j in n:
			if isCity(j):
				break
		else:
			City(coord)
	
	
ld = len(City.cits)

print ld, "Staedte\n\nProcessing terrain"

points = list(list(- 1 for i in range(ysz)) for i in range(xsz))

cpos = []

for i in City.cits:
	cpos.append(i.getPos())

CGRID = 8

print ""

for i in range(0, xsz, CGRID):
	progress(i, xsz, 16)
	for j in range(0, ysz, CGRID):
		if (i, j) in black:
			black.remove((i, j))
			dist = 1
			re = []
			last = False
			while dist <= xsz:
				dist *= 2
				xa = i - dist
				xb = i + dist
				ya = j - dist
				yb = j + dist
				for k in cpos:
					if xa <= k[0] <= xb:
						if ya <= k[1] <= yb:
							c = City.cits[cpos.index(k)]
							re.append((c.eucDist((i, j)), c))
				if re:
					if last:
						nc = min(re)[1]
						break
					last = True
			nc.addToLands((i, j))
			points[i][j] = nc.getDistrict()

print "Still processing terrain..."

for i in black:
	"""Punkte werden Städten und Ländern zugeordnet"""
	
	progress(black.index(i), len(black), 32)
	
	try:
		x0 = i[0] - (i[0] % CGRID)
		x1 = x0 + CGRID
		y0 = i[1] - (i[1] % CGRID)
		y1 = y0 + CGRID
		z0 = points[x0][y0]
		z1 = points[x1][y0]
		z2 = points[x0][y1]
		z3 = points[x1][y1]
		if z0 == z1 == z2 == z3:
			for j in range(x0, x1):
				for k in range(y0, y1):
					if isCity((j, k)):
						continue
					points[j][k] = z0
		else:
			raise IndexError
					
	except IndexError:
		lb -= 1
		dist = 1
		re = []
		last = False
		while dist <= xsz:
			dist *= 2
			xa = i[0] - dist
			xb = i[0] + dist
			ya = i[1] - dist
			yb = i[1] + dist
			for j in cpos:
				if xa <= j[0] <= xb:
					if ya <= j[1] <= yb:
						c = City.cits[cpos.index(j)]
						re.append((c.eucDist(i), c))
			if re:
				if last:
					nc = min(re)[1]
					break
				last = True
		nc.addToLands(i)
		points[i[0]][i[1]] = nc.getDistrict()



print lc, "Laender\n", ld + lc, "Staedte"

print "Rendering..."

def render(points):
	land = []
	for i, m in enumerate(points):
		progress(i, xsz)
		for j, n in enumerate(m):
			if n == - 1:
				world.putpixel((i, j), (0, 0, 127))
			elif n == 0:					#Für Debugging
				world.putpixel((i, j), (0, 0, 0))
			elif n == 1:					#Für Debugging
				world.putpixel((i, j), (255, 255, 255))
			else:
				land.append((i, j))
				world.putpixel((i, j), n.getColour())
	for i in Capital.caps:
		n = getNeighbours(i.getPos(), 2)
		for j in n:
			try:
				world.putpixel(j, (255, 0, 0))
			except:
				continue
	for i in City.cits:
		world.putpixel(i.getPos(), (255, 0, 0))
	return land

land = render(points)

world.save("WorldSC.bmp")

f = open("Lands.htg", 'w')
pickle.dump((City.cits, Capital.caps, District.dists, points, land), f)
f.close()
print "Welt gespeichert."

world.show()

#Family


people = []
living = []
msingles = []
fsingles = []



class Person():
	global living
	global people
	global msingles
	global fsingles
	
	population = 0
	
	
	def __init__(self, birth, father, mother, place, sex = - 1, given = None):
		self.num = Person.population
		self.place = place
		Person.population += 1
		self.birth = birth
		self.father = father
		self.mother = mother
		if sex == - 1:
			self.sex = randint(0, 1)
		else:
			self.sex = sex
			
		if given == None:
			self.given = genGiven(self.sex)
		else:
			self.given = given
		
		tradition = self.getFamilyNames()
		if len(tradition) > 0 and randint(0, 1) > 0:
			self.given = outOf(tradition)
		
		self.bannermen = []
		self.death = None
		self.married = False
		self.currentlyMarried = False
		self.weddings = []
		self.spouses = []
		self.children = []
		self.rule = None
		if self.father == None:
			self.name = genSurname()
		else:
			self.name = self.father.getSurname()
		
		if self.sex == 0:
			msingles.append(self)
		else:
			fsingles.append(self)
		living.append(self)
		people.append(self)
	
	
	def data(self):
		'Gibt das Datenblatt einer Person zurueck'
		
		re = """
		%s (%s)
		%s - %s
		Vater: %s
		Mutter: %s
		""" % (self, "mw"[self.sex], self.birth / 48, self.death / 48, self.father, self.mother)
		
		if self.married:
			re += "Partner:\n"
			for i in range(len(self.spouses)):
				re += "                " + str(self.weddings[i] / 48) + "   " + str(self.spouses[i]) + "\n"
			
			re += "                Kinder:\n"
			for i in self.children:
				re += "                " + str(i.birth / 48) + "   " + str(i) + "\n"
		
		if self.bannermen:
			re += "\n\nGefolgsleute:"
		for i in self.bannermen:
			re += "  - " + i
		return re
	
	
	def __str__(self):
		if self.death == None:
			return '%s - %s %s (*%s). Z.z. in %s' % (self.num, self.given, self.name, self.birth / 48, self.place.getName())
		return '%s - %s %s (%s - %s)' % (self.num, self.given, self.name, self.birth / 48, self.death / 48)
	
	
	def getAge(self, week):
		return (week - self.birth) / 48
		
	
	def getBirth(self):
		return self.birth / 48
	
	
	def getSex(self):
		return self.sex


	def getGiven(self):
		return self.given
	
	
	def getFamilyNames(self):
		ego = self
		try:
			if self.sex == 0:
				names = [self.mother.father.getGiven()]
			else:
				names = [self.father.mother.getGiven()]
		except:
			names = []
		while True:
			try:
				if self.sex == 0:
					ego = ego.father
				else:
					ego = ego.mother
				names.append(ego.getGiven())
			except:
				return names
	
	
	def getRule(self):
		return self.rule
	
	
	def rule(self, city):
		self.rule = rule
	
	
	def getSubRule(self):
		if self.rule == None:
			return []
		re = [self.rule]
		for i in self.bannermen:
			re.append(i.getSubRule())
		return re
	
	
	def strRule(self):
		re = "Graf %s %s von %s\n" % (self.given, self.name, self.rule)
		for i in self.getSubRule():
			re += "\n%s" (i)
		return re
		
	
	def getSurname(self):
		'Gibt den Nachnamen einer Person zurueck'
		
		return self.name
	
	
	def isMarried(self):
		return self.currentlyMarried
	
	
	def marry(self, spouse, week):
		self.spouses.append(spouse)
		self.weddings.append(week)
		self.married = True
		self.currentlyMarried = True
		try:
			msingles.remove(self)
		except ValueError:
			fsingles.remove(self)
	
	
	def getSpouse(self):
		return self.spouses[- 1]
	
	
	def careless(self, child):
		self.children.append(child)
	
	
	def getChildren(self):
		return len(self.children)
	
	
	def getFirstGradeRelatives(self):
		'Gibt die Eltern und Kinder einer Person zurueck'
		
		re = []
		if not self.father == None:
			re.append(self.father)
		if not self.mother == None:
			re.append(self.mother)
		for i in self.children:
			re.append(i)
		return re
	
	
	def detGrade(self, person):
		grade = 0
		relatives = [self]
		while grade < 4:
			next = []
			grade += 1
			for i in relatives:
				try:
					next += i.getFirstGradeRelatives()
				except:
					continue
			for i in next:
				if i not in relatives:
					relatives.append(i)
			if person in relatives:
				return grade
		return 4
			

	def die(self, week):
		self.death = week
		if self.currentlyMarried:
			self.getSpouse().currentlyMarried = False
			if self.sex == 0:
				fsingles.append(self.getSpouse())
			else:
				msingles.append(self.getSpouse())
		else:
			try:
				msingles.remove(self)
			except ValueError:
				fsingles.remove(self)
		'''if self in kings:
			#print "King dead"
			try:
				#print "Searching for successor"
				kings.append(self.getSuccessor(self.death))
			except AttributeError:
				kings.append(self.getSuccessor(self.death, False))'''
		living.remove(self)
	
	
	def getDeath(self):
		return self.death / 48
	
	
	def getSuccessor(self, year, salic = True):
		'Gibt den Nachfolger eines Regenten an.'
		
		if self.death == None:
			return self.death
		
		rels = self.getFirstGradeRelatives()
		
		for c in range(5):
			livingNow = []
			
			for i in rels:
				if i == None:
					continue
				if (year - i.birth) / 48 > 16 + randint(- 2, 2) and (year < i.death or i.death == None):
					livingNow.append((i.birth, i))
			livingNow.sort()
			for i in livingNow:
				#print salic, i[1].sex == 1, (salic and i[1].sex == 1)
				if not(salic and i[1].sex == 1):
					return i[1]
			next = []
			for i in rels:
				next += i.getFirstGradeRelatives()
			for i in next:
				if i not in rels:
					rels.append(i)
		return None
	
	
	def printDescendants(self, indent, generations = 100):
		if generations >= 0:
			print "|\t" * indent, "|------", self
			for i in self.children:
				i.printDescendants(indent + 1, generations - 1)
			for i in self.spouses:
				print "|\t" * (indent + 1), "  oo", i
	
	
	def printAncestors(self, indent, both = True, generations = 100):
		if generations >= 0:
			if not both:
				indent = 0
			if not self.father == None:
				self.father.printAncestors(indent + 1, both, generations - 1)
			print "\t" * indent, self
			if not self.mother == None and both:
				self.mother.printAncestors(indent + 1, both, generations - 1)
	
	def pledge(self, bannermanToBe):
		if bannermanToBe.getSex() == 0:
			self.bannermen.append(bannermanToBe)
	
	

#EOC Person

NOW = 0

for i in Capital.caps:
	i.appointRuler(Person(NOW - randint(16, 60) * 48, None, None, i, sex = 0))
	for j in range(randint(6, 24)):
		i.getRuler().pledge(Person(NOW - randint(16, 60) * 48, None, None, i, sex = 0))

for i in City.cits:
	if i in Capital.caps:
		continue
	i.appointRuler(Person(NOW - randint(16, 60) * 48, None, None, i, sex = 0))
	for j in range(randint(2, 12)):
		i.getRuler().pledge(Person(NOW - randint(16, 60) * 48, None, None, i, sex = 0))

YOU = City.cits[1].getRuler()
print YOU.getSubRule()
