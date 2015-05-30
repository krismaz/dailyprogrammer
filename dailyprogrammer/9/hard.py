#Cool Cool.
#I tried to keep it as  simple as possible
def next(s):
	cur, i, res = s[0], 1, ''
	for c in s[1:]:
		if cur == c:
			i += 1
		else:
			res += str(i) + cur
			i, cur = 1, c
	res += str(i) + cur
	return res

w = '1'

for i in range(40):
	print(w)
	w = next(w)
