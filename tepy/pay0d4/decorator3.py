#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
def foo():
    print('in the foo')
    def bar():
        print('in the bar')


    bar()
foo()