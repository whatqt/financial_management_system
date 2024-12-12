import json
import asyncio
from sys import path
path.append('..')
from financial_management_system.settings import \
    ASYNC_CONNECTION_MONGODB, ASYNC_CONNECTION_RABBITMQ
from mistral_ai import MistralAI, SaveAnswer



async def callback(body):
    body = json.loads(body)
    db = ASYNC_CONNECTION_MONGODB["usersdb"]
    print(body)
    # async with await clien_db.start_session() as session:
    #     async with session.start_transaction():
    #         await db.users.insert_one(body, session=session)
    # сессии невозможно использовать, так как надо запустить сервер на реплике
    await db.users.replace_one(body, body,upsert=True)
    print("Данные были успешно занесены в Базу данных")
    mistral_ai = MistralAI(body)
    answer = await mistral_ai.get_answer()
    print(answer)
    save_answer = SaveAnswer(answer, body["_id"])
    await save_answer.save()
    
async def main():
    connection = await ASYNC_CONNECTION_RABBITMQ
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("database")
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                await callback(message.body)
                await message.ack(True)

if __name__ == "__main__":
    print("Брокер запущен")
    asyncio.run(main())