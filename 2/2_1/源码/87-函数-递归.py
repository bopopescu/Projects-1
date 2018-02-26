#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
# 把10不断除于2，只能不能除为止，打印每次结果
"""
n = 10
def func(n):
    n =int(n/2)
    # print(n)
    return  n


r1 = func(10)
r2 = func(r1)
r3 = func(r2)
print(r3)
"""
n = 10
#import sys  默认是1000
#sys.getrecursionlimit(1000)   可以修改默认参数
#print(sys.getrecursionlimit())
def  func2():
    pass
#
# def func(n):
#     n =int(n/2)
#     print(n)
#     func(n)
#
# func(10)

def func(n):
    n =int(n/2)
    print(n)
    if n >0:
        func(n)
    print(n)

func(10)