# erp_backend/materials/urls.py

from django.urls import path
from .views import PrinterConfigViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'printer-config', PrinterConfigViewSet)

urlpatterns = router.urls
