from promt import promt_ai
import asyncio
import json
import os
from mistralai import Mistral
from pymongo import AsyncMongoClient


async def get_info_ai(content):
    api_key = os.getenv("MISTRAL_API_KEY")
    model_ai = "mistral-large-latest"
    client_ai = Mistral(api_key=api_key)
    promt = await promt_ai(content)
    response = await client_ai.chat.stream_async(
        model=model_ai,
        messages=[
            {
                "role": "user",
                "content": promt,
            },
        ],
        response_format = {
          "type": "json_object",
      }
    )
    data = ''
    async for chunk in response:
        if chunk.data.choices[0].delta.content is not None:
            data += chunk.data.choices[0].delta.content

    data = json.loads(data)
    data["_id"] = content["_id"]
    clien_db = AsyncMongoClient("localhost", 27017)
    usersdb = clien_db["usersdb"]
    print(data)
    old_data = await usersdb.finances.find_one({"_id": content["_id"]})
    await usersdb.finances.replace_one(old_data, data, upsert=True)
    print("Данные о бюджете были добавлены")
    # пересмотреть решение про replace_one, так как нужно разделять ответственности

    

# asyncio.run(get_info_ai({"income": 50000, "purpose": "накопление", "hobby": ["спорт", "игры"], "family": "женат",  "number_children": 2, "flat_or_house": ["квартира"]} ))