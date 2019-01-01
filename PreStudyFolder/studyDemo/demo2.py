class A: 
		clsAttr = 'Test'
		def __init__(self):
			print('Init method !!!')

		@classmethod
		def print_a(cls):
			print('Now init the instance A !!, and attribute is : ',cls.clsAttr)

a = A.print_a()
