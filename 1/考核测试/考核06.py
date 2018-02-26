#!/usr/bin/env python
#_*_ coding:utf8 -*-
#求1～100间所有偶数的和（亦可奇数和）（编程题）。
#求1到100的奇数和 偶数和
#同时打印出结果 不能分开计算
a = 0
b = 0
#while i <100:
#    if i %2 == 0:
#        a += '+'
#    elif i %3 == 0:
#        b += '+'
for i in range(0,101):
    if  i % 2 == 0:
        a += i
    elif i % 2 == 1:
        b += i
print(a,b)




