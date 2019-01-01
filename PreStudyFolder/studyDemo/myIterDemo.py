class myIter:
	def __init__(self,start,end):
		print('Init Iter ')
		self.count = start
		self.end = end 

	def __iter__(self):
		print('Iter -- ')
		return self 

	def __next__(self):
		if self.count < self.end :
			print('If -- ') 
			r = self.count 
			self.count += 1 
			return r 
		else : 
			raise StopIteration 

if __name__ == '__main__':
	for i in myIter(1,10) : 
		print(i)


