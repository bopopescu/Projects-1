#!/usr/bin/python
#_*_ coding: utf-8 _*_
import  os
s = open('wgs.txt','r').read()
if s.isdigit():
    s = int(s)
if s > 0 :
    print('yes')
else:
    print('no')
wgsh = input('shuru :>>>')
f = open('wgs.txt', 'w')
f.write(wgsh)
f.close()
