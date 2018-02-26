#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
import  time
user,password = 'alex','123456'

#def auth(func):
def auth(auth_type):
    """
    def wrapper(*args,**kwargs):
        username = input('username:').strip()
        password = input('password:').strip()


        if user == username and password == password:
            print("\033[32;1mUser has password authentication\033[0m")
           # func(*args,**kwargs)  #from home
            res = func(*args,**kwargs)
            print('--after authentication')
            return res
        else:
            exit("\033[31;1mInvalid  has password authentication\033[0m")
    return wrapper
    """
    print('authe func:',auth_type)
    def outer_wapper(func):
        def wrapper(*args, **kwargs):
            print('wrapper  func args:', *args,**kwargs)
            if auth_type == 'local':
                username = input('username:').strip()
                password = input('password:').strip()
                if user == username and password == password:
                    print("\033[32;1mUser has password authentication\033[0m")
                    # func(*args,**kwargs)  #from home
                    res = func(*args, **kwargs)
                    print('--after authentication')
                    return res
                else:
                    exit("\033[31;1mInvalid  has password authentication\033[0m")
            elif auth_type == 'ldap':
                print('搞毛线ldop')



        return wrapper
    return  outer_wapper
def index():
    print('weloco to index page')

@auth(auth_type="local") #我的home等于auth()
def home():
    print('weloco to home page')
    return 'from home'

@auth(auth_type="ldap")
def bss():
    print('welocoa to bss page')
index()
#home()
print(home())
bss()
