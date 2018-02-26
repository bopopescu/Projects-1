#!/usr/bin/env  python
#encoding=utf-8
#lau.liu@9street.org
# import  module_LD   #导入单个模块方法

# from module_LD import *   #代表导入所有的模块功能 不建议使用* 导入模块
"""
from module_LD import logger as  loogger #别名定义模块
# module_LD = all_code  module_LD .name 调用模块
from  module_LD import  name   #把个模块中的name的变量放在当前的位置
print(name)
"""

# print(module_LD.name)
# module_LD.say_hello)(

# module_LD.logger()

"""
def say_hello():
    print("hello ld")

def logger():  #;logger -----> 'pass'
    pass

def running():
    pass

"""
#
# def logger():  # logger --- >'print
#     print('in the main')
#
# logger()
# loogger()



import sys
import os
print(sys.path)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
si = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(si)
from  module_LD import  logger
# import  module_LD.logger()
logger()