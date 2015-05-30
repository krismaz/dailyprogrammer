#Again, vague description
#Here's something that does search and replace

find, filename, replace = input(), input(), input()

with open(filename, 'r') as f:
	content = f.readlines()

for c in content:
	print(c.replace(find, replace))