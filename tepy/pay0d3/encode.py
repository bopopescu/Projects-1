#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
#-*- coding:gbk -*-
"""
s = "哈哈"
print(s)
s_bak = s.encode("gbk")

print(s_bak)
gbk_to_utf8 = s_bak.decode("gbk").encode("utf8")
print(gbk_to_utf8)

print(s.encode("gbk"))
print(s.encode())
"""
#在不同的字符编码之前转换，都要转换成unicode
#不但转成编码 还转换成bs类型

s = "哈哈"
print(s)
print(s.encode("gbk"))
print(s.encode("utf8"))
print(s.encode("utf8").decode("utf8").encode("gb2312"))
print(s.encode("utf8").decode("utf8").encode("gb2312").decode("gb2312"))