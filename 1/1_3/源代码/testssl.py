#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
data = [
    {
        'text': '北京',
        'children': [
            {'text': '朝阳', 'children':[]},
            {'text': '昌平', 'children':[
                {'text':'沙河', 'children':[]},
                {'text':'回龙观', 'children':[]},
            ]},
        ]
    },
    {
        'text':'上海',
        'children':[
            {'text':'宝山','children':[]},
            {'text':'闸北','children':[]},
        ]
    }
]
# def name(n):
#     for i in n:
#         print(i['text'])
#         if i['children']:
#             name(i['children'])

# def name(n):
#     for  i in n:
#         if i.get('text'):
#             print(i['text'])
#         if  len(i.get('children'))!= 0:
#             print(i['children'])
uname = input('地名:>>> ')
def  name(n):
    for  i  in n:
        sl = i['text']
        if  sl == uname:
            print(True)
            break
        else:
            print(False)
            break
        if  i['children']:
         name(i['children'])
name(data)

