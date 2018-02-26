#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
import  os

# f_name= "1.txt"
# f_new_name = '%s.neew'%f_name
# old_str = '叶梓萱'
# new_str = '贺婉萱'
#
# #
# f = open(f_name,'r',encoding='gbk')
# f_new = open(f_new_name,'w',encoding='utf-8')
# for lien in f:
#     if  old_str in lien:
#         lien = lien.replace(old_str,new_str)
#     f_new.write(lien)
# f.close()
# f_new.close()

f_name= open("1.txt",'r+',encoding='gbk')
data = f_name.read()
print(f_name.readline())
print(f_name.tell())
print(f_name.seek(2))
print(f_name.readline())
f_name.truncate()
f_name.flush()
