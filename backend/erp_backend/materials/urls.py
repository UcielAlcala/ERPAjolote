# erp_backend/materials/urls.py

from django.urls import path
from .views import MaterialViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'materials', MaterialViewSet)

urlpatterns = router.urls
