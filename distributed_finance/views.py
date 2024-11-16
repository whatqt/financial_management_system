from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from distribution_finances.serializer import DistrFinancesSerializer
from pymongo import MongoClient



class DistributedFinance(APIView):
    def get(self, request: Request):
        client = MongoClient("localhost", 27017)
        usersdb = client["usersdb"]
        user = usersdb.users.find_one({"_id": request.user.username})
        serializer = DistrFinancesSerializer(data=user)
        if serializer.is_valid():
            finances = usersdb.finances.find_one(
                {"_id": request.user.username}
            )
            
            return Response(
                {"data": [serializer.data, finances]},
                status.HTTP_302_FOUND
            )
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
    # дописать документацию к каждой функции/классу