#!/usr/bin/evn python35
# kevim 
# lau.liu@9street.org
import os
#cmd_res = os.system("dir")  #调用系统命名 执行命令 ，不保存结果
cmd_res = os.popen("dir").read() #read 方法取回执行结果
print("---->",cmd_res)
