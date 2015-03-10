#Iterative dynamic programming. Pretty fast for the small inputs, but rather slow on the big ones

from random import choice

target, length = 43, 10

nt = target

bits = []
for i in reversed(range(16)):
	if 2**i <= nt:
		nt -= 2**i
		bits.append(i)

def recurse(bits):
	if len(bits)==1:
		return {2**i for i in range(bits[0]+1)}
	res = {sum(2**i for i in bits)}
	res.update(recurse(bits[::2]))
	res.update(recurse(bits[1::2]))
	return res

nums = recurse(bits)


print(' '.join(map(str,sorted(nums))))
