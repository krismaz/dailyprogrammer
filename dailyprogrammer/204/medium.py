#O(n log n) solution. It's handy, but slow. Use recursion (10 -> 02) for speed.

from itertools import product
from math import log2, ceil
from functools import reduce

target = int(input()) #Read input number
for perm in product([0,1,2], repeat = int(ceil(log2(target)))+1): #Iterate all hyperbinary numbers of binary length (or, 1 more, easiest this way)
    if target == reduce(lambda xs, x: 2**x[0]*x[1]+xs, enumerate(reversed(perm)), 0): #Test hyperbinary value
        print(''.join(map(str,perm)).lstrip('0')) #Print, with leading zeroes stripped