#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
f_name = open('1.txt','r+',encoding='utf-8')
date  = f_name.read()
odl_str = '岳妮妮'
new_str = '你好'

for    line in date:
    if  odl_str in line:
        line  = line.replace(odl_str,new_str)



# size=f_name.tell()
# f_name.truncate(size)
# f_name.flush()
# print(f_name.tell())
# f_name.close()

# f_name.truncate(f_name.tell())
# f_name.flush()f_name.write(line)
# f_name.write(line)
# f_name.close()


# print(f_name.read())
# print(f_name.tell())

