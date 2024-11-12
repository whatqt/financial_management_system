from rest_framework import serializers
from django.contrib.auth.models import User



class DistrFinancesSerializer(serializers.Serializer):
    _id = serializers.CharField()
    income = serializers.IntegerField()
    purpose = serializers.CharField()
    hobby = serializers.ListField(child=serializers.CharField())
    family = serializers.CharField()
    number_children = serializers.IntegerField()
    flat_or_house = serializers.ListField(child=serializers.CharField())

    def validate_puprose(self, value):
        values_validate = ["накопление", "распределение"]
        if value in values_validate:
            return value
        else: raise serializers.ValidationError(f"value {value} is not in {values_validate}")

    def validate_family(self, value):
        values_validate = ["женат", "не женат"]
        if value not in values_validate:
            raise serializers.ValidationError(f"value {value} is not in {values_validate}")            
        return value 

    def validate_flat_or_house(self, values):
        values_validate = ["квартира", "дом", "снимаю", "ипотека"]
        if values:
            for value in values:
                if value not in values_validate:
                    raise serializers.ValidationError(f"value {value} is not in {values_validate}")
            return values
        else: raise serializers.ValidationError(f"value is None")


# добавить из producer функцию send_data
# и сделать так, чтобы она показывала ошибки, если не правильно используют функцию
# добавить валидацию полей
#{"income": 50000, "purpose": "накопление", "hobby": ["спорт", "игры"], "family": "не женат", "flat_or_house": ["квартира"]} 
# {"income": 50000, "purpose": "накопление", "hobby": ["спорт", "игры"], "family": "не женат",  "number_children": 2, "flat_or_house": ["квартира"]} 