#!/usr/bin/env python
#_*_ coding:utf8 -*-
#实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
unameuser = 'alex'
password = '123'
username  = 'servern'
#默认用户名和密码
conut = 0
while  conut < 3:  #while 循环
    nameuser = input('请输入用户名:>>> ')
    passwd  = input('请输入密码:>>>> ')
    if  unameuser == nameuser and  password == passwd :  #进行对用户名和密码进行校验if 分支判断
        print('验证正确')
        break
    elif  username == nameuser and password ==  passwd:
        print('验证正确01')
        break
    else:
        print('输入错误')
    conut += 1