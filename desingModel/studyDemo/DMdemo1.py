# class moveObj:
# 	def set_move(self,movefunc):
# 		self.movefunc = movefunc()

# 	def move(self):
# 		self.movefunc.move()

# class A:
# 	def move(self):
# 		print('A .. move ..')

# class B : 
# 	def move(self):
# 		print('B .. move .. ')

# if __name__ == '__main__':
# 	m = moveObj()
# 	m.set_move(A)
# 	m.move()
# 	m.set_move(B)
# 	m.move()

def movea():
	print('move a ..')

def moveb():
	print('move b ..')

class moveObj:
	def set_move(self,movefunc):
		self.movefunc = movefunc

	def move(self):
		self.movefunc()

if __name__ == '__main__':
	m = moveObj()
	m.set_move(movea)
	m.move()