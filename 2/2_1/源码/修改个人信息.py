#!/usr/bin/env python
# coding=utf-8
# author = ‘landun’
def print(account,username):
    person_data=account[username]
    info ='''
    ------------------
    名字:   %s
    年龄:   %s
    职位 :   %s
    Dept:   %s
    Phone:  %s
    ------------------
    '''%(person_data[1],
         person_data[2],
         person_data[3],
         person_data[4],
         person_data[5]
         )
    print(info)

def save_file(account):
    f.seek(0)
    f.truncate() #清空原文件
    for k in account:
        row = ",".join(account[k])
        f.write("%s\n"%row)

    f.flush()  #强制保存到硬盘中

    pass
def change_personal_info(account,username):
    pass
