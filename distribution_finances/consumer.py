from pika import BlockingConnection, ConnectionParameters
from pymongo import MongoClient
# import json


def callback(ch, method, properties, body):
    print(f"{body}")
    clien_db = MongoClient("localhost", 27017)
    db = clien_db["usersdb"]
    # body = json.loads(body)
    db.users.insert_one(body)
    data = db.users.find_one()
    return data

connection = BlockingConnection(ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='test_queue')

channel.basic_consume(
    queue='test_queue',
    on_message_callback=callback,
    auto_ack=True
)
print("Ожидание сообщений")
channel.start_consuming()