#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
# def func_name(arg1,arg2,arg3,*args,**kwargs):
#     pass
#func_name(2,5)
# #func_name(1,arg2=5,arg3=3)
# func_name(4,5,6,7,8,9,name =alex)
# #3    4,5,6,(7,8,9),{'name':'alex'}
age = 22
names = ['alex','jack']
def change_age():
    #age = 24
    #当前变量
    names.append(45)
    return  True,333
    names[1] = 555
    print(age)
change_age()

res = change_age()
if res[0]:
    print(res)
#说确的结束条件
#问题规模每递归一次都应该比上一次的问题规模所有减少一次
#效率低

#高阶函数

