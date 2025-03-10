from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.models import Order

from orders.serializers.orders_serializers import (
    OrderAllFieldSerializer
)


class OrderDetailView(APIView):
    """
    Вью для просмотра деталей заказа с полями...
    .
    """
    
    # permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            serializer = OrderAllFieldSerializer(instance=order)
            serialized_data = serializer.data
        except Exception as e:
            return Response({'error':'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serialized_data, status=status.HTTP_200_OK)
