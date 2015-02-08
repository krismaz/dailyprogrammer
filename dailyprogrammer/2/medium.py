#I really didn't have the imiganination to make some grand grame of this.

#Glorious game map
game = '''\
fffllp
ffllpp
pphppp
pppppp
pppptp'''.split()

#Input mapping
direction = {'n':(-1,0, 'north'), 's':(1,0, 'south'), 'e':(0,1, 'east'), 'w':(0,-1, 'west')}

#Map mapping
names = {
	'f' : 'a forest',
	'l' : 'a lake',
	'p' : 'a plain',
	'h' : 'a house',
	't' : 'a wizard tower',
	-1	: 'the dark void'
}

#You are dead, or maybe the wizard is
deaths = {
	'f' : 'The forest is dark. {0} is eaten by a grue. {0} dies.',
	'l' : '{0} cannot swim. {0} drowns. {0} dies.',
	't' : '{0} kills the wizard. {0} wins!',
	-1  : '{0} falls of the edge of the world. {0} dies.',
	-2	: '{0} trips and falls. {0} dies.'
}

#Here be house
x, y = 2,2 

#Why????
name = input('Ur naem?')

while True:
	try:
		print('=    =    =')
		print(name, 'is standing in', names[game[x][y]])
	except:
		print(deaths[-1].format(name))#Spaaaaace
		break
	try:
		print(deaths[game[x][y]].format(name))#Clearly, you must learn that swimming is bad
		break
	except:
		pass
	for d in direction:
		s = names[-1] #Void
		dx, dy, dname = direction[d]
		try:
			s = names[game[x+dx][y+dy]]
		except:
			pass
		print('To the', dname, name, 'sees', s)
	get = input('Where do you go?')
	try:
		dx, dy, dname = direction[get]
		x, y = x+dx, y+dy
	except:
		print(deaths[-2].format(name))#Gotta leanr the hard way
		break;