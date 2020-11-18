def yes_or_no():
	answer = ['yes','no'] # I came up with 'answer' as this list's name before checking Colt's solution ;)
	count = 0
	while count < 2:
		if count == 0:
			yield answer[count]
			count += 1
		else:
			yield answer[count]
			count -= 1

answer = yes_or_no()
print(next(answer))
print(next(answer))
print(next(answer))
print(next(answer))
print(next(answer))
n = int(input("To get this over with, how many times you want this to happen?\n"))
for i in range(n):
	print(next(answer))

# OR

# def yes_or_no():
# 	answer = 'yes'
# 	while True:
# 		if answer == 'yes':
# 			yield answer
# 			answer = 'no'
# 		else:
# 			yield answer
# 			answer = 'yes'

# answer = yes_or_no()
# print('//////////')
# print(next(answer))
# print(next(answer))
# print(next(answer))
# print(next(answer))
# print(next(answer))