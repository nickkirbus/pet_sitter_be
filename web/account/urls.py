from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserDetailsView, UpdateUserDetailsView


urlpatterns = [
    path('user_details/', UserDetailsView.as_view(), name="user_details"),
    path('user_details/update', UpdateUserDetailsView.as_view(), name="user_details_update"),
]
