#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
def  stu_register(name,age,soures,country="CN"):
    print('----注册学生信息-----')
    print('姓名:',name)
    print('age:',age)
    print('课程',soures)
    print('国籍:',country)
    # print(name,age,soures,country)

# stu_register('王山炮',22,'ptyhone_devopt')
# stu_register('张三',21,'linux')
# stu_register('李四',21,'linux')
stu_register('王山炮',soures='ptyhone_devopt',age=22)