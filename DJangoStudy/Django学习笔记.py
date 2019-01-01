#Django Study note

安装Django :
pip 安装： 
	下载pip ： 
	https://pypi.org/project/pip/
	下载完成后解压
	解压后，去到解压目录： python setup.py install 
 
pip : 
	需要先配置环境变量： 
	python 安装目录： d:\python27 
	PYTHON_HOME = d:\python27
	path: %PYTHON_HOME%;%PYTHON_HOME%\Scripts\

安装命令： 
	pip install Django==1.5.11
	如果直接
	pip install Django 
	表示安装最新版本的 Django 
	配置 django 环境变量： 
		%PYTHON_HOME%\Lib\site-packages\django


Project Deployment: 
--=========================================
project folder : workspace/website/
app folder : workspace/website/blog/
==========================================
1 Enter project workspace 
	type : django-admin.py startproject projectname (in python 3.x , may use django-admin startproject projectName as well)

go-into website/website/  this folder 
2 update setting.py file : 
	TIME-ZONE='Asia/Shanghai'
	LANGUAGE_CODE='zh-cn'
	INSTALLED_APPS : add a website, like : blog 

3 update url.py file (add a line): 
	url(r'^blog/index/$','blog.views.index'),

	setting finished .. 
4 update file : blog.views.index : 
	add function : 

from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Hello world</h1>")
	

5 runserver : 
	goto the project folder : 
	type : 
		manage.py runserver
		# manage.py runserver 0.0.0.0:8080 
		# use 8080 port to run server.  
	mark: this command can not be used to release to production, only be used to test in development environment

6 open the website : 
	http://127.0.0.1:8000/blog/index/

#-==============================================
use html files to deploy project : 
1 in the blog/ folder : create folder : templates 
	create html files in templates/ folder 
	like index.html : 

<!doctype html>
<html lang="en">
	<head>
		<meta charset="UTF-8"> 
		<title>Document</title>
	</head>

	<body>
		<h1>Hello world in html files .. </h1>
	</body>
</html>

2 in blog/views.py file : 

# Create your views here.
from django.http import HttpResponse
from django.template import loader,Context
# use this import function to get html files in tempates/ folder 

def index(request):
	# loader : load the html files 
	t = loader.get_template("index.html")
	# context : tranfer the variable between html files and py files .
	c = Context({})
	return HttpResponse(t.render(c))

3 Access the website/blog in the website : 
	http://localhost:8000/blog/index/

--============transfer variable between heml and py files : 
1 in the views.py files : 
	c = Context({}) # Input the dictionary in the Context()

2 In the html files : 
	use {{variable_name}} to recieve the variable from the py files . 

--=============html logic statement ===================================
1 if else : 
	{% if Condition %}

	{% else %}

	{% endif%}

	remark : no else if in this logic .. 

	if not string or number: 
		when a string after if :
			it means that it will judge whether the string is empty 
		when a NUMBER after if : 
			it will judge whether the number is zero(0)

2 for : 
{% for book in booklist %}
	<li>{{book}}</li>
{% endfor %}
# in for tab , the variable : booklist no need the {{}} between the %% . 
# but in the context of the for loop , need to use {{}}

	Something abt dictionary : 
	if we want to access the key and value of the dict at the same time, we can use the keyword : item.
	like : 
	user = {"name":"Eric Wang dada","age":18,"height":171}
	{% for key,value in user.items %}
		<li>{{key}} : {{value}}</li> 
	{% endfor %}

 keyword of for loop : 
 	== reversed == 
 	reversed : reverse(反向) iteration (迭代) loop 
{% for book in booklist reversed %}
	<li>{{book}}</li>
{% endfor %}
	== empty == 
	empty : judge the variable whther it is empty：  
{% for book in booklist reversed %}
	<li>{{book}}</li>
{% empty %}
	# if the variable booklist is empty, run the program below : 
	<h2>Empty booklist!!</h2>
{% endfor %}

	the keyword above is same as : 
	==============================
{% if not booklist %}
	{% for book in booklist reversed %}
		<li>{{book}}</li>
	{% endfor %}	
{% else %}
	<h2>Empty booklist!!</h2>	
{% endif %}

	# 当前的循环number ： counter 表示正向 revcounter 表示反向
	======= forloop.counter =========
	the current loop number(begin with 1 )

	======= forloop.counter0 ============
	the current loop number(begin with 0 )

	======= forloop.revcounter ============
	the current reversed loop(minvalue is 1)

	======= forloop.revcounter0 ============
	the current reversed loop(minvalue is 1)

	======= forloop.first ============
	judge whether the forloop.counter is the first value of the loop 

	======= forloop.last ============
	judge whether the forloop.counter is the last value of the loop 

{% if booklist %}
	{% for book in booklist reversed %}
		<li>{{book}}</li>
		# Here judge this loop whether it is the first loop 
		# forloop.first will return a boolean value : true of false .
		{% if forloop.first %}
			<li>Begin</li>
		{% endif %}

		
		<li>forloop.counter : {{forloop.counter}}</li>
		<li>forloop.counter0 : {{forloop.counter0}}</li>
		<li>forloop.revcounter : {{forloop.revcounter}}</li>
		<li>forloop.revcounter0 : {{forloop.revcounter0}}</li>

		# Here judge this loop whether it is the last loop of ther whole loop 
		{% if forloop.last %}
			<li> End  </li>
		{% endif %}
	{% endfor %}	
{% else %}
	<h2>Empty booklist!!</h2>	
{% endif %}

--================Filter in the html =============================
1 in the variable in the html like {{variable_name}}
	we can use this way to filter the variable : 
		{{variable_name | upper }}
2 The filter of date : 
	{{variable_date | date:"Y-m-d"}}

3 Write the filter by ourselvies: 
	create a folder templatetags/ in the website/blog/ folder : 
	create a empty file : __init__.py in that folder .
	create the filder py files :

# Import the template folder  
# Filter files storage in the /blog/templatetags
from django import template

# No understand, may be create a register . 
register = template.Library()
def percent(value):
	return value + "%"

# register the function to filter : 
register.filter(percent)


============================
We also can do like this :
# No understand, may be create a register . 
from django import template
register = template.Library()

@register.filter
def percent(value):
	return value + "%" 
--=====================Url configuration====================================
1 config the url prefix in the url.py 
	urlpatterns = patterns('blog.views',
	then you can use the function name to config the below url : 
	url(r'^blog/index/$','blog.views.index'), -- new -- > url(r'^blog/index/$','index'),
    url(r'^blog/time/$','time'),

url file： 
urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/index/$','index'),
    url(r'^blog/time/$','time'),
)


2 management of the url files : 
	we can separate the url like : 
	In the second urlpatterns, need to add a + to knew it is the second urlpatterns

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/index/$','index'), 
)

urlpatterns += patterns('blog.views',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)), 
    url(r'^blog/time/$','time'),
)


3 Take the urls files to the app folder , like blog/
	urls file in website project folder : 

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include('blog.urls')), 
)



	urls file in the blog/ folder 

urlpatterns = patterns('blog.views', 
    url(r'^index/$','index'), 
    url(r'^time/$','time'),
)


--====== transfer parameter via url =======================
1 url?parameter=value
	http://localhost:8000/blog/staffid/?name=123

	in the view.py ,use request.GET.get("parameter_name") to get the parameter value from url : 
	name = request.GET.get("name")

2 url/parameter1/p2 
	in the urls.py, need to config the url parameter first : 
	urls.py : 
	url(r'^foo/(\w+)/$','foo'),

	view.py (need to add the parameter to the function parameter): 
	def foo(request,p1):
	p1 is the parameter from the url 


3 determine the parameter name in the urls file: 
	url(r'^foo2/(?P<id>\w+)/(?P<name>\w+)/$','foo2'),

	In the view.py, the function need to determine the parameter name when define it : 
	def foo2(request,id,name):
	t = loader.get_template("foo2.html")  
	c = Context({"name":name,"id":id})
	return HttpResponse(t.render(c))

	http://localhost:8000/blog/foo2/44127258/EricWang/













