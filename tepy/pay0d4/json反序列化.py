#!/usr/bin/eenv  python
#encoding=utf-8
#lau.liu@9street.org
#import json
import pickle
def sayhi(name):
    # print("hello ",name)
    print("hello2 ", name)

f = open("test.text","rb")
# data = json.loads(f.read())
data = pickle.loads(f.read())
print(data["name"])
print(data["age"])
print(data["func"]("kevim"))
f.close()
#pickle 只能在python里使用 通用json
