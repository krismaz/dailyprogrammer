#I suck at hangman

from random import choice

with open('dictionary', errors='ignore') as f:
    content = f.readlines()
content = [s.strip() for s in content if not "'" in s]

secret, letters, errors = choice(content), set(), 10

while errors and secret != set(letters):
	print(' '.join(str(c) if c in letters else '_' for c in secret ))
	print(' '.join(map(str, letters)))
	char = input()[0]
	letters.add(char)
	if not char in secret:
		print('WRONK!')
		errors -= 1
		print(errors, 'BANGS LEFT')

print('WAS', secret)
if errors:
	print('IZ WINR!')
else:
	print('IZ LOZR!')