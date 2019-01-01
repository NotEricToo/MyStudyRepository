1 单例模式： 
	某一个类，只有一个实例存在。
	验证: 
	用一个类，去实例化多个实例，使用 id(instance) 进行验证
	结果： 同一个类对应的 id 是同一个。

# --==============================================================================
# --============================ 分割线 ===========================================
# --==============================================================================
2 工厂模式： 
	即通过 超类 ， 提供一个抽象化的接口，用于创建特定类型的对象。
	例子： 
class Person:
	def __init__(self):
	    self.name = None
	    self.gender = None

	def getName(self):
	    return self.name

	def getGender(self):
	    return self.gender

class Male(Person):
	def __init__(self, name):
	    print "Hello Mr." + name

class Female(Person):
	def __init__(self, name):
	    print "Hello Miss." + name

# 通过这个超类， 对 Male 和 Female 进行实例化。
class Factory:
	def getPerson(self, name, gender):
	    if gender == 'M':
	            return Male(name)
	        if gender == 'F':
	        return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Chetan", "M")

# --==============================================================================
# --============================ 分割线 ===========================================
# --==============================================================================

3 策略模式（封装代码，灵活替换）： 
    网上的定义： 
    策略模式也是常见的设计模式之一，它是指对一系列的算法定义，并将每一个算法封装起来，而且使它们还可以相互替换。策略模式让算法独立于使用它的客户而独立变化。 

    自己的理解： 
	只要多个类中，拥有相同名字的方法，就可以通过策略模式，对该名字的类进行不同类中方法的调用。
	即， 把一系列的算法，封装在不同的类或者函数中，通过调用这些方法，实现算法之间的相互替换。 
	实现: 把类或者函数作为某个参数传入到策略模式定义的函数或者类中进行实现。

	例子1 ： 把 类 作为参数进行传递实现策略模式: 
	# 只要类中含有 move 函数，就可以通过调用以下类的实例，对某个 move 函数进行调用：
class moveObj:
	def set_move(self,movefunc):
		self.movefunc = movefunc()

	def move(self):
		self.movefunc.move()

class A:
	def move(self):
		print('A .. move ..')

class B : 
	def move(self):
		print('B .. move .. ')

if __name__ == '__main__':
	m = moveObj()
	# 这里定义 m 的move 函数为 A的move函数
	m.set_move(A)
	m.move()
	# 这里定义 m 的 move 函数为 B 的 move 函数
	m.set_move(B)
	m.move() # 此处调用的就是B的move函数

例子2 把 函数 作为参数进行传递实现策略模式（封装代码，灵活替换）： 

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

# --==============================================================================
# --============================ 分割线 ===========================================
# --==============================================================================

4 装饰模式： 
	可以不以继承的方式而动态地修改类的方法。 
	可以不以继承的方式而返回一个被修改的类

例子 1 （使用装饰模式，对原来的类 A 进行类似继承的修改）： 
class A:
	def func_a(self):
		print('a .. ')

class B :
	def __init__(self,cla):
		self.cla = cla()

	# 重写 原来的类的该函数，进行修改。
	def func_a(self):
		print('Updated .. ')
		self.cla.func_a()

if __name__ == '__main__':
	a = A()
	a.func_a()
	# 使用装饰对原来的类进行修改的 设计模式
	b = B(A)
	b.func_a()


例子 2 通过继承装饰类进行修改
class Water:
	def __init__(self):
		self.name = 'water'

	def show(self):
		print(self.name)

class Deco:
	def show(self):
		print(self.name)

class Sugar(Deco):
	def __init__(self,water):
		self.name = 'sugar'
		self.water = water 

	def show(self):
		print(self.name)
		print(self.water.name)

class Salt(Deco):
	def __init__(self,water):
		self.name = 'salt'
		self.water = water 

	def show(self):
		print(self.name)
		print(self.water.name)

if __name__ == '__main__':
	w = Water()
	s = Sugar(w)
	s.show

	类装饰器： 




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