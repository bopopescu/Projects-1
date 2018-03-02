#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
def range2(n):
    conut = 0
    while  conut < n:
        print('conut',conut)
        conut += 1
        yield   conut #return


print(range2(10))
range2(10)
new_range = range2(4)
r1 = next(new_range)
print(r1)
r2 = next(new_range)
print(r2)
next(new_range)
next(new_range)