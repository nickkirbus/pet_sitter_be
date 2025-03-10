from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from orders.models import Order, PetOwner, PetSitter
from users.models import User

class OrderDetailViewTest(APITestCase):
    def setUp(self):
        self.petowner = PetOwner.objects.create(
            id=1,
        )
        self.petsitter = PetSitter.objects.create(
            id=1,
        )
        self.user = User.objects.create(
            id=1
        )
        self.order = Order.objects.create(
            created_at = '2025.03.09 12:10:15',
            petowner = self.petowner,
            petsitter = self.petsitter,
            status = 'InPr',
            detail = 'woof woof no meaow',
            approved_by_sitter = self.user
        )
        self.url = reverse('order_details', args=[self.order.id])

    def test_get_order_detail_success(self):
        """
        Тест успешного получения деталей заказа.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'InPr')
        self.assertEqual(response.data['detail'], 'woof woof no meaow')
        self.assertEqual(response.data['petsitter'], 1)

    def test_get_order_detail_not_found(self):
        """
        Тест случая, когда заказ не существует.
        """
        non_existent_order_id = 9999
        url = reverse('order_details', args=[non_existent_order_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Order not found")