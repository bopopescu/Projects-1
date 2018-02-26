#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
import pymysql
import  sys
from mysqld import  dns_list
print(dns_list)
while True:
    for dns_https in dns_list:
        print( dns_https)


#db = pymysqlzhe.connect(host="192.168.192.100",port=3306,user='root',password="123456",)