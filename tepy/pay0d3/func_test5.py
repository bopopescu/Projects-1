#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
def test(x,y,z):
#def test(x, y):
    print(x)
    print(y)
    print(z)
#有参数函数 位置参数 x,y 实行参

#test(1,2)#与形参一一对应
#1，2是实参
#x=1
#y=2
#这个和函数定义不同两个不同数据
#test(y=1,x=2)#关键字调用，顺序无关
#关键字调用h和位置参数调用
test(x=1,y=4,z=5)
#test(3,6,y=2)  #关键参数不能写在位置参数前面，
