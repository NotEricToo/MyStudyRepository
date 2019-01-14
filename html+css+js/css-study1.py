css:


== 漂浮在最上面：
z-index:10

header,footer{
	
	z-index:10; # 值越大，越上面
	position:fixed; # 固定定位
}





height:1.5rem; # 使用rem， 需要配置base.js 文件：
# 10rem 可以看作屏幕宽度或者高度
# 1.5rem 相当于 1.5/10 的屏幕宽度或者高度

== base.js:
$(document).ready(function(){
	# 定义移动端，根据屏幕大小进行适配
	# innerWidth : 屏幕宽度
	document.documentElement.style.fontSize = innerWidth / 10 + "px"

	# setTimeout : 延迟 100 毫秒执行
	setTimeout(function(){

		},100)
	})




display:flex; # 弹性盒子布局，默认 水平布局， 由 main axis and cross axis 组成， 默认 main axis 主轴（水平方向）


== 位置固定：
使用： 
position:fixed; # 固定定位

然后使用：
header{
	# 设置这2个就可以设定 header 在最上面
	top:0;
	left:0;
}

footer{
	# 设置这2个就可以设置 footer 在最下面
	bottom:0;
	left:0;
}


footer a{
	text-align:center;
	width:25%;
}


overflow:auto; # 滚动条
overflow:hidden; # 溢出隐藏
# overflow 就是溢出处理 



# 轮播： 
Swiper .

轮播的小圆点：
pagination:'.swiper-pagination'


