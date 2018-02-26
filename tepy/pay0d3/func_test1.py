#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
#函数
def func1():
    """test 测试"""
    print('in the func1')
    return 0
#过程
def func2():
    """test ing 2"""
    print('in the func2')

x = func1()
y = func2()
#函数和过程两这都可以条用，python的过程也当做了一个函数
#python给阴的过程定义了返回结果
print('from func1 return is %s' %x)
print('\t from func2 return is %s' %y)
