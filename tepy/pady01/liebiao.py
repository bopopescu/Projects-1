#!/usr/bin/evn python35
# kevim 
# lau.liu@9street.org
import  copy
'''
name = ['ming','minghu','jack',22,'age']
#print(name)
#name.insert(-1,"kevim")
#name.insert(5,"alex") #插入
#print(name)
#name.remove('alex')  #删除
#print(name,"##########")
#name2 = name[2:3]
#print(name2)
#del name[2:5]#删除内存中的数据库
name2 = name.pop()
print(name2)

#print(name,"****************")
#print(name[0::3])  #隔数取值  后值可以自定义
#print(name[::3])  #不常
'''
"""
name = ['misng','minghus','jacks',225,'agse',3,'mings',3,'minghua',3,'jacka',224,9,1000,2000,78,'ages','minga','minghu','jsack',223,'agyej','dmying','mingyhu','jacik',226,'asge']
print(9 in name)
name2 = ["zhangsan","lisi","wangwu",9]
"""
'''
#if 9 in name:   #判断列表中是否存在一个元素 python自带算法
#     setal = name.count(3) #获取列表中有几个（）中的数值统计
#     print("[%s]9 is/are in name" % setal)
'''
"""
if 9 in name:
    num_of_ele = name.count(9)
    posistion_of_ele = name.index(9)
    name[posistion_of_ele] = 999
    print("[%s]9 is/are in name,posistion:[%s]" %(num_of_ele,posistion_of_ele))
    print(name)
"""
'''
#for i in range(name.count(9)):
#    ele_index = name.index(9)
#    name[ele_index] = 99
#name.extend(name2) #扩展进来一个新的列表
print(name)
name.reverse() #翻转列表
#name.sort()  #python2.7版本支持 ，3.0以上不支持，字符串和字符不能在一起使用
#name2.pop() #默认删除最后一个

print(name)
#print(name2)
#print(name2)
'''
"""
print(name)
name3 = name.copy()
print(name3)
name[0] = "Misng"
name[3][1] = 2345657
#name2[3][2] = "567890"
print(name)
name2[1][2] = '234'
print(name2)
"""
'''
name3 = name[:6][2:5][1]
print(name3)
'''
"""
name3 = name.copy()  #python 默认copy第一层
name4 = copy.copy(name)#表层copy 建立内存软连接
name5 = copy.deepcopy(name)  #深度copy 独立
#name[1] = "kevim"
name3[3][2] = 444444444444444
print(name)
print(name3)
print("name",name4)
print("name5",name5)
"""
'''
name3 = name.copy()
name4 = copy.deepcopy(name)
id1 = id(name)
id2 = id(name3)
id3 = id(name4) #id是查看内存地址
print(id1,"sfe")
print(id2)
print(id3)
# copy  模块
# reverse
# sort
# pop
# extend
# index
# conut
# list[::1]
# del
'''