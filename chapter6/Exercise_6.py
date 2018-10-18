import math

def distance(x1, y1, x2, y2):
	x = x2 - x1
	y = y2 - y1
	x = x**2
	y = y**2

	ans = math.sqrt(x + y)
	return ans

def hypotenuse(x, y):
	x_square = x**2
	y_square = y**2

	hypotenuse = math.sqrt(x_square + y_square)
	return hypotenuse

dist = distance(1,2,4,6)
_hypotenuse = hypotenuse(9,13)
print(dist)
print(_hypotenuse)

