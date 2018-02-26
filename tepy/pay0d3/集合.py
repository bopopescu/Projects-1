#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
#列表是我们最以后最常使用的数据库类型之一，通过列表可以对数据库实现最方便的存储，修改等操作
#定义列表
#集合是一个无序的，不重重的数据组合，他的主要作用
#去重、把一个列表变成集合，就自动去重了
#关系测试、测试两组数据之前的交集、差集、并集等关系
list_1 = [1,4,5,7,3,6,7,9,2]
list_1 = set(list_1)     #集合
list_2 = set([2,6,0,66,22,8,4])  #集合
list_3 = set([1,3,7])
"""
print(list_1,list_2)
list_1.intersection(list_2)
#交集
print(list_1.intersection(list_2))
#并集
print(list_1.union(list_2))
#差集 in list_1 but not in list_2
print(list_1.difference(list_2))
#去反差
print(list_2.difference(list_1))
#子集
print(list_1.issubset(list_2))
#父集  不是子集返回False 是子集 返回True
print(list_1.issuperset(list_2))
print(list_1.issuperset(list_3))
#对称差集
print(list_1.symmetric_difference(list_2))
print("-----------------------------")
#list_2.isdisjoint()
list_4 = set([5,6,8])
print(list_3.isdisjoint(list_4))
"""
#关系测试
print(list_1 & list_2) #交集
print(list_2|list_1)  #求并集
print(list_1 - list_2) #in  list_1 but not in list_2 求差集
print(list_1 ^ list_2) #对称差集
#subset and upperset
#print(list_1  - list_2)
list_1.add(999) #添加
list_1.update([888,777,555]) #更新
#print(list_1)
#list_1.remove() #使用remove()可以删除一项 remove一个不存在的会报错
#print(len(list_1)) #set的长度
#set的长度
"""
x in s
#测试x是否是s的成员

x not in s
#测试x是否不是s的成员

s.issubset(t)
s <= t
#测试是否s中的每一个元素都在t中

s.issuperset(t)
s >= t
#测试是否t中的每一个元素都在s中

s.union(t)
s | t
#返回一个新的set包含s和t中的每一个元素

s.intersection(t)
s & t
#返回一个新的set包含s和t中的公共元素

s.difference(t)
s - t
#返回一个新的set包含s中有但是t中没有的元素

s.symmetric_difference(t)
s ^ t
#返回一个新的set包含s和t中不重复的元素

s.copy()
#返回set “s”的一个浅复制
"""
#print(list_1.pop()) #任意删除
list_1.discard('6') #删除指定一个值