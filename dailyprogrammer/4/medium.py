#Using python tokenizer is fo nizzle. It's missing functions and negative numbers, but has support for paranthesis and a multitude of operations

from tokenize import generate_tokens
from tokenize import *
from io import StringIO
from collections import deque
import sys
from operator import *


dataz = input()#'3+3-2*2+8//3+3**2%5-2**(6/2)+6(4+3)'


operators = {'+':(1, add), '-':(1, sub), '*':(0, mul), '/':(0, truediv), '//':(0, floordiv), '%':(0, mod), '**':(-1, pow)}

output, stack = [], []

def handle(t, s, o, a, lt):
	if t == NUMBER:
		o.append(int(s))
	elif t == OP:
		if s == '(':
			if lt == NUMBER:
				handle(OP, '*', o, a, t)
			a.append(s)
		elif s == ')':
			while len(a) > 0 and not a[-1] == '(':
				o.append(a.pop())
			if not a:
				print("Error unbalance!")
			else:
				a.pop()
		else:
			try:
				opDetails = operators[s]
			except:
				print('Unknown operator:', s)
			while len(a) > 0 and not a[-1] == '(' and a[-1][0] <= opDetails[0]:
				o.append(stack.pop())
			stack.append(opDetails)
	elif t == ENDMARKER:
		pass
	else:
		print('Warning unknown token:')
		print(token)

for token in generate_tokens(StringIO(dataz).readline):
	t, s = token.type, token.string
	handle(t, s, output, stack, lt)
	lt = t

if '(' in stack:
	print('Error paran!')

output += reversed(stack)

result = []

for var in output:
	if isinstance(var, int):
		result.append(var)
	else:
		if len(result) < 2:
			print('Error malapplicanse!')
		else:
			o1, o2 = result.pop(), result.pop()
			result.append(var[1](o2, o1))


if not len(result) == 1:
	print("Error non-use")

print(result[0])

