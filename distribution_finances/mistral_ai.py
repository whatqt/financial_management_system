import asyncio
import os
from mistralai import Mistral
from pymongo import AsyncMongoClient



async def main():
    api_key = os.getenv("MISTRAL_API_KEY")
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)


    response = await client.chat.stream_async(
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