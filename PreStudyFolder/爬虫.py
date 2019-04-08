爬虫

正则表达式：
import re 

str = "asd #123 "
re.compile(r"#(\S+)") # 可以获得下一个空格为止的 字符串
# 括号表示只取括号内的东西 

re.compile("#(.*)>") # 取第一个 # 到最后一个<的所有

mr = re.compile(r'#(.*?)>') # 取所有符合 # * > 的东西

# 取一定长度的字符串： 
mr = re.compile('#(.{3}?)>') # 取符合 #..> 中， # 开头的3个字符


re.compile('#（\d）') # 取 “#” 后面的数字

list = re.findall(mr,str) # 从 str 中匹配符合mr表达式的字符串存到list中

用来下载的方法： 
import urllib
urllib.urlretrieve()

str = "vedio\\%s.mp4" % (i[1].decode('utf-8').encode('gbk')) # 先解码成 utf-8 编码成 gbk 

