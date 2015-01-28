#Ezmode, added some randomness

import random

line, low, high = '', 0, 100

while not line == 'r':
	num = sorted([random.choice(range(low, high+1)) for i in range(5)])[2]
	line = input("I guess {}\n".format(num))
	if line == 'h':
		high = num - 1
	elif line == 'l':
		low = num + 1
	elif line == 'r':
		print('\o/')
		break
	else:
		print("(h)igh/(l)ow/(r)ight")