#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
# a = [i for  i in range(1000)]
# print(a)
# >>> a = [i for  i in range(1000)]
# >>> a
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,...... 997, 998, 999]
# >>> a2 = (i for i in range(10000))
# >>> a2
# <generator object <genexpr> at 0x10bf13570>  #generator 生成器
# >>> next(a2)
# 0
# >>> next(a2)
# 1
# >>> next(a2)
# 2
# >>> next(a2)
# 3
# >>> next(a2)
# 4
# <generator object <genexpr> at 0x10bf13570>
# >>> next(a2)  #继续生产
# 5
# >>> next(a2)  #next() 执行往下执行 不能回退

# 9
# >>> next(a3)
# Traceback (most recent call last):  #走到最后 出错提示 执行完了 没有数据库可以继续生产
#   File "<input>", line 1, in <module>
# StopIteration
a3 = (i for i in range(10))
for i in a3:
    print(i)   #建议使用for循环 不建议使用while循环