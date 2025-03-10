from rest_framework import serializers
from orders.models import Order


class OrderAllFieldSerializer(serializers.ModelSerializer):
    """Сериализатор с полным набором полей заказа."""

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'petowner', 'petsitter', 'status', 'detail', 'approved_by_sitter']

