#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’

user_status = False   #用户登录了就把这个改成True
def login(auth_type):
    def auth(func):
        def inner(*args,**kwargs):
            _username = "alex" #假装这是DB里存的用户信息
            _password = "abc123" #假装这是DB里存的用户信息
            global user_status
            if user_status == False:
                username = input("user:")
                password = input("pasword:")
                if username == _username and password == _password:
                    print("welcome login....")
                    user_status = True
                else:
                    print("wrong username or password!")
            else:
                print("用户已登录，验证通过...")
            if  user_status == True: #判断user_status 是不是True  如果不是True  就返回登录界面
                func(*args,**kwargs)  #可以传任何参数
            else:
                print("only support qq ")
        return inner
    return auth

def home():
    print("---首页----")


def america():
    print("----欧美专区----")

@login('wx')
def japan():
    print("----日韩专区----")

@login('qq')  #henan = login('qq')(henan) = inner
def henan(style):
    print("----河南专区----",style)




#
# xx = login('qq')
# print(xx)
# henan=xx(henan)
# print(henan)

henan('3p')
japan()

