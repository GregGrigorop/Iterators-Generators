def my_for(iterable,func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
			# func(thing) # instead of the 'else' we could use this line directly
		except StopIteration:
			break
		else:
			func(thing)

def square(x):
	print(x**2)

def square_root(x):
	print(x**(1/2))

my_for("Bulls",print)
my_for([1,2,3,4,5],square)
my_for([1,2,3,4,5],square_root)