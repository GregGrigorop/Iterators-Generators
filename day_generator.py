def week():
	days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	count = 0
	while count <= 6:
		yield days[count]
		count += 1

days = week()
print(next(days))
# for i in days: # if this is used we don't get a StopIteration
	# print(i)
for i in range(7):
	print(next(days))