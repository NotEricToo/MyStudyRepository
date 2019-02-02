js:

DOM树 加载完成后，：
# 这些属于 JQuery
$(function(){}) 和 $(document).ready(function(){})


$(document).ready(function()
	var doc = document.getElementId('id')

	# focus : 获得焦点
	# blur ： 失去焦点
	# change ： 改变
	# click ： 点击
	doc.addEventListener('focus',function(){
		# 在这里可以是用 this 可以表示 doc 
		value = doc.value
		if (value.length<10){
			error = document.getElementId('errormsg')
			error.style.display = 'block' # 显示错误信息
		}
	},false)

})

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
        	# 页面跳转 
            window.location.href =data.referer_url
        }else{
            alert(data.errormsg)
        }
    },
})

view:
使用 JsonResponse

ajax:
// 验证是否存在
$.get('/reg_username/',{'username':uname},function(data){
    // var data = $.parseJSON(callback)
    // alert(data.status)
    if(data.status=="error"){
        unameexists.style.display = 'block'
    }
})


================= 使用屏幕宽度 10rem :
# 设置完了以下js， 可以在css中使用 width or height : 2.5rem 
== base.js:
$(document).ready(function(){
	# 定义移动端，根据屏幕大小进行适配
	# innerWidth : 屏幕宽度
	document.documentElement.style.fontSize = innerWidth / 10 + "px"

	# setTimeout : 延迟 100 毫秒执行
	setTimeout(function(){

		},100)
})


== js 中使用 ajax 进行数据验证：
$.post('url',data,callback_function(data,status){})
$.post('{% url 'test' %}',{"userid":userid},callback_function(data,status){


	})




==================== 通过 html 的 class 对每个循环的div 或者其他标签添加事件 ：

html : 
 <dt><a class="red2 am-cf getid" id="{{ sub.id }}" ga="{{ sub.id }}">{{ sub.cg_name }}</a></dt>

 js: 
 
 var ids = document.getElementsByClassName("getid")

    for (var i = 0 ; i<ids.length;i++){
        subid = ids[i]

        subid.addEventListener("click",function(){
            var pid = this.getAttribute("ga")
            # 这里 只能使用 this， 直接使用 subid 没有效果
            alert(pid)
        })
    }


============= javascript 判断字符串是否为空
password.replace(/\s+/g,"") == "" 


== 获取 某个字符的位置：
str.indexOf("aaa")
如果没有，则返回 -1


==============Dom 与 Jquery 之间的转换：
Dom 转 JQ：
var $jqDOm = $("#jqdom")
var domDiv =  $jqDOm[0] # 取第一个，就是需要的 dom 元素

JQ 转 DOM ：
var dom = document.getElementId("aaa") 
var $newJQ = $(dom) # 直接把 dom 放进去




 