import tkinter
import threading
import time
class Shape:
	def __init__(self,cvns,points):
		self.cvns = cvns
		self.points = points
		self.pid = None

	def delete(self):
		if self.pid : 
			self.cvns.delete(self.pid)

class DrawCircle(Shape):
	def draw(self):
		self.pid = self.cvns.create_oval(*self.points)

class Game : 
	gFlag = True
	j = 1
	k = 1
	def __init__(self,cvns,root,points,size = 2):
		self.root = root
		self.cvns = cvns 
		self.points = points
		self.size = size 
		self.r = self.size / 2
		self.points.append(self.points[0] + self.size)
		self.points.append(self.points[1] + self.size)
		self.circle = DrawCircle(self.cvns,self.points)
		 
		 
	def move(self):
		if self.points[1]>=500 : 
			self.j = -1 * self.j 
		elif self.points[1] <=10 : 
			self.j = 1

		if self.points[0] >= 500 : 
			self.k = -1*self.j
		elif self.points[0] <= 10 :
			self.k = 1

		x1 = self.points[0] + self.size*self.k
		y1 = self.points[1] + self.size*self.j
		x2 = self.points[2] + self.size*self.k
		y2 = self.points[3] + self.size*self.j
		return x1,y1,x2,y2   

	def walk_step(self):
		self.points = self.move()
		self.circle.delete() 
		self.circle = DrawCircle(self.cvns,self.points)
		self.circle.draw()

	def run(self):
		while self.gFlag :   
		# for i in range(10):
			self.walk_step()
			print(self.points)
			self.root.update() 
			time.sleep(0.4)
			 
			



if __name__ == '__main__':
	root = tkinter.Tk()
	cvns = tkinter.Canvas(root,width=600,height=665,bg='white')
	cvns.pack() # 开始布局
	g = Game(cvns,root,[300,10],30)
	t = threading.Thread(target=g.run)
	t.setDaemon(True)
	t.start()
	root.mainloop()
