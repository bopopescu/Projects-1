#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
#变量可以指向函数，函数的参数能接收变量，那么一个函数就是可以接收另一个函数作为参数，这函数就称之为高阶函数
"""
def func(x,y):
    return  x+y

def  ss(x):
    return  x
# f = lambda x:x*x
# n =func
# ss(n)
# print(ss(func))
f = ss(func)
print(f(5,7))
"""
def func2(x,y):

    return  abs,x,y

res = func2(4,10)
print(res)