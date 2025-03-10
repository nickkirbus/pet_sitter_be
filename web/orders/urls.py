from django.urls import path
# from users.views.registration_views import UserRegistrationView
# from users.views.users_views import UsersListView, UserDetailsView
from orders.views.details_views import OrderDetailView


urlpatterns = [
    path('details/<int:order_id>/', OrderDetailView.as_view(), name='order_details'),
]