def deco(aclass):
	class NewClass:
		def __init__(self,age,color):
			self.instance = aclass(age)
			self.color = color

		def display(self):
			print(self.color)
			self.instance.display()
	return NewClass

@deco
class Cat:
	def __init__(self,age):
		self.age = age

	def display(self):
		print(self.age)


if __name__ == '__main__':
	c = Cat(11,'Yellow')
	c.display()

	c2 = Cat(11,2)
	c2.display()