import aio_pika
import json
import asyncio
from pymongo import AsyncMongoClient
from mistral_ai import get_info_ai


async def callback(body):
    body = json.loads(body)
    clien_db = AsyncMongoClient("localhost", 27017)
    db = clien_db["usersdb"]
    print(body)
    # async with await clien_db.start_session() as session:
    #     async with session.start_transaction():
    #         await db.users.insert_one(body, session=session)
    # сессии невозможно использовать, так как надо запустить сервер на реплике. Решение есть, но стоит ли оно того?
    data = await db.users.find_one({"_id": body["_id"]})
    if data:
        print("Данные были не были занесены, так как такая запись уже есть")
        return
    await db.users.insert_one(body)
    print("Данные были успешно занесены в Базу данных")
    await get_info_ai(body)
    
async def main():
    connection = await aio_pika.connect_robust()
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("database", auto_delete=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                await callback(message.body)
                queue = await channel.declare_queue(exclusive=True)

if __name__ == "__main__":
    print("Брокер запущен")
    asyncio.run(main())