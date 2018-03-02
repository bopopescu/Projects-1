#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
a = (i  for i in  range(10))
print(a)

# s = next(a)
# print(s)
# while   True:        #while 循环会报错
#     print(next(a))


# for  i in  a:              #一般都是采用for循环
#     print(i)

# for  i in range(10):     #range 也是一个生成器
#     print(i)

#python2 的 xrange 与    python3 的range

# python2
#     range = list
#     xrange = 生成器
# python3
#     range  = 生成器
#     xrange = 没有
#  yield  vs  return
#  return 返回 并终止function
#  yield  返回 数据 并冻结当前的执行过程
#  next() 唤醒冻结的执行过程  继续执行 直到遇到下一个yield
