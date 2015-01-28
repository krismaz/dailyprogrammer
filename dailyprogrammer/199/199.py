#Done and working... too lazy for IO

input = """000000000
111111111
490067715"""

dataz = [
		[' _ ','   ', ' _ ', ' _ ', '   ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '],
		['| |','  |', ' _|', ' _|', '|_|', '|_ ', '|_ ', '  |', '|_|', '|_|'],
		['|_|','  |', '|_ ', ' _|', '  |', ' _|', '|_|', '  |', '|_|', ' _|']
		]

for string in input.split():
	print(''.join(dataz[0][int(c)] for c in string))
	print(''.join(dataz[1][int(c)] for c in string))
	print(''.join(dataz[2][int(c)] for c in string))
