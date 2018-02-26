#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# kevim 
# lau.liu@9street.org
pocdo_list = [
    ('iphone',5800),
    ('iMac Pro',9800),
    ('office',3000),
    ('leveo',3400),
    ('alex python',81),
    ('kafei',31),
    ('niunai',89),
]
user_list = input("请输入你的工资：")
shopping_list = []
if user_list.isdigit():
    user_list = int(user_list)
    while True:
        #for item in pocdo_list:
        for index,item in enumerate(pocdo_list):
            #print(item)
            print(index,item)

            user_choice = input("你要买吗>>>>:")
            if user_choice.isdigit():
                user_choice = int(user_choice)
            elif user_choice == 'q':
                print("exit .....")
            else:
                print("hvae bought below")
            """
        break