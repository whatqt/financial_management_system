from django.shortcuts import render
from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import CreateUserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist


class CreateUser(APIView):
    def post(self, request: Request):
        print(request.data)
        serializer = CreateUserSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.data["username"],
                password=serializer.data["password"],
            )
            return Response({"status": "User created"}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# {"username": "test", "password": 1234}