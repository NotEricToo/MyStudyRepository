====================================================Ajax 1 (异步数据获取技术)
Introduce :
	Ajax can refresh the web page, no need to reload all page when we need some data from service .
	We can only refresh the data we need .

================== 简单的 javascript 例子: 
<script type="text/javascript">
function doAjax(the_request)
{
# create a httprequest object: 
	var request = null ;
	if(windows.XMLHttpRequest){
		request = new XMLHttpRequest();
		
	}else if(windows.ActiveXObject){
		request = new ActiveXObject('Microsoft.XMLHTTP');
		
	}else{
		alert("Browser does not support ajax!")
		# If the browser alert this prompt, means the browser is out-of-date. 
		
	}
	

}
</script>

<input type="button" onclick="doAjax('ajax-02.txt')"/>

===============request（响应） 对象的一些属性(attribute)
使用 request 噶 attribute: 	
	request.attribute_name ..
	
3 more important attribute:
	onreadystatechange : 
		存储服务器响应的函数
		# 呢度应该就系重构呢个函数或者系话定义呢个attribute 响应噶过个 function 
	request.onreadystatechange = function(){
		// Coding something here  
		if (request.readyState == 4 ) {
		// Status = 4 means the request is completed in the service, we can get some data here ..
		# 一般只需要对 readyState == 4 的状态进行处理，其他的基本不用处理。
		// coding something here
		}
	}
	readyState : 
		this attribute is for get the status of the request :
		(服务器响应的状态信息)
		in case the status of the request is changed, the function in onreadystatechange will be execute once . 
		(一旦响应的状态改变，onreadystatechange 属性的函数就会被调用一次)
		5 value in this attribute :
		0 : request is not inited. # 请求未初始化,还没有发出请求
		1 ： request is raised, but it has not been sent yet. (请求已经提出，但是还没被发送)
		2 : request has been sent, normally we can get the head info in the response  
		3 : The request you raised is in process in service, but not yet complete (服务器正在处理中，尚未完成)
		4 : The request in the service is completed, and it is in use(请求在服务器中已完成，并且使用它了)
	
	responseText : 
		获取服务器返回的数据: 
		即在每一次 调用 onreadystatechange 的函数中，在完成了 request 后，使用这个 attribute 来 storage our data  from the service 
		example : 
		if (request.readyState == 4 ) {
		// Status = 4 means the request is completed in the service, we can get some data here ..
		// coding something here
		alert(request.responseText); 
		// Then we can prompt the data from service .
		}
		
	呢3个attribute 就系 service request 噶 3个attribute 。
	
	
发送request to service ：
we need use some function :
	open()
		open functoin need 3 parameter:
		GET/POST (the request type : get or post)
		URL : Determine script in the service. 
		异步处理标志 ：asynchronous processing flag: 规定对请求使用异步处理 asynchronous  Determine to deal with the request with the asynchronous processing. 
		example: 
		open("GET","Code.txt",true)
	send() 
		To send our request to the service .
		example: 
		send(null)
		
		
================= javascript to create ajax : 

<script type="text/javascript">
	function ajax_function(the_request_url){
		var xmlHttp;
		try{
			xmlHttp = new XMLHttpRequest();
		}
		catch(e){
			try{
				xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
			}catch(e){
				try{
				xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
				}catch(e){
					alert("Your browser does not support ajax ! ");	
					return false; 
				}	
			}
		}
		
		if(xmlHttp){
			xmlHttp.open('GET',the_request_url,true);
			# Define this function, in case the status of the readyState is changed, then execute the below function : 
			xmlHttp.onreadystatechange = function(){
				if(xmlHttp.readyState == 4){
				# when the request status == 4 : 
					if(xmlHttp.status == 200){
						document.getElementById('vv').innerHTML = xmlHttp.responseText ;
						# This get the response from the service and assign it to the element which id is 'vv'
					}
				}
			}
			# Call this function, and send the request to the service 
			# This menthod only for GET menthod to get data.
			xmlHttp.send(null);
		}else{
			alert('error .. ')
		}
		
		return true ;  
	}  
</script>
		
== In the body area ：
<input type="button" id = "test" value = "test" onclick="javascript:ajax_function('/blog/xxxfunction')"/>
<br/><br/>
<div id = "vv"> Script area </div>	
		
======= ajax get the xml file content : 
1 Get the xml element from the responce which is from the server.
# These code should be written in the response function onreadystatechange function .  
	var xmlRoot = XmlHttp.responseXML.documentElement;
	try{
		var xmlItem = xmlRoot.getElementsByTagName("Item")
	}catch(e){
		alert(e.message)
	}
	
2 open() : 
	xmlHttp.open("GET","data.xml",true);
	xmlHttp.send(null);

== XML file: 
data.xml:
<?xml version="1.0" encoding="UTF-8" ?>
<root>
	<Item> This is the message in the xml file . . </Item>
</root>

=================== eval function :
1 Be used to calculate the string :
	document.write(eval("3+5"))
	
	result: 8
	
	
2 利用 eval 解析 json( similar dictionary type data in python) 格式的数据; 
var txt = "{'Name':'iyili','Age':17}";
var txtObject = eval("("+txt+")");
document.write(txtObject.Name);
	
============================= DOM 创建元素：
1 DOM 就是 document 对象：
	用 document 来创建或者删除一些 html 元素
	
====创建元素（在已有的元素后面追加元素，使用 element_name.appendChild("element_id")） :
<div id="div1">
<p id="p1">第一段落</p>

</div>	

<script type="text/javascript">
var tnode = document.createTextNode("新的文本");
var tp = document.createElement("p");
tp.appendChild(tp);

var div_element = document.getElementById("div1");
div_element.appendChild(tp); 

</script>

====delete element from parent element:
<div id="div1">
<p id="p1">第一段落</p> 
<p id="p2">第2段落</p> 
</div>	

<script type="text/javascript">  

var div_element = document.getElementById("div1");
var del_element = document.getElementById("p2");
div_element.removeChild(del_element);

</script>



================== 关于使用 method = "POST":
ajax 在使用post提交数据的时候
在 views.py 文件需要引入一个装饰器：
from django.views.decorators.csrf import csrf_exempt
# 使用post 的时候，需要 import 这个装饰器到该文件

然后在post调用的函数前面加上装饰器：
@csrf_exempt

''' 
在使用post提交表单的时候，django 默认会进行  csrf_token 的验证，
所以在html 中需要加上 {% csrf_token %} 在 <form> 下面的那一行
-- 此处来源: course vedio。 

'''
===================== 关于 python 把dict 转换成 json ：
import json
dict = {"name":"abc"}
jsonStr = json.dumps(dict)

	
	
	


==================== 新学的ajx 数据提交及返回：
== js 中使用 ajax 进行数据验证：
$.post('url',data,callback_function(data,status){})
$.post('{% url 'test' %}',{"userid":userid},callback_function(data){
	if(data.status == 'error'){
		xxxx
	}

})


views.py :
from django.http import JsonResponse

def test(request):
	# 这里对应的是 js 里面的callback ： 
	return JsonResponse({'result':'ok','status':'success'})  
	return JsonResponse({'result':'错误','status':'error'})


====================== ajax 动态改变页面：
== 
$.get("/cglist/",{"sub_id":sub},function(data){
    if(data.length>0){

        $("#cg-prodlist").html(data)
    }

})


views.py : 
def get_cg_prod_list(request):

    sub = request.GET.get("sub_id")
    try:
        prodlist = Product.objects.filter(prod_cg__id=sub)
        return render(request, 'shop/function/category_listprod.html', {"prodlist": prodlist})
    except Product.DoesNotExist:
        pass


html :
分开2个html， 一个是总的html 
另外一个html，只有需要替换的id对应的div里面的内容




============= 获取来源页面：

http_referer = request.META.get('HTTP_REFERER', 'Not defined')
