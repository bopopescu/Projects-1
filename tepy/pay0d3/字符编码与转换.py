#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
#unicode 默认所有字符占两个字节 中文两个字节 utf-8 统一占用三个字节
#encode  编码  decode 解码
import  sys
print(sys.getdefaultencoding())
s = u'你好'
#s_to_unicode  = s.decode("utf8")
#print (s_to_unicode)
s_to_gbk = s.encode("gbk")
print (s_to_gbk)

#print (s_to_unicode,type(s_to_unicode))
s_to_gbk = s.encode("gbk")
s_to_gbk = s.decode("").encode("gbk")
#s_to_gbk = s_to_unicode.encode("gbk")#
print (s_to_gbk)
#默认在python2.7会自动解码  默认编码是ascii  会按照系统编码解码#
gbk_to_utf8 = s_to_gbk.decode("gbk").encode("utf8")
print (gbk_to_utf8)
#反解码 字符集
n = uprint(n)

#utf8 和unicode 可以直接打印

