#!/usr/bin/env python3
# kevim 
# lau.liu@9street.org
#encoding=utf-8
import  pymysql
import  sys
#print(sys.getdefaultencoding())
db = pymysql.connect(host='192.168.192.140',port=3306,user='root',passwd='123456',db="jiankong",charset='utf8')
coun =db.cursor()
sql = "select name_dns,https_date from domain01"

coun.execute(sql)
row1 = coun.fetchall()
print(row1)
def dns_list():

   # db = pymysql.connect(host='192.168.192.140', port=3306, user='root', passwd='123456', db="jiankong", charset='utf8')
   # coun = db.cursor()
    #sql = "select name_dns,https_date from domain01"

    coun.execute(sql)
    row1 = coun.fetchall()
    print(row1)
    #while True:
    #    for item in row1:
     #       dns1 = item[0]
      #      print(dns1)

    coun.close()
    db.close()
  #  user_choice = input("选择要买吗>>>:")
 #   if user_choice.isdigit():
 #       user_choice = int(user_choice)
#        if user_choice < len(product_list) and user_choice >= 0:
#            p_itme = product_list[user_choice]
#            if p_itme[1] <= salary:  # 代表买的起
#                shopping_list.append(p_itme)
#                salary -= p_itme[1]
  #              print("added %s int shopping ,cart current balance is \033[31;1m%s\033[0m " % (p_itme, salary))
 #           else:
 #               print("\033[41;1m 你的余额只剩[%s]啦，还买个毛线\033[0m" % (salary))
 #       else:
 #           print("product code [%s] is not exitst" % user_choice  #
     #       elif user_choice == 'q':
 #           print('exit.....')
     #       print("-------------------shopping_list--------------------")
     #       for p in shopping_list:
     #           print(p)
   #         print("Your current balance:", salary)
   #         exit()
   #         else:
    #        print('hvae bought below')

coun.close()
db.close()