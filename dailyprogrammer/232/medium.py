#Implementation of https://www.cs.umd.edu/~samir/grant/cp.pdf
#Not really optimized much

from math import sqrt, inf
from collections import defaultdict
from random import sample
from itertools import chain, combinations, product

#Utility functions
def dist(p1, p2):
	return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def N(k, mesh):
	sum = set()
	for x, y in product([-1,0,1],repeat = 2):
		sum.update(mesh[(k[0]+x, k[1]+y)])
	return sum

def mesh(S, b):
	res = defaultdict(set)
	for p in S:
		res[(int(p[0]/b),int(p[1]/b))].add(p)
	return res

#Read all of the points from stdin
S = {tuple(map(float, input().replace('(','').replace(')','').split(","))) for _ in range(int(input()))}

#Step 0
S1 = set(S)

while len(S1) != 0:
	#Step 1
	x = sample(S1,1)[0]
	#Step 2
	b = min(map(lambda p: inf if p==x else dist(x,p), S1))/3
	sieve = mesh(S1, b)
	X1 = set(chain.from_iterable(sieve[k] for k in list(sieve.keys()) if len(N(k, sieve)) == 1))
	S1 -= X1
	#Step 3

#Step 4
finalMesh = mesh(S, min(map(lambda p: inf if p==x else dist(x,p), S)))

smallestPair = min(chain.from_iterable(map(lambda k: combinations(N(k, finalMesh), 2), list(finalMesh.keys()))), key = lambda ps: dist(*ps))

print(*smallestPair)