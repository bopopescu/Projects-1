#!/usr/bin/evn python35
# kevim 
# lau.liu@9street.org
'''
name = ['sss',2,'d']
#len 长度 统计任何长度
print("name",len(name))
'''
"""
r = (1,2,3,4,5,6,7,8,9,0) #只读列表，元组 不可以再次赋值修改，
r[1] = 3
"""
"""
#字符串常用功能 1：移除空白； 2：分割；3：长度； 4：索引； 5：切片
"""
'''
username = input("user")
if username.strip() == 'kevim':  #strip 脱掉空格 tab键 或者指定字符
    print("wokecaom")
'''
"""
#names = "alex ,jack,rain"
#name2 = names.split(",") #字符串分割，只能指定一种字符分割 、分割方法 、成一个列表
#print("|".join(name2))  #join 是合起来
#name = "kevim  Li"
#print('' in name)  #判断有没有空格
#***** print(name.capitalize())
"""
 '''
msg = "Hello,{name},it s been a long {age} since time sopke...."
msg3 = "hahah{0},ddddd{1}"

# print(msg3.format('kevim',33)) #替换{}里面的数据
msg2 = msg.format(name="MingHu", age="2222")
print(msg2)
# name.format()  #字符格式化
name = "kevim li"
#print(name[2:4])
print(name.center(40,'-')) #字符串分割，不够40个，自动使用-填充
print(name.find('1'))  #返回-1，代表没有找到
 '''
""""
age = input("your age:")
if age.isdigit():
    age = int(age)
else:
    print("invaild data type")
"""
"""
name = 'a3K'
print(name.isalnum()) #是否有一个字符串或者整数
print(name.endswith('dfsd'))
print(name.startswith('dfsd'))
print(name.upper().lower())
"""
