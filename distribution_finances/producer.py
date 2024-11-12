from pika import BlockingConnection, ConnectionParameters
from time import sleep
import json


def send_data(msg):
    connection = BlockingConnection(ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='t')
    
    channel.basic_publish(
        exchange='',
        routing_key='t',
        body=msg
    )
    print("Сообщение было отправлено")
    connection.close()
