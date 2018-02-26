#!/usr/bin/env python3
#encoding=utf-8
# kevim 
#lau.liu@9street.org
name = "kevim \t a {alex}isl lsdfa and is {yes} old"  #\t 代表tab键
print(name.capitalize())  #首字母大写
print(name.count("a")) #统计
print(name.center(50,"_"))# 打印自动不全
print(name.endswith("a")) #判断一个结尾
print(name.expandtabs(tabsize=30))  #添加空格
print(name[name.find("lsdfa"):]) #查找
print(name.format(alex='hello',yes='34'))
