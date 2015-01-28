#mostly just the scrabble-bot ai part, assume repeat letters (not sure easy change)

from itertools import combinations

with open('dictionary', errors='ignore') as f:
    content = f.readlines()

lookup = dict((''.join(sorted(i[:-1].lower())),i[:-1].lower()) for i in content)

inputs = 'zombies'

keys = lookup.keys()

for comb in [''.join(sorted(c)) for i in range(3, len(inputs)+1) for c in combinations(inputs, i)]:
	if comb in keys:
		print(lookup[comb])