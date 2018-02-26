#!/usr/bin/python
# -*- coding: utf-8 -*-
products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
shooping_cart = []
exit_flag = False
while not  exit_flag:
# while True:
    print('***********商品列表********')
    for index,p in enumerate(products):
        print("%s: %s  %s" %(index,p[0],p[1]))

    choice = input("输入想买商品:")

    if choice.isdigit():
        choice = int(choice)
        if  choice >=0 and choice < len(products):
            shooping_cart.append(products[choice])
            print("adod product %s into shopping cart " %(products[choice]))
        else:
            print("商品不存在")
    elif choice == "q":
        if  len(shooping_cart) >0:
            print("**********************已购买一下商品 ******************")
            for index,p in enumerate(shooping_cart):
                print("%s: %s  %s" %(index,p[0],p[1]))
        # break
        exit_flag  = True