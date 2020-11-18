# without a generator function
def fibonacci(n):
	l = []
	a,b = 0,1
	while len(l) < n:
		l.append(a)
		a,b = b, a + b
	return l

print(fibonacci(10))
print(fibonacci(1))
print(fibonacci(2))

# with a generator function
def fibonacci_gen(n):
	a, b = 0, 1
	count = 0
	while count < n:
		yield a
		a, b = b, a+b
		count += 1

fib = fibonacci_gen(5)
for i in fib:
	print(i)
fib = fibonacci_gen(15)
for i in range(16): # the generator will be exhausted and we'll get a StopIteration
	print(next(fib))