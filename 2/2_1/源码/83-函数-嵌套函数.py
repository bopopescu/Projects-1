#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
#嵌套函数
#
# def  func():
#     print('alex')
#     def func2():
#         print('eric')
#     func2()
# func()



#=====>1、函数内部可以再次定义函数。2、要想被执行必须要调用函数名 <======

# age = 19
# def  func1():
#     age = 73
#     print(age)
#     def func2():
#         age = 84
#         print(age)
#     func2()
# func1()
#函数变量 从最里面函数 找变量层层找  最后到全局变量

age = 19
def  func1():
    global  age
    def func2():
        print(age)
    age = 73
    func2()

func1()
print(age)