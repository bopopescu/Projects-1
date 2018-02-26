#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org


import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield #yield是保存当前状态

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

c = consumer('chengzhonghua')
c.__next__()
b1 = '韭菜馅'
# b2 = '猪肉大葱'
# c.send(b1)  #可以给yield 传值，同时调用yield
#
#
# c.__next__()
# #c.__next__()
def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")
#携程 是从在单线程里面