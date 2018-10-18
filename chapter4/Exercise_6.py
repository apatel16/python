import math

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	x = dx**2
	y = dy**2
	
	ans = math.sqrt(x + y)
	return ans

dist = distance(1,2,4,6)
print(dist)