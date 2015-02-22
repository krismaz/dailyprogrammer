#Scrabble-bot Strikes again!
from collections import defaultdict
from string import *

with open(input(), errors='ignore') as f:
    content = f.readlines()

lookup = defaultdict(set) #We need a new mapping this time, one that remembers more words

for line in content:
	for word in line.split(): #Assume we're getting some plaintext
		word = word.strip(punctuation) #Sometimes Python3 makes things a little too easy
		lookup[''.join(sorted(word.strip().lower()))].add(word.strip().lower()) #Plain old scrabble-bot

for v in lookup.values():
	if len(v)-1: #len >=2
		print(*v)