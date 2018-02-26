#!/usr/bin/eenv  python
#encoding=utf-8
#lau.liu@9street.org
#kevim  开发监控zabbix结合消息

import  requests
import  json
url = requests.get('https://api.telegram.org/bot444285376:AAFgmYTILr-EW8uk3VIgjr1scQKtEmNNgZM/getUpdates')
user_pwd = "user:****"
data = json.dumps()
r = requests.get(url,data,user_pwd)
status = r.status_code
print r.json
print status