#!/usr/bin/evn python35
# kevim 
# lau.liu@9street.org
#'''
count = 0
while True:
    count +=1
    if count > 50 and count < 60:
        continue
    print("你是风儿我是沙,缠缠绵绵到天涯...",count)
        #count +=1
    if count == 100:
        print("去你妈的风和沙,你们这些脱了裤子是人,穿上裤子是鬼的臭男人..")
        break
#'''
"""
my_age = 28
count = 0
while  count < 3:
    user_input = int(input("input your guess num:"))
    if user_input == my_age:
        print("congratulations, you got it !")
        break
    elif user_input < my_age:
        print( "Oops ,think bigger!")
    else:
        print("think smaller!")
    count += 1 #每次loop 计数器+1
else:
    print("你猜这么多次都不对，你是个笨蛋")
"""