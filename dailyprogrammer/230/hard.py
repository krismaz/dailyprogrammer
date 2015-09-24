#Functional programming killed the Python

from itertools import chain, zip_longest

dataz = []
for _ in range(int(input())):#Read input lines from stdin
	dataz.append(input())

words = list(chain.from_iterable(map(str.split, dataz))) + list(chain.from_iterable(map(str.split, map(''.join, zip_longest(*dataz, fillvalue=' '))))) #Split words, both horizontally ad vertically

with open('dictionary.txt', 'r') as f: #Load a dictionary
	dictionary = set(map(str.strip, f.readlines()))

def greed(word): #Greedy match. Note lack of spaghetti code
	if len(word) < 3:
		return ''
	if word.lower() in dictionary:
		return word
	if word.lower()[::-1] in dictionary:
		return word[::-1]
	return max(greed(word[1:]), greed(word[:-1]), key=len)

for w in sorted(w for w in map(greed, words) if w ): #Filtering and worting
	print(w.lower())