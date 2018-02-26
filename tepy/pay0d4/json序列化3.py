#!/usr/bin/eenv  python
#encoding=utf-8
#lau.liu@9street.org
import  json

# def sayhi(name):
#     print("hello ",name)

info = {
    'name':'alex',
    'age':22,

}

f = open("test.text","w")
print(json.dumps(info))
f.write(json.dumps(info))

info['age'] = 21
f.write(json.dumps(info))






f.close()
