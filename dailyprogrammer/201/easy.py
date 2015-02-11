#Input format is identical to challenge
from datetime import date
now = date.today()
while True:
	try:
		target = date(*map(int, input().split()))
		print('{} days from {} to {}'.format((target-now).days, now, target))
	except:
		break