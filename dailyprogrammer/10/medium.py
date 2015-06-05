#Yes, searching a big space was, as I suspected the easiest way to do this. Luckily, the code was rather straight-forward, and some pruning could be done easily.
#It much faster than I would have expected from python search

#This is taken from 8 medium
nn = ["","", "twenty", "thirty","fourty","fifty", "sixty","seventy", "eighty","ninety"]
nn2 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def ppn(i):
	if i > 999999999:
		return("A lot")
	if i > 999999:
		return "{} million {}".format(ppn(i//1000000), ppn(i%1000000))
	if i > 999:
		return "{} thousand {}".format(ppn(i//1000), ppn(i%1000))
	if i > 99:
		return "{} hundred {}".format(ppn(i//100), ppn(i%100))
	if i>19:
		if i%10:
			return "{} {}".format(nn[i//10], ppn(i%10))
		else:
			return nn[i//10]
	return nn2[i]


#Here begins the real code
def anagram(s1, s2):
	return list(sorted(s1)) == list(sorted(s2))#Angranams

nmax = 30

for i in range(1,nmax):
	for j in range(i,nmax):#Prune
		for k in range(i,(i+j)//2):#Pruuuuune
			if i!=k and j!=k and anagram(ppn(i)+ppn(j), ppn(k)+ppn(i+j-k)):
				print('{} + {} = {} + {}'.format(i,j,k,i+j-k))
