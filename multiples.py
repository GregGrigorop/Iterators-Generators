def get_multiples(num=1,c=10):
	# if n > 0:   (what about negative multiples?)
		a = 0
		num2 = num
		while a < c:
			if num2%num == 0:
				yield num2
				num2 += 1
				a += 1
			else:
				num2 += 1

multiples_two = get_multiples(2,3)
for i in multiples_two:
	print(i)
default_multiples = get_multiples()
multiples_5 = get_multiples(5,6)
l = []
for i in range(6):
	l.append(next(multiples_5))
print(l)
# OR
for i in range(11): # this results in a StopIteration (as by default c=10)
	print(next(default_multiples))