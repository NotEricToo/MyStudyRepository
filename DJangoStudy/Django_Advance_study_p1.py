Django Advance Study 1 

# ==============Auth table :  User extend ========================
#
#
#
#
# ============================================================================================

# ============== 1st method : use UserProfile to extend ==========
对 Django 的User 表进行扩展：
	如： 添加 简介 description :
	
1 In models.py :
import django.contrib.auth.models import User 

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	desc = models.TextField(null=True)
	
2 In admin.py :
	we need to register our new objects to this file :

from blog.models import Student,Teacher,Group,UserProfile
from django.contrib.auth.models import User 
	
# I can not understand the function of the following function : ??????????????????????
# ???????????? 
class ProfileInline(admin.StackedInline):
	model = UserProfile 
	verbose_name = 'profile'

# ???????????? 
class UserAdmin(admin.ModelAdmin):
	inlines = (ProfileInline,)
	
# In the code itself, the user has been registered, so we need to unregsiter it first 
admin.site.unregister(User)
# After unregister User, we register this 2 objects :

admin.site.register(User,UserAdmin)

After this 2 steps, we can see the desc text frame when we add a new user .. 

# ======================== 2nd method: inherit(继承) AbstractUser ======================
1 In models.py :
	import the class AbstractUser :	

from django.contrib.auth.models import AbstractUser 

# Rewrite the User class :
class User(AbstractUser):
	desc = models.TextField(blank = True,null = True)
	
2 project folder : 
	setting.py :
	add a new line in this file :
	# let the system use the User Class defined by us : 
	AUTH_USER_MODEL = 'blog.User'
	
3 In admin.py :
	we need to register our new User Class to the app : 
from blog.models import User 

admin.site.register(User)


# ================================= 2th Login extend =========================================
#
#
#
#
# ============================================================================================
	define the login function by user himself.
	we can update the login authentication 
1 define the form class in views.py 
	import the related class 
from django import forms 
from django.shortcuts import render_to_response,HttpResponseRedirect
# HttpResponseRedirect be used to go to a new page 
# Example : return HttpResponseRedirect("/blog/login")

# render_to_response : response to a page, and render some variable : 
# Example : return render_to_response('login.html',{"lf":lf})
	
class LoginForm(forms.Form):
	email = forms.CharField(max_length = 100,label = "E-Mail")
	# widget 组件
	pwd = forms.CharFIeld(max_length=100,label = "Password",widget = forms.PasswordInput)
	# This style of below function is copied by the course
def login(request):
	if ('email' or 'pwd') not in request.GET :
		lf = LoginForm()
		return render_to_response("login.html",{"lf":lf})
		
	lf = LoginForm(request.GET)
	email = lf.data['email']
	pwd = lf.data['pwd']
	try:
		user = User.objects.get(email = email)
	except User.DoesNotExist:
		return HttpResponse("No this user : " + email)
	else : 
		if user.check_password(pwd) :
			return HttpResponse("Login successfully : " + email)
	return HttpResponseRedirect("/blog/login")

	# The function below is writed by me 
def login(request):
	if ('email' or 'pwd') not in request.GET:
		lf = LoginForm()
		return render_to_response('login.html',{"lf":lf})
	try:
		user =User.objects.get( email = request.GET.get("email") ) 
	except User.DoesNotExist : 
		return HttpResponse("User not exist")
	else : 
		if user.check_password(request.GET.get("pwd")) : 
			return HttpResponse("Login successfully : " + user.email)
		else:
			return HttpResponseRedirect("/blog/login")
			
urls.py : 
	Add a new line in this file : 
url(r'^login/$','login'), 
	

	
# ==============================3rd Permission extend ==========================================	
#	Need to familar the permission system via the register method .	
#	
#
#
# ===============================================================================================
1 add a register page (similar as the login page) 

# register.html 
<!doctype html>
<html lang="en">
	<head>
		<meta charset="UTF-8"> 
		<title>Document</title>
	</head>

	<body>
		<h1>Welcome to register page .. </h1>
		<form method = "get" entype = "multipart/form-data">
		{{lf}}
		<input type = "submit" value = "ok">
		</form>
	</body>
</html>

# Under the object need to be add permission : 
	
	class Meta:
        db_table = 'student'
        permissions = (("can_see_student","Can see student .. "),
        				("can_add_student","Can add student .."),
        				("can_update_student","Can update student .. "),
        				("can_delete_student","Can delete student .. "))
						
# In views.py : 
# Import the permission to the file :
from django.contrib.auth.models import Permission 

when login , after check the password , we can add some permission checking there .. 
if user.check_password(pwd) :
	if user.has_perm("blog.can_see_student"):
		return HttpResponse("Login successfully : " + email + " and you have the permissoin to see student .. ")
	return HttpResponse("Login successfully : " + email)

permission setting : 
user.user_permissions = [Permission.objects.get(codename = "can_see_student"),Permission.objects.get(codename = "can_update_student")]
				
# ==============================4th (Init the common model)初始化公共模块  ==========================================	
#	 
#	
#
#
# ===============================================================================================

# Base.html :
<!doctype html>
<html lang="en">
	<head>
		<meta charset="UTF-8"> 
		<title>{{title}}</title>
		# Block is the common block tab 
		# 块的标签
		{% block head_css %}
			<link src="base.css"/>
		{% endblock%}
		{% block head_js %}
			<link src="base_head.js"/>
		{% endblock%}
	</head>

	<body>
		{% block header %}
			 
		{% endblock%}
		{% block container %}
			 
		{% endblock%}
		{% block footer %}
			 
		{% endblock%}
		{% block foot.js %}
			 <link src="base_foot.js"/>
		{% endblock%}
	</body>
</html>

# login.html : 
{% extends "base/base.html" %}

{% block header %}
	<h1>Welcome to login html .. </h1>		 
{% endblock%}
{% block container %}
		<form method = "get" entype = "multipart/form-data">
		{{lf}}
		<input type = "submit" value = "ok">
{% endblock %}


# ============================== 5th user-defined tag in html  ==================================	
#	 
#	
#
#
# ===============================================================================================
1 create a templatetags/ folder in app folder . 
	in templatetags/ folder, create 2 python files (the tag file you need and the empty init file : __init__.py) :
	excample : 
	upper.py :

from django import template 

register = template.Library()

class UpperNode(template.Node):
	def __init__(self,nodelist):
		self.nodelist= nodelist 
		
	def render(self,context):
		content = self.nodelist.render(context)
		return content.upper()

@register.tag
def upper(parser ,token):
	nodelist = parser.parse("endupper")
	parser.delete_first_token()
	return UpperNode(nodelist)
	
2 In html files :
# need to load the tag first :
{% load upper %}
{% upper %}
xxx 
{% endupper %}
	
# ============================== 6th user-defined filter in the html   ==================================	
#	 
#	
#
#
# ===============================================================================================	
1 in the variable in the html like {{variable_name}}
	we can use this way to filter the variable : 
		{{variable_name | upper }}
2 The filter of date : 
	{{variable_date | date:"Y-m-d"}}

3 Write the filter by ourselvies: 
	create a folder templatetags/ in the website/blog/ folder : 
	create a empty file : __init__.py in that folder .
	create the filder py files : percent.py:

# Import the template folder  
# Filter files storage in the /blog/templatetags
from django import template

# No understand, may be create a register . 
register = template.Library()
@register.filter
def percent(value):
	return value + "%"

===== environment variable :
in setting.py :
example:
IS_DELVELOP = True 

in other python files (import the variable from the setting file):
from blog.setting import IS_DELVELOP

# Then we can use  IS_DELVELOP in this python file .. 















	
	
	




	














