import aio_pika
import json
import asyncio
from sys import path
path.append('..')
from financial_management_system.settings import CONNECTION_MONGODB, ASYNC_CONNECTION_RABBITMQ
from mistral_ai import MistralAI, SaveAnswer



async def callback(body):
    body = json.loads(body)
    db = CONNECTION_MONGODB["usersdb"]
    print(body)
    # async with await clien_db.start_session() as session:
    #     async with session.start_transaction():
    #         await db.users.insert_one(body, session=session)
    # сессии невозможно использовать, так как надо запустить сервер на реплике. Решение есть, но стоит ли оно того?
    await db.users.replace_one(body, body,upsert=True)
    print("Данные были успешно занесены в Базу данных")
    mistral_ai = MistralAI(body)
    answer = await mistral_ai.get_answer()
    print(answer)
    save_answer = SaveAnswer(answer, body["_id"])
    await save_answer.save()
    # await get_info_ai(body)
    
async def main():
    connection = await ASYNC_CONNECTION_RABBITMQ
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