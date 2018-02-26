#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
# def  calc(x,y):
#     if x < y:
#         return  x*y
#     else:
#         x/y
# print(lambda  x,y:x*y)
#
# # func = lambda x,y:x*y
# func = lambda x,y:x*y if  x <y else x/y
# print(func(3,5))
#
# print(calc(3,8))
data  = list(range(10))
# print(data)
#
# for  index,i in enumerate(data):
#     data[index] = i*i
# print(data)

data  = list(range(10))
def f2(n):
    return  n*n
print(list(map(f2, data)))
print(list(map(lambda x:x*x ,data)))
#匿名函数节省代码量
#看着高级
