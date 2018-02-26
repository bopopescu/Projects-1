#!/usr/bin/env python
#_*_ coding:utf8 -*-
#将列表['alex', 'steven', 'egon'] 中的每一个元素使用 ‘\_’ 连接为一个字符串（编程
list = ['alex', 'steven', 'egon']
print(type(list))
a = '\_'
l = a.join(list)
print(l)