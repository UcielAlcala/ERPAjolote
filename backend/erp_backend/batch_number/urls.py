# erp_backend/batch_number/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BatchNumberViewSet

router = DefaultRouter()
router.register(r'batch_numbers', BatchNumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
