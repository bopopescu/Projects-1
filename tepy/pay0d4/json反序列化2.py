#!/usr/bin/eenv  python
#encoding=utf-8
#lau.liu@9street.org
#import json
import pickle
def sayhi(name):
    print("hello2 ", name)

f = open("test.text","rb")
date = pickle.load(f)
# data = pickle.loads(f.read())
print(date)
f.close()

