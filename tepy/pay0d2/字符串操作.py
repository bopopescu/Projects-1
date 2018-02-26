#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org
name = "my  \t name is {alex} and is am {yes}"
print(name.capitalize())              #首字母大写
print(name.count("a"))                #统计字符串里的字母统计
print(name.center(50,"-"))            #一共打印50个字符，不够用-不全 前后对应
print(name.endswith("ex"))            #判断字符串以什么结尾
print(name.expandtabs(tabsize=30))    #\t tab键打印30个
print(name[name.find("i"):])          #find查找 可以对字符串进行切片
print(name.format(alex='kevim',yes=23)) #字符串格式化输出
print(name.format_map({'alex':'kevim','yes':'30'})) #字典是格式化输出
print(name.isalnum())#阿拉伯的数字 包含阿拉伯数字的，不能包含特殊字符 可以
print('abc123'.isalnum())
print(name.isalpha()) #纯英文字符 包含大小写，不能包含特殊字符 数字
print('abx'.isalpha())
print('1'.isdecimal()) #判断是不是十进制整数
print('1A'.isdigit()) #判断是不是整数
print('a'.isidentifier()) #判断是不是一个合法标识符 'a!'.'' True false
print('a'.islower()) #判断是不是小写
print('a 1A'.isnumeric()) #判断是不是一个数字
print('22244'.isnumeric())
print(' '.isspace()) #判断是不是一个空格
print('My name is '.istitle()) #首字母大写
print('My name Is '.isprintable()) # 当你是一个tty file drive file
print('My name Is'.isupper())#判断是不是全部大写
print('='.join(['1','2','3'])) #间隔符 数字
print(name.ljust(50,'*')) #不够50个字符，用星号补全 ，后面补全
print(name.rjust(50,'#')) #不够50个字符，用星号补全 ，前面补全
print('KEVIM'.lower())  #全部大写变小写
print('kevim'.upper())  #全部小写变大写
print('\nkevim'.lstrip()) #空格回车，换行 去掉默认左边的空格回车 print('\nkevim')
print("--------------") #验证
print('\nkevi\n'.rstrip()) #空格回车，换行 去掉默认右 边的空格回车 print('kevim\n')
print("--------------") #验证
print('\nkevim\n'.strip()) #空格回车，换行 去掉默认左右边的空格回车 print('\nkevim\n')
print("--------------") #验证
p = str.maketrans("abcdef",'123456')
print("alex li".translate(p)) #用于随机密码 设置
print('alex a'.replace('a','A',1)) #替换对应的字符 对应参数，替换设置
print('alex lie lie '.rfind('e')) #查找最后面的值，返回
print('alex lil'.split()) #把一个字符串按照空格分成一个列表
print('1+2\n+3'.splitlines())#安装换行来分
print('alex Li'.swapcase()) # 全部大写
print('alex Li'.title())  #每个字符开头变成大写
print('alex li'.zfill(50)) #不够用0补全
