#I am not a fan of this one. It's tedious, and rarely has a good solution
#Instead of tryong to aply log, I went with lookup tables and big ifs. I find they work better for this kind of problem
from datetime import *

ordinals = 'stndrdthththththththththththththththththstndrdthththththththstndrdththththththth'
months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

start, end = (date(*map(int, s.split('-'))) for s in '2022-09-05 2023-09-04'.split())
now = date.today()
diff = end-start

if start.year == now.year and end.year != now.year and diff.days < 365:
	formatting = '{1} {0}{6} - {4} {3}{7}'
elif start == end and start.year == now.year:
	formatting = '{1} {0}{6}'
elif start == end:
	formatting = '{1} {0}{6}, {2}'
elif start.year == end.year and start.month == end.month and start.year == now.year:
	formatting = '{1} {0}{6} - {3}{7}'
elif start.year == end.year and start.month == end.month:
	formatting = '{1} {0}{6} - {3}{7}, {2}'
elif start.year == end.year  and start.year == now.year:
	formatting = '{1} {0}{6} - {4} {3}{7}'
elif start.year == end.year:
	formatting = '{1} {0}{6} - {4} {3}{7}, {2}'
else:
	formatting = '{1} {0}{6}, {2} - {4} {3}{7}, {5}'


print(formatting.format(start.day, months[start.month-1], start.year, end.day, months[end.month-1], end.year, ordinals[2*start.day-2:2*start.day],ordinals[2*end.day-2:2*end.day]))