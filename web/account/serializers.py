from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения данных пользователя.
    """
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'status', 'details']


class UpdateUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления имени и/или email
    """
    class Meta:
        model = User
        fields = ['name', 'details']
