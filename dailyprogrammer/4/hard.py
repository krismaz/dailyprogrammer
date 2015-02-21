#Brute force solution using the calculator from 2 easy (not 4 medium, 2 easy is smaller and onle +-*/ are needed).

from operator import *
from functools import reduce
from itertools import *

operators = [('+', add), ('-', sub), ('*', mul), ('/', truediv)] #Only support simple binary operators

def handle(s, ops): #Recursively handle operators
	if len(ops) == 0: #No more left, just give an int
		return int(s)
	os, of = ops[0] #Current Operator
	return reduce(of, map(lambda chunk : handle(chunk, ops[1:]), s.split(os))) #Note horribly inefficient list licing, should really track depth instead


def force(nums):
	for ops in combinations_with_replacement([op[0] for op in operators], len(nums)-2): #Find all  combinations of operators
		for opperm in permutations(ops+('=',)): #For each permutation of operators and equality sign
			for ns in permutations(nums): #For each placement of numbers
				ss = ''.join(chain(*zip_longest(ns, opperm, fillvalue = ''))) #Construct the equation
				left, right = ss.split('=') #Split equation into left and right parts
				if handle(left, operators) == handle(right, operators): #If the equality holds
					print(ss)

while True: #Read all lines on stdin
	try:
		force(input().split(', '))
	except:
		break