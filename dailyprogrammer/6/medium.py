#Question is super vague, and missing stuff, I also think the ezamples are wrong

dataz = input()
def strip(word): #Quick estimate, O(n^4)
	keep = [True for _ in word]
	for start in range(len(word)):
		for length in range(4, len(word)-start):
			for check in range(start+length, len(word)-length+1):
				if word[start:start+length] == word[check:check+length]:
					keep[check:check+length] = [False for _ in range(length)]
	return ''.join(c for i, c in enumerate(word) if keep[i])

print(' '.join([strip(word) for word in dataz.split()]))


#Note, 'ates' eats the last 'a' of 'BlaBla', why does the example omit this
#aaatestBlaBl aaathisBlaBl aaathatBlaBl aaagoodBlaBl aaagood1BlaBla123
#aaatestBlaBla aaathisBlaBla aaathatBlaBla aaagoodBlaBla aaagood1BlaBla123