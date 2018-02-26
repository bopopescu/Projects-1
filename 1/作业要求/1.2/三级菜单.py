#!/usr/bin/python
# -*- coding: utf-8 -*-

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

exit_flag = False
while not  exit_flag :
    for i in data:
        print(i)
    next_n = input("选择地区进入下一级,按d返回上一级、按q退出:")
    if  next_n in data:
        while not  exit_flag:
            for i2 in data[next_n]:
                print(i2)
            next_n2 = input("选择地区下一级,按d返回上一级、按q退出:")
            if  next_n2  in data[next_n]:
                while not exit_flag:
                    for i3 in  data[next_n][next_n2]:
                        print(i3)
                    next_n3 =  input("选择地区下一级,按d返回上一级、按q退出:")
                    if  next_n3 in  data[next_n][next_n2]:
                        while not exit_flag:
                            for i4  in data[next_n][next_n2][next_n3]:
                                print( i4)
                            next_n4 = input("选择最后一级,按d返回上一级、按q退出:")
                            if next_n4 == 'd':
                                break
                            elif next_n4 == 'q':
                                exit_flag = True
                    if next_n3 == 'd':
                        break
                    elif next_n3 == 'q':
                        exit_flag =True
            if  next_n2 == 'd':
                 break
            elif next_n2 == 'q':
                exit_flag = True
    elif next_n == 'q':
        exit_flag = True
