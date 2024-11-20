from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import DistributionFinancesSerializer
from .producer import SendData, SerializationMsg


class DistributionFinances(APIView):
    def post(self, request: Request):
        request.data["_id"] = request.user.username
        serializer = DistributionFinancesSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serialized_msg = SerializationMsg(
                serializer.validated_data
            )
            msg = serialized_msg.serialization_msg()
            data = SendData(msg)
            data.send_data()
            return Response({"data": serializer.data}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
