# #!/usr/bin/python
# #_*_ coding: utf-8 _*_
# s1 = "路 飞"
# print(s1)
# s2 = s1.encode('utf-8')
# print(s2)
# s3 = s2.decode('utf-8')
# print(s3)
# s4 = s3.encode('utf-8')
# s5 = s1.encode('gbk')
# print(s5)
import  os
list = os.popen("lastlog").readlines()
f = open('test.log','a')
f.write(".join"(list))
