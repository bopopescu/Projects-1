#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
'''
def test(x,y,z=2):
    print(x)
    print(y)
    print(z)

test(1,2)
#不能超出定义参数，也不能少于定义参数
#参数组
def test1(*args):
    print(args)
test1(1,2,3,4,5,6,7,888,99)
#把形参放在元组里
test1(*[1,2,3,4,5,6,67,7,8,8,]) #args=tuple([1,2,3,4,5,6]) 元组
#列表传参
'''
"""
def test2(x,*args):
    print(x)
    print(args)
test2(1,2,3,4,5,6,6,7,8,9,)
#args接受N个位置参数，转换成元组形式

"""
'''
def test3(**kwargs):
 #   print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
test3(name='alex',age=8,sex="F")
test3(**{'name':'alex','age':'8'})

#关键字参数
#**kwargs 把N个关键字参数，转换成字典的方式
'''
"""
def test3P(name,**kwargs):
    print(name)
    print(kwargs)
test3P('alex',age=8,sex='m')
"""
'''
#def test4(name,age=8,**kwargs):
def test4(name, age=8,*args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger('test4')

def logger(source):
    print("from  %s" % source)



#test4('alex', sex="m", hobby='tesla')
test4('alex',sex="m",hobby='tesla',age=18)
#位置参数不能写在关键字参数后面
'''
def test4(name, age=8,*args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger('test4')
#test4('alex',sex="m",hobby='tesla',age=18)
def logger(source):
    print("from  %s" % source)
test4('alex', sex="m", hobby='tesla', age=18)