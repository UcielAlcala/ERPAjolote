# erp_backend/inventories/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet, InventoryItemViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'inventory_items', InventoryItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
