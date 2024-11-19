from pika import BlockingConnection, ConnectionParameters
from pymongo import AsyncMongoClient, MongoClient
from aio_pika import connect as aio_connect




class ConnectionRebbitMq:
    def connect(self):
        try:
            connection = BlockingConnection(ConnectionParameters('localhost'))
            return connection
        except Exception as e:
            raise e
        
class AsyncConnectionRebbitMq:
    async def connect(self):
        try:
            connection = await aio_connect()
            return connection
        except Exception as e:
            raise e

class AsyncConnectionMongoDB:
    def connect(self):
        try:
            connection = AsyncMongoClient("localhost", 27017)
            return connection
        except Exception as e:
            raise e

class ConnectionMongoDB:
    def connect(self):
        try:
            connection = MongoClient("localhost", 27017)
            return connection
        except Exception as e:
            raise e
    
# сделать декоратор для обработки ошибки, чтоб не повторяться

