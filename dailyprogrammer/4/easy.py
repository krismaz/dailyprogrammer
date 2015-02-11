#Nothing interesting here

from random import sample
from string import * 

n, k = int(input('How many passwords?')), int(input('How many characters?'))

for _ in range(n):
	print(''.join(sample(set(printable)-set(whitespace), k)))