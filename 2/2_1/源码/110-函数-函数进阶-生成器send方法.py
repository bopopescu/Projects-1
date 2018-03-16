#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
def range2(n):
    conut = 0
    while  conut < n:
        print('conut',conut)
        conut += 1
        sign = yield   conut     #return   区别是
        if sign  == 'stop':
            print('----sign', sign)
            break
        print('----sign', sign)
    return  3333

new_range = range2(3)

n1 = next(new_range)
print('do  sth else ...')
new_range.send('stop')

#1、唤醒并继续执行
#2、 发送一个信息到生成 器内部
