#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
data = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

"""
exit_flag = False
current_layer = menu

layers = [menu]

while not  exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice == "b":
        current_layer = layers[-1]
        #print("change to laster", current_layer)
        layers.pop()
    elif choice not  in current_layer:continue
    else:
        layers.append(current_layer)
        current_layer = current_layer[choice]

三年菜单文艺青年版
"""
'''
while True:
    for i in  data:
        print(i)

    choice = input("选择进入1>>>:")
    if choice in data:
        while True:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("选择进入2>>>:")
            if choice2 in data[choice]:
                while True:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("选择进入3>>>:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t",i4)
                        choice4 = input("选择最后一层,按d返回>>>:")
                        if choice4  == "d":
                            #break
                            pass  #占位符
                    if choice3 == "d":
                        break
            if choice2  == "d":
                break
'''
exit_flag = False

while not exit_flag: #这个条件不成立，就跳出当前循环
    for i in  data:
        print(i)   #第一层

    choice = input("选择进入1>>>:")
    if choice in data:
        while not  exit_flag:
            for i2 in data[choice]:  #打印第二层
                print("\t",i2)
            choice2 = input("选择进入2>>>:")
            if choice2 in data[choice]:
                while not  exit_flag:
                    for i3 in data[choice][choice2]:  #第三层
                        print("\t\t",i3)
                    choice3 = input("选择进入3>>>:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:   #第四层
                            print("\t\t",i4)
                        choice4 = input("选择最后一层,按d返回>>>:")
                        if choice4  == "d":
                            #break
                            pass  #占位符
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "d":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2  == "d":
                break
            elif choice2 == "q":
               exit_flag = True