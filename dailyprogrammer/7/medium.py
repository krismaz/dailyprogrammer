#Mandelbrot set
#Colours could use a better resolution

from PIL.Image import * 
from PIL.ImageDraw import * 

def f(z, c):
	return z**2+c


def fn(c, n):
	res = 0
	for i in range(n):
		res = f(res, c)
		if abs(res) > 2:
			return i
	return n

def col(res, n):
	if res == n:
		return (0,0,0)
	fac = res * 255 // n
	return (fac, 0, 255-fac)


w, h, nmax = 1000,1000, 255

img = new('RGB', (w, h) , (255, 255, 255))

drawing = Draw(img)


for x in range(w):
	for y in range(h):
		colour = col(abs(fn(complex((x-w/2)/(w/4), (y-h/2)/(h/4)), nmax)),nmax)
		drawing.point((x,y), fill = colour)

img.show()