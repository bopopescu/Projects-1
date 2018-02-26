conu_username = 'kevin'                                      #用户名
_password = '123456'                                     #密码
conut  = 0
#变量空值，用来计数
while conut < 3:                                          #使用while循环，大于3次就退出程序循环
    username = input('UserName: ')                       #输入用户名
    password = input("PASSWORD: ")                       #输入用户密码
    file_list = open("user.txt", "r").read()
    if file_list == "1":
        print("由于您的账户已被锁定，无法登陆")
        # exit(1)
        kou = input("您的账户由于被锁定，请问是否解锁账户(y/n)?: ")
        if kou == 'y' or kou == 'y':
            file_list = open("user.txt","w")
            file_list.write("0")
            file_list.close()
        else:
            exit(1)
            continue
    if  _username == username  and _password == password: #进行用户名和密码校验对比，是否正确，结果为True
        print("欢迎登陆成功")                             #用户校验正确，输入正确欢迎信息
        break                                            #用户明和密码正确，break结束while循环
    else:
        print("用户名或者密码验证错误，请重输入")            #用户名或者密码不对，输出提示信息
    conut += 1
    if  conut == 3:
        file_user = open("user.txt", "w")
        file_user.write("1")
        file_user.close()
        print('账户已被锁定，退出登录，请联系管理员解锁账户')
        exit()


