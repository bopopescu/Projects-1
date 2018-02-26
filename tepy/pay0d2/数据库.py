#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# kevim 
# lau.liu@9street.org
#names = ["11 22 33 44 55 66 77 88 99 110"]
names =["4kevim","Aalex" ,"#hugo","joyy","lucy"]
#print(names[1:3])#简单切片
#print(names[0:-1])#简单切片
names.append("hugo")#增加
names.insert(-1,"matt")#插入
#names[2] = "xiaoming"
#names.remove("hugo") #删除
#names.pop()#删除
#del names[0] #删除
#ame = names[names.index("hugo")]
#print(names.count("hugo")) #统计
#print(names.clear()) #清空
#names.reverse() #反转
#names.sort()
names2 = [1,2,3,4,5,6,7,8,9]
names.extend(names2)#合并
del names2#删除变量名

print(names)
