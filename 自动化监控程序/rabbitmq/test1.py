#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
# import  pika
# credentials  = pika.PlainCredentials('admin','admin')
# connection =pika.BlockingConnection(pika.ConnectionParameters(host='192.168.192.112'))
# channel = connection.channel()
# channel.queue_declare(queue='test_01')
# for i  in range(100):
#     channel.basic_publish(exchange='',routing_key='test_01',body='hellow word'+str(i))
#     print('sent ....',i)
# connection.close()
import pika
credentials = pika.PlainCredentials('admin','admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.192.112',5672,'/',credentials))
channel = connection.channel()

#声明queue
channel.queue_declare(queue='test_queue')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
for i in range(100000):

    channel.basic_publish(exchange='', routing_key='test_queue', body='Hello World!' + str(i))


    # print(" [x] Sent 'Hello World!'")
connection.close()