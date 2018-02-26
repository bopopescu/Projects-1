#!/usr/bin/env python3
#encoding=utf-8
# kevim
# lau.liu@9street.org
"""
def bar():
    print('in the bar')
def test1(func):
    print(func)

test1(bar)
"""
###################################
'''
def bar():
    print('in the bar')
def test1(func):
    print(func)
    func()
test1(bar)
func = bar()
'''
###################################
"""
import time
def bar():
    print('in the bar')
    time.sleep(3)
def test1(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print('the func run time is %s' %(stop_time - start_time))
test1(bar)
func = bar()
"""
###################################
import  time
def bar():
    time.sleep(3)
    print('in the bar')
def test2(func):
    print(func)
    return  func
print(test2(bar))
t=test2(bar)
print(t)
t()
bar=test2(bar)
bar()
