Python - 学习笔记

1 全局变量： 
如果想 函数内部改变全局变量的值，需要在变量前加 global :
一开始的定义不能定义在函数中
 
x = 1 
def t_var():
    global x
    print('x now is : ' + str(x))
    x = 2 
    print('x after 2 is : ' + str(x))
    return x 

t_var()
print('After return x is : ' + str(x))

result: 
After return x is : 2

=================================分割线====================================
=================================分割线====================================
2 函数默认参数： 
def function_name(arg1 , arg2 = 2 ):
  xxx

表示在 arg2 没有指明值的情况下，默认给 2 ，
调用的方式： 
function_name(1)
function_name(1,2)

=================================分割线====================================
=================================分割线====================================
3 带星号(*)的参数
def duoge(arg1,*arg2,**arg3):
    print('arg1 is : ' + str(arg1))
    print('arg2 is : ' + str(arg2))
    print('arg3 is : ' + str(arg3))
    
duoge('123',4,5,6,a=1,b=2)
解析:  
1个星号（*）表示： 会把参数作为tuple(不可改变的 list ) 传入到函数中
2个星号（*）表示： 会把参数作为dictionary（键值对 key value） 传入参数

=================================分割线====================================
=================================分割线====================================
4 if else 
if a=1 : 
  xx
elif a=2 : 
  xx
else :
  xx 

xx 

=================================分割线====================================
=================================分割线====================================
5 -- for 循环
range() -- 函数，包括左边的值不包括右边的值，即下面的例子包括1不包括100只循环99次
for i in range(1,100) : 
  xx
else: 
  xx 

-- list
tlist = [a,b,c,d,e]
for i in tlist :
  print(i)
else:
  print('b')

for i in variable(variable 可以是 list 也可以是 tuple，也可以是 dictionary, 如果是 dict 会选择key进行循环)

-- dict :
t_dict = {'a':1,'b':2,'c':3}
for i,j in t_dict.items() : 
    print(i,j)
=================================分割线====================================
=================================分割线====================================
6 dictionary.items() : 
获得字典的key 和 value。
承接第五个
=================================分割线====================================
=================================分割线====================================
7 控制流 break continue pass 
  break : 跳出整个循环
  continue : 跳出本次循环
  pass : 直接跳过本行代码，继续往下执行（没有跳出或者跳过单次循环）
=================================分割线====================================
=================================分割线====================================
8 boolean : 
true : 1 
false : 0 
not 0 = true --> 所有非0，可以视为true（在not number 中）

=================================分割线====================================
=================================分割线====================================
9 output string : 
    1 :print('This is string1' + str(str1) + ' and this is str2 : ' + str(str2))
    2 : print('this is string1 {0} and this is string2 {1}'.format(str1,str2))
    3 :print('this is string1 {} and this is string2 {}'.format(str1,str2))
=================================分割线====================================
=================================分割线====================================
10 exception handing(错误处理) : 
try:
  xxx
except  exception as err: -- exception 表示所有的 exception  
  print(err)
=================================分割线====================================
=================================分割线====================================
11 类
__init__ :构造函数，默认创建实例的时候执行
self : 实例本身的意思，创建类的时候不需要传这个参数

=================================分割线====================================
=================================分割线====================================
12 装饰器
def add_lz(cake_func):
    def insert_lz():
        return cake_func() + ' add lazhu la !!!'
    return insert_lz

@add_lz
def make_cake():
    return 'cake'
     
# make_cake = add_lz(make_cake)
print(make_cake()) 

解析: 表示调用 make_cake 的时候，把make_cake 作为参数，调用@所在的函数 

=================================分割线====================================
=================================分割线====================================
13 GUI 简单笔记： 
使用 GUI 需要 import 包
from tkinter import * 
import tkinter.simpledialog as dl 
import tkinter.messagebox as mb 

每次使用前需要init 一个入口，可以用 showinfo 或者 label 。
mb.showinfo('Hello Man','Welcome to Guess Number Game!')
or: 
root= Tk()


w=Label(root,text="Welcome to Guess Number Game!")
w.pack() 

# pack 函数是一个布局函数，默认从左上方开始 

然后才可以用 dl.askxxx 来获取用户输入

=================================分割线====================================
=================================分割线====================================
14 sublime 上执行python :
  1 menu->preferences->browse package
  2 new folder -> rename to python
  3 go into python folder
  4 create a file and rename it to Python.sublime-commands
  5 open Python.sublime-commands file and type below info into the file :
{
"cmd":["python.exe", "-u", "$file"],
"path":"D:\Python37",
"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
"selector": "source.python"
}
  6 update the path of above to the python path you install 
  7 menu->tools->build system->Python
  8 finished   -- You can use ctrl+B to run your python program 

=================================分割线====================================
=================================分割线====================================
15 私有属性： 
以双下划线定义的属性： __ab (类内可以访问，是由于在初始化后，默认改变类私有属性的名称，所以在类外继续以 __ab 访问的话，是无法访问到这个属性的)
以单下划线定义的属性：_ab(类及其子类可以访问--外部仍然可以访问，只是标志性的，没有特殊的限制，自己想访问仍然可以访问)

=================================分割线====================================
=================================分割线====================================
16 特殊属性： 
  __doc__ : 文档属性，保存类的介绍
  __name__ : 类的名称
  __dict__ : 类的属性名及值，类似字典
 __module__ : 保存类的模块名
  __base__ : 类的父类

使用 dir(类名) 可以知道所有的特殊属性。

=================================分割线====================================
=================================分割线====================================
17 类的方法的定义： 
class A:
  def funA(self):
    xxx
function 中，self 是必须的。


=================================分割线====================================
=================================分割线====================================
18 实例属性和类属性： 
  定义在类中且在类的方法之外的属性，叫做类属性。
  定义在类中且定义在类的构造函数(__init__)中的属性，为实例属性。
  实例属性，必须在类被实例化之后，才能够引用，否则报错。
  类属性，只能通过 类名.属性名 进行调用。
  如果类属性和实例属性同名，使用 实例名.属性 调用的是实例属性。

=================================分割线====================================
=================================分割线====================================
17 通过函数进行属性的设置，取值，以及判断是否存在：
hasattr(object_name,attr)
getattr(object_name,attr)
setattr(object_name,attr)
例子:
class A:
  def __init__(self):
self.a = 10
a = A()
getattr(a,'a')
注意 'a' 是以字符串的形式进行调用的。 

=================================分割线====================================
=================================分割线====================================
18 属性使用装饰器： 
class Washer():

	def __init__(self,water=100,scour=20):
		self._water = water
		self.scour = scour
		print('Now init a washer, it\'s water is ',self._water,' and it\'s scour is ',self.scour)

	@property
	def water(self):
		return self._water
	
	@water.setter
	def water(self,water):
		if 500 >= water >= 0 : 
			self._water = water 
		else:
			print('Too much water, can not be setup !!')

        def set_water(self,water):
		self._water = water

在外面想调用_water，直接调用 water 即可。
w = washer()
print(w.water)
w.water=100
print(w.water)

属性包装如果想要既能读取也能设置的话，
@property
@attribute_name.setter
两个装饰器都需要设置。

属性包装： 
 -   把类中的方法，以属性的形式展现给用户。 即以上例子中的 water属性。
 -  属性包装使用装饰器 @property 可以虚拟一个虚拟属性，其实它是类里面的一个方法。
  如(假设500是water上限)： 
@property
def remain_water(self):
  return 500-self._water

w.remain_water 即可获得还可添加的水量。

=================================分割线====================================
=================================分割线====================================
19 描述符： 
数据描述符： 调用了 get set delete 3个全部都方法。
非数据描述符，调用了 get set delete 3个中部分函数的方法。

描述符必须作为另一个类的类属性：
class NonNeg:
    def __init__(self):
        xx
    def __get__(self,instance,owner):
        xx 
   def __set__(self,instance,val):
       xx
  def __delete__(self,instance):
       pass 
  
class Movie:
   rate = NonNeg()
   score = NonNeg() -- 描述符 这里的作用，避免在此处定义多个 get set  方法。

m = Movie()
m.rate = 1 -- 通过 NonNeg()  进行设置，调用 __set__ 方法。

所有的类成员函数(定义在类中的函数)都是非数据描述符。
同名的实例属性，即 m.rate ，可以掩盖类中的 rate函数。
如果类中定义了 __call__(self) 函数，那么实例也可以直接使用 instance_name() 进行调用。



============== 字符串截取：
str = ‘0123456789’
print str[0:3] #截取第一位到第三位的字符
print str[:] #截取字符串的全部字符
print str[6:] #截取第七个字符到结尾
print str[:-3] #截取从头开始到倒数第三个字符之前
print str[2] #截取第三个字符
print str[-1] #截取倒数第一个字符
print str[::-1] #创造一个与原字符串顺序相反的字符串
print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
print str[-3:] #截取倒数第三位到结尾
print str[:-5:-3] #逆序截取，具体啥意思没搞明白？

012
0123456789
6789
0123456
2
9
9876543210
781
789
96


