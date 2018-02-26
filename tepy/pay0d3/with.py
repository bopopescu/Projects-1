#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
"""
with open('l',"r",encoding="utf-8") as f:
    #print(f.readline())
    for line in f:
        print(line)
#是帮你关闭
"""
#python官方开发规范，一行不能同时打开80个字符，'
with open('l',"r",encoding="utf-8") as f, \
        open('l', "r", encoding="utf-8") as f2:
    #print(f.readline())
    for line in f:
        print(line)