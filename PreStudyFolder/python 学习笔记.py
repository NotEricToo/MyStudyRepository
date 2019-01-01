python 学习笔记
==============================
python and django related version :
	django : 1.4 python : 2.5 2.6 2.7
	django : 1.7 1.8 python : 2.7 and 3.2 3.3 3.4 
	django 1.9  python : 2.7 3.4 3.5 
	
Install Python :
	In linux : 
su - root
wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz --no-check-certificate
tar -zxvf Python-3.4.3.tgz
=============================
20 静态方法
	@staticmethod 装饰的方法
	参数不需要使用self
	静态方法不能 引用或者访问 实例属性（定义在 __init__ 中的属性？，即不能使用 self.attribute）
	调用方法：
		可以直接使用 类名.方法名 进行调用
		也可以用 实例名.方法名 进行调用

21 类方法 （另外一种创建类实例的方法） : 
	@classmethod 装饰的方法
	首个参数必须提供 cls （这个cls其实相当与类名，相当于把类作为参数传入到 classmethod 中） 参数
	类方法也不能 引用或者访问 实例属性（self.attribute）这一点跟静态方法一样
	使用 classmethod 进行实例创建的时候，会跳过 __init__ 的 method 的 
	例子： 
	class A: 
		clsAttr = 'Test'
		def __init__(self):
			# 使用 classmethod 会跳过 __init__
			pass

		@classmethod
		def print_a(cls):
			print('Now init the instance A !!, and attribute is : ',cls.clsAttr)
	# 这样可以直接使用 method 进行类的定义
	a = A.print_a()

22 类的继承： 
	如果同时继承多个类，且多个类中，有的 method 同名，则根据先继承原则，默认选择先继承的类的 method 
	class A:
		def foo(self):
			print('A foo')

	class B:
		def foo(self):
			print('B foo')

	class C(A,B):
		pass

	c = C()
	c.foo() # 结果是优先使用 A 的 foo 

	调用父类的方法, 其中 super 后面必须跟上括号: () 
	super().method_name()  进行调用

23 关于元类(可以在创建一个实例的时候，默认给这个实例一些默认的属性attribute或者method方法)：
	所有的类，都是 type 类的 实例 
	可以用 isinstance 函数进行判断
	class A:
		pass 

	isinstance(A,type)
	result : True 

	每次创建实例的时候，都相当于默认使用 type 作为元类进行实例的创建

	所以可以重写自己需要的元类： 
	class myMeta(type):
		def __init__(self,name,bases,dicts):
			print('init my meta ')

		def __new__(cls,name,bases,dicts):
			# lambda 使用与创建函数 
			dicts['info'] = lambda self:print('Info method')
			# 这里必须调用父类的 new 方法进行一个实例的创建，否则你重写的方法没有创建实例的功能
			res = type.__new__(cls,name,bases,dicts)
			res.company = 'Eric company'
			return res #此处返回的就是一个实例，即可以用这个来创建实例

	# 这里指定了元类使用自己定义的元类 myMeta 
	class custom(metaclass=myMeta):
		pass

	if __name__ == '__main__':
		cus = custom()
		cus.info()


24 关于实例的初始化过程： 
	使用类实例化一个实例的时候，是分别调用了 __new__ 和 __init__ 
	__new__ ： 进行实例的创建 （其实这个new就是一个 classmethod 类方法，所以如果重载，需要传入参数 cls ）
	__init__ : 进行实例的初始化
	例子： 
	class test:
	def __init__(self):
		print('Init method')

	def __new__(cls,*args,**xargs):
		print('New instance method')
		# object 是父类，返回父类的 __new__ 进行一个 instance 实例的创建。
		return object.__new__(cls,*args,**xargs)

	if __name__ == '__main__':
		t = test()

25 类 构造序列
	如果想把1个类构造成一个序列，需要实现的方法： 
	__len__(self)
	__getitem__(self,key) # 这里的 key 就是传入的序列号
	__setitem__(self,key,value)
	__delitem__(self,key)

class mySeq:
	def __init__(self):
		self.mseq = ['I','II','III','IV']

	def __len__(self):
		return len(self.mseq)

	def __getitem__(self,key):
		if 0 <= key < 4 :
			return self.mseq[key]

if __name__ == '__main__':
	m = mySeq()
	print('Len of mySeq : ',len(m))
	for i in range(len(m.mseq)):
		print(m.mseq[i])


26 类 迭代器构造 ： 
	class myIter:
		def __init__(self,start,end):
			# 正常的 init 函数，用于初始化类的属性
			print('Init Iter ')
			self.count = start
			self.end = end 

		# 这里的 iter 函数，表明该类是一个 iter 迭代器
		def __iter__(self):
			print('Iter -- ')
			return self 

		# 定义 next 函数，迭代器每次执行完一个就会顺序去执行下一个 next 函数
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

27 可以重写 python 中的特殊方法： 
	如： 
	序列： 
	__len__
	__getitem__
	__delitem__
	__setitem__

	迭代器： 
	__iter__
	__next__	

	比较函数： 
	__lt__ 
	__le__
	__gt__ 
	__ge__ 
	__eq__
	__ne__ 

	可运算类： 
	__add__
	__sub__
	__mul__
	__div__

	关于 add 的例子： 
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
	# 这里的 myAdd 函数，一定要使用self 作为参数，不能忽略self 而定义3个参数作为函数的参数
	# 原本想的是 def myAdd(self,ins1,ins2): 然后直接使用 myadd(p4,p5) <-- 不过这个貌似不行 
	# 所以直接把 myadd 改成静态函数 @staticmethod
	p6 = myPoint.myAdd(p4,p5)
	p6.info()

28 关于多态： 
	某种类型的多种表现形式。
	如继承与接口形式进行代码的重载，使得函数有多种表现形式。
	动态语言： 
		变量绑定的类型具有不确定性(说白了就是一个变量，可以定义成 integer 也可以是 varchar2)
		函数和方法可以接受任何类型的参数






				


