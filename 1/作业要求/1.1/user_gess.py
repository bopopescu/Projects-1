_username = 'kevin'                                      #用户名
_password = '123456'                                     #密码
conut  = 0                                               #变量空值，用来计数
while conut <3:                                          #使用while循环，大于3次就退出程序循环
    username = input('UserName: ')                       #输入用户名
    password = input("PASSWORD: ")                       #输入用户密码
    if _username == username  and _password == password: #进行用户名和密码校验对比，是否正确，结果为True
        print("欢迎登陆成功")                             #用户校验正确，输入正确欢迎信息
        break                                            #用户明和密码正确，break结束while循环
    else:
        print("用户名或者密码验证错误，请重输入")            #用户名或者密码不对，输出提示信息
    conut += 1                                           #每次循环一次加一
###########################################################################################################
conut = 0
while conut <=100:
    if conut %2 == 0:
        print('偶数',conut)
    conut +=1
print('++++++偶数+++++\n')


conut = 0
while conut <= 100:
    if conut %2 == 1:
        print("奇数",conut)
    conut += 1
print('++++++奇数+++++')
count = 0
while count <= 100:
    if count %2 == 0 :
        print(count)
    if count %2 == 1:
        print(count)
    count += 1