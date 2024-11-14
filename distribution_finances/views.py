from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from django.http import HttpRequest
from .serializer import DistrFinancesSerializer
from .producer import send_data
import json



class DistributionFinances(APIView):
    def post(self, request: Request):
        print("РАБОТАЕТ")
        print(request.data)

        request.data["_id"] = request.user.username
        print(request.data)
        # return Response("test", status.HTTP_201_CREATED)
        serializer = DistrFinancesSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            print(serializer.validated_data)
            send_data(json.dumps(serializer.validated_data))
            return Response({"data": serializer.data}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
