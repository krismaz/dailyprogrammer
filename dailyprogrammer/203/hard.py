#Easy Part. Intermediate shouldn't be too hard, but it is not going to be much fun, since the ui will be shit.
#TODO:Everything else

from random import choice

h, w, d = 100, 100, 10 #Dimensions

dist = ['A']*10+['D']*3+['S']*2+['L'] #Terrain distribution

maps = [[[choice(dist) for i in range(d)] for i in range(h)] for i in range(w)] #Random map

maps[99][99][9] = '#'
maps[0][0][1] = 'D'
maps[0][0][0] = 'H'

for di in range(0, d-1): #Gravity loop
	for hi in range(h):
		for wi in range(w):
			code = maps[wi][hi][di]+maps[wi][hi][di+1]
			if code == 'LA':
				maps[wi][hi][di+1] = 'L'
			if code == 'SA':
				maps[wi][hi][di+1], maps[wi][hi][di] = 'S','A'

for di in range(d): #Output
	for hi in range(h):
		print(''.join(maps[wi][hi][di] for wi in range(w)))
	print('########################################')