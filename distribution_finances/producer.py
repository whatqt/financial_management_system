from pika import BlockingConnection, ConnectionParameters
from time import sleep
import json


def send_data(msg):
    connection = BlockingConnection(ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='database')
    
    channel.basic_publish(
        exchange='',
        routing_key='database',
        body=msg
    )
    print("Сообщение было отправлено в брокер для бд")
    connection.close()
    print("Отключение")