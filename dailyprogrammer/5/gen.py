#Generate Username+Password and Secret for 5 easy
import hashlib
from random import * 

m = hashlib.sha512()

m.update(b'Krismaz##1234')

with open('pw.dat', 'wb') as f:
	f.write(m.digest())

seed('Krismaz##1234')

with open('secrets.dat', 'wb') as f:
	for c in 'TrustNo1':
		f.write(bytes([randint(0, 256)^ord(c)]))
