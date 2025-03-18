from django.urls import path
# from users.views.registration_views import UserRegistrationView
# from users.views.users_views import UsersListView, UserDetailsView
from orders.views.views import (
    OrderDetailClientView,
    OrderDetailPetsitterView,
    OrderCreateView,
    OrderChangeView
)


urlpatterns = [
    path('details/client/<int:order_id>/', OrderDetailClientView.as_view(), name='order_details_client'),
    path('details/petsitter/<int:order_id>/', OrderDetailPetsitterView.as_view(), name='order_details_petsitter'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('change/', OrderChangeView.as_view(), name='order_change')
]