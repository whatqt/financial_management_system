from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import DistrFinancesSerializer
from django.contrib.auth.models import User
from .producer import send_data
import json


class DistributionFinances(APIView):
    def post(self, requst: Request):
        print(requst.data)
        serializer = DistrFinancesSerializer(data=requst.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            print(serializer.validated_data)
            send_data(json.dumps(serializer.validated_data))
            return Response({"data": serializer.data})
        return Response(serializer.errors)