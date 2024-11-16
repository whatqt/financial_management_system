from django.contrib.auth.models import User



class UserService:
    def __init__(self, validated_data: dict):
        self.validated_data = validated_data

    def create_user(self) -> User:
        user = User.objects.create_user(
            username=self.validated_data["username"],
            password=self.validated_data["password"]
        )
        return user