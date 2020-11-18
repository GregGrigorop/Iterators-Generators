def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num

# OR
# def get_unlimited_multiples(num=1):
# 	next_num = num
# 	while True:
# 		if next_num%num == 0:
# 			yield next_num
# 			next_num += 1
# 		else:
# 			next_num += 1

tens = get_unlimited_multiples(10)
for i in range(5):
	print(next(tens))
ones = get_unlimited_multiples()
for i in range(12):
	print(next(ones))