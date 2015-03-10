#Thurpers shortest addition chain. Lightning fast but, slightly off lenght at bigger numbers

from math import log2, ceil

n = 4123456

def Thurper(n,k):
	if n < 2**(k+1) and n%2==0:
		return {2} | set(range(1, 2**k, 2)) | {n}
	elif n >= 2**(k+1) and n%2==0:
		return Thurper(n//2,k) | {n}
	elif n < 2**(k+1) and n%2==1:
		return Thurper(n-(n % (2**int(ceil(log2(n))-k))), k) | {n}
	else:
		return Thurper(n-(n % 2**k),k) | {n}

def Prune(th):
	s = list(sorted(th))
	unreachable = set(s[1:])
	res = set()
	for i in range(len(s)):
		thi = s[i]
		urprunes = set()
		for j in unreachable:
			if j-thi in s[:i+1]:
				res.add(thi)
				res.add(j-thi)
				urprunes.add(j)
		unreachable -= urprunes
	return res | {s[-1]}

res = sorted(Prune(Thurper(n,2)))
print(len(res), '-',' '.join(map(str, res)))

