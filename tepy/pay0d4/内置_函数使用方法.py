# #!/usr/bin/env python3
# #encoding=utf-8
# # kevim
# # lau.liu@9street.org
# # print(all([0,-5,3]))
# # #非零及为真
# # print(any([]))
# # ########################################
# # a = ascii([1,2,"年后"])
# # print(type(a),[a])
# """
# #>>>bin(1)
# '0b1'
# #>>>bin(255)
# '0b11111111'
# #把数字转换成二进制 在进行运算
# """
# '''
# >>>bool(1)
# True
# >>>bool(0)
# False
# >>>bool([1])
# True
# '''
# """
# a = bytes('abcde',encoding='utf8')
# b = bytearray ('abcde',encoding='utf8')
# print(b[1])
# b[1] = 100
# print(b)
# #print(a.capitalize(),a)
# #字符串不能修改，二进制不可以修改   ，列表可以修改
# """
# '''
# def sayhi():pass
# print(callable([]))
# print(callable(sayhi))
# #函数加calleable可以调用
# '''
# """
# >>>chr(98)
# 'b'
# >>>ord('b')
# 98
# """
# '''
# code = "for i in range(10):print(i)"
# print(code)
# c = compile(code,'','exec')
# # 预编译 可执行文件
# exec(c)
# '''
# """
# code = '1+3/2*6'
# #print(code)
# c = compile(code,'','eval')
#  print(c)
# print(eval(c))
# """
# #dict() #生成默认字典
# # dir是查看方法
# """
# >>>divmod(3,6)
# (0, 3)
# >>>divmod(5,6)
# (0, 5)
# >>>divmod(5,2)
# (2, 1)
# >>>divmod(5,4)
# (1, 1)
# #除于等于余数
# """
# '''
# def sayhi(n):
#     print(n)
# sayhi(3)
# '''
# """
# (lambda n:print(n))(5)
# #匿名函数 只能处理简单的数据 只能用于三元运算方法
# calc = lambda n:print(n)
# calc(8)
# """
# '''
# import functools
# res = filter(lambda  n:n>5,range(10))
# #一组数据过滤想要的数据库
# rse = map(lambda n:n**n,range(10))
# #对传入的值进行，
# ser = functools.reduce(lambda x,y:x+y,range(10))
# print(ser)
# # for i in rse:
# #     print(i)
# '''
# """
# a = frozenset([1,3,333,213,44,44,12,4])
# """
# '''
# print(globals())
# #查看当前文件里有哪些变量
# '''
# """
# print(hash('alex'))
# #hash 数据算法
# """
# def aset():
#     local_var = 333
#     print(locals())
#     print(globals())
# aset()
# print(globals())
# print(globals().get("local_var"))

#object
#面向对象 世界万物都是都对象
#print(oct(9))
#oct 是与8八进一，oct是八进制
#print(pow(2,32))
#pow 计算方式

# >>>code = "for i in range(10):print(i)"
# >>>c = compile(code,'','exec')
# >>>c
# <code object <module> at 0x104495b70, file "", line 1>
# >>>repr(c)
# '<code object <module> at 0x104495b70, file "", line 1>'
# #变成一个字符串
# round(11.3342,4)
# 11.3342
# slice(2,5)
# slice(2, 5, None)
# d = range(20)
# d
# range(0, 20)
# d[slice(2,5)]
# range(2, 5)

# a = {6:2,8:0,1:4,-5:6,99:11,4:22}
# print(sorted(a.items()))
# print(sorted(a.items(),key=lambda x:x[1]))
# print(a)
# #字典是无序的，排序，安装key排序，值排序
# a = [1,2,3,4,5]
# b = ['a','b','c','d','e']
# print(zip(a,b))
# for i in zip(a,b):
#     print(i)

import  decorator
__import__('decorator')
