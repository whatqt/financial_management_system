from rest_framework import serializers
from .service import ValidateType
from .decorators import check_type



class DistributionFinancesSerializer(serializers.Serializer):
    _id = serializers.CharField()
    income = serializers.IntegerField()
    purpose = serializers.CharField()
    hobby = serializers.ListField(child=serializers.CharField())
    family = serializers.CharField()
    number_children = serializers.IntegerField()
    flat_or_house = serializers.CharField()

    @check_type
    def validate_purpose(self, value):
        pass

    @check_type    
    def validate_family(self, value):
        pass
    
    @check_type
    def validate_flat_or_house(self, value):
        pass


# добавить из producer функцию send_data
# и сделать так, чтобы она показывала ошибки, если не правильно используют функцию
# добавить валидацию полей
#{"income": 50000, "purpose": "накопление", "hobby": ["спорт", "игры"], "family": "не женат", "flat_or_house": "квартира"} 
# {"income": 50000, "purpose": "накопление", "hobby": ["спорт", "игры"], "family": "женат",  "number_children": 2, "flat_or_house": "квартира"} 