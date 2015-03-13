seq1, seq2 = input(), input()

D = [[0]*(len(seq2)+1) for _ in range(len(seq1)+1)]

for i in range(1,len(seq1)+1):
	for j in range(1,len(seq2)+1):
		a = seq1[i-1]
		b = seq2[j-1]
		v1 = D[i-1][j-1] + (2 if a == b else -1)
		v2 = D[i][j-1] + (-2 if i != len(seq1) else 0)
		v3 = D[i-1][j] + (-2 if j != len(seq2) else 0)
		D[i][j] = max(v1, v2, v3)

upperAlign, lowerAlign = '', ''

i, j = len(seq1) ,len(seq2)
while i != 0 and j != 0:
	a = seq1[i-1]
	b = seq2[j-1]
	if D[i][j] == D[i-1][j-1] + (2 if a == b else -1):
		upperAlign = upperAlign + a
		lowerAlign = lowerAlign + b
		i, j = i-1, j-1
	elif D[i][j] == D[i][j-1] + (-2 if i != len(seq1) else 0):
		upperAlign = upperAlign + ('-' if i != len(seq1) else ' ')
		lowerAlign = lowerAlign + b
		j = j-1
	elif D[i][j] == D[i-1][j] + (-2 if j != len(seq2) else 0):
		upperAlign = upperAlign + a
		lowerAlign = lowerAlign + ('-' if j != len(seq2) else ' ')
		i = i-1
	else:
		print(i,j)

upperAlign += ' '*j+seq1[:i][::-1]
lowerAlign += ' '*i+seq2[:j][::-1]

upperAlign, lowerAlign = upperAlign[::-1], lowerAlign[::-1]

print(upperAlign)
print(lowerAlign)