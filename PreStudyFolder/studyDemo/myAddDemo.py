class point:
	def __init__(self,x,y):
		self.x= x 
		self.y = y

	def __add__(self,oth):
		#这里直接返回一个 point 的实例
		return point(self.x+oth.x,self.y+oth.y)

	def info(self):
		print(self.x,self.y)

class myPoint:
	def __init__(self,x,y):
		self.x = x 
		self.y =y 

	@staticmethod
	def myAdd(ins2,ins1):
		return myPoint(ins1.x+ins2.x,ins1.y+ins2.y)

	def info(self):
		print(self.x,self.y)	

if __name__ == '__main__':
	p1 = point(1,2)
	p2 = point(3,4)
	# 这样用一样可以
	# p3 = point.__add__(p1,p2)
	# p3 这里接收到的返回值就是一个实例，所以p3就是一个 point 的实例
	p3 = p1 + p2 	 
	p3.info()

	# 使用以下方法，一样可以实现对于特殊的加法的实现。
	p4 = myPoint(5,5)
	p5 = myPoint(1,2)
	p6 = myPoint.myAdd(p4,p5)
	p6.info()