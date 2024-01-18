from django.urls import path
from .views import UserProfileListCreateView, TransactionListCreateView
from .views import YourApiView, transfer_coins

urlpatterns = [
    path('api/users/', UserProfileListCreateView.as_view(), name='user-list-create'),
    path('api/transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('your-endpoint/', YourApiView.as_view(), name='your-api-view'),
    path('transfer-coins/', transfer_coins, name='transfer-coins'),
]
