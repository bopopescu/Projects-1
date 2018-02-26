#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
#报警邮件
# def send_alert(mas,*args):
#     for u in args:
#         print('发送给某个ren',u)
#
#
# # send_alert('量','alex','see')
# #方式一
# #如果参数中出现，*users，传递的参数就可以不再固定个数，传过来的所有参数打包元祖  *args, **kwargs
#
#
# #方式二
# #
# def send_email(msg,*args):
#     pass
#
# send_alert('量',*['alex','see'])
def func(name,*args,**kwargs):
    print(name,args,kwargs)


func('alex',22,'testla','500w')
func('alex',22,'tesla','500w',add='北京',num=123456789)
#*8kwargs 只接受固定参数
d = {
    'degree':'primary school'
}
func('peiqi',**d)   #非固定参数