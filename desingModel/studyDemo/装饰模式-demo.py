class A:
	def func_a(self):
		print('a .. ')

class B :
	def __init__(self,cla):
		self.cla = cla()

	def func_a(self):
		print('Updated .. ')
		self.cla.func_a()

if __name__ == '__main__':
	a = A()
	a.func_a()

	b = B(A)
	b.func_a()