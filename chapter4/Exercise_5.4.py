
def is_triangle(side1, side2, side3):
	if ((side1+side2) > side3) or ((side2+side3) > side1) or ((side3+side1) > side2):
		print('NO')
	else:
		print('YES')


a = input('a :')
b = input('b :')
c = input('c :')

is_triangle(int(a), int(b), int(c))