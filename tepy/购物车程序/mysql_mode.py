#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
import  pymysql
import  sys
#print(sys.getdefaultencoding())
db = pymysql.connect(host='192.168.192.140',port=3306,user='root',passwd='123456',db="jiankong",charset='utf8')
coun = db.cursor()
sql = "select * from domain01"

coun.execute(sql)
row1 = coun.fetchall()
print(row1)
for dns_list in row1:
    dns_list1 = dns_list[2]
    print(dns_list[1],dns_list1,dns_list[4])

coun.close()
db.close()
