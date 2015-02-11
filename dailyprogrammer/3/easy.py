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


print(decrypt(encrypt('Krismaz', 7),7))
print(encrypt(encrypt('Krismaz', 13),13))