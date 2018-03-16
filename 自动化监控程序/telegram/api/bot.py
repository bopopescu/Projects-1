#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
# lucy 2017-5-10
# coding=utf-8
import telebot, sys, argparse
import time
import signal
import  os,sys
sys.path.append("../core")
from ssh import Zabbix



def signal_handler(signal_num, frame):
    tb.send_message(master, 'I get a signal, I go die!, signal_num: %s' % signal_num)
    exit()


BOT_TOKEN = '556230219:AAHQ4xKOL7KNlxqfI0MRz0B9GaoP60wLmr4'
tb = telebot.TeleBot(BOT_TOKEN)
z = Zabbix()
user_limit = [ '-210815767']

master = '-210815767'
signal.signal(signal.SIGINT, signal_handler)  # ctrl-c kill
signal.signal(signal.SIGTERM, signal_handler)  # default kill
message_new_id = message_old_id = 0
while 1:
    print
    'Running...'
    mess_list = tb.get_updates(timeout=3)
    for mess_obj in mess_list:
        try:
            message_new_id = mess_obj.message.message_id
            if not message_old_id:
                message_old_id = mess_obj.message.message_id

            if message_old_id >= message_new_id:
                break
            print
            mess_obj
            message = mess_obj.message.text
            user_id = mess_obj.message.from_user.id
            message_old_id = message_new_id
            if message in ['/nginx', '/php']:
                if user_id not in user_limit:
                    tb.send_message(master, 'HeHe! No Way simida')
                    print
                    user_id, type(user_id)
                    continue
                tb.send_message(master, z.item_get(message))
            if message in ['/dns']:
                if user_id in user_limit:
                    tb.send_message(master, url.dns())
            if message in ['/help']:
                if user_id in user_limit:
                    tb.send_message(master, '嗨，主人，你可以执行的指令有:/nginx,/php,/dns,/help')


        except IndexError:
            print
            'IndexError'

        except AttributeError:
            print
            'AttributeError'

        except KeyboardInterrupt:
            tb.send_message('-210815767', 'I am going die!')

    time.sleep(1)

# def getHost(self):
#     data = json.dumps({
#         'jsonrpc': '2.0',
#         'method': 'host.get',
#         'params': self.para_dic['host.get'],
#         'auth': self.auth,
#         'id': 1,
#     })