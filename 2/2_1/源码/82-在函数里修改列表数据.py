#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
names = ['alex','Black Girl','Peiqi']

def  change_name():
    del names[2]
    names[1]='黑姑娘'
    print(names)
change_name()
print(names)


#这个就是一个内存地址  能被修改 列表 字典 集合  以及以后学到对象  如果元组包含一个列表修改  不能被修改的 字符串  数字