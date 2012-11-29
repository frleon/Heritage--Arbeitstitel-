# -*- coding: latin-1 -*-

from BaseOps import *
from Family import *
from Geography import *
from WorldGeneration import *


def initialise(NOW, save):
	'''Wird zu Beginn eines neuen Spieles ausgeführt.
	
	<save> ist eine Ziffer.'''
	
	world = Image.open(path + "\\imFiles\\Quadrat.bmp")
	
	xsz = world.size[0]
	ysz = world.size[1]
	
	QUADRATLOGSIZE = int(abs(log(xsz, 2)))
	print u"Kartengröße:", strMapSize(QUADRATLOGSIZE)
	
	field = generateWorld(world, QUADRATLOGSIZE, xsz, ysz, save)
	
	black = generateLandscape(field)
	ld = len(City.cits)
	
	print ld, "Staedte\n\nProcessing terrain"
	
	sea = City(NOTACITY, False, void = True)
	# Eine Dummystadt zu Vergleichszwecken
	
	points = list(list(sea for i in range(ysz)) for i in range(xsz))
	
	cpos = []
	
	for i in City.cits:
		cpos.append(i.getPos())
	
	CGRID = 2
	
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
					'''Durch x/y wird ein wachsendes Quadrat um den Punkt gelegt'''
					dist *= 2
					xa = i - dist
					xb = i + dist
					ya = j - dist
					yb = j + dist
					for k in cpos:
						if xa <= k[0] <= xb:
							if ya <= k[1] <= yb:
								'''Wenn sich k im Quadrat befindet:'''
								c = City.cits[cpos.index(k)]
								if c.getPos() == NOTACITY:
									continue
								else:
									re.append((c.eucDist((i, j)), c))
					if re:
						if last:
							nc = min(re)[1]
							break
						last = True
				points[i][j] = nc
				nc.addToLands((i, j))
	
	
	print "Processing more terrain..."
	
	lb = len(black)
	lc = len(Capital.caps)
	
	for i in black:
		'''Punkte werden Städten und Ländern zugeordnet'''
		
		progress(black.index(i), len(black), xsz ** 2 / 1500)
		
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
						if z0.getPos() == NOTACITY:
							continue
						points[j][k] = z0
						z0.addToLands((j, k))
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
							if c.getPos() == NOTACITY:
								continue
							re.append((c.eucDist(i), c))
				if re:
					if last:
						re.sort()
						nc = re[0][1]	#Kleinstes Element
						if nc.getPos() == NOTACITY:
							nc = re[1][1]	#Zweitkleinstes Element
						break
					last = True
			nc.addToLands(i)
			points[i[0]][i[1]] = nc
	
	
	print lc, "Laender\n", ld + lc, "Staedte"
	
	print "Determining Borders"
	
	for n, i in enumerate(City.cits):
		progress(n, ld)
		i.yieldBorders()
	
	print "Continuing..."
	
	for n, i in enumerate(District.dists):
		progress(n, len(District.dists))
		i.yieldBorders()
	
	print "Rendering..."
	
	world2 = world.copy()
	
	land = renderCities(xsz, ysz, world)
	world.save("\\imFiles\\World%s\\Cities.bmp") % save
	
	f = open("Lands.htg", 'w')
	pickle.dump((City.cits, Capital.caps, District.dists, points, land), f)
	f.close()
	
	land = renderCountries(points, xsz, ysz, world2)
	world2.save("\\imFiles\\World%s\\Countries.bmp") % save
	
	print "Welt gespeichert."
		
	#Bevölkerung ansiedeln
	
	for i in Capital.caps:
		i.appointRuler(Person(NOW - randint(16, 60) * Person.DAYSPERYEAR, None, None, i, sex = 0))
		for j in range(randint(20, 60)):
			i.getRuler().pledge(Person(NOW - randint(16, 60) * Person.DAYSPERYEAR, None, None, i, sex = 0), True)
			Person(NOW - randint(16, 60) * Person.DAYSPERYEAR, None, None, i)
		
		n = i.getDistrict().getBordering()
		for district in n:
			Path(i, district.getCap(), i.eucDist(district.getCap().getPos()))
		
	
	for i in City.cits:
		if i in Capital.caps:
			continue
		p = Person(NOW - randint(16, 60) * Person.DAYSPERYEAR, None, None, i, sex = 0)
		i.appointRuler(p)
		i.getCap().getRuler().pledge(p, True)
		for j in range(randint(2, 12)):
			i.getRuler().pledge(Person(NOW - randint(16, 60) * Person.DAYSPERYEAR, None, None, i, sex = 0), True)
			Person(NOW - randint(16, 60) * Person.DAYSPERYEAR, None, None, i)
		
		#Straßen initialisieren
		
		Path(i, i.getCap(), i.eucDist(i.getCap().getPos()))
		n = i.getBordering()
		for city in n:
			Path(i, city, i.eucDist(city.getPos()))
	
	
	
	cityOne = Capital.caps[0]
	
	# Sicherstellen, dass alle Städte miteinander verbunden sind
	
	for n, i in enumerate(Capital.caps):
		if n == 0:
			continue
		if not i.wayToExists(cityOne):
			print i
			for j in range(n + 1):
				Capital.caps[j].forgetAllWays()
			Path(i, cityOne, i.eucDist(cityOne.getPos()))
			
			
	
	return land
