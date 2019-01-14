				Django Project Deployment :
================= django environment;
	linux : centos: 6.5 
	django 1.8.3 
	python 3.4.3
	
Install Python :
	In linux : 
su - root
wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz --no-check-certificate
tar -zxvf Python-3.4.3.tgz

# Install the dependence of Python 3.4.3 : 
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel  tk-devel python-devel mysql-devel gcc make
# yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
cd Python-3.4.3 
./configure --enable-shared
# --enable-shared : 开启共享库。
 '''

mkdir -p /usr/local/python3
./configure --prefix=/usr/local/python3
make && make install 

'''
make
# 编译源代码， 生成库文件 
make install 

# Backup the original python :
cd /usr/bin
mv python python_bak 
# Use the shortcut to link to the new python folder :
ln /usr/local/bin/python3.4 python 
or
ln -s /usr/local/bin/python3.4 /usr/bin/python 
# After we link to the new python-3.4.3, the command yum may occur some errors. 
# We can update this command to link to the old python :
vi /usr/bin/yum 
# Update the first line : 
#!/usr/bin/python_bak  

'''
== Install pip for python :
# Setup the setuptools first : 
wget --no-check-certificate  https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26

tar -zxvf setuptools-19.6.tar.gz

cd setuptools-19.6.tar.gz

python setup.py build

python setup.py install


pip : 
wget --no-check-certificate  https://pypi.python.org/packages/source/p/pip/pip-8.0.2.tar.gz#md5=3a73c4188f8dbad6a1e6f6d44d117eeb

tar -zxvf pip-8.0.2.tar.gz

cd pip-8.0.2

python setup.py build

python setup.py install

'''

# Upgrade the pip command : 
pip install --upgrade pip 
'''
== Install mysql in windows -- use the zip file of Mysql :
put the mysql to d:\mysql\
d:\mysql\mysql-5.6

== Update the environment variable :
path=$path:d:\mysql\mysql-5.6\bin 

== Update the my-default.ini in d:\mysql\mysql-5.6\ 

basedir = D:\mysql\mysql-5.6
datadir = D:\mysql\mysql-5.6\data

== Install msyql :
== 使用管理员打开 cmd ：
== 进入 ： d:\mysql\mysql-5.6\bin 执行： 
mysqld -install

== start the mysql service :
net start mysql

'''

======================= Install mysql 
yum install mysql-server 

# start the service of mysql 
etc/init.d/mysqld start

# 让mysql 开机启动：
chkconfig mysqld on 
# In vedio :
	# service mysqld start 
# Login mysql : 
mysql -u root 
# When first login, it will have no password in it. 

use mysql 

# update user set password=password('root') where user = 'root' and host='localhost';
set password for root@localhost=password("root");

# Clear cache in database. 
flush privileges; 

# After we setting password in mysql :
mysql -u root -p 
# Type the password. 

create database blog_db CHARSET=utf8

grant all on *.* to username@localhost identified by "password"

== Install the bridge between mysql and django :
	pip install mysqlclient 
	
== Install django :
	pip install django==1.8.3
	# pip install django 
	# Install the lastest version of django. 
	
	setting.py :
DATABASE={
	'default':{
		'NAME':'user_data',
		'ENGINE':'django.db.backends.mysql',
		'USER':'mysql_user',
		'PASSWORD':'password',
		'HOST':'127.0.0.1',
		'PORT':''
	}
}

== install mysql client
pip install pymysql

== project_folder:
== __init__.py : 

import pymysql
pymysql.install_as_MySQLdb()


== when we use the mysql client version too low, need to setup : 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER':'django',
        'PASSWORD':'django',
        'HOST':'192.168.204.130',
        'PORT':'3306',
		# follow code can solve the question of : SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED
		# Due to the verson of mysql too low.
        'OPTIONS':{'isolation_level':None}
    }

}

== invalid the debug function :
	
add below codes in the setting files:

import socket

if socket.gethostname()=='YouPcName' :
	DEBUG = TEMPLATE_DEBUG = True
	# we can update the database here too :
	DATABASE_NAME = 'dev_db'
else :
	DEBUG = TEMPLATE_DEBUG = False 
	DATABASE_NAME = 'prod_db'
	
	
== settings.py :
ALLOWED_HOSTS=['localhost']

== use email to receive the error report of the server :
# Receive the system errors report 
ADMINS=(
	('Shawn','xxx@xxx.com'),
)
# This setting receive the 404 errors. 
# This need to add a middleware (中间件)
MANAGERS=(
	('Shawn','xxx@xxx.com'),
)

== Get django installation path :
python
import django 
django.__path__
or use the below command to get path of django :
python -c "import django;print(django.__path__);"

== amend the django configuration file:
# This file is the global configuration file of django .(django 的全局配置文件) 
vi /usr/local/lib/python3.4/site-packages/django/conf/global_settings.py 
# 这个文件可以配置我们用来发送邮件的服务器邮箱。 

============================ django errors handling 
 == we can config the urls.py files :

	handler404='blog.views.my_webpage_not_found_page'
	HttpResponseNotFound
	# When occurs 404 fault, it will access the view : my_webpage_not_found_page
	
	handler500='blog.view.my_webpage_errors_page'
	HttpResponseServerError
	
	handler403='blog.view.my_webpage_permission_denied_page'
	HttpResponseForbidden
	
	handler400='blog.view.my_webpage_bad_request_page'
	HttpResponseBadRequest
	
views.py:
from django.http import HttpResponse, HttpResponseNotFound 
from django.template import loader,Context

def my_webpage_not_found_page:
	#...
	t = loader.get_template("404.html")
	c = Context({})
	# return HttpResponseNotFound(<h1>404 not found</h1>)
	return HttpResponseNotFound(t.render(c))
	
	
 == The 2th ways to define our errors page. 
	== In template/ ： 
	404.html 500.html 403.html 400.html  
	

	
 == All these ways only valiable when DEBUG = False 
 
===]==================================== Installation of memchached: 
	== dependence : 
	# We can use the below link to download or download in the software official website. 
== 1 libevent :
# wget https://sourceforge.net/projects/levent/files/libevent/libevent-2.0/libevent-2.0.22-stable.tar.gz --no-check-certificate
wget https://github.com/libevent/libevent/releases/download/release-2.0.22-stable/libevent-2.0.22-stable.tar.gz
# wget http://www.monkey.org/~provos/libevent-2.0.tar.gz
tar -zxvf xxx.tar.gz 
cd xxx 
./configure --prefix=/usr
make 
make install 

== 2 memcached: 
wget http://www.memcached.org/files/memcached-1.4.24.tar.gz

解压 :

cd xxx 
./configure --with-libevent=/usr
make
make install 
	
	
	== memcached: 
	# installation :
pip install python-memcached
	
	== configuration :
/usr/local/bin/memcached -u root -d -p 11211 -c 256 -P /tmp/memcached.pid
	# -u : use which server account to run memcached .
	# -d : start it and treat it as a service. # 把它当作服务启动。
	# -p : (lower) the port.
	# -P : (upper) the file. 
	
# We can put this command to the start files, when the system start, the service can start at the same time.
vi /etc/rc.local


== config the settings.py: 
CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION':'127.0.0.1:11211',
		'''
		multiple machine : 
		or :
		'LOCATION':[
			'ip1:11211',
			'ip2:11211',
			]
		'''
	}
}

# 然后添加两个中间件的class:
MIDDLEWARE_CLASSES={
	# middle 中间件放在前面， 第一行
	'django.middleware.cache.UpdateCacheMiddleware', 
	...
	# fetch 中间件 放在最后面，最后一行。
	'django.middleware.cache.FetchFromCacheMiddleware'
}

	
=========================== database model sync .
# django old version , use below command to sync db : 
# python manage.py syncdb

# after 1.7 version :
pyhon manage.py migrate
# This command will create database table according to the models.py file. 



========================= installation of django-debug-toolbar : 
pip install django-debug-toolbar 

settings.py :
INSTALLED_APPS = (
    #... 
	'debug_toolbar',
)

== 注意事项:
== 默认的 django-debug-toolbar 使用的是Google的jquery，我们访问不了，需要换成：
== 我们所有使用pip安装的软件，都是放在 	python/site-packages/ 目录下面的
== debug tool bar 只有在 debug 模式下才会有效
== update /python/site-packages/debug_toolbar/settings.py : 
CONFIG_DEFAULTS={
	# Toolbar option.
	...
	'JQUERY_URL':'//cdn.bootcss.com/jquery/2.1.4/jquery.min.js',
}

urls.py: 
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns


===================== The deployment of the cource in the vedio :
# 视频中，部署 blog project 的时候遇到的问题
# 该项目会依赖于下面的2个东西
1 create database in mysql :
	create database blog_db charset=utf8 
	
2 install dependent library :
	yum install libjpeg-devel 
	
3 install Pillow :
	pip install Pillow 
	
4 sync database from models.py :
	python manage.py migrate 
	

5 sync database and create super user of the system.
	python manage.py syncdb 
	
	
================================================================================
================================================================================
================== wsgi + apache to deploy service:
================================================================================
django will generate a wsgi file in the project. 
This file is the bridge between wsgi and django.
Django can run the program by wsgi. 
================================================================================
apache :
	== install apache :
	yum install httpd httpd-devel -y 

	== set up the self-starting of the apache :
	chkconfig httpd on 
	# linux 下执行了这个命令后，apache 会在service 下次启动的时候自启动。

	== Start the apache this time :
	service httpd start 
	# 启动本次

re-compile the python3.4 :
	# 重新编译 python : 
	cd python3.4.3 
	make clean 
	# Clean the complie previous time
	
	./configure --enable-shared 
	make 
	make install 
	
	# setting the lib of the shared-lib 
	vi /etc/ld.so.conf 
	# add the below path to the end of the file :
	/usr/local/lib 
	
	# make it valid (create the share-lib(共享库) and make it effective) :
	/sbin/ldconfig -v 
	
	
==================== file between apache and wsgi :
	# in the project folder, we can create a file :
	apache_django_wsgi.conf 
	
	# Content of the config file: 
<IfModule mod_wsgi.c>

WSGISocketPrefix /var/run/wsgi 

Alias /uploads/ /home/work/blog_project/uploads/
Alias /static/ /home/work/blog_project/static/

<Directory /home/work/blog_project/static>
Order deny, allow 
Allow from all 
# Required all granted 

# The comment string, is for apache >= 2.4 

</Direcotry>

<Directory /home/work/blog_project/uploads>
Order deny, allow 
Allow from all 
# Required all granted 
</Direcotry>

<Directory /home/work/blog_project/blog_project>
<Files wsgi.py>
Order deny, allow 
Allow from all 
# Required all granted 

</Files>
</Direcotry>

# This means treat the wsgi as a service process in the OS. 
WSGIDaemonProcess blogprj python-path=/home/work/blog_project:/usr/local/lib/python3.4/site-packages user=apache group=apache 
WSGIProcessGroup blogprj 
WSGIScriptAlias / /home/work/blog_project/blog_project/wsgi.py 
AddType text/html .py 

</IfModule> 


== In httpd.conf of apache, we need to add below to the end of the apache conf file:
vi /etc/httpd/conf/httpd.conf 


LoadModule wsgi_module modules/mod_wsgi.so 
Include /home/work/blog_project/apache_django_wsgi.conf

== After setting this, we can restart the apache :
service httpd restart # Or service httpd start ? 

when apache no permission to access the conf file:  apache_django_wsgi.conf, we can :
chown -R apache:apache blog_project 
chmod -R 755 blog_project 
chmod 755 work 
===================== Install wsgi :
	== download the wsgi tar file from official website. 
	== or use other link to wget the tar file :
	tar -zxvf the tarfile(wsgi-4.4.15.tar.gz).# Here use the 4.4.15 version wsgi .
	cd wsgi-4.4.15 
	./configure 
	make 
	make install 
	
	vi /etc/selinux/config 
	update: # This module manage the permission and security in linux 
	SELINUX=enforcing
	to :
	SELINUX=diabled
	
	# After setting this module, it will not effective immediately.
	# If we want to make it effective immediately, use the below command: 
	# if it  still not effective, we can restart our  system : reboot 
	setenfoce=0 
	
	
============================== After setting this, we can restart the apache :
service httpd start
service httpd restart # Or service httpd start ? 
	
	== log:
	apache log :
	cat /var/log/httpd/error_log
	
	== use apache to start the service, may occurs the error of log path :
	# we can amend the settings.py :
	# at the end of the settings.py :
	when you see : log/script.log or other :
	update to :
	BASE_DIR + '/log/script.log' 
	# or other .
	
	
=============== Question about static files (css,js,images):
# When we deploy the project in apache, it can not find the static files in the /static/ 
	so we need to move the static files of django to project_folder/static/ 
	
	set the static_root in setting.py :
	vi setting.py 
	# add one line : 
	STATIC_ROOT= os.path.join(BASE_DIR,'collected')
	
	use the below command :
	python manage.py collectstatic 
	
	# After this command, we need to move the /collected/admin to /static/ 
	cd collected 
	mv admin ../static/ 
	
	# Restart the apache.
	
================================================================================
================================================================================
============================= Gunicom + django + nginx + mysql 
================================================================================
================================================================================

	== install nginx 
	yum -y install nginx 
	
	# 如果安装不了或者找不到nginx的源， 则手动添加文件
	/etc/yum.repos.d/nginx.repo 
	
	# 在里面输入 :

(nginx)
name=nginx repo 
baseurl=http://nginx.org/packages/centos/6/$basearch/
gpgcheck=0
enabled=1 

	== 再一次执行该命令：
	yum -y install nginx 
	
	== 开机启动：
	chkconfig nginx on 
	service nginx start 
	
	
	== update the configuration of nginx 
	vi /etc/nginx/nginx.conf 
	update the user in the file to your username. e.i. work 
	
	== install gunicorn 
	/usr/local/bin/pip install gunicorn 
	
	== create a gunicorn conf file in the project folder. 
	gunicorn.conf.py : 

import multiprocessing

bind='127.0.0.1:8000'
workers=2
# workers = the amount of CPU in your system + 1 . 
errorlog='/home/shawn/blog_project/gunicorn.error.log'
#accesslog='./gunicorn.access.log'
#loglevel='debug'
proc_name='gunicorn_blog_project'



	== create a nginx conf file : 
		nginx.conf :
		
server{
	listen 80;
	server_name localhost example.com;
	# This server_name should be set to settings.py : ALLOWED_HOSTS parameter. 
	access_log /home/work/blog_project/nginx.access.log;
	error_log /home/work/blog_project/nginx.error.log; 
	
	location / {
		proxy_pass http://127.0.0.1:8080; 
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	}
	
	location /robots.txt {
		alias /home/work/blog_project/static/robots.txt;
	}
	
	location /favicon.ico {
		alias /home/work/blog_project/static/img/favicon.ico;
	}
	
	location ~ ^/(media|static)/ {
		root 	/home/work/blog_project; 
		expires 30d; 
	}	
	
	# this prevents hidden files (beginning with a period) from being served
	location ~ /\. {
		access_log off; log_not_found off; deny all; 
	}
}

	== create a shortcut about this file nginx.conf to nginx path :
	# 建立一个快捷方式到 nginx 的配置目录下
sudo ln -s /home/work/blog_project/nginx.conf /etc/nginx/conf.d/blog_project.conf 
	# after this, nginx can access this config file. 
	# 这样之后，nginx就可以读到这个配置文件。
	
	== Update the settings.py :
	ALLOWED_HOSTS = ['localhost','example.com']
	
	== 启动 gunicorn (类似于tomcat 或者 weblogic 等的server软件)： 
sudo nohup /usr/local/bin/gunicorn blog_project.wsgi:application -c /home/work/blog_project/gunicorn.conf.py & 
	# 这个命令需要在 /home/work/blog_project 目录下 
	
	== 打开 防火墙相关的 80 端口 : 
sudo /sbin/iptables -I INPUT -p tcp --dport 80 -j ACCEPT 
service iptables save 
# 2th command make the port effective. 

	== 重启 nginx ：
	service nginx restart 
	
	== 当遇到 static files 的问题，参照apache笔记中，static files 的处理方法。
	
	
	
	

	



	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	







