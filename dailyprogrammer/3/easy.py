#Simple Caesar cypher.

from string import *
from collections import deque

def key(n): #Slightly round-about way of generating the lookup-table, in order to preserve case
	lower = deque(ascii_lowercase)
	upper = deque(ascii_uppercase)
	lower.rotate(n)
	upper.rotate(n)
	return list(lower)+list(upper)

def encrypt(s, n):
	return ''.join(ascii_letters[key(n).index(c)] for c in s)

def decrypt(s, n):
	return ''.join(key(n)[ascii_letters.index(c)] for c in s)


op, text, n = input().split()
if op == 'e':
	print(encrypt(text, int(n)))
elif op == 'd':
	print(decrypt(text, int(n)))
else:
	print('Unknown option, use "d/e text n"')