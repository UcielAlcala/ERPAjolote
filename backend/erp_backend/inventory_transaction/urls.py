# erp_backend/inventory_transaction/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryTransactionViewSet

router = DefaultRouter()
router.register(r'inventory_transactions', InventoryTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
