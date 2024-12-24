# erp_backend/final_products/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinalProductViewSet

router = DefaultRouter()
router.register(r'final_products', FinalProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
