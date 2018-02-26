#!/usr/bin/evn python35
# kevim 
# lau.liu@9street.org
#type(2**32）  #type 是查看数据类型
msg = "我爱北京天安门"
print(msg)
print(msg.encode(encoding="utf-8" ))   #没有指定编码，默认使用系统默认编码
print(msg.encode(encoding="utf-8" ).decode())
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))
