from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.models import Order
from orders.permissions import IsPetOwner, IsPetSitter

from orders.serializers.orders_serializers import (
    OrderAllFieldSerializer,
    OrderCreateSerializer,
    OrderChangeSerializer
)


class OrderDetailClientView(APIView):
    """Вью для просмотра деталей заказа клиентом."""
    
    permission_classes = [IsAuthenticated, IsPetOwner]

    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            serializer = OrderAllFieldSerializer(instance=order)
            serialized_data = serializer.data
        except Exception as e:
            return Response({'error':'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serialized_data, status=status.HTTP_200_OK)
    

class OrderDetailPetsitterView(APIView):
    """Вью для просмотра деталей заказа исполнителем."""
    
    permission_classes = [IsAuthenticated, IsPetSitter]

    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            serializer = OrderAllFieldSerializer(instance=order)
            serialized_data = serializer.data
        except Exception as e:
            return Response({'error':'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serialized_data, status=status.HTTP_200_OK)


class OrderCreateView(APIView):
    """Вью для создания заказа заказчиком с полями 'created_at', 'petowner' и 'detail'."""

    permission_classes = [IsAuthenticated, IsPetOwner]

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            raise serializers.ValidationError("You must authenticate before creating orders.")
        request.data['petowner'] = user
        
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "Результат": "Заказ успешно создан",
                "id": serializer.validated_data.get('id'),
                "created": serializer.validated_data.get('created_at'),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderChangeView(APIView):
    """Вью для изменения заказа заказчиком с полями id и detail."""

    permission_classes = [IsAuthenticated, IsPetOwner]

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            raise serializers.ValidationError("You must authenticate before creating orders.")

        serializer = OrderChangeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "Результат": "Заказ успешно изменен",
                "id": serializer.validated_data.get('id'),
                "detail": serializer.validated_data.get('detail'),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)