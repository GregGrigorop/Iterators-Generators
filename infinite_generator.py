def current_digit(): # we want to be getting one result at a time
	digit = (1,2,3,4)
	count = 0
	while count < 4: # OR: while True:
		if count == 3:
			yield digit[count]
			count = 0
		else:
			yield digit[count]
			count += 1

digit = current_digit()
print(next(digit))
print(next(digit))
print(next(digit))
print(next(digit))
print(next(digit))
print(next(digit))
print(next(digit))
print(next(digit))
n = int(input("To get this over with, how many times you want this to happen?\n"))
for i in range(n):
	print(next(digit))