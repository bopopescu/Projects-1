#!/usr/bin/env  python
#encoding=utf-8
#lau.liu@9street.org
"""
import time
# x = time.localtime()
# print(x)
# print(x.tm_year)
# print('this is 973 day:%d' %x.tm_yday)
# print(time.strftime("%Y-%m-%d %H:%M:%S",x))
# print(time.strptime('2017-09-18 13:28:51',"%Y-%m-%d %H:%M:%S" ))
#
# print(time.gmtime(time.time()))

v  = time.ctime() #时间戳
# 'Tue Sep 19 19:56:11 2017'
print(v)
d = time.asctime()
# 'Tue Sep 19 19:56:39 2017'
print(d)
"""
"""
import  datetime
print(datetime.datetime.now()) #获取当前时间
print(datetime.datetime.now() + datetime.timedelta(3))  #后三天时间
print(datetime.datetime.now() + datetime.timedelta(-3)) #获取三天前时间
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #后三个小时时间
print(datetime.datetime.now() + datetime.timedelta(hours=-3)) #前三个小时钱的时间
"""