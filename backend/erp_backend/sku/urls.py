# erp_backend/sku/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SKUViewSet

router = DefaultRouter()
router.register(r'skus', SKUViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
