from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient


class RegisterUserTests(TestCase):
    def setUp(self):
        # Настраиваем клиента API
        self.client = APIClient()
        self.register_url = reverse('register')  # Имя маршрута совпадает с urls.py

    def test_register_user_success(self):
        """Тест успешной регистрации пользователя"""
        data = {
            'name': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword123',
            'status': 'petsitter'  # Указываем статус
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Ожидаем статус 201
        self.assertIn('name', response.data)  # Проверяем, что ответ содержит 'name'
        self.assertIn('email', response.data)  # Проверяем, что ответ содержит 'email'
        self.assertIn('status', response.data)  # Проверяем, что ответ содержит 'status'
        self.assertEqual(response.data['status'], 'petsitter')  # Проверяем значение статуса

    def test_register_user_missing_field(self):
        """Тест регистрации с отсутствием обязательного поля"""
        data = {
            'name': 'testuser',
            'password': 'securepassword123',  # Отсутствует email
            'status': 'client'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Ожидаем статус 400
        self.assertIn('email', response.data)  # Проверяем, что ошибка указана для 'email'

    def test_register_user_invalid_email(self):
        """Тест регистрации с некорректным email"""
        data = {
            'name': 'testuser',
            'email': 'not-an-email',  # Некорректный email
            'password': 'securepassword123',
            'status': 'client'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Ожидаем статус 400
        self.assertIn('email', response.data)  # Проверяем, что ошибка указана для 'email'

    def test_register_user_invalid_status(self):
        """Тест регистрации с некорректным статусом"""
        data = {
            'name': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword123',
            'status': 'invalid_role'  # Некорректный статус
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Ожидаем статус 400
        self.assertIn('status', response.data)  # Проверяем, что ошибка указана для 'status'

    def test_register_user_duplicate_username(self):
        """Тест регистрации с уже существующим именем пользователя"""
        # Сначала создаем пользователя
        self.client.post(self.register_url, {
            'name': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword123',
            'status': 'client'
        }, format='json')

        # Пробуем зарегистрировать с тем же username
        data = {
            'name': 'testuser',  # Имя уже существует
            'email': 'anotheremail@example.com',
            'password': 'securepassword123',
            'status': 'petsitter'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Ожидаем статус 400
        self.assertIn('name', response.data)  # Проверяем, что ошибка указана для 'name'

    def test_register_user_duplicate_email(self):
        """Тест регистрации с уже существующим email"""
        # Сначала создаем пользователя
        self.client.post(self.register_url, {
            'name': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword123',
            'status': 'client'
        }, format='json')

        # Пробуем зарегистрировать с тем же email
        data = {
            'name': 'anotheruser',
            'email': 'testuser@example.com',  # Email уже существует
            'password': 'securepassword123',
            'status': 'petsitter'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Ожидаем статус 400
        self.assertIn('email', response.data)  # Проверяем, что ошибка указана для 'email'