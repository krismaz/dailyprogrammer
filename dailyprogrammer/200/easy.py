#Nice clean and should handle a few common tricks

n,m = map(int, input().split())
mem = [list(input()) for _ in range(m)]
x,y,c = input().split()
x,y = int(x), int(y)
base = mem[y][x]
working = {(x,y)}

if not base == c:
	while len(working) > 0:
		x, y = working.pop()
		if mem[y][x] == base:
			mem[y][x] = c
			working.update({((x-1)%n,y), ((x+1)%n, y), (x, (y-1)%m), (x, (y+1)%m)})

for s in mem:
	print(''.join(s))