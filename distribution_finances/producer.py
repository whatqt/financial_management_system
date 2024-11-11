from pika import BlockingConnection, ConnectionParameters
from time import sleep
import json


def send_data(msg):
    connection = BlockingConnection(ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='test_queue')
    
    channel.basic_publish(
        exchange='',
        routing_key='test_queue',
        body=msg
    )
    print("Сообщение было отправлено")
    connection.close()

# while True:
#     send_data(json.dumps({"income": 50000, "purpose": "машина", "hobby": ["спорт", "игры"]}))
#     sleep(10)