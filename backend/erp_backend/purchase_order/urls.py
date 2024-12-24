from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PurchaseOrderViewSet, PurchaseOrderItemViewSet

router = DefaultRouter()
router.register(r'purchase_orders', PurchaseOrderViewSet)
router.register(r'purchase_order_items', PurchaseOrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
