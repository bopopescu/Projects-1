#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
#在整个代码顶层定义的变量，都是全局变量 生效
'''
school = "01dboy edu"
def changge_name(name):
    global  school
    #改之前，声明global
    school = 'mage linux'
    print("before chenge",name,school)
    name = "Alax Li"
    age =  34
#局部变量，是这个函数就是这个变量作用域
    print("after change",name)
name = "alex"
changge_name(name)
print(name)
print(school)
'''
"""
school = "01dboy edu"
def change_name():
#    global  name
    name = 'alex'
change_name()
print(name)
#这个不能使用这种方法 global
"""
'''
names = ['Alex','Jack','Rain']
names_tuple = (1,2,3,4) #元组只读   字典，列表，类  集合 可以改
#字符串和整数不能修改变量
def change_name():
    names[0] = '金角大王'
    print('inside func',names)
change_name()
print(names)
'''
"""
全局与局部变量

在子程序中定义的变量称为局部变量，在程序的一开始定义的变量称为全局变量。
全局变量作用域是整个程序，局部变量作用域是定义该变量的子程序。
当全局变量与局部变量同名时：
在定义局部变量的子程序内，局部变量起作用；在其它地方全局变量起作用。
"""