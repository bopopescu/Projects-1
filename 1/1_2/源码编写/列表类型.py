#!/usr/bin/python
# -*- coding: utf-8 -*-
# list_test=[‘张三‘,‘李四’,'alex']
# print(list_test)
# list_test=list('alex')
#
# list_test=list([‘张三‘,‘李四’,'alex'])
# print(list_test)x
# names = ['shangshan','longting']
# print(names)
# namee = []
# # 建立一个空列表
# print(namee)
# L2 = ['a','b','c','d']
# L2 [2]
# print(L2[1])


# count = 0
# for i in  names:
#     print(count,i)
#     count += 1
# enumerate() #枚举
# for i in  enumerate(names):
#     print(i)
#

# for index,i in  enumerate(names):
#     print(index,i)


# for index,i in  enumerate(names):
#     if index%2 == 0:
#         names[index] = -1
#         print(index,i)
# print(names)
# fist_index = names.index(2)
# new_list=names[fist_index+1:]
#
# second_index=new_list.index(2)
# second_val = names[fist_index + second_index+1]
# print(new_list,fist_index,second_index)
# # print(names.index(2))
# print(second_val)


products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]

print("*******************商品列表************************")
for index,p in enumerate(products):
    print("%s. %s %s" %(index, p[0],p[1]))
    continue