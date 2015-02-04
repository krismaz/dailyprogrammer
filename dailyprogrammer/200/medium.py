#Require rectangles of same character to be seperated, aquire strange solution
#Obviously, this is not how it should be solved, but it shows an alternative approach that disregards normal code structure

#Load bounds
w, h = map(int, input().split())

#Read map, pad with '.'
lines = ['.'*(w+2)]+['.'+input()+'.' for _ in range(h)]+['.'*(w+2)]

#Rotate map
lines2 = [''.join(l[i] for l in lines) for i in range(w+2)]

#Find all changes between horizotal lines by enumerating each line, and doing set difference. For each set, append the line number
h1 = frozenset((l+1, frozenset(enumerate(l2)) - frozenset(enumerate(l1))) for l, (l1, l2) in enumerate(zip(lines, lines[1:])))
#Select endpoints that are not '.', and duplicate single endpoints. Put into sorted order to have upper left before upper right
h2 = list(sorted(list((i,j,c) for i, s in h1 for j, c in s if not c == '.' and (not (j+1,c) in s or not (j-1, c) in s)) + list((i,j,c) for i, s in h1 for j, c in s if not c == '.' and (not (j+1,c) in s and not (j-1, c) in s))))
#Create dict mapping upper left to upper right
hd = dict(zip(h2[::2], h2[1::2]))

#Do the same for the rotated map, but find upper left ad lower left. Coordinates are still flipped
v1 = frozenset((l+1, frozenset(enumerate(l2)) - frozenset(enumerate(l1))) for l, (l1, l2) in enumerate(zip(lines2, lines2[1:])))
v2 = list(sorted(list((i,j,c) for i, s in v1 for j, c in s if not c == '.' and (not (j+1,c) in s or not (j-1, c) in s)) + list((i,j,c) for i, s in v1 for j, c in s if not c == '.' and (not (j+1,c) in s and not (j-1, c) in s))))
vd = dict(zip(v2[::2], v2[1::2]))

#Match triplets of points, and map back rotated coordinates
print('',*('{}x{} tile of \'{}\' located at {} \n'.format(hd[t][1]-t[1]+1, vd[(t[1], t[0], t[2])][1]-t[0]+1, t[2], (t[1]-1, t[0]-1)) for t in hd))