from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class DistrFinancesSerializer(serializers.Serializer):
    income = serializers.IntegerField()
    purpose = serializers.CharField()
    hobby = serializers.ListField(child=serializers.CharField())

# добавить из producer функцию send_data
# и сделать так, чтобы она показывала ошибки, если не правильно используют функцию
# добавить валидацию полей
#{"income": 50000, "purpose": "машина", "hobby": ["спорт", "игры"]}