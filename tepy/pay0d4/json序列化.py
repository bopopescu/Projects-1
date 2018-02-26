#!/usr/bin/eenv  python
#encoding=utf-8
#lau.liu@9street.org
#import  json
import  pickle
def sayhi(name):
    print("hello ",name)

info = {
    'name':'alex',
    'age':22,
     'func': sayhi
}

f = open("test.text","wb")
# print(json.dumps(info))
# f.write(json.dumps(info))
print(pickle.dumps(info))



f.write(pickle.dumps(info))
f.close()
