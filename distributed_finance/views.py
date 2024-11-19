from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from distribution_finances.serializer import DistrFinancesSerializer
from pymongo import MongoClient
from .service import UserData, FinancesData



class DistributedFinance(APIView):
    def get(self, request: Request):
        user_data = UserData(request.user.username).get_data()
        serializer = DistrFinancesSerializer(data=user_data)
        if serializer.is_valid():
            finances_data = FinancesData(request.user.username).get_data()
            return Response(
                {"data": [serializer.data, finances_data]},
                status.HTTP_302_FOUND
            )
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
    # дописать документацию к каждой функции/классу