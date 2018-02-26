name = input("name:")
# age = input("Age:")
age = int(input("Age:"))  #强制转换成证书
job = input("Joh:")
hometown  = input("Hometown:")
info  = """
-------- info o %s --------
Name    :           %s
Age     :           %d
Job     :           %s
hometwo :           %s
----------and-------------
""" % (name,name,age,job,hometown)
print(info)
# %s是站位符，%连接符
# d  digit 是数字
# f float 小数点