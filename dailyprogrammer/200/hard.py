#Greedy solution supporting rotation, no exact matches, original problem in NP

from itertools import permutations

boxes = []
stacked = []

def  boxify(s): #Take a 3-dimensional scratchpad and revert to box
	return (len(s), len(s[0]), len(s[0][0]))

def stackify(b): #take box and create scratchpad
	return[[[True for _ in range(b[2])] for _ in range(b[1])] for _ in range(b[0])]

def fits(b, s):#Determine if a given box fits inside a scratchpad
	bx, by, bz = b
	sx, sy, sz = boxify(s)
	if b == boxify(s): #Disallow exact matches
		return False
	for x in range(sx-bx+1):#Simple scratchpad matching
		for y in range(sy-by+1):
			for z in range(sz-bz+1):
				good = True
				for i in range(x, x+bx):
					for j in range(y, y+by):
						for k in range(z, z+bz):
							if not s[i][j][k]:
								good = False
				if good:
					return(x, y, z) #\o/ it fits
	return False

def put(b, rot, s, pos,  bl, sl): #Take a rotated box fit, and update our state
	bl.remove(b)
	sl.append(stackify(b))
	px, py, pz = pos
	bx, by, bz = rot
	for x in range(px, px+bx):
		for y in range(py, py+by):
			for z in range(pz, pz+bz):
				s[x][y][z] = False



#Input reading happens here
stacked.append(stackify(tuple(map(int, input().split()))))

input()

while True:
	try:
		boxes.append(tuple(map(int, input().split())))
	except:
		break

done = False

while not done: #Keep trying to fit more boxs
	done = True
	for stack in stacked:
		for box in boxes:
			fs = [(p, fits(p, stack)) for p in permutations(box) if fits(p, stack)] #Rotations!
			if len(fs) > 0:
				rot, fit = fs[0]
				put(box, rot, stack, fit, boxes, stacked)
				print("Insert box {} into {} at {} rotated to {}".format(box, boxify(stack), fit, rot)) #Sanity
				done = False

print("Filled {} boxes into the {} {} {}:".format(len(stacked)-1, *boxify(stacked[0])) ) #Output wooo
for stack in stacked[1:]:
	print(boxify(stack))
