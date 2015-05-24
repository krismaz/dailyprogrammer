#Python has good decimals it appears

from fractions import *
from decimal import *

getcontext().prec = 50

#https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula#The_BBP_formula_for_.CF.80
def digit(k):
	return Decimal(1)/Decimal(16**k)*Decimal(120*(k**2)+151*k+47)/Decimal(512*(k**4)+1024*(k**3)+712*(k**2)+194*k+15)

print(sum(digit(k) for k in range(40)))

#3.141592653589793238462643383279502884197169399375105820974944592307816406286
#3.1415926535897932384626433832795028841971693993751