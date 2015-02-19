#Knuth algorithm, strange and not pretty

def easter(y):
	g = y%19 + 1
	c = y//100 + 1
	x, z = (3*c)//4 - 12, (8*c+5)//25 - 5
	d = (5*y)//4 - x - 10
	e = (11*g + 20 + z - x) % 30
	n = 44 - e
	n = n + 30 if n < 21 else n
	n = n + 7 - ((d + n) % 7)
	return '{}/{}/{}'.format(y, 4 if n > 31 else 3, n-31 if n > 31 else n)

for date in map(easter, range(2015, 2026)):
	print(date)