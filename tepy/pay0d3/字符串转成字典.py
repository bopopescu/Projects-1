#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
b = """ {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }"""
print(b)

print(eval(b))