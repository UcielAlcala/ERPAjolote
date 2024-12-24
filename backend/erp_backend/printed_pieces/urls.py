# erp_backend/printed_pieces/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrintedPieceViewSet, PrintedPieceMaterialViewSet

router = DefaultRouter()
router.register(r'printed_pieces', PrintedPieceViewSet)
router.register(r'printed_piece_materials', PrintedPieceMaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
