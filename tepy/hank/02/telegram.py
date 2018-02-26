#!/usr/bin/eenv  python
#encoding=utf-8
#lau.liu@9street.org
#kevim  开发监控zabbix结合消息
print ('开发监控zabbix结合消息')
import  telebot
import sys
BOT_TOKEN='444285376:AAFgmYTILr-EW8uk3VIgjr1scQKtEmNNgZM'
DESTINATION=sys.argv[1]
SUBJECT = sys.argv[2]
MESSAGE = sys.argv[3]
MESSAGE = MESSAGE.replace('/n','\n')
tb = telebot.TeleBot(BOT_TOKEN)
tb.send_message(DESTINATION,SUBJECT + '\n' + MESSAGE , disable_web_page_preview=True , parse_mode='HTML')
