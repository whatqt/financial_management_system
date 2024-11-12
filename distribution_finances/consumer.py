import aio_pika
import json
import asyncio
from motor import motor_asyncio


async def callback(body):
    new_body = json.loads(body)
    if new_body["number_children"] == 0:
        del new_body["number_children"]
    
    clien_db = motor_asyncio.AsyncIOMotorClient("localhost", 27017)
    db = clien_db["usersdb"]
    print(new_body)
    # async with await clien_db.start_session() as session:
    #     async with session.start_transaction():
    #         await db.users.insert_one(new_body, session=session)
    # сессии невозможно использовать, так как надо запустить сервер на реплике. Решение есть, но стоит ли оно того?
    data = db.users.find_one({"_id": new_body["_id"]})
    if data:
        print("Данные были не были занесены, так как такая запись уже есть")
    await db.users.insert_one(new_body)
    print("Данные были успешно занесены в Базу данных")
    
# убрать это из консюмерс, поскольку он должен (наверное) 
# только принимать и отдавать данные, а не совершать над ними манипуляции

async def main():
    connection = await aio_pika.connect_robust()
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("t")
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                await callback(message.body)

if __name__ == "__main__":
    print("Брокер запущен")
    asyncio.run(main())