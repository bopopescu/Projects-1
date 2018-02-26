#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
def cale(n,count):
    print(n,count)
    if  count  < 5:
        return  cale(n/2,count+1)      #里面那一层 返回 最终结果
    else:
        return  n       #这个return 不可以少

res = cale(188,1)
print('res',res)

