from rest_framework import serializers
from orders.models import Order


class OrderAllFieldSerializer(serializers.ModelSerializer):
    """Сериализатор с полным набором полей заказа."""

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'petowner', 'petsitter', 'status', 'detail', 'approved_by_sitter']


class OrderCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания нового заказа."""

    detail = serializers.CharField(max_length=500)
    
    class Meta:
        model = Order
        fields = ['created_at', 'petowner', 'detail']

    def create(self, validated_data):
        order = Order(**validated_data)
        order.save()
        return order
    
class OrderChangeSerializer(serializers.ModelSerializer):
    """Сериализатор для редактирования деталей заказа."""

    detail = serializers.CharField(max_length=500)

    class Meta:
        model = Order
        fields = ['id', 'detail']