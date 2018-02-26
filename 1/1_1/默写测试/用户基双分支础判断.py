"""
_username = "kevin"
_password = '123456'

username = input("username: ")
password = input("password: ")

if username == _username and password == _password :
    print("welcome" , _username)
else:
    print("wrong username or password")

"""

name = input("name： ")
sex = input("sex: ")
age = int(input("age: "))
#if ex  == 'f':
#1如果 是女生
 # 1.1 如果年龄 小于28
 #   1.1.1 打印喜欢女生
 # 1.2 打印姐弟恋
 #   2 如果是男生 打印搞基
if sex == "f":
    if age <28 :
         print("I love girls")
    else :
        print("姐弟恋很好")
else:
    print ("一起来搞基")