# coding:utf-8
import tkinter as tk 
from tkinter import scrolledtext as sc 
import requests

import re ,urllib

mr = re.compile(r'(.*?)list(.*?)html')
str = "http://www.qishu.cc/xuanhuan/list1_1.html"

if re.match(mr,str) is not None :
	print("Match!!")
else:
	print("Not Match !!!")

l = ['a','b','c','b']
print(l)

l.remove('b')

print(l)