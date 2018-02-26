#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
#"""
info = {
    'stu1101':"TengLan Wu",
    'stu1102':"LongZe Luola",
    'stu1103':"Xiaoze Maliya",
}
#key-value
#print(info)

"""
print(info["stu1101"])  #查找
info["stu1101"] = "武藤兰" #修改
info["stu1104"] = "添加"  #添加
del  info["stu1101"]  #标准删除
info.pop("stu1102") #标准删除
info.popitem()    #随机删除

print(info.get('stu1103'))  #正常使用
print('stu1104' in info) #python 2.7 info.has_key('stu1104')
"""

#print(info)
#"""
'''
av_catalog = {
    "uomei":{
        "wwwyoupron":[" 质量"],
    },
    "日韩":{
    "tokyo-host":["质量不清楚"],
   },
    "大陆":{
        "1024":["全部","免费"]
    },
}

print(av_catalog)   #字典嵌套
av_catalog["大陆"]["1024"][1] = "可以做镜像" #修改
print(av_catalog)
print(av_catalog.keys()) #拿到他的key索引
print(av_catalog.values()) #拿到他的 键值
print(av_catalog.setdefault("台湾",{"www.baidu.com":[1,2]})) #增加一个新的值
print(av_catalog)
print(av_catalog.update())
'''
"""
b = {
    'stu1101':"alex",
    1:3,
    2:5,
}
print(b)
info.update(b)  #更新字典，没有的新添加，更新已存在的
print(info)
c = dict.fromkeys([6,7,8],[1,{"name":"alex"},444])#初始化一个新的字典
print(info.items()) #把一个字典转成一个列表
print(c)
c[7][1]['name'] = "jck chen"
print(c)
"""
for i in info:
    print(i,info[i])  #字典转换列表 for循环字典列表

for k,v in info.items():
    print(k,v)