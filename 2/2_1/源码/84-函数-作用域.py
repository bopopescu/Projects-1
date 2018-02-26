#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
#作用域
#在python中函数就是一个作用域 (javascript),局部变量放置在其作用域中
#C# Java 中作用域{}
#定义完成后，作用域已经生成，作用域链条向上查找

# age = 19
# def  func1():
#     age = 73
#     def func2():
#         print(age)
#     return 666
# val = func1()
# print(val)
#+++++++++++++++++++++++++++++++++++++++==
age = 19
def  func1():
    age = 73
    def func2():
        print(age)
    return func2
val = func1()
print(val)

#什么结果？
#函数名可以当返回值
