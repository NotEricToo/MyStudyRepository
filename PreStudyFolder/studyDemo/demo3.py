class test:
	def __init__(self):
		print('Init method')

	def __new__(cls,*args,**xargs):
		print('New instance method')
		return object.__new__(cls,*args,**xargs)

if __name__ == '__main__':
	t = test()