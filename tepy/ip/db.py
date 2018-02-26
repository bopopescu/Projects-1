#enconding: utf-8
# -*- coding: utf-8 -*-
import urllib.request
import urllib.response
import urllib.parse
import pymysql.connections as sql
import redis,re
#抓取ip地址归属地
def curl_ip(ip):
   conn_req=urllib.request
   conn_pre=urllib.parse
   conn_res=urllib.response
   user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.15 Safari/537.36'
   headers = {'User-Agent' : user_agent,
               'Accept':'text/javascript, */*; q=0.01',
               'Accept-Language':'zh-CN,zh;q=0.8',
               }
   try:
       url='http://ip138.com/ips138.asp?ip=%s' %(ip)
       req=conn_req.Request(url,None,headers)
       fb=conn_req.urlopen(req)
       for page in fb.readlines():
           m = re.search('本站主数据',str(page,encoding = "gb2312"))
           if m:
               ad = re.findall('<li>本站主数据：(.*)</li><li>',str(page,encoding = "gb2312"))
               return(ad[0])
       fb.close()
   except Exception as e:
       print(e)
#抓取结果写入数据库
def sql_ip(data):
   conf={'user':'root',
   'password':'123456',
   'port':'3306',
   'db':'ip'
   }
   try:
       conn=sql.connect(**conf)
       cur=conn.cursor(buffered=True)
       if data:
           sql_query = ("insert into data(startip,endip,address) values(%s,%s,%s);")
           cur.execute(sql_query,data)
           conn.commit()
           cur.close()
           conn.close()
   except Exception as e:
       print(e)
#临时ip写入redis127.0.0.
def redis_ip(ip):
   redis_w = redis.StrictRedis(host='192.168.192.140', port=6379, db=0)
   redis_r = redis.StrictRedis(host='192.168.192.140', port=6379, db=0)
   ad=curl_ip(ip)
   ad1 = str(redis_r.get('ad_w'),encoding='utf-8')
   if not ad1:
      ad1 = 'no address'
   if ad and ad != ad1:
       try:
           sip=str(redis_r.get('ip_w'),encoding='utf-8')
           if not sip:
              sip='0.0.0.0'
           redis_w.set('ip_w',ip)
           redis_w.set('ad_w',ad)
           data=(sip,ip,ad)
           sql_ip(data)
           return(data)
       except Exception as e:
               print(e)
#历遍获取ip
def main():
   for i1 in range(0,254):
       for i2 in range(0,254):
           for i3 in range(0,254):
               for i4 in range(0,254):
                   ip='%s.%s.%s.%s' %(i1,i2,i3,i4)
                   if i1 not in (0,10,172,192,127):
                       print(ip)
                       try:
                           print(redis_ip(ip))
                       except Exception as e:
                              print(e)
                              continue
main()