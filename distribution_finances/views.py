from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from django.http import HttpRequest
from .serializer import DistrFinancesSerializer
from .producer import SendData
import json



class DistributionFinances(APIView):
    def post(self, request: Request):
        request.data["_id"] = request.user.username
        serializer = DistrFinancesSerializer(data=request.data)
        if serializer.is_valid():
            data = SendData(serializer.validated_data)
            data.send_data()
            return Response({"data": serializer.data}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
