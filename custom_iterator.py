class Counter:
	def __init__(self,low,high):
		self.current = low
		self.last = high

	def __iter__(self):
		return self #instead of: return iter("...") - this way 'self' here is set up with 'next' below

	def __next__(self): # here we define __next__ because the 'self' returned from the __iter__ above is not an iterator yet and we'd get an error
		if self.current < self.last:
			num = self.current
			self.current += 1
			return num
		raise StopIteration

for x in Counter(0,10): # for will call the __iter__ on this instance of Counter (Counter(0,10)), __iter__ returns self and this self is here set up with the __next__ method, so it can call next over and over and over, until next returns StopIteration
	print(x)

for x in Counter(25,40):
	print(x)