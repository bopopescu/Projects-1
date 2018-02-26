name = input("name: ")
#age = input("Age: ")
age = int(input("Age: "))
job = input("Joh: ")
howten = input("howten: ")
#格式输出 标准规范格式

info = """
************info or %s ************   
name     :           %s
age      :           %d 
job      :           %s
howten   :           %s
***************and *****************
""" % (name,name,age,job,howten)
print(info)
#%s 是占位符
#%d 是整数
#%f 小数