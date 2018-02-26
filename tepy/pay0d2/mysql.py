#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# kevim 
# lau.liu@9street.org
import  pymysql
import sys
print(sys.getdefaultencoding())
db = pymysql.connect(host='192.168.192.100',port=3306,user='root',passwd='123456',db="zabbix_status")
cursor= db.cursor()
sql = "SELECT * FROM domain_status  WHERE id >'%d'" %(1)
try:
    cursor.execute(sql)
    results = cursor.fetchone()
    for row in results:
        id = row[0]
        name = row[1]
        print("id =%d,name=%s" % (id ,name))
#cursor.execute('select version()')
#data1=cursor.fetchone()
#print('db version is:%s' %data1)
except:
    print("Error :unable to fecth data")
db.close()