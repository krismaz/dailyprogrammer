#Ugly but working
dataz="""
 _  _  _  _  _  _  _  _  _ 
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|


  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |

    _  _  _  _  _  _     _ 
|_||_|| || ||_   |  |  ||_ 
  | _||_||_||_|  |  |  | _|
"""

display = """
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
"""

display, dataz = display.replace('\n',''), [line if not line == '' else ' '*27 for line in dataz.split('\n')] #Preprocess Input
lookup = dict()

for i in range(10):
	lookup[''.join(display[i*3:i*3+3] + display[30+i*3:30+i*3+3] + display[60+i*3:60+i*3+3])]  = str(i) #Create lookup table

for i in range(1, len(dataz)-2, 4): #For each input line
	line = ''
	for j in range(0, len(dataz[i]), 3): #For each character
		identifier = ''.join([dataz[k][l] for k in range(i, i+3) for l in range(j, j+3)]) #Slice out the identifier
		line += lookup[identifier] #Look up number 
	print(line)