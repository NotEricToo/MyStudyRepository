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


# 下划线：
border-bottom:0.04rem solid #e0e0e0
z-index:1  # 让它一直在最上面显示


# Span 变成圆形：
border-radius: 2em 1em 4em 3em;
等价于分别设置了四个角：
border-top-radius: 2em;
border-right-radius:1em;
border-bottom-radius: 4em;
border-left-radius:3em;
当然单位上也是可以选择的常用单位：em、px、 %
注：1em=16px
