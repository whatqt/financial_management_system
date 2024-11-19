import json
from financial_management_system.settings import CONNECTION_RABBITMQ



class SerializationMsg:
    def __init__(self, msg: dict):
        self.msg = msg
    
    def serialization_msg(self):
        msg = json.dumps(self.msg)
        return msg

class SendData:
    def __init__(self, msg: dict):
        self.msg = msg
        self.connection = CONNECTION_RABBITMQ
    
    def send_data(self):
        channel = self.connection.channel()
        channel.basic_publish(
            exchange='',
            routing_key='database',
            body=self.msg
        )

        print("Сообщение было отправлено в брокер для бд")

