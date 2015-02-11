#Simple substitution cypher, supports any alphabet

from string import *

skey = '''$2iS8 l<R&~|BK
5=u0?>!M4)7s("}A6e#*@\y,W%Xc^zE'a/HbL;.+NmGU`JC1d93:pxIv
rwDPoTQt[jOk{Vgnfh]ZF_-Y	q'''

def encrypt(s, key = skey, alphabet = printable):
	return ''.join(alphabet[key.index(c)] for c in s)

def decrypt(s, key = skey, alphabet = printable):
	return ''.join(key[alphabet.index(c)] for c in s)

print(decrypt(encrypt('Krismaz')))

