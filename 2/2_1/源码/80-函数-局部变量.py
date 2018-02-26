#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
#局部变量
name = 'Vlack girl'  #全部变量 不可变量
#
# def change_name():
#     # name = '黑色姑娘'
#     print('在',name,'里面。。。',id(name))   #局部可以掉用全局变量     外面不可调用函数里面变量
# def func2():
#     name = 'rain'
# func2()
# change_name()
# print(name,id(name))
#定义在函数外部一级代码变量，叫做全部变量  全局能用
#局部变量 就是指定义 在函数里面的变量  只能在局部生效
#
#在函数内部，可以引用 全局变量
#如果：全局和局部都 有一个变量，叫nam  函数查找 变量的顺序时由内而外的
#
#在函数里修改全局变量
name = 'Vlack girl'  #全部变量 不可变量
def change_name():

    global name   # 先声明修改全局变量
    name = '黑色姑娘' # 在函数里修改全局变量
    print('在',name,'里面。。。',id(name))   #局部可以掉用全局变量     外面不可调用函数里面变量

change_name()
print(name,id(name))