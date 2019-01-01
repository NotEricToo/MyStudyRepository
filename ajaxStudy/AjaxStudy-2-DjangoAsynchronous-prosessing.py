XMLHttpRequest, 比较原始的一种异步交互方式，直接上代码：

前端代码：

<!DOCTYPEhtmlPUBLIC"-//W3C//DTDXHTML1.1//EN"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html lang='en'>
  <meta charset='utf-8'>
  <head>
    <title>测试ajax</title>
    <script>
      var xmlHttp;
      function createXMLHttpRequest(){
        if(window.ActiveXObject)
          xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
        else if(window.XMLHttpRequest)
          xmlHttp = new XMLHttpRequest();
      }
//GET的发送方式
      function startRequest(){
        createXMLHttpRequest();
        xmlHttp.open('GET','/home/back?name=littleget',true);  //GET发送数据的方式
        xmlHttp.onreadystatechange = function(){
          if(xmlHttp.readyState == 4 && xmlHttp.status == 200)//判断返回码
            alert('已经连接'+xmlHttp.responseText)
        }
        xmlHttp.send(null);                                    //GET发送的内容不再send(）中
      }
 
//POST的发送方式
      function startPOST(){
        createXMLHttpRequest();
        xmlHttp.open('POST','/home/back/',true);
        xmlHttp.onreadystatechange = function(){
          if(xmlHttp.readyState == 4 && xmlHttp.status == 200)
            alert('POST已经连接'+xmlHttp.responseText)
        }
        xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded"); //POST发送必须加请求头
        xmlHttp.send('name=littlepost');
      }
      </script>
    <input type='button' value='test' onClick='startRequest()'>
    <input type='button' value='post' onClick='startPOST()'>
    </head>
  </body>


JDANGO作为服务端的代码：

def back(request):
	if request.method == 'POST':
		content = request.POST.get('name')
		return HttpResponse('POST receive success, name is ' + content)
	else:
		content = request.GET.get('name')
		return HttpResponse('GET receive success, name is ' + content)
		

	========================= 整个 ajax 执行过程的代码封装： 
	
// 这一整个就是 ajax 的请求过程
// 这里把 ajax 请求过程封装成封装库

var AjaxUtil = {
	//基础选项
	options : {
		method : "get", // 默认的提交方法 get post
		url : "", // 请求的路径 required
		params : {} , // 请求的参数,json 格式(format)
		type: 'text', // 返回的内容类型,text,xml,json
		callback : function(){
			 // 回调函数 required

		}
	},

	//创建XMLHttpRequest对象
	createRequest : function(){
		var xmlhttp;
		try{
			xmlhttp = new ActiveXObject("MsXML2.XMLHTTP"); // IE6 以上的版本
		}catch(e){
			try{
				xmlhttp = new ActiveXObject("Microsoft.XMLHTTP"); // IE6 以下版本	
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

	//设置基础选项
	setOptions : function(newOptions){
		for(var pro in newOptions){
			this.options[pro] = newOptions[pro];
		}
	},

	//格式化请求参数
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

	//状态改变的处理
	readystatechange : function(xmlhttp){
		//获取返回值
		var returnValue;
		if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
			switch (this.options.type){
				case "xml":
					// xml 格式的返回值需要使用 responseXML 来获取
					returnValue = xmlhttp.responseXML;
					break;
				case "json":
					var jsonText = xmlhttp.responseText;
					// Json 格式的数据使用 responseText 获取然后使用 eval 来对json格式的数据进行解析：
					if(jsonText){
						returnValue = eval("(" + jsonText + ")");
					}
					break ; 
				default : 
					// 其他默认的数据，直接使用 responseText 来获取即可
					returnValue = xmlhttp.responseText; 
					break; 
			}
			if(returnValue){
				# 没有定义 function name 的话，直接使用 attribute_name.call() 进行调用
				this.options.callback.call(this,returnValue);
			}else{
				this.options.callback.call(this);
			} 
		}
	},

	// 发送 ajax 请求：
	// {method : 'GET'}
	requets:function(options){
		var ajaxObj = this;

		// 设置参数
		ajaxObj.setOptions.call(ajaxObj,options);

		// 创建 XMLHttpRequest 对象
		var xmlhttp = ajaxObj.createRequest.call(ajaxObj);

		// 设置回调函数
		xmlhttp.onreadystatechange = function(){
			ajax.readystatechange.call(ajaxObj,xmlhttp);
		}

		// 格式化参数 
		var formatParams = ajaxObj.formatParameters.call(ajaxObj);

		// 请求的方式
		var method = ajaxObj.options.method;
		var url = ajaxObj.options.url;

		if("GET" == method.toUpperCase()){
			url = url + "?" + formatParams ; 
		}

		// 建立连接
		xmlhttp.open(method,url,true);
		if("GET" == method.toUpperCase()){
			xmlhttp.send(null);
		}else if("POST" == method.toUpperCase()){
			// 如果 POST 提交， 设置请求头信息
			xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
			xmlhttp.send(formatParams);
		}
	} 
};


================== 测试代码： 
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
			$("msg").innerHTML = "用户不存在";  
			$("id").innerHTML = "";  
			$("username").innerHTML = "";  
			$("age").innerHTML = "";  
		}  
}  


function $(id) {  
	return document.getElementById(id);  
}
 