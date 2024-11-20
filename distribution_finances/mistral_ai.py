import json
import os
from mistralai import Mistral
from financial_management_system.settings import \
    ASYNC_CONNECTION_MONGODB, API_KEY_AI



class MistralAI:
    def __init__(self, content):
        self.content = content
        self.api_key_ai = API_KEY_AI
        self.__model_ai = "mistral-large-latest"

    async def __promt_ai(self, content):
        promt = f"""
Ты Бюджетный аналитик и Финансовый менеджер с многолетним опытом.
Ты должен мне дать ответ в виде формата json по нужным мне ключам И НИКАКИХ ВОДНЫХ СЛОВ. Если ты ошибёшься - мне придётся страдать и я умру. За правильный ответ я буду давать тебе 1000000 долларов.
Мой бюджет - {content["income"]}
Моя цель - {content["purpose"]} 
Обо мне - hobby: {content["hobby"]}, family: {content["family"]}, number_children: {content["number_children"]}, flat_or_house: {content["flat_or_house"]} 
Вот ключи, по которым ты будешь распределять бюджет: Продукты питания, дом или квартира (если свой дом или квартира - коммунальные услуги. Если нету, то напиши примерную суму аренды и напиши ее в значение БЕЗ НОВОГО СЛОВАРЯ) , транспорт, семья (учитывай кол-во детей и это очень важно). 
И так же дай следующим ключам значения: {content["hobby"]}.  
И Так же добавь ключ "прочие расходы" и "остаток" и остаток не может быть равен нулю. 
ПРОАНАЛИЗИРУЙ ОТВЕТ ПЕРЕД ЕГО ОТПРАВКОЙ И ИСПРАВЬ ОШИБКИПРОАНАЛИЗИРУЙ ОТВЕТ ПЕРЕД ЕГО ОТПРАВКОЙ И ИСПРАВЬ ОШИБКИ
"""
        return promt
    
    async def get_answer(self):
        client_ai = Mistral(api_key=self.api_key_ai)
        promt = await self.__promt_ai(self.content)
        response = await client_ai.chat.stream_async(
            model=self.__model_ai,
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
        answer = ''
        async for chunk in response:
            if chunk.data.choices[0].delta.content is not None:
                answer += chunk.data.choices[0].delta.content
        return answer

class SaveAnswer:
    def __init__(self, answer, id):
        self.answer = answer
        self.id = id

    async def __change_answer(self):
        self.answer = json.loads(self.answer) # преобразуем в dict 
        self.answer["_id"] = self.id

    async def save(self):
        # мб разделить это на два класса: сохранение данных и их редактирование
        # ибо бд даёт дополнительную зависимость (проверить информацию об этом)
        clien_db = ASYNC_CONNECTION_MONGODB
        usersdb = clien_db["usersdb"]
        await self.__change_answer()
        old_data = await usersdb.finances.find_one({"_id": self.id})
        await usersdb.finances.replace_one(old_data, self.answer, upsert=True)
        print("Данные о бюджете были добавлены")
