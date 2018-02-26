#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
def add(a,b,f):
    return f(a)+f(b)

res = add(3,-6,abs)
print(res)