#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
"""
def loggol():
    with open('a.txt' ,'a+') as f:
        f.write('and action\n')

def test1():
    print ("test1 starting action...")
    loggol()

def test2():
    print ("test2 starting action...")
    loggol()
def test3():
    print ("test3 starting action...")
    loggol()
"""


import  time
def logger():
    #添加日期时间 模块time时间模块
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    with open('a.txt','a+') as f:
        f.write("time  %s and action....\n" %time_current)
def test1():
    print('test1 start ')
    logger()
def test2():
    print('test1 starts ....')
    logger()
def test3():
    print('test3 stalsl')
    logger()
test1() #打印输出打一个函数的标准输出
test2()
test3()
