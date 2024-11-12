import asyncio
import os

from mistralai import Mistral
from pymongo import AsyncMongoClient
from pprint import pprint

async def main():
    api_key = os.getenv("MISTRAL_API_KEY")
    model = "mistral-large-latest"
    client_ai = Mistral(api_key=api_key)
    clien_db = AsyncMongoClient("localhost", 27017)
    clien_db.aconnect()
    user = {
        "username": "testttttt", 
        "text": "texttttt", 
        "numbers": 1234566666
    }  
    db = clien_db["usersdb"]
    # users = db.users
    await db.users.insert_one(user)
    data = await db.users.find_one()
    print(data)
    async for user in db.users.find():
        pprint(user)


    response = await client_ai.chat.stream_async(
        model=model,
        messages=[
             {
                  "role": "user",
                  "content": "Рассчитай мне мой бюджет в размере 50000р для накопление одной вещи, которая будет стоить 150000р. Вот моё краткое описание: занимаюсь спортом, езжу на общ. транспорте, у меня своя квартира, я не женат.",
              },
        ],
    )
    async for chunk in response:
        if chunk.data.choices[0].delta.content is not None:
            print(chunk.data.choices[0].delta.content, end="")