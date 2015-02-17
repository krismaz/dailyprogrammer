#Very simple solution using standard Python type conversion

lines = ''
while True: #Read all lines of input from command line
	try:
		lines += input()
	except:
		break

word = ''
for i in range(0,len(lines),8):
	word += chr(int(lines[i:i+8], 2)) #Int base 2, chr is ascii

print(word)