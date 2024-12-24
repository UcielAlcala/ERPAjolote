# erp_backend/orders/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderItemViewSet, OrderDetailViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order_items', OrderItemViewSet)
router.register(r'order_details', OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
