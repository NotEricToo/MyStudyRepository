class testClss():
	cattribute = 'class-attribu'
	def __init__(self):
		self.a=11
		self.b=10
		 

	def info(self):
		print("a : ",self.a," b : ",self.b," caatribute: ",self.cattribute)

	def amend_a(self,a):
	 	self.a = a 
	 	print("now a is : ",self.a)

if __name__ == '__main__':
	tc = testClss()
	tca = testClss()
	tc.info()
	tca.info()

	 


