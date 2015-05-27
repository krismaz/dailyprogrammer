#It looks kind of strange, due to formating being entirely space based, but this makes more sense in terms of special cases

nn = ["","", "twenty", "thirty","fourty","fifty", "sixty","seventy", "eighty","ninety"]
nn2 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "elleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

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
			return pre + nn[i//10]
	return nn2[i]

print(ppn(input()))