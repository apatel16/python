
def do_four(f,string):
	f(string)
	f(string)

def print_twice(string):
	print(string*2)

do_four(print_twice,'spam ')