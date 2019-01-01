XMLHttpRequest, �Ƚ�ԭʼ��һ���첽������ʽ��ֱ���ϴ��룺

ǰ�˴��룺

<!DOCTYPEhtmlPUBLIC"-//W3C//DTDXHTML1.1//EN"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html lang='en'>
  <meta charset='utf-8'>
  <head>
    <title>����ajax</title>
    <script>
      var xmlHttp;
      function createXMLHttpRequest(){
        if(window.ActiveXObject)
          xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
        else if(window.XMLHttpRequest)
          xmlHttp = new XMLHttpRequest();
      }
//GET�ķ��ͷ�ʽ
      function startRequest(){
        createXMLHttpRequest();
        xmlHttp.open('GET','/home/back?name=littleget',true);  //GET�������ݵķ�ʽ
        xmlHttp.onreadystatechange = function(){
          if(xmlHttp.readyState == 4 && xmlHttp.status == 200)//�жϷ�����
            alert('�Ѿ�����'+xmlHttp.responseText)
        }
        xmlHttp.send(null);                                    //GET���͵����ݲ���send(����
      }
 
//POST�ķ��ͷ�ʽ
      function startPOST(){
        createXMLHttpRequest();
        xmlHttp.open('POST','/home/back/',true);
        xmlHttp.onreadystatechange = function(){
          if(xmlHttp.readyState == 4 && xmlHttp.status == 200)
            alert('POST�Ѿ�����'+xmlHttp.responseText)
        }
        xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded"); //POST���ͱ��������ͷ
        xmlHttp.send('name=littlepost');
      }
      </script>
    <input type='button' value='test' onClick='startRequest()'>
    <input type='button' value='post' onClick='startPOST()'>
    </head>
  </body>


JDANGO��Ϊ����˵Ĵ��룺

def back(request):
	if request.method == 'POST':
		content = request.POST.get('name')
		return HttpResponse('POST receive success, name is ' + content)
	else:
		content = request.GET.get('name')
		return HttpResponse('GET receive success, name is ' + content)
		

	========================= ���� ajax ִ�й��̵Ĵ����װ�� 
	
// ��һ�������� ajax ���������
// ����� ajax ������̷�װ�ɷ�װ��

var AjaxUtil = {
	//����ѡ��
	options : {
		method : "get", // Ĭ�ϵ��ύ���� get post
		url : "", // �����·�� required
		params : {} , // ����Ĳ���,json ��ʽ(format)
		type: 'text', // ���ص���������,text,xml,json
		callback : function(){
			 // �ص����� required

		}
	},

	//����XMLHttpRequest����
	createRequest : function(){
		var xmlhttp;
		try{
			xmlhttp = new ActiveXObject("MsXML2.XMLHTTP"); // IE6 ���ϵİ汾
		}catch(e){
			try{
				xmlhttp = new ActiveXObject("Microsoft.XMLHTTP"); // IE6 ���°汾	
			}catch(e){
				try{
					xmlhttp = new XMLHttpRequest();
					if(xmlhttp.overrideMimeType){
						xmlhttp.overrideMimeType("text/xml"); 
					}
				}catch(e){
					alert("Your browser does not support ajax!");
				}
			}
		}
		return xmlhttp;
	},

	//���û���ѡ��
	setOptions : function(newOptions){
		for(var pro in newOptions){
			this.options[pro] = newOptions[pro];
		}
	},

	//��ʽ���������
	formatParameters : function(){
		var paramsArray = [];
		var params = this.options.params;
		for(var pro in params){
			var paramValue = params[pro];
			if(this.options.method == "GET"){
				paramValue = encodeURIComponent(params[pjo]);
			}
			paramArray.push(pro + "=" + paramValue);
		}
		return paramArray.join("&");
	},

	//״̬�ı�Ĵ���
	readystatechange : function(xmlhttp){
		//��ȡ����ֵ
		var returnValue;
		if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
			switch (this.options.type){
				case "xml":
					// xml ��ʽ�ķ���ֵ��Ҫʹ�� responseXML ����ȡ
					returnValue = xmlhttp.responseXML;
					break;
				case "json":
					var jsonText = xmlhttp.responseText;
					// Json ��ʽ������ʹ�� responseText ��ȡȻ��ʹ�� eval ����json��ʽ�����ݽ��н�����
					if(jsonText){
						returnValue = eval("(" + jsonText + ")");
					}
					break ; 
				default : 
					// ����Ĭ�ϵ����ݣ�ֱ��ʹ�� responseText ����ȡ����
					returnValue = xmlhttp.responseText; 
					break; 
			}
			if(returnValue){
				# û�ж��� function name �Ļ���ֱ��ʹ�� attribute_name.call() ���е���
				this.options.callback.call(this,returnValue);
			}else{
				this.options.callback.call(this);
			} 
		}
	},

	// ���� ajax ����
	// {method : 'GET'}
	requets:function(options){
		var ajaxObj = this;

		// ���ò���
		ajaxObj.setOptions.call(ajaxObj,options);

		// ���� XMLHttpRequest ����
		var xmlhttp = ajaxObj.createRequest.call(ajaxObj);

		// ���ûص�����
		xmlhttp.onreadystatechange = function(){
			ajax.readystatechange.call(ajaxObj,xmlhttp);
		}

		// ��ʽ������ 
		var formatParams = ajaxObj.formatParameters.call(ajaxObj);

		// ����ķ�ʽ
		var method = ajaxObj.options.method;
		var url = ajaxObj.options.url;

		if("GET" == method.toUpperCase()){
			url = url + "?" + formatParams ; 
		}

		// ��������
		xmlhttp.open(method,url,true);
		if("GET" == method.toUpperCase()){
			xmlhttp.send(null);
		}else if("POST" == method.toUpperCase()){
			// ��� POST �ύ�� ��������ͷ��Ϣ
			xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
			xmlhttp.send(formatParams);
		}
	} 
};


================== ���Դ��룺 
function findUser() {  
	var userid = $("userid").value;  
	if (userid) {  
		AjaxUtil.request({  
			url:"servlet/UserJsonServlet",  
			params:{id:userid},  
			type:'json',  
			callback:process  
		});  
	}  
}  

function process(json){  
		if(json){  
			$("id").innerHTML = json.id;  
			$("username").innerHTML = json.username;  
			$("age").innerHTML = json.age;  
		}  
		else{  
			$("msg").innerHTML = "�û�������";  
			$("id").innerHTML = "";  
			$("username").innerHTML = "";  
			$("age").innerHTML = "";  
		}  
}  


function $(id) {  
	return document.getElementById(id);  
}
 