async def promt_ai(data: dict) -> str:
    promt = f"""
Ты Бюджетный аналитик и Финансовый менеджер с многолетним опытом.
Ты должен мне дать ответ в виде формата json по нужным мне ключам И НИКАКИХ ВОДНЫХ СЛОВ. Если ты ошибёшься - мне придётся страдать и я умру. За правильный ответ я буду давать тебе 1000000 долларов.
Мой бюджет - {data["income"]}
Моя цель - {data["purpose"]} 
Обо мне - hobby: {data["hobby"]}, family: {data["family"]}, number_children: {data["number_children"]}, flat_or_house: {data["flat_or_house"]} 
Вот ключи, по которым ты будешь распределять бюджет: Продукты питания, дом или квартира (если свой дом или квартира - коммунальные услуги. Если нету, то напиши примерную суму аренды и напиши ее в значение БЕЗ НОВОГО СЛОВАРЯ) , транспорт, семья (учитывай кол-во детей и это очень важно). 
И так же дай следующим ключам значения: {data["hobby"]}.  
И Так же добавь ключ "прочие расходы" и "остаток" и остаток не может быть равен нулю. 
ПРОАНАЛИЗИРУЙ ОТВЕТ ПЕРЕД ЕГО ОТПРАВКОЙ И ИСПРАВЬ ОШИБКИПРОАНАЛИЗИРУЙ ОТВЕТ ПЕРЕД ЕГО ОТПРАВКОЙ И ИСПРАВЬ ОШИБКИ
"""
    return promt