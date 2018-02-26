#!/usr/bin/eenv  python
#encoding=utf-8
#lau.liu@9street.org
import datetime
d1 = datetime.datetime(2017,1,15)
d2 = datetime.datetime.now()
print (u'相差：%s天'%(d1-d2).days)