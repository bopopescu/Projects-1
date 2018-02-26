# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

from ipip import IP
from ipip import IPX



def main():
<<<<<<< HEAD
    f = file('ip.txt', 'a+')
    for i1 in range(0,254):
       for i2 in range(0,254):
           for i3 in range(0,254):
               for i4 in range(0,254):
                   ip='%s.%s.%s.%s' %(i1,i2,i3,i4)
                   if i1 not in (0,10,172,192,127):

    f = file('ip.txt','a+')
    for i1 in range(0,254):
        for i2 in range(0,254):
            for i3 in range(0,254):
                for i4 in range(0,254):
                    ip='%s.%s.%s.%s' %(i1,i2,i3,i4)
                    if i1 not in (0,10,172,192,127):

                      # print(ip)
                        try:
                           #print(ip)
                            IP.load(os.path.abspath("mydata4vipday2.datx"))
                           # IP.load(os.path.abspath("monipdb.dat"))
                            print IP.find(ip)
                            IPX.load(os.path.abspath("mydata4vipday2.datx"))
                           # IP.load(os.path.abspath("monipdb.dat"))

                           ip1 = IPX.find(ip)
                           print ip,ip1
                           codelst = ['\n',ip,ip1,'\n']
                           f.writelines(codelst)




                            ip1 = IPX.find(ip)
                            #print ip,ip1
                            codelst = ['\n',ip,ip1,'\n']
                            f.writelines(codelst)

                        except Exception as e:
                              print(e)
                              continue
main()






=======
>>>>>>> origin/master
