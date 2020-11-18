def make_song(count=99,beverage='soda'):
	c = 0
	r = count
	while c <= count:
		if r == 1:
			yield f"Only 1 bottle of {beverage} left"
			c += 1
			r = 0
		elif r == 0:
			yield f"No more {beverage}!"
			c += 1 # if I don't add this line the loop becomes infinite
		else:
			yield f"{r} bottles of {beverage} on the wall"
			r -= 1
			c += 1

default_song = make_song()
for i in range(100):
	print(next(default_song))
north_song = make_song(10,'North')
for i in north_song:
	print(i)
for i in range(11):
	print(next(north_song))