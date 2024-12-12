
**О проекте**: API для клиентской части, которая распределяет бюджет. Бюджет распределяет Нейросеть от mistral.ai https://chat.mistral.ai/. Самую простую модель можно использовать бесплатно.

**Стэк используемых технологий:**
- Fraemwork: django rest framework
- Database: MongoDB, PostgreSQL
- Broker: RabbitMQ
- Libraries for DB: pymongo, motor, psycopg2
- Libraries for Broke: aio-pika, pika
- Library for tests: UnitTest
- Library for mistral.ai: mistralai

**Запуск приложения.**
1. Создать виртуальную среду и клонировать репозиторий.
2. Установить зависимости из requirements.txt
3. Добавить переменные среды: SECRET_KEY для Django, PASSWORD базы данных в settings.py, api_key для mistral_ai.py
4. Поднять: MongoDB по порту 27017,  RabbitMQ по порту 15672 и PostgreSQL по порту 5432
5.  Запустить проект при помощи manage.py.
