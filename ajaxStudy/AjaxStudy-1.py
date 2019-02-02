====================================================Ajax 1 (�첽���ݻ�ȡ����)
Introduce :
	Ajax can refresh the web page, no need to reload all page when we need some data from service .
	We can only refresh the data we need .

================== �򵥵� javascript ����: 
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

===============request����Ӧ�� �����һЩ����(attribute)
ʹ�� request �� attribute: 	
	request.attribute_name ..
	
3 more important attribute:
	onreadystatechange : 
		�洢��������Ӧ�ĺ���
		# �ض�Ӧ�þ�ϵ�ع��ظ���������ϵ�������ظ�attribute ��Ӧ������ function 
	request.onreadystatechange = function(){
		// Coding something here  
		if (request.readyState == 4 ) {
		// Status = 4 means the request is completed in the service, we can get some data here ..
		# һ��ֻ��Ҫ�� readyState == 4 ��״̬���д��������Ļ������ô���
		// coding something here
		}
	}
	readyState : 
		this attribute is for get the status of the request :
		(��������Ӧ��״̬��Ϣ)
		in case the status of the request is changed, the function in onreadystatechange will be execute once . 
		(һ����Ӧ��״̬�ı䣬onreadystatechange ���Եĺ����ͻᱻ����һ��)
		5 value in this attribute :
		0 : request is not inited. # ����δ��ʼ��,��û�з�������
		1 �� request is raised, but it has not been sent yet. (�����Ѿ���������ǻ�û������)
		2 : request has been sent, normally we can get the head info in the response  
		3 : The request you raised is in process in service, but not yet complete (���������ڴ����У���δ���)
		4 : The request in the service is completed, and it is in use(�����ڷ�����������ɣ�����ʹ������)
	
	responseText : 
		��ȡ���������ص�����: 
		����ÿһ�� ���� onreadystatechange �ĺ����У�������� request ��ʹ����� attribute �� storage our data  from the service 
		example : 
		if (request.readyState == 4 ) {
		// Status = 4 means the request is completed in the service, we can get some data here ..
		// coding something here
		alert(request.responseText); 
		// Then we can prompt the data from service .
		}
		
	��3��attribute ��ϵ service request �� 3��attribute ��
	
	
����request to service ��
we need use some function :
	open()
		open functoin need 3 parameter:
		GET/POST (the request type : get or post)
		URL : Determine script in the service. 
		�첽�����־ ��asynchronous processing flag: �涨������ʹ���첽���� asynchronous  Determine to deal with the request with the asynchronous processing. 
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
		
== In the body area ��
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
	
	
2 ���� eval ���� json( similar dictionary type data in python) ��ʽ������; 
var txt = "{'Name':'iyili','Age':17}";
var txtObject = eval("("+txt+")");
document.write(txtObject.Name);
	
============================= DOM ����Ԫ�أ�
1 DOM ���� document ����
	�� document ����������ɾ��һЩ html Ԫ��
	
====����Ԫ�أ������е�Ԫ�غ���׷��Ԫ�أ�ʹ�� element_name.appendChild("element_id")�� :
<div id="div1">
<p id="p1">��һ����</p>

</div>	

<script type="text/javascript">
var tnode = document.createTextNode("�µ��ı�");
var tp = document.createElement("p");
tp.appendChild(tp);

var div_element = document.getElementById("div1");
div_element.appendChild(tp); 

</script>

====delete element from parent element:
<div id="div1">
<p id="p1">��һ����</p> 
<p id="p2">��2����</p> 
</div>	

<script type="text/javascript">  

var div_element = document.getElementById("div1");
var del_element = document.getElementById("p2");
div_element.removeChild(del_element);

</script>



================== ����ʹ�� method = "POST":
ajax ��ʹ��post�ύ���ݵ�ʱ��
�� views.py �ļ���Ҫ����һ��װ������
from django.views.decorators.csrf import csrf_exempt
# ʹ��post ��ʱ����Ҫ import ���װ���������ļ�

Ȼ����post���õĺ���ǰ�����װ������
@csrf_exempt

''' 
��ʹ��post�ύ����ʱ��django Ĭ�ϻ����  csrf_token ����֤��
������html ����Ҫ���� {% csrf_token %} �� <form> �������һ��
-- �˴���Դ: course vedio�� 

'''
===================== ���� python ��dict ת���� json ��
import json
dict = {"name":"abc"}
jsonStr = json.dumps(dict)

	
	
	


==================== ��ѧ��ajx �����ύ�����أ�
== js ��ʹ�� ajax ����������֤��
$.post('url',data,callback_function(data,status){})
$.post('{% url 'test' %}',{"userid":userid},callback_function(data){
	if(data.status == 'error'){
		xxxx
	}

})


views.py :
from django.http import JsonResponse

def test(request):
	# �����Ӧ���� js �����callback �� 
	return JsonResponse({'result':'ok','status':'success'})  
	return JsonResponse({'result':'����','status':'error'})


====================== ajax ��̬�ı�ҳ�棺
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
�ֿ�2��html�� һ�����ܵ�html 
����һ��html��ֻ����Ҫ�滻��id��Ӧ��div���������




============= ��ȡ��Դҳ�棺

http_referer = request.META.get('HTTP_REFERER', 'Not defined')
