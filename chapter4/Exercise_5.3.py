"""Exercise 5.3. Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
 		an + bn = cn

1. Write a function named check_fermat that takes four parameters—a, b, c and n—and that
for any values of n greater than 2.
checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that
		an + bn = cn
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”

2. Write a function that prompts the user to input values for a, b, c and n, converts them to
integers, and uses check_fermat to check whether they violate Fermat’s theorem.
"""


def check_fermet(a, b, c, number):
	if number > 2:
		l = a**number + b**number
		r = c**number
		if l == r:
			print('Holy smokes, Fermat was wrong!')

		else:
			print('“No, that doesn’t work.”')


a = input('Enter a : ')
b = input('Enter b : ')
c = input('Enter c : ')
n = input('Enter n : ')
check_fermet(int(a), int(b), int(c), int(n))