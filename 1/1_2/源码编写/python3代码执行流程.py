# _*_ coding:utf-8 _*_

# s = "路飞学成" #unicode
# print(s)

s1 = "路飞学成"
print(s1)
s5 = s1.decode("utf-8")
print(s5)
print(type(s5))

s6 = s5.encode('gbk')
print(s6)
print(type(s6))

s7 = s5.encode("utf-8")
print(s7)
print(type(s7))
#
# print(type(s1))print(type(s2))
# s2 = s1.encode("gbk")
# print(s2)
# print(type(s2))
#
# s3 = s1.encode('utf-8')
# print(s3)
# print(type(s3))