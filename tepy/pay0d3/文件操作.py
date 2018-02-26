#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
"""
#需要添加字符集编码 utf-8，
#data = open("yesterday",encoding='utf8').read() #赋值一个值 打开文件 ，读取里面的内容
f = open("yesterday2",'a',encoding='utf8') #文件句柄 #包含这个文件名，内存地址，硬盘地址， #w是写，创建模式 #r是读 读的模式
# #print(data)
#a 是append 追加
f.write("我爱北京天门.....,\n")
#a 是append 追加
f.write("\n when i was young i listen to the radiof\n")
f.write("天安门太阳升....") #写内容
f.write("东方红")
"""
#f = open("yesterday",'r',encoding='utf8')
"""
#low loop
#for i in range(5):
#    print(f.readline())
#循环读取前五行
#print(f.readlines()) #这是列表
for index,line in enumerate(f.readlines()): #这个只是适合读取小文件

    if index == 9:
        print("----aa-------")
        continue
    print(line.strip())
"""
'''
count = 0
for lien in f:
    if count == 9:
        print("------我是分割线---%s---====="%count )
        count += 1
        continue
    print(lien )
    count += 1
#高效使用方法  这个变成迭代器
'''
"""
print(f.tell())
print(f.readline()) #默认只读所有
print(f.readline())
print(f.readline())
#print(f.read(5))    #默认只读所有
print(f.tell()) #默认是按照字符计数
f.seek(10)#默认回去光标
print(f.readline())#这两个搭配这是用
print(f.encoding)
#print(f.errors) #这个是异常处理
#print(f.fileno()) #返回内存中的参数
print(f.name) #打印文件名字
#print(f.seekable()) #不是所有的文件用seekable   如果是普通二进制、字符串 判断
"""
#print(f.flush()) #flush 是刷新 默认是等到缓存满了，在写到内存 可以使用强制刷新
#print(dir(f.buffer) )
#f = open("yesterday2",'a',encoding='utf8')
#f.write("hello 1\n")
#f.write("hello 2\n")
#f.write("hallo 3\n")
#f.seek(10)
#f.truncate(20)#truncate 是截断 默认是从头开始截断
#实现文件读和写
"""
f = open("yesterday2",'r+',encoding='utf8')
print(f.readline())
print(f.readline())
print(f.readline())
f.write("----------------diao-----------------------")
#读写
"""
'''
f = open("yesterday2",'a+',encoding='utf8')#追加读 
f = open("yesterday2",'w+',encoding='utf8')#亵渎模式 没啥用
print(f.readline())
print(f.readline())
print(f.readline())哦'

print(f.tell())
f.write("----------------diao-----------------------\n")
f.write("----------------diao-----------------------\n")
f.write("----------------diao-----------------------\n")
f.write("----------------diao-----------------------\n")
f.write("----------------diao-----------------------\n")
print(f.tell())
f.seek(10)
print(f.tell())
print(f.readline())
f.write("should be in the begining of tthe second line")
f.close()
#亵渎模式 没啥用
'''
"""
f = open("yesterday2",'rb')#二进制文件 可读二进制文件
print(f.readline())
print(f.readline())
print(f.readline())
#b代表   #网络传输，只能使用二进制模式传输
"""
'''
f = open("yesterday2",'wb')#可写二进制文件
f.write("hello binary\n".encode(encoding='utf8'))  #申明：要申明字符集
f.close()
'''

