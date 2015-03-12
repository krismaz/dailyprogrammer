#Using python tokenizer is a strange deal.
from tokenize import generate_tokens
from tokenize import *
from io import StringIO
from operator import *

dataz = input().strip().strip('"').replace('x', ' x ') #Do some pre-processing so python is happy.
operators = {'+':(1, add), '-':(1, sub), 'x':(0, mul), '*':(0, mul), '/':(0, floordiv)} #Ordering of operators can be changed here

output, stack = [], []

def handle(t, s, o, a): #Magical translation of tokens
	if t == NUMBER: #Number \o/
		o.append(int(s))
	elif t == OP or t == NAME:
		if s == '(': #Parenthesis begin
			a.append(s)
		elif s == ')': #Parenthesis end
			while len(a) > 0 and not a[-1] == '(':
				o.append(a.pop())
			a.pop()
		elif s.strip() == '': #Whitespace
			pass
		else: #Operators down here
			try:
				opDetails = operators[s]
			except:
				print('Unknown operator:', s)
			while len(a) > 0 and not a[-1] == '(' and a[-1][0] <= opDetails[0]:
				o.append(stack.pop())
			stack.append(opDetails + (s,))
	else:
		pass

for token in generate_tokens(StringIO(dataz).readline): #Main tokenizer loop
	t, s = token.type, token.string
	handle(t, s, output, stack)

output += reversed(stack)
result, prints = [], []

for var in output: #Computations loop
	if isinstance(var, int):
		result.append(var)
		prints.append(str(var))
	else:
		o1, o2 = result.pop(), result.pop()
		result.append(var[1](o2, o1))
		prints.append(var[2])

print(' '.join(prints), '=', result[0])