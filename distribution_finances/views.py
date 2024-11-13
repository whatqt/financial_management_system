from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import DistrFinancesSerializer
from .producer import send_data
import json


class DistributionFinances(APIView):
    def post(self, requst: Request):
        print(requst.data)
        requst.data["_id"] = requst.user.username
        serializer = DistrFinancesSerializer(data=requst.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            print(serializer.validated_data)
            send_data(json.dumps(serializer.validated_data))
            return Response({"data": serializer.data}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)