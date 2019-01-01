===================django ����study :
1 How to test cache in django :
	memcached (�ڴ滺��ϵͳ): 
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


== memcached �İ�װ��
	��װ����1.4.4�汾���ϵġ�
	dependencies:
		GCC
		Libevent(ʱ�䴥�������)
	
	���尲װ���裬����¼
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

��ѹ :

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
	_is_expired(self,f):	judge a file whether it is expired(�ж��ļ��Ƿ����)
	_list_cache_files(self): 	list all cache files in server. (.djcache files)
	_cull(self) : 	random to delete some cache files in server. According to max_entries(Number of files) and cull_frequency(Ƶ��)
	has_key : judge whether the key  exist
	add(any parameters) : add a new cache (key-value), if the key exists, it will raise an exception. 
		example: 
		add(key,value,version='v1')
			return true
		add(key,value,version='v2')
			return true 
		add(key,value,version='v2')
			return false
		conclusion(����): we can not add the version exists key. 
		
	set(any parameters) �� set up the value of the key, if not exists this key, will add one new. 
		set(key,value,version='v1') # set ��������set version ��ͬ��ֵ�� �����ԭ�е�version 
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
		'LOCATION':'my_cache_table',#table name in database ���ݿ����
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
		'LOCATION':'my_cache_table',#table name in database ���ݿ����
	}, # Default database is necessary # Default datatabase �Ǳ����.
	'db_name1':{
		'BACKEND':'django.core.cache.backend.db.DatabaseCache',
		'LOCATION':'my_cache_table2',
		#table name in database ���ݿ����, no need determine the table name when we use command to create tabel in db
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
DATABASE_ROUTERS = ['myproject.config.cache_router.CacheRouter'] # myproject.config.cache_router is the path of file �� CacheRouter.py 

	����
	����DB�����������ָ�� cache_replica DB ������ݿ�
	д�� 
	����db�����д��������ָ�� cache_primary DB ������ݿ⡣
	migration:
	������ cache_primary DB ��ִ�� Migration 

	== All database cache function :
	def get(self,key,default = None,version=None): ...
	
	def set(self,key,value,timeout=DEFAULT_TIMEOUT,version=None): ... 
	
	def add(self,key,value,timeout=DEFAULT_TIMEOUT,version=None): ... 
	
	def _base_set(self,mode,key,value,timeout=DEFAULT_TIMEOUT): ... 
	
	def delete(self,key,version=None): ... 
	
	def has_key(self,key,version=None): ... 
	
	def _cull(self,db,cursor,now): ... 
	
	def clear(self) : ..
	
	
	
	
============================== local-memory local���� 
  == configuration 
  
CACHES={
	'default':{
		'BACKEND':'django.core.cache.backend.locmem.LocMemCache',
		'LOCATION':'unique-snowflake',#table name in database ���ݿ����
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


 == �û����޷����߳̽��л��棬Ч�ʲ��Ǻܸߣ����鿪�����Ե�ʱ��ʹ�á�
 
 == Դ�������
class LocMemCache:
	def __init__(self,name,params):
	
	def add(self,key,value,timeout=DEFAULT_TIMEOUT,version=None):
	
	def set(self,key,value,timeout=DEFAULT_TIMEOUT,version=None): 
	
	def get(self,key,default=None,version=None,acquire_lock=True):
	
	def _set(self,key,value,timeout=DEFAULT_TIMEOUT):
	
	def _has_expired(self,key):
	# Check whether the key is expired. 
	
	def incr():
	# ������
	def decr():
	# �Խ� 
	
	def delete(self,key):
	
	def clear(self):
	

 =============================== dummy ���棨����ʹ�ã�
 == ������release ��ʱ�����޸Ĵ��룬��������ʱ���ֲ��뻺�����ݣ������ֺ����ڿ������Ե�ʱ�򣬾����ݻ�����Ӱ�죬���ǾͿ���ʹ��dummy ���档
CACHES={
	'default':{
		'BACKEND':'django.core.cache.backend.dummy.DummyCache',
		# ֻ��Ҫ��������Ϳ���ʹ��dummy�����ˡ�
	}
}

== Դ�������
# �������Ļ���ʹ�û���һ��,���Ǻܶ�function �������ȥʵ�֣���Ҫ�������ڲ��ԡ� 
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
	
	
	
============================ setting.py �� Cache configuration :
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
# ��Ч�Ĳ����ᱻ���ԣ�������Ӱ��program process. 

============================= ������ࣺ
վ�㻺�棺 ��򵥵Ļ���Ҳ�����Ļ��棬 ��������վ����л���

����view���棺 ������Ҫ����Ҫ�����view���л���
	ʹ�ü�:
	
	from django.views.decorators.cache import cache_page
	
	@cache_page(60*15)
	def my_view(request):
	
	== ���url ָ��ͬһ�� view �ᱻ�ֱ𻺴�
	��һ��������timeout 
	��ѡ����:
		cache: ��ָ�����棨setting.py���������Cache����default is 'default'
		key_prefix: 
		
	Ҳ������URLS.py ��ʹ��view���棺 
	from django.views.decorators.cache import cache_page
	url(r'^index/$',cache_page(60*50)(my_view))
	
Template Ƭ�λ��� �� 
	���ã�
	�� html �У� ʹ�ñ�ǩ��
	{% load cache %}
	{% cache 500 Ƭ��name %}
	
	{% endcache %}
	
�ײ㻺��API��������ϸ�ģ� �� ���Ը������󻺴�ĳ�����͵�object�� list ���ȱ����� 
LOW-LEVEL���棺
 
 
 
============================ redis ��Ϊ����:
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

# Ȼ����������м����class:
MIDDLEWARE_CLASSES={
	# middle �м������ǰ��
	'django.middleware.cache.UpdateCacheMiddleware', 
	...
	# fetch �м�� ���������
	'django.middleware.cache.FetchFromCacheMiddleware'
}


============================== redis ��װ�����ã�
	== install : 
	sudo apt-get install redis-server 
	
	== run redis-server:
	redis-server 
	# redis-server --port 6380 --slaveof 127.0.0.1 6379 
	== check redis whether running normally:
	redis-cli 
	
	# ���������У���ʾ����������
	
	== redis ����ʱ�� ����ʹ�� : 
		CONFIG SET and CONFIG GET ����ȡ������redis parameter 
		# ����2���������õ����ã�����redis �����ã� ��Ϊ��2��û�б��棬ֻ��session���á�
		
================================ redis ��������
	SET key value [EX seconds] [PX milliseconds] [NX|XX]
		ex �� px �������ù���ʱ�䣬һ����λ�� seconds һ���� millseconds 
		NX �� key �����ڵ�ʱ�򣬲����� k-v 
		XX�� ֻ��key ���ڵ�ʱ�򣬲����� k-v 
		example: 
			set k1 v1 
			set k2 v2 
			set k3 v3 ex 300 # ex: expire 300 seconds. 
			set k1 v1 nx # nx : set the key when it not exists. if exists, don't set 
				# if exists, return (nil), means set fail. 
			set k4 v4 xx # set the key when it exists, in case it not exists, return nil. means setting key fail. 
			
			
	SETNX key value ��
		�� key �����ڵ�ʱ�򣬲����� k-v�� �൱�� set key value nx �� 
		# ��������������ĺ��� add()
		example:
			setnx k5 v5 # if k5 not exists, return 1 , means setting successfully. 
			setnx k5 v5-new # k5 exists, return 0, means setting fail. 
			
	
	MSET key value [key value]
		���ö��key-value�������ʱ���ں���׷�ӡ�
		example :
			mset k1 v1 k2 v2 k3 v3 
	GET key ��
		��ȡkey�Ļ���ֵ��
			key �����ڣ����� "nil"
		�������ֵ����string ���ͣ��򱨴�get ����ֵ����string ���͵Ļ���ֵ
		example :
			get k1 
		
	MGET key [key2 key3 ... ]
		��ȡ���key�Ļ���ֵ
		���key���߻���ֵ�����ڣ��ͷ��� "nil", ��Ϊ�ò�������ʧ�ܡ�
	
	INCR key :
		����ֵ +1 
		���key �Ļ���ֵ�����ڣ�����Ϊ 0 
		��� value ����ת������ֵ���򱨴�
	
	INCRBY key increment
		����ֵ���� increment ��ֵ 
		
	DECR key 
		����ֵ ����1 
		
	DECRBY key increment 
		����ֵ���ٸ�����incrementֵ 
		
	RENAME key newkey 
		������ key 
		example : 
			rename k1 k2 
			get k1 # not exists 
			get k2 # exists, return value 
			
	EXISTS key [key2 key3 .. ]
		���ش��ڵ�key������ 0 ��ʾһ����û��
		
	DEL key [key2 key3 ... ]
		ɾ��ָ����key , ignore the keys not exists. 
		
	== key ��ƥ�䣺
		h?llo : hello hallo hbllo 
		h*llo : hello hllo heeello 
		h[ae]llo : hallo hbllo hcllo .. hello , when the world > e, then can be touch .
		h[^e]llo : all h?llo but not : hello 
		h[a-b]llo : only : hallo hbllo 
		
	TTL key : 
		���� key �Ĵ��ʱ�䣺
			���� -2 ��ʾ key ������ 
			���� -1 ��ʾ key ���ڣ����Ǹ�keyû�����ù���ʱ�� 
	PERSIST KEY 
		delete the expired time of the key. # ɾ��key �Ĺ���ʱ��
		����1 delete the expired time successfully 
			# �ɹ�ɾ������ʱ��
		����0 return 0 means the key not exists or the key have not set the expired time. 
			# ��ʾ key �����ڻ���˵, û�����ù���ʱ�䡣
		
	EXPIRE key seconds 
		setting the expired time of the key. # ��key�趨����ʱ�䣺
		
	FLUSHALL ��
		clear all cache data in server. 
		
	FLUSHDB : 
		clear all cache in current db. 
		
	KEYS * :
		list all keys in the cache. 
		we can use ģ��ƥ�� ������ list ��
		keys k* : �г�����k��ͷ��keys
		
		
== redis ��˳��ú���������
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
	def clear -> FLUSHDB/DEL��
	
			
		

==============================django redis���� �İ�װ
������Ҫ��װredis-server
	sudo apt-get install redis-server # ��װredis-server 
	.~/myprojectenv/bin/activate # 	source project �����⻷��
	pip install django-redis-cache  # install redis-cache in django 
	
django configuration of redis : 
== setting.py: 
	
CACHES={
	'default':{
		'BACKEND':'redis_cache.cache.RedisCache',
		'LOCATION':'127.0.0.1:6379', # LOCATION ��redis ����������Ϣ address/port Ҳ�����Ƿ������׽��֡�
			# LOCATION �����ǵ���String Ҳ������ string ���б�
			# Unix ���׽��� /path/to/socket�� unix://[:password]@/path/to/socket.sock?db=0
			# ��ͨ�� tcp : redis://[:password]@localhost:6379/0
			# SSL ��װ�� TCP :  rediss://[:password]@localhost:6379/0
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

	
	
	
		
	
		
		
		
	
	
		
		
	
	
		
		
		
		
	
	
	
	
 











