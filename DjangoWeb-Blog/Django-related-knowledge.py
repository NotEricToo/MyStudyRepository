--=============== Django-related knowledge(Django 相关知识)

=================== 虚拟环境： virtualenv : 
	'''
	# use this to deploy the environment, 
	# we can easy to deploy the project to other environment when we migrate the project to other service.
	# 使用 virtualenv 可以简化我们的部署步骤，我们部署到 prod 的时候，可以直接把虚拟环境给拷贝到service 上直接进行部署
	# 这个 copy 相当于把我们环境需要的软件和其他配置环境同时进行拷贝到我们的 prod service 
	'''

	== Install virtualenv : 
	pip install virtualenv 
	
	== create a virtualenv in local PC : 
	cd workspace/
	virtualenv --system-site-packages blog_projectenv
	
	== Go into the virtualenv :
	blog_projectenv\Scripts\activate
	
	== Install software :
	pip install django 
	
	
===================== pycharm related :
create a django project :
Base interpreter :
blog_projectenv\Scripts\python.exe 

Location : 
select a workspace location and add the project name behind the location :
E:\Study\python\workspace\MyGit\shop_project

More Settings:
Application name:
shop 


==


	
======================== staticfiles setting ... 
== files transfer :
	# Put all static html files to /static/ folder。
== settings.py 
STATICFILES_DIRS = (
	os.path.join(BASE_DIR,'static'),
)

== index.html ：
{% load static %} # at line 1 
<link rel="stylesheet" type="text/css" href="{% static 'css/materialize.css' %}">
	
	# After this setting, we can access the index.html 

========================== logging setting ;
settings.py :
# Here's a fairly complex setup of logging .
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'special': {
            '()': 'project.logging.SpecialFilter',
            'foo': 'bar',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['special']
        },
		'default': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['special']
        },
		'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler', 
			'filename':os.path.join(BASE_DIR,'log/error.log'),
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'myproject.custom': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'filters': ['special']
        },
		'blog.views': {
            'handlers': ['default','error'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


''' 


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'error': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR,'log/error.log'),
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['error','console',],
            'level': 'DEBUG',
            'propagate': True,
        },
        'blog.views': {
            'handlers': ['console',],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


'''
# above setup of logging can be use, but only have console and error file log setup . 


	# How to use the logging filter blog.views. 
	# views.py : 
import logging 

logger = logging.getLogger('blog.views')


try : 
	pass
except exception as e : 
	logger.error(e)
	
================================ settings.py 全局变量设置：
# In settings.py, we can define some variables in the file. 

SITE_NAME='Ericla Blog'

# In views.py, we can define a global function to return this variable to the html page:
from django.conf import settings

def global_setting(request):
	SITE_NAME = settings.SITE_NAME
	return locals()

	== add the settings to settings.py :
# In settings.py :
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
				# ====================================================
				# add the below line :
				'blog.views.global_setting',
				# ====================================================
            ],
        },
    },
]

	== In html, we can use {{ variable_name }} to access the variable: 
# html: 
<p> {{ SITE_NAME }} </p>







===================== database: 
== createj user django :
create user 'django'@'%' identified by 'django';

create database blog_db charset=utf8;

grant all privileges on blog_db.* to django@'%' identified by 'django' ;
grant all privileges on shop.* to django@'%' identified by 'django' ;


===========================  关于分页：
== paginator:
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

article_list = Article.objects.all()
paginator = Paginator(article_list,10)
try:
	page = request.GET.get('page',1)
	article_list = paginator.page(page)
except (EmptyPage,InvalidPage,PageNotAnInteger) :
	article_list = paginator.page(1)
	




<div id = "xxx">
	<ul id="">
	{% if article_list.has_previous %}
		<li class="" ><a href="?page={{article_list.previous_page_number}}">&laquo;上一页</a></li>
	{% else %}
		<li class="">&laquo;上一页</li>
	{% endif %}
	<li class="active">{{ article_list.number }}/{{ article_list.paginator.num_pages }}</li>
	{% if article_list.has_next %}
		<li class="" ><a href="?page={{article_list.next_page_number}}">&laquo;下一页</a></li>
	{% else %}
		<li class="">&laquo;下一页</li>
	{% endif %}
	</ul>
	
</div>
		
	
	
=========================== admin 管理页面，如何显示多列：
In admin.py :
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	# Use below variable to set columns in admin page.
	list_display = ('id','atc_topic','atc_desc','click_count','like_count',)
    fieldsets = (
        ('Article', {
            'fields': ('atc_topic','atc_desc', 'atc_content', )
        }),
        ('Time', {
            'classes': ('readonly',),
            'fields': ('create_time', 'update_time',)
        }),
    )

	
	

=========================== password :
== validate the password : 
from django.contrib.auth.hashers import make_password

lf = LoginForm()
# encrypt the password
password=make_password(lf.cleaned_data['password'])


== login method from django :
from django.contrib.auth import logout,login,authenticate

login(request,user)
user = authenticate(username=username,password=password)
if user is not None:
    pass


== register 

=== 关于 ajax 的使用：

$.ajax({
    url:"{% url 'validate_login' %}",
    method:"POST",
    data:{'email':$('#login_email').val(),'password':$('#login_password').val(),'referer_url':$('#referer_url').val()},
    type:"json",
    success:function(callback){
        # json 数据返回，需要调用 var data = $.parseJSON(callback) 把 数据转换成json 数据
        var data = $.parseJSON(callback)
        if (data.lg_flag == 1){
            window.location.href =data.referer_url
        }else{
            alert(data.errormsg)
        }
    },
})


======================= 富文本编辑器：
种类：
    ckeditor, ueditor, kindeditor, tinymce .. 

== kindeditor:
    download kindeditor :

unzip the zip file, and copy them to /static/js/ directory :

config the admin.py:
    
class Media:
    js = (
        '/static/js/kindeditor-4.1.10/kindeditor-min.js',
        '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
        '/static/js/kindeditor-4.1.10/lang/config.js',
        )

config.js:
KindEditor.ready(function(K)){
    K.create('textarea[name=xxx]',{
        width:500,
        heigth:500,
        })
}

== file upload setup:
in vedio django project blog 10 :


====================== files upload :
settings.py :
MEDIA_URL="/uploads/"
MEDIA_ROOT = os.path.join(BASE_DIR,'uploads') 

urls.py :
url(r"^uploads/(?P<path>.*)$","django.views.static.serve",{"document_root":settings.MEDIA_ROOT})

models.py :
xxx = models.ImageField(upload_to='xxx/xxx/',default='xxx/xx/x',max_length=200,blank=True)


== For django + pycharm + debug :
Run -> Edit configurations -> Python -> + ->
Name : mydebug
Script path : E:\Study\python\workspace\blog_project\manage.py
Parameters: runserver

== My study of upload:

url.py:
from django.conf.urls.static import static

urlpatterns=[]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

models.py :
 xxx = models.ImageField(upload_to='%Y/%m/%d/',default='xxx/xx/x',max_length=200,blank=True)
 # upload_to='xxx/xxx/' 表示会存到 MEDIA_ROOT/%Y/%m/%d/ 下

settings.py:
# Media_ROOT 被用在models.py 
MEDIA_ROOT=os.path.join(STATIC_URL,'media')
# MEDIA_URL 用在 html 中
MEDIA_URL='/media/'

html:
<img src="{% static single_article.img.url %}"/>

=================== django login token :
models.py:
userToken = models.Charfield(max_length=50)

views.py:
import random 
usertoken = time.tim() + random.randrange(1,1000000)
usertoken = str(usertoken)


== files upload :
from django.conf import settings 
file = request.FILES["imgName"]
filepath = os.path.join(settings.MEDIA_ROOT,filename)
# 这里的  filename 可以自己命名，可以根据account 或者其他进行命名 
# 文件写入 ： 
with open(filepath,'wb') as fp :
    for data in file.chunks():
        fp.write(data)


==== logout:
from django.contrib.auth import logout
def logout(request):
    logout(request)
    return redirect("homepage")


============== 给 button 添加值value：
<button class="xxx" ga="{{item.xxx}}"> button</button>

获取ga值 ：
var bt = getElementByClassName("xxx")
ga = bt.getAttribute("ga")


=================== 通过管理类修改 models 原有的函数：
class CartManager(models.Manager):
    def get_queryset(self):
        return super(CartManager,self).get_queryset().filter(isDelete=False)

class Cart(models.Model):


    objects = CartManager()












