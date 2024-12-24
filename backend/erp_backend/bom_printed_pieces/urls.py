# erp_backend/bom_printed_pieces/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BOMPrintedPieceViewSet

router = DefaultRouter()
router.register(r'bom_printed_pieces', BOMPrintedPieceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
