#!/usr/bin/env python
#_*_ coding:utf8 _*_
#求100以内不能被3整除的所有数，并把这些数字放在列表sum=[]里，并求出这些数字的总和和平均数。
s = []
for  i in range(0,101):
    if  i %3 == 0:
        print('yes',i)
    else:
        print('no',i)
        s.append(i)
ls = sum(s)
print(ls)
print(ls / len(s))
