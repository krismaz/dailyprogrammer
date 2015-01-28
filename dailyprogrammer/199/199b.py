#Done and working... too lazy for IO

input = """000000000
111111111
490067715"""

display = """
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
"""

[print(s) for k in input.split() for l in range(1, 94, 31) for s in [''.join([display[i] for n in k for i in range(l+int(n)*3,l+int(n)*3+3)])]]
