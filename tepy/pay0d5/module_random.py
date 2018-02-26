#!/usr/bin/env  python
#encoding=utf-8
#lau.liu@9street.org
import random
print(random.random()) #随机数  0到1之间的浮数
print(random.randint(1 , 5)) #之间数
print(random.randrange(1,4))#包含开头，不包含结尾数
print(random.choice('hello')) #序列，字符串，元组
print(random.sample('hello',2)) #定位去数位
print(random.uniform(1,3)) #之间浮动
items = [1,2,3,4,5,6,7]
print(items)
x = random.shuffle(items)
print(x)
print(items)
# print(help(random.random))