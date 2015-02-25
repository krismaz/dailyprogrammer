#Some silly non-crypto stuff. I should really have used pycrypto, but I didn't feel like it. Besides, it's a fun little excersize.
#I chose to brush up on Python3 bytes stuff rather than pycrypto.
import hashlib
from random import * 

m = hashlib.sha512()

user = input('Username:')
pw = input('Password:')

m.update(bytes(user + '##' + pw, 'utf8')) 

with open('pw.dat', 'rb') as f1:
	if f1.read(64) == m.digest(): #Note, missing salt. SHA-512 for passwords? Bad idea
		print()
		print('Correct')
		secret = []
		seed(user + '##' + pw) #Using a mersene twister as encryption is not a good idea. Like. Ever.
		with open('secrets.dat', 'rb') as f2:
			byte = f2.read(1)
			while byte != b'':
				secret.append(chr(int.from_bytes(byte, byteorder='big') ^ randint(0,256)))
				byte = f2.read(1)
		print(''.join(secret))
