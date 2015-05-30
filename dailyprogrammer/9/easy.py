#Very vague description, I take it they want something like this
numbers, strings = [],[]

for word in input().split():
	try:
		numbers.append(int(word))
	except:
		strings.append(word)

print('\n'.join(map(str,sorted(numbers)))
print('\n'.join(sorted(strings)))
