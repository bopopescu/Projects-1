#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org

import time

def timer(func): #嵌套韩式使用
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
       #func()
        #return func #使用return返回高阶函数的值
        stop_time = time.time()
        print('the func run time is %s' %(stop_time - start_time))
    return  deco

# def timer():
#     def deco():
#         pass
# #嵌套函数使用方法

@timer
def test1():
    time.sleep(3)
    print('in the test1')
# @timer
# def test2():
#     time.sleep(3)
#     print('in the test2')

# deco(test1)
# deco(test2)
################################
#这种是改函数的调用方式
################################
# test1=deco(test1)
# test1()
# test2=deco(test2)
# test2()
#**********************************
# print(timer(test1))
@timer #test 等于timer传到test3 等于（deco） test3()添加括号
def test3(name,age ):
    time.sleep(3)
    print('in the test3',name,age)

test1()
#test2()
test3('alex',22)
