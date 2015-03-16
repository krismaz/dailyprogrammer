#This translates well into Python
from operator import *

ops = {'+':add, '-':sub, '*':mul, '/':floordiv} #Operator lookup table, floored division
relation, base, n = input(), int(input()), int(input()) #Read input file
for i in range(n+1):
	print('Term {}: {}'.format(i, base))
	for r in relation.split(' '):
		base = ops[r[0]](base, int(r[1:])) #Apply operators