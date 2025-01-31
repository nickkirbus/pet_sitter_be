from django.contrib import admin
from django.urls import path, include

from .views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(),name='register'),
]