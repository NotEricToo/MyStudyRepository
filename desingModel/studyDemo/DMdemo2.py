class Water:
	def __init__(self):
		self.name = 'water'

	def show(self):
		print(self.name)
 

class Sugar():
	def __init__(self,water):
		self.name = 'sugar'
		self.water = water 

	def show(self):
		print(self.name)
		print(self.water.name)

class Salt():
	def __init__(self,water):
		self.name = 'salt'
		self.water = water 

	def show(self):
		print(self.name)
		print(self.water.name)

if __name__ == '__main__':
	w = Water()
	s = Sugar(w)
	s.show()