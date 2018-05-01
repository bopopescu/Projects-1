#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
"""
import pika,time,threading
credentials = pika.PlainCredentials('admin', 'admin')
# 连接到RabbitMQ服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.192.112', 5672, '/', credentials))
channel = connection.channel()
# 指定一个队列，如果该队列不存在则创建
channel.queue_declare(queue='test_queue')
# 定义一个回调函数
def callback(ch, method, properties, body):
    print(body.decode('utf-8'))
    time.sleep(1)
    ch.
channel.basic_qos(prefetch_count=1 )
# 告诉RabbitMQ使用callback来接收信息
channel.basic_consume(callback, queue='test_queue', no_ack=False)
# print('waiting...')
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。
channel.start_consuming()
"""
import pika,time,threading
credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.192.112', 5672, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='test_queue')
# 定义一个回调函数
def test(ch, method, properties, body):
    print(body.decode('utf-8'))
    time.sleep(1)

def callback(ch,method,properties,boody):
    t = threading.Thread(target=test,args=(ch,method,properties,boody))
    t.start()
channel.basic_qos(prefetch_count=10000 )
# 告诉RabbitMQ使用callback来接收信息
channel.basic_consume(callback, queue='test_queue', no_ack=True)
# print('waiting...')
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。

channel.start_consuming()