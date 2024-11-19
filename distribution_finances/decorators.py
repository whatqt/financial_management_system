from rest_framework import serializers
from .service import ValidateType


def check_type(func):
    def wrapper(self, *args, **kwargs):
        value = args[0]
        name = func.__name__
        validate_type = ValidateType()
        methods = validate_type.methods()
        values_validate = methods[name.split("_", 1)[1]]()
        print(values_validate)
        if value not in values_validate:
            raise serializers.ValidationError(
                f"value {value} is not in {values_validate}"
            )
        
        # func(self, value)
        return value
    
    return wrapper