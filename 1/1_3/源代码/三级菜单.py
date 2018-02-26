#!/usr/bin/python
#_*_ coding: utf-8 _*_
data = { '北京':{
            '海淀':{'五道口':{'soho':{},'网易':{},'google':{},},
            '中关村':{ '爱奇艺':{},'汽车之家':{},'youku':{},},
            '上地':{ '百度':{},}, },
            '昌平':{'沙河':{'老男孩':{},'北航':{},},
            '天通苑':{},'回龙观':{},},
            '朝阳':{},
            '东城':{},},
      '上海':{
            '闵行':{"人民广场":{'炸鸡店':{} ,} ,},
            '闸北':{'火车战':{'携程':{},},},
            '浦东':{}, },
     '山东':{},
     }

current_layer =  data

layer = []

while True:
    for k in  current_layer:
        print(k)
    choice = input('>>>:').strip()
    if not  choice:continue
    if  choice in current_layer:
       layer.append(current_layer)
       print(layer)
       current_layer = current_layer[choice]

    elif choice == 'b':
        if len(layer) != 0:
            current_layer = layer.pop(-1)
        else:
            print("已经是顶层了")
    elif choice == 'q':
        exit('bye 再见')








