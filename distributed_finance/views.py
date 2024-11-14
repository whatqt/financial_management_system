from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from distribution_finances.serializer import DistrFinancesSerializer
import json
from pymongo import MongoClient
from django.contrib.auth.models import User

class DistributedFinance(APIView):
    def get(self, request: Request):
        client = MongoClient("localhost", 27017)
        usersdb = client["usersdb"]
        user = usersdb.users.find_one({"_id": request.user.username})
        serializer = DistrFinancesSerializer(data=user)
        print(serializer.is_valid())
        if serializer.is_valid():
            finances = usersdb.finances.find_one(
                {"_id": request.user.username}
                )
            user = User.objects.get(username="test")
            print(user.username)
            return Response(
                {"data": [serializer.data, finances]},
                status.HTTP_302_FOUND
            )
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
    # фиксить баги и убирать костыли
    # а так же начать писать к этому unit test и писать хоть какую-то документацию