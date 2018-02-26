#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
#'''
import  sys
#find_str = sys.argv[1] #
#replace_str = sys.argv[2]#替换文件
f = open("l","r",encoding='utf8')
f_new = open("2","w",encoding="utf8")
#'''
#"""
for line in f:
    if "肆意的快乐等我享受" in line:
  #  if find_str in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等alex享受") #replace 方法替换修改 保存到新的文件里
        #line = line.replace(find_str,replace_str)  # replace 方法替换修改 保存到新的文件里
        f_new.write(line)
    f_new.write(replace_str)
   # else:
        #f_new.write(line)

f.close()
f_new.close()
#"""
with open('log','r') as f:
#自动关闭with文件

#with语句为了避免打开文件后忘记关闭，可以通过管理上下文，即：

#with open('log', 'r') as f:
#    ...
#如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件资源。
#在Python2.7后，with又支持同时对多个文件的上下文进行管理，即：

#with open('log1') as obj1, open('log2') as obj2:
#    pass