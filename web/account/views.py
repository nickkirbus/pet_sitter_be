from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from web.account.serializers import UserSerializer, UpdateUserSerializer


class UserDetailsView(APIView):
    """
    Ендпоинт для получения данных пользователя
    """
    def get(self, request: Request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UpdateUserDetailsView(APIView):
    """
    Ендпоинт для обновления данных пользователя (имя и/или email)
    """
    def path(self, request: Request):
        serializer = UpdateUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        serializer = UpdateUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.error_messages)