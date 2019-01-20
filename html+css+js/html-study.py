html:
布局：

# 头部
<header></header>

# 底部
<footer> </footer>

# 菜单 ： 横向排列：
<nav> 
	<a>菜单1</a>
	<a>菜单2</a>
	<a>菜单3</a>
	<a>菜单4</a>
</nav>

<nav>
	<ul>
		<li>菜单1</li>
		<li>菜单2</li>
	</ul>
</nav>
# 效果： 菜单1   菜单2 

# 侧边栏
# 可以做侧边栏菜单
<aside>
<ul>
	<li></li>
</ul>
</aside>

# 引入 css 和 js 文件:
# css: 
<link rel="stylesheet" type="text/css" href="xxx.css" />

# js :
<script type="text/javascript" charset="utf-8" src="xxx.js" ></script>


== 删除节点:
var li = document.getElementById("xxx")
li.parentNode.removeChild(li)