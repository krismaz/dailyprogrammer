from math import factorial

def pascal(n,k):
	n, k = n-1, k-1
	if k>n:
		return "No such number"
	return factorial(n)//(factorial(k)*factorial(n-k))

print(pascal(*map(int, input().split())))