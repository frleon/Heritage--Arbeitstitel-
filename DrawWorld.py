# -*- coding: latin-1 -*-

#\x84\x94\x81 = äöü	\x8e\x99\x9a = ÄÖÜ

import Image, ImageDraw, PIL.ImageOps
import pickle
from random import *
from cmath import log



class City(object):
	cits = []
	
	def __init__(self, pos, isCap = False, void = False):
		XSZ = 1024
		
		self.pos = pos
		self.lands = []
		if not void:
			City.cits.append(self)
			if not isCap:
				for i in range(0, XSZ + 1, XSZ / 32):
					posCap = self.yieldCap(i)
					if not type(posCap) == type(None):
						self.cap = posCap
						self.cap.addToRealm(self)
						self.district = self.cap.getDistrict()
						break
	
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
					#print re[- 1][0], str(re[- 1][1])
		if re:
			#print "\t", min(re)[0], min(re)[1]
			return min(re)[1]
		else:
			return None
		'''for i in range(max(0, self.pos[0] - dist), min(xsz, self.pos[0] + dist)):
			for j in range(max(0, self.pos[1] - dist), min(ysz, self.pos[1] + dist)):
				if Capital((i, j), void = True) in Capital.caps:
					re.append((self.eucDist((i, j)), getCapAt((i, j))))
		if re:
			return min(re)[1]
		else:
			return None'''
		
	def getDistrict(self):
		return self.district
	
	def getPos(self):
		return self.pos
	
	def __str__(self):
		return str(self.pos)
		


class Capital(City):
	caps = []
	num = 0
	
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



def getCapAt(pos):
	for i in Capital.caps:
		if i.getPos() == pos:
			return i
	raise ZeroDivisionError

def getCityAt(pos):
	for i in City.cits:
		if i.getPos() == pos:
			return i
	raise ZeroDivisionError


class District():
	dists = []
	
	def __init__(self, cap, num):
		self.cap = cap
		self.num = num
		self.area = []
		self.colour = (randint(128, 255), randint(0, 63), randint(128, 255))
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


f = open("Lands.htg", 'r')
data = pickle.load(f) # (City.cits, Capital.caps, District.dists, points)
f.close()
XSZ = len(data[3])

City.cits = data[0][:]
Capital.caps = data[1][:]
Capital.num = len(Capital.caps)
District.dists = data[2][:]

ld = len(City.cits)

print ld, "Staedte\n\nProcessing terrain"

points = data[3][:]

cpos = []

print "Rendering..."

world = Image.open("Quadrat.bmp")

def getNeighbours(point, r = 1, mx = 1024):
	n = []
	for i in range(max(- r, 0), min(r + 1, mx)):
		for j in range(max(0, - r), min(r + 1, mx)):
			n.append((point[0] + i, point[1] + j))
	n.remove(point)
	return n
	
	
def render():
	global points, world
	for i, m in enumerate(points):
		if i % 32 == 0:
			print i
		for j, n in enumerate(m):
			if n == - 1:
				world.putpixel((i, j), (0, 0, 127))
			else:
				world.putpixel((i, j), n.getColour())
	for i in Capital.caps:
		n = getNeighbours(i.getPos(), 1)
		for j in n:
			try:
				world.putpixel(j, (255, 0, 0))
			except:
				continue
	for i in City.cits:
		world.putpixel(i.getPos(), (255, 0, 0))

render()

f = open("WorldSCR.bmp", 'w')
world.save("WorldSCR.bmp")
f.close()
print "Welt gespeichert."

world.show()
