#!/usr/bin/python
#_*_ coding:utf-8 _*_
#KEVIM = 'Kevim Liu'
# lau.liu@9street.org
#函数尾部的代码要想获取函数的执行结果，就可以在函数利用return语句把结果返回
# def  stu_register(name,age,soures,country="CN"):
#     print('----注册学生信息-----')
#     print('姓名:',name)
#     print('age:',age)
#     print('课程',soures)
#     print('国籍:',country)
#     if  age > 22:
#         return  False
#     else:
#         return True
# status = stu_register('王山炮',24,soures='ptyhone_devopt',country='JP')
# if  status:
#     print('注册成功')
# else:
#     print('too old  to be a student....') 案例
#注意
#函数在执行过程中只要遇到return语句，就会停止执行比返回结果，so也可以理解为return 语句代表着函数的结果
#如果未在函数中指定return，那这个函数的返回值None
# def stu_register(name,age,soures,conutry):
#     print(name,age,soures,conutry)
#     if  age >22:
#         return False
#     else:
#         return  True
# if status:
#     print('z注册成功')
# else:
#     print('注册失败')
def stu_register(name,age,soures,conutry):
    print(name,age,soures,conutry)
    return name,age    #不管return后面有多少个  返回就一个元组 可以用逗号分开

status = stu_register('alex',23,'安保',conutry='CN')
print(status)
