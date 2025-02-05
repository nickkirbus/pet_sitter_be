from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UsersListView


urlpatterns = [
    path('', UsersListView.as_view(), name='user-list'),
]
