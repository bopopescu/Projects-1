# while循环
#要求循环100次
coun  = 0
# while  coun <= 100:
#     print("loop", coun)
#     coun += 1
#需求二 循环1到一百次 只打印奇数
# while coun <= 100:
#     if coun %2 == 1:
#         print("conu",coun)
#     coun += 1
#需求三 while循环 一直一百次 不打印50至60之间 70到80的平方
"""
1.1 count <= 100
    1.1.1 打印("conu",coun)
      1.2 if conut >= 50 and count <=60
        1.2.1  打印所有的数 除了50至60之间数不打印
      1.3 if conut >=70 and conut <=80:
        1.2.1 打印70至80之间相乘的平方
    1.1.2 每次循环累计加一
"""
while coun <=100:
    #print('conu',coun)
    if coun >=50 and coun  <=60:
        #print("conunt",coun)
        pass #pass是一个占位行符
    elif coun >=70 and coun <=80:
        print('countn',coun*coun)
    else:
        print('conu', coun)
    coun += 1