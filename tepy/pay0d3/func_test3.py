#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
def test01():
    pass
def test02():
    return 0
def test03():
    return  0,10,'hello',['alex ','lb'],{'wuoalang':'lb'}
t1 =test01()
t2 = test02()
t3 = test03()
print('form test01 return is [%s]:' %type(t1),t1)
print('form test01 return is [%s]:' %type(t2),t2)
print('form test01 return is [%s]:' %type(t3),t3)