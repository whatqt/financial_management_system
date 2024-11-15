from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import CreateUserSerializer
from django.contrib.auth.models import User


class CreateUser(APIView):
    def post(self, request: Request):
        print(request.data)
        serializer = CreateUserSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.data["username"],
                password=serializer.data["password"],
            )
            print(user)
            return Response({"status": "User created"}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# {"username": "test", "password": 1234}