#!/usr/bin/python
#_*_ coding:utf-8 _*_
su = []
for i in range(0,100):  #0到100数
    if i %3 == 0:
        print(i,'y')
    else:
        su.append(i)
ls = sum(su)
print(ls)
sl = ls / len(su)
print(su,'列表')
print(sl,'平均值')
# sum