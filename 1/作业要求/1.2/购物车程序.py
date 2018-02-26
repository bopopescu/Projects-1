#!/usr/bin/python
#_*_ coding:utf-8 _*_
goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998},
        {"name":'IPhonex',"price":9000},
        {"name":'vivox',"price":4000},
        {"name":'macbook ',"price":8200},
]
shopping_cart= []  #空的列表
nameuser = 'alex';paswod = '123456'    #用户名和密码 默认变量
wage = input('请输入你的工资：>>>:')             #   输入工资
if  wage.isdigit():
    wage = int(wage)     #对输入的工资进行init类型转换
unameser = input('unameuser:>>>'); password = input('PASSWORD:>>>>')     #输入用户 密码
if unameser == nameuser and  paswod == password:   #对用户名和名密码进行校验  是否正确
    print('登录成功，进入选购买商品')
    while True:
        for index,p in enumerate(goods):
            print(index,p['name'],p['price'])
        cheice = input("请输入你需要购买的商品：>>>")
        if cheice.isdigit():
            cheice = int(cheice)
            if cheice >= 0 and cheice < len(goods):
                sl = goods[cheice]['price']
                if  wage >= goods[cheice]['price']:
                    print ('有钱')
                    wage = wage - goods[cheice]['price']
                    print(wage)
                    shopping_cart.append(goods[cheice])
                else:
                    print('你好，你的余额不足，退出请输入<q>')
        elif cheice == 'q':
            print('*' * 25, "你收购买的商品", '*' * 25)
            for  index,k in enumerate(shopping_cart):
                print ('\33[40;31m')
                print(index,k['name'],k['price'] )
                print ('\33[0m')
            print('*'*25,"你的余额%s" %(wage),'*'*25)
            exit()
else:
    print('密码或者用户输入错误')