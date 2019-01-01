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

class custom(metaclass=myMeta):
	pass

if __name__ == '__main__':
	cus = custom()
	cus.info()