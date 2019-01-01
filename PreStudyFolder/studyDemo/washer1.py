class Washer():
	clsAttr = 'Class attribute'
	def __init__(self,water=100,scour=20):
		self._water = water
		self.scour = scour
		print('Now init a washer, it\'s water is ',self._water,' and it\'s scour is ',self.scour)

	# 静态方法，不能调用 实例属性 self.attribute
	# 静态方法可以调用 类名.类变量 进行调用 attribute 
	@staticmethod
	def wash_time(times):
		print('Now set times to washer :',Washer.clsAttr)
		# print('Water is : ',self._water)
		return times*15
		
	# 装饰器，可以使得每次实例调用attribute 的时候，都能够通过这里进行调用
	# 可以在这里给 attribute 加逻辑和加工
	@property
	def water(self):
		return self._water
	
	# setter 装饰器，是的每次给 attribute 进行 setup值的时候，都能过进行逻辑判断或者加工
	@water.setter
	def water(self,water):
		if 500 >= water >= 0 : 
			self._water = water 
		else:
			print('Too much water, can not be setup !!')

	def set_water(self,water):
		self._water = water

	def set_scour(self,scour):
		self.scour = scour

	def add_water(self,water):
		self._water = self._water + water 	
		print('Added water ',water,' , now water is : ',self._water)

	def add_scour(self,scour):
	 	self.scour = self.scour + scour
	 	print('Added scour ',scour,', now scour is : ',self.scour)

	def start_washer(self,water,scour):
		print('Now washer start working, begin add scour and water now .. ')
		self.add_water(water)
		self.add_scour(scour)

if __name__ == '__main__':
	w = Washer()
	print(w.wash_time(3))