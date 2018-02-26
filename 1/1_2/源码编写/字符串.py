#!/usr/bin/python
# -*- coding: utf-8 -*-
s = 'Hello World'
print(s.swapcase()) #原来大写变小写 原来的小写变大写
print(s.casefold()) #全部变小写
print(s.center(50,'*'))  #补全，
print(s.count('o'))

print(s.expandtabs()) #每个单词首字符大写
s2 = 'a\tb'
print(s2)  #tab 键

print(s2.expandtabs())
print(s2.expandtabs(20))
print(s.find('o'))
print(s.find('osdf'))
print()