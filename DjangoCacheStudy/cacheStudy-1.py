===================django 缓存study :
1 How to test cache in django :
	memcached (内存缓存系统): 
setting.py :
CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION':'127.0.0.1:11211',
	}
}

== or : 
CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION':'unix:/tmp/memcached.sock',
	}
}

== or 
CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION':[
			'ip1:11211',
			'ip2:11211',
			'ip3:11211',
		],
	}
}

== or in windows : 
CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION':'c:\tmp\bar',
	}
}

== memcached-related question :
1 In linux will use root to start the memcached. 
2 Sure the location in the setting files, the account of the web need to have permission to access the folder in LOCATION option.


========== 2 use the cache in django
in .py files:
from django.core.cache import caches 
== after import the above lib , we can get the setting in setting files: 
caches['default']

from django.core.cache import cache 
== After import the above lib, we can set cache and access the cache our setting before 
cache.set('key','value',30) # 30 means the cache will disapear after 30 sec. 

# Get the cache :
cache.get('key')


== memcached 的安装：
	安装至少1.4.4版本以上的。
	dependencies:
		GCC
		Libevent(时间触发网络库)
	
	具体安装步骤，不记录
Download mencached :

== libevent :
# wget https://sourceforge.net/projects/levent/files/libevent/libevent-2.0/libevent-2.0.22-stable.tar.gz --no-check-certificate
wget https://github.com/libevent/libevent/releases/download/release-2.0.22-stable/libevent-2.0.22-stable.tar.gz
# wget http://www.monkey.org/~provos/libevent-2.0.tar.gz
tar -zxvf xxx.tar.gz 
cd xxx 
./configure --prefix=/usr
make 
make install 

== memcached: 
wget http://www.memcached.org/files/memcached-1.4.24.tar.gz

解压 :

cd xxx 
./configure --with-libevent=/usr
make
make install 
	
== memcached setting :
	-p port : default : 11211 
	-U monitor port : default : 11211 
	-I ip address, if been set to 127.0.0.1 means only local machine can access this web .(default monitor all ip address)
	-d means process the thread in single process
	-u <username> means which account can access the cache .
	-m <num> means the maximum cache can be used , default unit is M .
	
=====================command to install python memcached :
pip install python-memcached

====================== memcached-related configuration 

	
	
======================= memcached-related function :
	_is_expired(self,f):	judge a file whether it is expired(判断文件是否过期)
	_list_cache_files(self): 	list all cache files in server. (.djcache files)
	_cull(self) : 	random to delete some cache files in server. According to max_entries(Number of files) and cull_frequency(频率)
	has_key : judge whether the key  exist
	add(any parameters) : add a new cache (key-value), if the key exists, it will raise an exception. 
		example: 
		add(key,value,version='v1')
			return true
		add(key,value,version='v2')
			return true 
		add(key,value,version='v2')
			return false
		conclusion(结论): we can not add the version exists key. 
		
	set(any parameters) ： set up the value of the key, if not exists this key, will add one new. 
		set(key,value,version='v1') # set 函数可以set version 相同的值， 会替代原有的version 
		or 
		set(key,value)
	get(any parameters) : get the value of the key, if the key not exists , will not return anything. 
	delete(key) : delete the key and value in the cache. 
	clear(self): remove all cache files. 
	== if you set the key with a version name, you use has_key or get or other function need to use the version too.
	
=============================== database cache setting : 
setting.py : 
	== configuration :

CACHES={
	'default':{
		'BACKEND':'django.core.cache.backend.db.DatabaseCache',
		'LOCATION':'my_cache_table',#table name in database 数据库表名
	}
}

	== command to create cache table in database : 
	python manage.py createcachetable   # this table name is the parameter in the setting files. 
	
	default : create this table to default database .
	
	if we want to create the cache table to other database, we need to use --database parameter to determine database :
	python manage.py createcachetable --database db_name 
	
	== database setting in setting.py :
DATABASES={
	'default':{
		'NAME':'DB_NAME',
		'ENGINE':'django.db.backends.postgresql_psycopg2', # I do not know this database 
		'USER':'Username',
		'PASSWORD':'Password'
	}
	'db_name1':{ # This use mysql to be an example. 
		'NAME':'DB_NAME',
		'ENGINE':'django.db.backends.mysql', # I do not know this database 
		'HOST':'127.0.0.1',
		'PORT':'3306',
		'USER':'Username',
		'PASSWORD':'Password' 
	}
}
	
	== multiple database setting :
CACHES={
	'default':{
		'BACKEND':'django.core.cache.backend.db.DatabaseCache',
		'LOCATION':'my_cache_table',#table name in database 数据库表名
	}, # Default database is necessary # Default datatabase 是必须的.
	'db_name1':{
		'BACKEND':'django.core.cache.backend.db.DatabaseCache',
		'LOCATION':'my_cache_table2',
		#table name in database 数据库表名, no need determine the table name when we use command to create tabel in db
	}
}
	when we use multiple database, we can use below function to control the read,write and migrate about database :

	#CacheRouter.py :  
class CacheRouter(object):
	# In this function : cache_replica and cache_primary are the database name , 
	# we can define them to db_name1 or db_name2 in setting.py files.
	# It is configed in database variable. 
	def db_for_read(self,model,**hints):
		...
		if model.meta.app_label == 'django_cache':
			return 'cache_replica'
		return None 
		# All read operation point to cache_replica, this database. 
		
	def db_for_write(self,model,**hints):
		...
		if model.meta.app_label == 'django_cache':
			return 'cache_primary'
		return None 
		#All write operation will point to cache_primary database. 
		
	def allow_migrate(self,db,app_label,model_name=None,**hints):
		...
		if app_label == 'django_cache' :
			return db=='cache_primary'
		return None 
		# Allow to do migration in database : cache_primary 
		
	== use cache router:
	setting.py :
DATABASE_ROUTERS = ['myproject.config.cache_router.CacheRouter'] # myproject.config.cache_router is the path of file ： CacheRouter.py 

	读：
	所有DB缓存读操作都指向 cache_replica DB 这个数据库
	写： 
	所有db缓存的写操作都会指向 cache_primary DB 这个数据库。
	migration:
	允许在 cache_primary DB 上执行 Migration 

	== All database cache function :
	def get(self,key,default = None,version=None): ...
	
	def set(self,key,value,timeout=DEFAULT_TIMEOUT,version=None): ... 
	
	def add(self,key,value,timeout=DEFAULT_TIMEOUT,version=None): ... 
	
	def _base_set(self,mode,key,value,timeout=DEFAULT_TIMEOUT): ... 
	
	def delete(self,key,version=None): ... 
	
	def has_key(self,key,version=None): ... 
	
	def _cull(self,db,cursor,now): ... 
	
	def clear(self) : ..
	
	
	
	
============================== local-memory local缓存 
  == configuration 
  
CACHES={
	'default':{
		'BACKEND':'django.core.cache.backend.locmem.LocMemCache',
		'LOCATION':'unique-snowflake',#table name in database 数据库表名
		# In case there is only one cache, we can ignore the attribute of LOCATION.
		# In case it is a multiple cache configuration, need to config at least one LOCATION in the configuration.
	},
	'app':{
		'BACKEND':'django.core.cache.backend.locmem.LocMemCache',
		'LOCATION':'unique-snowflake2',  
	}
}

# 2 setting exists here, if we want to determine which setting to be used, we can use :
cache1 = cache['app']
cache1.set('key','value')
cache1.get('key')


 == 该缓存无法跨线程进行缓存，效率不是很高，建议开发测试的时候使用。
 
 == 源码解析：
class LocMemCache:
	def __init__(self,name,params):
	
	def add(self,key,value,timeout=DEFAULT_TIMEOUT,version=None):
	
	def set(self,key,value,timeout=DEFAULT_TIMEOUT,version=None): 
	
	def get(self,key,default=None,version=None,acquire_lock=True):
	
	def _set(self,key,value,timeout=DEFAULT_TIMEOUT):
	
	def _has_expired(self,key):
	# Check whether the key is expired. 
	
	def incr():
	# 自增长
	def decr():
	# 自降 
	
	def delete(self,key):
	
	def clear(self):
	

 =============================== dummy 缓存（开发使用）
 == 当我们release 的时候不想修改代码，（开发的时候又不想缓存数据）但是又害怕在开发测试的时候，旧数据会有所影响，我们就可以使用dummy 缓存。
CACHES={
	'default':{
		'BACKEND':'django.core.cache.backend.dummy.DummyCache',
		# 只需要配置这里就可以使用dummy缓存了。
	}
}

== 源码解析：
# 跟其他的缓存使用基本一致,但是很多function 不会真的去实现，主要就是用于测试。 
class DummyCache:
	def get()
	def set()
	def delete()
	def add()
	def clear() : pass 
	def get_many() : pass 
	def set_many() : pass 
	def delete_many(): pass 
	def has_key():
	
	
	
============================ setting.py 中 Cache configuration :
caches = {
	'default':{
		'BACKEND':'django.core.cache.backends.filebased.FileBasedCachew',
		'LOCATION':'/var/tmp/django_cache',
		'TIMEOUT':60,
		'OPTION':{
			'MAX_ENTRIES':1000
		}
	}
}
# The invalid parameter will be ignore by the program . 
# 无效的参数会被忽略，而不会影响program process. 

============================= 缓存分类：
站点缓存： 最简单的缓存也是最大的缓存， 基于整个站点进行缓存

基于view缓存： 根据需要把需要缓存的view进行缓存
	使用简单:
	
	from django.views.decorators.cache import cache_page
	
	@cache_page(60*15)
	def my_view(request):
	
	== 多个url 指向同一个 view 会被分别缓存
	第一个参数是timeout 
	可选参数:
		cache: 可指定缓存（setting.py里面的配置Cache），default is 'default'
		key_prefix: 
		
	也可以在URLS.py 中使用view缓存： 
	from django.views.decorators.cache import cache_page
	url(r'^index/$',cache_page(60*50)(my_view))
	
Template 片段缓存 ： 
	引用：
	在 html 中， 使用标签：
	{% load cache %}
	{% cache 500 片段name %}
	
	{% endcache %}
	
底层缓存API（粒度最细的） ： 可以根据需求缓存某个类型的object， list ，等变量。 
LOW-LEVEL缓存：
 
 
 
============================ redis 作为缓存:
CACHES={
	'default':{
		'BACKEND':'django.core.cache.RedisCache',
		'LOCATION':'127.0.0.1:6379',
		'OPTIONS':{
			'CLIENT_CLASS':'redis_cache.client.DefaultClient',
		},
		'KEY_PREFIX':'MyProject',
		'TIMEOUT':480
		
	},
}

# 然后添加两个中间件的class:
MIDDLEWARE_CLASSES={
	# middle 中间件放在前面
	'django.middleware.cache.UpdateCacheMiddleware', 
	...
	# fetch 中间件 放在最后面
	'django.middleware.cache.FetchFromCacheMiddleware'
}


============================== redis 安装与配置：
	== install : 
	sudo apt-get install redis-server 
	
	== run redis-server:
	redis-server 
	# redis-server --port 6380 --slaveof 127.0.0.1 6379 
	== check redis whether running normally:
	redis-cli 
	
	# 出现命令行，表示正常工作。
	
	== redis 运行时， 可以使用 : 
		CONFIG SET and CONFIG GET 来获取和设置redis parameter 
		# 用这2个进行设置的配置，重启redis 会重置， 因为这2个没有保存，只是session设置。
		
================================ redis 基本命令
	SET key value [EX seconds] [PX milliseconds] [NX|XX]
		ex 和 px 都是设置过期时间，一个单位是 seconds 一个是 millseconds 
		NX ： key 不存在的时候，才设置 k-v 
		XX： 只有key 存在的时候，才设置 k-v 
		example: 
			set k1 v1 
			set k2 v2 
			set k3 v3 ex 300 # ex: expire 300 seconds. 
			set k1 v1 nx # nx : set the key when it not exists. if exists, don't set 
				# if exists, return (nil), means set fail. 
			set k4 v4 xx # set the key when it exists, in case it not exists, return nil. means setting key fail. 
			
			
	SETNX key value ：
		当 key 不存在的时候，才设置 k-v， 相当于 set key value nx ， 
		# 类似与其他缓存的函数 add()
		example:
			setnx k5 v5 # if k5 not exists, return 1 , means setting successfully. 
			setnx k5 v5-new # k5 exists, return 0, means setting fail. 
			
	
	MSET key value [key value]
		设置多个key-value，多个的时候，在后面追加。
		example :
			mset k1 v1 k2 v2 k3 v3 
	GET key ：
		获取key的缓存值，
			key 不存在，返回 "nil"
		如果缓存值不是string 类型，则报错，get 函数值处理string 类型的缓存值
		example :
			get k1 
		
	MGET key [key2 key3 ... ]
		获取多个key的缓存值
		如果key或者缓存值不存在，就返回 "nil", 因为该操作不会失败。
	
	INCR key :
		缓存值 +1 
		如果key 的缓存值不存在，设置为 0 
		如果 value 不能转换成数值，则报错。
	
	INCRBY key increment
		缓存值增加 increment 的值 
		
	DECR key 
		缓存值 减少1 
		
	DECRBY key increment 
		缓存值减少给定的increment值 
		
	RENAME key newkey 
		重命名 key 
		example : 
			rename k1 k2 
			get k1 # not exists 
			get k2 # exists, return value 
			
	EXISTS key [key2 key3 .. ]
		返回存在的key个数， 0 表示一个都没有
		
	DEL key [key2 key3 ... ]
		删除指定的key , ignore the keys not exists. 
		
	== key 的匹配：
		h?llo : hello hallo hbllo 
		h*llo : hello hllo heeello 
		h[ae]llo : hallo hbllo hcllo .. hello , when the world > e, then can be touch .
		h[^e]llo : all h?llo but not : hello 
		h[a-b]llo : only : hallo hbllo 
		
	TTL key : 
		返回 key 的存活时间：
			返回 -2 表示 key 不存在 
			返回 -1 表示 key 存在，但是该key没有设置过期时间 
	PERSIST KEY 
		delete the expired time of the key. # 删除key 的过期时间
		返回1 delete the expired time successfully 
			# 成功删除过期时间
		返回0 return 0 means the key not exists or the key have not set the expired time. 
			# 表示 key 不存在或者说, 没有设置过期时间。
		
	EXPIRE key seconds 
		setting the expired time of the key. # 给key设定过期时间：
		
	FLUSHALL ：
		clear all cache data in server. 
		
	FLUSHDB : 
		clear all cache in current db. 
		
	KEYS * :
		list all keys in the cache. 
		we can use 模糊匹配 来进行 list ：
		keys k* : 列出所有k开头的keys
		
		
== redis 后端常用函数解析：
	def set -> SET/SETEX
	def get -> GET
	def add -> SETNX/EXPIRE 
	def set_many -> MSET/SETEX
	def get_many -> MGET 
	def incr -> EXISTS/INCRBY/GET/SET/SETEX 
	def decr -> -1 
	def has_key -> EXISTS 
	def ttl -> EXISTS/TTL 
	def expire -> EXPIRE
	def persist -> PERSIST 
	def delete -> DEL 
	def clear -> FLUSHDB/DEL　
	
			
		

==============================django redis缓存 的安装
首先需要安装redis-server
	sudo apt-get install redis-server # 安装redis-server 
	.~/myprojectenv/bin/activate # 	source project 到虚拟环境
	pip install django-redis-cache  # install redis-cache in django 
	
django configuration of redis : 
== setting.py: 
	
CACHES={
	'default':{
		'BACKEND':'redis_cache.cache.RedisCache',
		'LOCATION':'127.0.0.1:6379', # LOCATION 是redis 服务器的信息 address/port 也可以是服务器套接字。
			# LOCATION 可以是单个String 也可以是 string 的列表。
			# Unix 域套接字 /path/to/socket： unix://[:password]@/path/to/socket.sock?db=0
			# 普通的 tcp : redis://[:password]@localhost:6379/0
			# SSL 封装的 TCP :  rediss://[:password]@localhost:6379/0
			'''
			'LOCATION':[
				'127.0.0.1:6379', # First 
				'127.0.0.1:6380', # Second
				'127.0.0.1:6381', # Third	
				]
			'''
		'OPTIONS':{
			'DB':1, # let different cache storage to different room.  Default is 1. 
			'PASSWORD':'abcde',
			'PARSER_CLASS':'redis.connection.HiredisParser',
			'CONNECTION_POOL_CLASS':'redis.BlockingConnectionPool',
			'PICKLE_VERSOIN':-1
			'''
			# If use multiple server to storage cache, need to config below configuration :
			'MASTER_CACHE':'127.0.0.1:6379'
			'''
		'KEY_PREFIX':'MyProject',
		'TIMEOUT':480
		}, 
	},
}

	
	
	
		
	
		
		
		
	
	
		
		
	
	
		
		
		
		
	
	
	
	
 











