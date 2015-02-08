#I couldn't figure out what to calculate, so I made a calculator

from operator import *
from functools import reduce

dataz = input() #'4+3-2*2+8/4/2'

operators = [('+', add), ('-', sub), ('*', mul), ('/', truediv)] #Only support simple binary operators

def handle(s, ops): #Recursively handle operators
	if len(ops) == 0: #No more left, just give an int
		return int(s)
	os, of = ops[0] #Current Operator
	return reduce(of, map(lambda chunk : handle(chunk, ops[1:]), s.split(os))) #Note horribly inefficient list licing, should really track depth instead


print(handle(dataz, operators)) #Error handling? Pffffff!

