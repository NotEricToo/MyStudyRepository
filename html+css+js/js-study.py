js:

DOM树 加载完成后，：
# 这些属于 JQuery
$(function(){}) 和 $(document).ready(function(){})


$(document).ready(function()
	var doc = document.getElementId('id')

	# focus : 获得焦点
	# blur ： 失去焦点
	# change ： 改变
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

