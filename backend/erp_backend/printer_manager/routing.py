# erp_backend/printer_manager/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/printer/(?P<serial_number>[^/]+)/$', consumers.PrinterStateConsumer.as_asgi()),
]
