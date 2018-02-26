#!/usr/bin/eenv  python
#encoding=utf-8
#lau.liu@9street.org
#kevim  开发监控zabbix结合消息
import logging
import telebot
import os
# from telegram import InlineKeyboardButton, InlineKeyboardMarku
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

bot=telebot.TeleBot("405298089:AAGVrOj_Dilv97yxOqOScEL13L2B9bAiXcE")
# updater = Updater("405298089:AAGVrOj_Dilv97yxOqOScEL13L2B9bAiXcE")
SHELL = '/data'
user_list = [58081176,12321,241196016]


def get_user_id(message):
    if message.from_user.id in user_list:
        return 1
    else:
        return 0

def start(bot, update):
    keyboard = [[InlineKeyboardButton("NB线上git更新", callback_data='sh user.sh'),InlineKeyboardButton("SJ线上svn更新", callback_data='sh user.sh')],[InlineKeyboardButton("V6访问延迟排名地区", callback_data='python city.py')],[InlineKeyboardButton("V6-gate签名过期时间",callback_data='python timedd.py')],
                 [InlineKeyboardButton("V6-gate当天国内人数", callback_data='python mysql.py'),InlineKeyboardButton("V6-GATE历史失败次数", callback_data='python fail_gate.py')],
                 [InlineKeyboardButton("V6域名当天国内人数T10", callback_data='python url_web.py'),InlineKeyboardButton("V6在线人数", callback_data='python person_sum.py')],
                [InlineKeyboardButton("V6-gate状态码检查", callback_data='sh gate.sh')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    print(dir(InlineKeyboardButton))
    update.message.reply_text('请选择命令:', reply_markup=reply_markup)

def button(bot, update):
    query = update.callback_query
    bb = query.from_user
    if bb.id  in user_list:
       result = os.popen(query.data).read()
       bot.edit_message_text(text="%s" % result,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          parse_mode='HTML')
    else:
        bot.edit_message_text(text="对不起，U没有权限执行!",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
    f=query.from_user
    print(f.id)
    print(f.first_name)
    print(f.name)
#    print(f.username)
#    print(dir(f))


def help(bot, update):
    update.message.reply_text("可以从 /start 命令开始使用该机器人.")


def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))


# Create the Updater and pass it your bot's token.
#updater = Updater("405298089:AAGVrOj_Dilv97yxOqOScEL13L2B9bAiXcE")

# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CallbackQueryHandler(button))
# updater.dispatcher.add_handler(CommandHandler('help', help))
# updater.dispatcher.add_error_handler(error)

# Start the Bot
# updater.start_polling()
#bot.polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
# updater.idle()