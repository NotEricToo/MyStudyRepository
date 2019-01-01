# 2 个形状，1个带角度，1个不带角度
# 不带角度
# 形状类
class Shape:
	def __init__(self,cvns,points):
		self.cvns = cvns
		self.points = points
		self.pid = None

	def delete(self):
		if self.pid :
			self.cvns.delete(self.pid)

# 带角度的 
# 形状类
class ShapeAngles(Shape):
	def __init__(self,cvns,points,angles=(10,170)):
		super().__init__(cvns,points)
		self.angles = {'start':angles[0],'extent':angles[1]}

# 帽子 顶部 圆形
class HatTop(Shape):
	def draw(self):
		# create_oval 函数是绘制 圆形 的函数
		self.pid = self.cvns.create_oval(*self.points)

# 帽子 底部 三角形
class HatBottom(Shape):
	def draw(self):
		# 这个函数 create_polygon 是绘制多边形的函数，需要传入3个点
		self.pid = self.cvns.create_polygon(*self.points)

# 帽子 整体 函数
# 帽子需要绘制， 需要delete 需要计算坐标
class Hat:
	def __init__(self,cvns,start_point,w,h):
		self.cvns = cvns
		self.start_point = start_point
		self.w = w
		self.h = h 
		self.ht = HatTop(self.cvns,self.ht_cacu())
		self.hb = HatBottom(self.cvns,self.hb_cacu())

	def draw(self):
		self.ht.draw()
		self.hb.draw()

	def delete(self):
		self.ht.delete()
		self.hb.delete()

	# 根据帽子的起始坐标计算帽子的顶部坐标和底部坐标
	# 是一个圆形
	def ht_cacu(self):
		r = self.h/3/2
		x1 = self.start_point[0] + self.w/2 - r 
		y1 = self.start_point[1]
		x2 = x1 + 2 * r 
		y2 = y1 + 2 * r 
		return x1,y1,x2,y2
	# 3 角多边形 需要给 3 个点的坐标
	def hb_cacu(self):
		x1 = self.start_point[0] + self.w / 2 
		y1 = self.start_point[1] + self.h / 3
		x2 = self.start_point[0] + self.w / 3
		y2 = self.start_point[1] + self.h 
		x3 = self.start_point[0] + self.w / 3 * 2 
		y3 = y2 
		return x1,y1,x2,y2,x3,y3 


class Sense(ShapeAngles):
	def draw(self):
		# create_arc 函数是绘制 弧形 的函数
		self.pid = self.cvns.create_arc(*self.points,**self.angles)

class Face(HatTop):
	pass

class Head : 
	def __init__(self,cvns,start_point,w,h):
		self.cvns = cvns 
		self.start_point = start_point
		self.w = w 
		self.h = h 
		# 脸部的起始坐标 左边的 ： 
		self.left_point = (self.start_point[0]+ (self.w - self.h) / 2,self.start_point[1])
		eye_points0 = self.eye0_calcu()
		dx = self.h / 3 + self.h / 9 
		eye_points1 = (eye_points0[0] + dx,eye_points0[1],
						eye_points0[2] + dx, eye_points0[3])
		self.face = Face(cvns,self.face_calcu())
		self.eye0 = Sense(self.cvns,eye_points0)
		self.eye1 = Sense(self.cvns,eye_points1)
		self.mouth = Sense(self.cvns,self.mouth_calcu(),(-10,-170))

	def draw(self):
		self.face.draw()
		self.eye0.draw()
		self.eye1.draw()
		self.mouth.draw()

	def face_calcu(self):
		x1 = self.left_point[0] 
		y1 = self.left_point[1] 
		x2 = x1 + self.h 
		y2 = y1 + self.h 
		return x1,y1,x2,y2 

	def eye0_calcu(self):
		x1 = self.left_point[0] + self.h / 6 
		y1 = self.left_point[1] + self.h / 3 
		x2 = x1 + self.h / 3 
		y2 = self.left_point[1] + self.h / 2 
		return x1,y1,x2,y2 

	def mouth_calcu(self):
		x1 = self.left_point[0] + self.h / 3
		# self.h / 6 = 眼睛长度（横向）
		# x1 = self.left_point[0] + self.h/ 2 - self/12
		# x2 = # x1 = self.left_point[0] + self.h/ 2 + self/12
		y1 = self.left_point[1] + 2 * self.h / 3 
		x2 = x1 + self.h / 3 
		y2 = y1 + self.h / 3 / 2 
		return x1,y1,x2,y2 


class BodyOutLine(HatTop):
	pass

class Button(HatTop):
	pass

class Body: 
	def __init__(self,cvns,start_point,w,h):
		self.cvns = cvns
		self.start_point = start_point
		self.w = w 
		self.h = h 
		self._button_size = 10 
		self.buttons = []
		self.bo = BodyOutLine(self.cvns,self.body_calcu())
		for pnts in self.all_button_points():
			self.buttons.append(Button(self.cvns,pnts))

	def draw(self):
		self.bo.draw()
		for bttn in self.buttons : 
			bttn.draw()

	def body_calcu(self):
		x1,y1 = self.start_point
		x2 = x1 + self.w 
		y2 = y1 + self.h 
		return x1,y1,x2,y2 

	def calcu_botton0(self):
		r = self.h / 9 / 2 
		x1 = self.start_point[0] + self.w / 2 - r 
		y1 = self.start_point[1] + r * 2 
		# y1 = self.start_point[1] 
		x2 = x1 + r * 2 
		y2 = y1 + r * 2 
		return x1,y1,x2,y2 


	def move_dy(self,points,size):
		y1 = points[1] + size 
		y2 = points[3] + size
		return points[0],y1,points[2],y2

	def all_button_points(self):
		bt0 = self.calcu_botton0()
		size = self.w / 9 * 2 
		points = []
		for i in range(4): 
			points.append(self.move_dy(bt0,i*size))
		return points

class Snow: 
	def __init__(self,cvns,points, w=150,h=450):
		self.cvns = cvns 
		self.points = points 
		self.w = w 
		self.h = h
		self.hat = Hat(self.cvns,self.points,self.w,self.h/6)
		self.head = Head(self.cvns,(self.points[0],self.points[1]+self.h/6),self.w,self.h/3)
		self.body = Body(self.cvns,(self.points[0],self.points[1] + self.h/6 + self.h/3),self.w, self.h/2)

	def draw(self):
		self.hat.draw()
		self.head.draw()
		self.body.draw()

if __name__ == '__main__':
	import tkinter
	root = tkinter.Tk()
	cvns = tkinter.Canvas(root,width=600,height=665,bg='white')
	cvns.pack()
	snow = Snow(cvns,(10,5),300,660)
	snow.draw()
	root.mainloop()
	







