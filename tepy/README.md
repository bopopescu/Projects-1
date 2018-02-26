#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
product = [
    ('iphone',58000),
    ('Mac Pro', 9800),
    ('Bike',800),
    ('whtch',10600),
    ('Coffice',31),
    ('alex python',120),
]

shopping_list = []

salary  = input("请输入你的金额：")

if salary.isdigit():

    salary = int(salary)   #判断输入的是不整数 如果不是整数，强制转换为整数

    while True:

        for index,item in  enumerate(product):

            print(index,item)

        user = input("xuan zen gou mai :>>>")


        if user.isdigit():

            user = int(user)


            if  user < len(product) and user  >=0:
                p_item = product[user]

                if p_item[1] <= salary:

                    shopping_list.append(p_item)
                    print("---->",shopping_list)
                    salary -= p_item[1]


                    print("add  %s int shopping ,cart currnt is%s"%(p_item,salary))

                else:

                    print('你的余额只剩%s啦，余额不够卖了'%(salary))


            else:
                print('sss')

        elif user == 'q':

            print('exit ......')
            print("==================shopping_list======================")
            for  p in shopping_list:
                print(p)
            print("还剩 %s 钱"%(salary))
            exit()

        else:
            print('have bought below')

      #  break