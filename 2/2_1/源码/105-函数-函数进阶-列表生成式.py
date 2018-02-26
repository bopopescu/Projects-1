#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’

>>> a = list(range(10))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a = [ i for i in a]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a = [i*i for i  in a]
>>> a
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> a = [i if i <5  else  i*i for i in a]
>>> a
[0, 1, 4, 81, 256, 625, 1296, 2401, 4096, 6561]