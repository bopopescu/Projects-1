#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# kevim 
# lau.liu@9street.org
import copy
names =["4kevim","Aalex","kevos", ["alex ","lsex"],"#hugo","joyy","lucy"]
names2 = names.copy()#浅复制
name3 = copy.deepcopy(names)#深复制
print(names2)
print(names)
names[2] = "好好"
names[3][0] = "heos"
print(names)
print(names2)
print(name3)
'''
person = ['name',['sacing',100]]

pl = copy.copy(person)
p2 = person[:]
p3 = list(person)
print(p3)
'''
person = ['name',['sacing',100]]
#p1 = copy.copy(person)
p1 = person[:]
p2 = person[:]
p1[0] = 'alex'
p2[0] = 'fengjie'
p1[1][1] = 50
print(p1)
print(p2)

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print (fib(40))
