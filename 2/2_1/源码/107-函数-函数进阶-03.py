#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b,a + b #b 重新赋值为a值   a 重新赋值 b
#         n = n + 1
#     return  "done"
# fib(10)
# print(fib(11))
# f = fib(15)
# next(f)
# print(next(f))


def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield  b  #yield 把函数执行过程 冻结在这一步 ，并且把b的值，返回给外面的next()函数
        a,b = b,a + b #b 重新赋值为a值   a 重新赋值 b
        n = n + 1
    return  "done"
f = fib(15)
for i in f:
    print(i)