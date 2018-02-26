#!/usr/bin/python
#_*_ coding:utf-8 _*_
aaa = ''
bbb = 1
#for i in range(1, 100):
i = 1

while i < 100:
    i += 1
    aaa += str(i)
    if i % 2 == 0:
        aaa += '-'
        print(aaa)
        bbb += i
        print(bbb)
        print('yes')
    else:
        aaa += '+'
        print(aaa)
        bbb -= i
        print(bbb)
        print('no')

print('字符串输出: \r\n %s \r\n计算结果: \r\n %s' %(aaa.rstrip('-'),bbb))
