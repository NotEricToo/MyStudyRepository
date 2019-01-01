Django database study
sqlite3:
--=========================================
project folder : workspace/website/
app folder : workspace/website/blog/
==========================================
in app folder , exists a models.py file , all database models storage here. 
	every class be defined in models.py, need to dependece the parent class models.Model:

class Student(models.Model):
	stu_id = models.CharField(max_length = 20 )
	stu_name = models.CharField(max_length = 100)
	stu_age = models.IntegerField()
	class Meta:
		db_table = 'student'
		# this code will determine the table name in the database . 
config the databse setting : 
	open setting.py file : 
	update the info in (when use sqlite3 as a database, only need to config the ENGINE(引擎) and NAME parameter ):

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'blogdb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

== If use mysql :
pip install pymysql

== project_folder:
== __init__.py : 

import pymysql
pymysql.install_as_MySQLdb()


then go into project folder : 
	manage.py syncdb
	this command will create a database file in the project folder 
	/workspace/website/blogdb
	this file is a database file, we can open this file with the tool SQLiteStudio2.1.5.exe ;

sync the new db table to the models.py file : 
	execute command : manage.py inspectdb
	this command will display all models classes to the monitor
	execute command : manage.py inspectdb > blog/models.py 


--==================get db data from class object ( single table query )===========
1 import class in views.py 
from blog.models import Student

2 use ClassName.objects.all() to get all data from table in db 
stu_list = Student.objects.all()

example : 
def student_list(request):
	t = loader.get_template("student_list.html")  
	# Student.objects.all() to get all data from table in database .. 
	stu_list = Student.objects.all()
	c = Context({"stu_list":stu_list})
	return HttpResponse(t.render(c))

in html file, we can use forloop to output the student list : 

{% for i in stu_list %}
 	<h2>student id is : {{i.stu_id}}</h2>
 	<h2>student name is : {{i.stu_name}}</h2>
 	<h2>student age is : {{i.stu_age}}</h2>
{% endfor%}

3 if we want to order the data order by some fields.
	we can use this way : 
		stu_list = Student.objects.all().order_by("stu_age")
		stu_list = Student.objects.all().order_by("stu_age","stu_id")
	if want to desc order the data :
		stu_list = Student.objects.all().order_by("-stu_age")

4 if we want to use filter to filter data :
	# age = 18
	stu_list = Student.objects.filter(stu_age = 18 )
	# age >= 18
	stu_list = Student.objects.filter(stu_age__gte = 18 )
	# age > 18 
	stu_list = Student.objects.filter(stu_age__gt = 18 )
	# age <= 18 
	stu_list = Student.objects.filter(stu_age__lte = 18 )
	# age < 18 
	stu_list = Student.objects.filter(stu_age__lt = 18 )

	__contains = like '%%'
	stu_list = Student.objects.filter( stu_name__contains = "Eric" )

	__exact = like 'aaa'

	__iexact = 忽略大小写的 like 'aaa'

	__icontains = 忽略大小写的 like '%%'

	__gt = > 
	__gte = >= 
	__lt = < 
	__lte = <= 

	__startswith = "aa" = like 'aa%'
	__istartswith = 忽略大小写的 like 'aa%'
	__endswith = like '%a'
	__iendswith = 忽略大小写的 like '%a'

	__range 在。。范围内
	__year 日期字段的年份
	__month 日期字段的月份
	__day 日期字段的日
	__isnull = True/False 

	===== filter ：
	parameter in fiter is a dictionary : 
	wargs = {}
	wargs["id"] = 1 
	wargs["stu_name"] = "eric"
	User.objects.filter(**wargs)
	
	
	
	Normal query function :
	User.objects.get(id=10)
	User.objects.filter(id < 10 )
	User.objects.all() # Get all users 
	User.objects.exclude() # 除开
	User.objects.all().order_by("field name") # Order by a field 
	User.objects.all().distinct().values("field_name")
	
	# ======================== 聚合函数:  annotate  ====== 
	聚合函数:  annotate : 
	User.objects.all().annotate(comment_count=Count('comment')).order_by('-comment_count')
	
	
	
	[0:10] # 偏移量，取 0-10 个
	example : 
	User.objects.filter(id < 10 ).distinct().values("field_name").order_by("field_name")[1:100]
	非运算: 
	from django.db.models import Q 
	User.objects.filter(Q( id = 1)|Q(name = "ELI"))
	
5 get one object :
	student = Student.objects.get(stu_id = 1)

6 update the data in database with the function in views.py 
def student_list(request):
	t = loader.get_template("student_list.html")  
	student = Student.objects.get(stu_id = 1 )
	student.stu_name = "Tom"
	student.stu_age = 3
	student.save()
	# This function will update the data into database 
	c = Context({"student":student})
	return HttpResponse(t.render(c))

7 updata a lot of data : 
	student = Student.objects.filter(stu_age__lt = 30 ).update( stu_name = "Tom") 


8 Insert a new record into table :
new_stu = Student(stu_id = 10,stu_name = 'Jerry',stu_age = 31)
new_stu.save()
# Be Similar to the update method, use instance.save() method to update/insert the records in database.. 

9 delete records in the database : 
	del_stu = Student.objects.get(id=1)
	del_stu.delete()
	# instance.delete() method to delete records in the database . 

10 批量 delete records in the table : 
	Student.objects.filter(stu_id = 10).delete()
	Student.objects.all().delete() # this will delete all records in the table 

--=================database one related many and many to many relationship =============
1 one to many :

# One Side
class Teacher(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length = 50)
	class Meta:
		db_table = 'teacher'

# Many Side 
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    stu_id = models.CharField(max_length=20)
    stu_name = models.CharField(max_length=100)
    stu_age = models.IntegerField()
    # define a foreignkey to relate to the one side table 
    # this need to be defined in the many this side .. 
    teacher = models.ForeignKey(Teacher,related_name = "foreignkey_name")
	# student instance can use teacher.field_name to get teacher sets.
	# teacher instance can use teacher.foreignkey_name.filter() to get student set ..
    class Meta:
        db_table = 'student'

In this case, one teacher to many student .. 
so, 
	1 student -> 1 teacher 
	1 teacher -> many student 

we want to get the teacher name of one student : 
	in html file : 
	student.teacher.name
	can get the teacher name 
	student.teacher : This is a teacher instance .. 

In case we want to get all students according to the teacher: 
	teacher = Teacher.objects.get(id = 1 )
	student_list = teacher.teacher.all()
	or : 
	student_list = teacher.student_set.all()
	# This can get all student of  teacher who's id = 1 

if we do not define the foreignkey name in the student class, 
	it will define a default name of the foreignkey name : student_set. 
	mean it will create a foreignkey name by class name : classname_set  .. 

How to add a new records to the table which is one to many : 
	student = Student(xxx)
	teacher.student_set.add(student)


2 Many to Many:
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    stu_id = models.CharField(max_length=20)
    stu_name = models.CharField(max_length=100)
    stu_age = models.IntegerField()
    # define a foreignkey to relate to the one side table 
    # this need to be defined in the many this side .. 
    teacher = models.ForeignKey(Teacher,related_name = "foreignkey_name")
    class Meta:
        db_table = 'student'

class Group(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length = 50)
	# This means the field to relate the table student .. 
	member = models.ManyToManyField(Student,through = "MemberShip")
	class Meta:
		db_table = 'group'


# This is the relationship table
# have 2 foreignkey in this table 
# This table is not necessary, if we do not define this class here, database will create this table automaticly
# But if database create this table itself, the table name will not be the name we want.
# So the best is we define this class here by ourself..
class MemberShip(models.Model):
	id = models.IntegerField(primary_key=True) 
	student = models.ForeignKey(Student)
	group = models.ForeignKey(Group)

	class Meta:
		db_table = 'membership'

The method to get records list just be similar to the case one to many .
	student_list = group.member.all()
	or : 
	group_list = student.group_set.all()



=========================Django admin ========================================================
1 uncomment the admin info in the setting.py and urls.py : 
setting.py : ('django.contrib.admin',)

INSTALLED_APPS = (
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.sites',
'django.contrib.messages',
'django.contrib.staticfiles',
'blog',
# Uncomment the next line to enable the admin:
'django.contrib.admin',
# Uncomment the next line to enable admin documentation:
# 'django.contrib.admindocs',
)
	
urls.py :
# Uncomment the below code : 
from django.contrib import admin
admin.autodiscover()

url(r'^admin/', include(admin.site.urls)),

2 create database superuser in CMD :
	# when we create the database with command : manage.py syncdb , if we create the superuser at this step, we can ignore the below info and go to the 3th step :
	cd project folder :
		manage.py createsuperuser
		admin
		admin
		
3 run server and login the admin page : 
	cd project folder : 
		manage.py runserver 
	Open web browser: 
	http://127.0.0.1:8000/admin/ 
	account : admin
	password : admin
	
4 sync database table to the admin management page 
	Goto the app folder : 
	create a admin.py file :
		admin.py:
#import the admin :
from django.contrib import admin
# import the class in the models.py: 
from blog.models import Student,Teacher,Group 

# Register the class : 
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)

After the above step, sync database with command : 
cd project folder :
	manage.py syncdb 
	
	4.2 Login the website management page to look at the result :
		After this step, the tables will be showed at the admin page, but the objects do not show the object detail in the page .
		
5 Config the models.py to show object's detail info in the management page :
	Add the below function to every class which you want to show detail info in the management page .
def __unicode__(self):
	return self.field 
	# field is the variable in the class. just like Teacher Class : return self.name 
	


========================== multiple table query ===================================
1 We can do some multiple table query via the foreignkey ..
	teacher.foreignkey_set.filter(student__stu_name = "name")[1:100]
	
	or 
	
	student.objects.filter(teacher__name = "xxx")
	
============================ Use SQL to get results from database =================
1 import the related lib from django.db 

from django.db import transaction,connection

student_list = Student.objects.raw("select id,stu_id as student_id,stu_name as student_name,stu_age from student where id <= 4 ")
# use objects.raw() function to use query to get result
# raw function must include the primary key in the sql 

l1 = []
for stu in student_list :
	l1.append("<br> Student id : " + stu.student_id )
	l1.append("<br> Student name : " + stu.student_name )
	l1.append("<br> Student age : " + str(stu.stu_age) )
	l1.append("<br>" )
return HttpResponse(l1)

# The second method:
sql = 'select id,stu_id as student_id,stu_name as student_name,stu_age from student where id <= 4' 
cursor = connection.cursor()
cursor.execute(sql)
stulist = cursor.fetchall()

for i in range(len(student_list)):
	for j in range(len(student_list[i])):
		l1.append("<br> Student  info :  " + str(student_list[i][j]) ) 
	l1.append("<br>")
return HttpResponse(l1)

# When we execute the DDL like insert : 
sql = 'insert xxx'
cursor = connection.cursor()
cursor.execute(sql)
transaction.commit_unless_managed()


=========================== django 的惰性机制 =====================================
1 在 定义了如 Class_name.objects.all() 的时候，django 是不会去查询数据库的，这个时候可以对查出来的结果集进行更深入的filter
	如： 
stu_list = Student.objects.all()
stu_list = stu_list.filter( age__lte = 18)
stu_list = stu_list.filter( id__gte = 18)

当我们执行for循环去获取信息的时候，django 才会根据所有的filter 去执行数据库的查询并获取结果集

============================= 关于 class_name.objects 的 objects : 
objects 其实就是manager 的一个实例：
所以我们可以定义关于objecs的函数：
class ReviewManager(models.Manager):
	def review_count(self):
		return self.all().count()
		
class Review(models.Model):
	objects = ReviewManager()
	
就可以使用 Review.objects.review_count() 来获得条数.

============================ 关于 object.__str__ ：
当调用 str(object) 去对一个object 进行转化的时候，就会默认调用 object.__str__() 函数：
所以可以重载这个函数:
def __str__(self):
	return self.field # 返回这个对象的某一个属性 property/attribute


============================ 关于表单: 
class LoginForm(forms.Form):
	email = forms.CharField(max_length = 100,label = 'E-mail')
	pwd = forms.CharField(max_length=100,label='Password',widget = forms.PasswordInput)
	age = forms.IntegerField(label = "age:",min_value = 0,max_value = 100)
	# 在这里，有对表单的验证： 比如 max_length = 100 ， html 表单就会去验证这个 form 。
	
	# 在 class 中对表单进行验证：
	def clean_email(self):
		# 从表单中 get 到Email 
		# cleaned_data 就是相当于 request.GET
		email = self.cleaned_data.get("email").trim()
		if len(email.split('@') < 2 ) :
			raise forms.ValidationError("email is not correct")
		# 可以在这里添加其他的更多的校验。。
		return email 
		
def valid(lf)
	if not lf.is_valid():
		return xxx 
		#验证不通过直接返回，不进行操作
		
	















	
	












