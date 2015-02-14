#LP region solution

from pulp import *
from itertools import product

def linify(s): #Take a line of variable settings, and contruct the set of internal variable names
	res = set()
	for si in s.replace(' &', '').split():
		if '!' in si:
			res.add('f('+si[1:]+')')
		else:
			res.add('t('+si+')')
	return frozenset(res)

lines = []
n, *names = input().split()

regions = {frozenset(i):LpVariable(''.join(i), 0, 1) for i in product(*(['t('+n+')', 'f('+n+')'] for n in names))} #Generate regions
lines.append(sum(regions.values()) == 1.0) #All reagions sum to 1

for _ in range(int(n)): #Read different contraints
	c, v = input().split(':')
	lines.append(sum(regions[r] for r in regions if r>=linify(c)) == float(v)) #Note use of set to filter regions

ob = linify(input())
lines.append(sum(regions[r] for r in regions if r>=ob)) #Again, set sums regions

maxprob = LpProblem("test1", LpMaximize)#Use both minimization and maximization to check if they are the same
minprob = LpProblem("test2", LpMinimize)#There is probably some smarter way to do this

for l in lines:
	maxprob += l
	minprob += l

#Something 
GLPK(msg = 0).solve(maxprob)
maximum = value(maxprob.objective)
GLPK(msg = 0).solve(minprob)
minimum = value(minprob.objective)


if minimum == maximum: #If both the minimization adn maximization is the same, then we have a fixed solution
	print(minimum)
else:
	print('Not enough information.')