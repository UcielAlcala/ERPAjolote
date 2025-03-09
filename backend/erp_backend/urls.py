"""
URL configuration for erp_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('erp_backend.materials.urls')),
    path('api/', include('erp_backend.printed_pieces.urls')),
    path('api/', include('erp_backend.final_products.urls')),
    path('api/', include('erp_backend.bom_printed_pieces.urls')),
    path('api/', include('erp_backend.inventories.urls')),
    path('api/', include('erp_backend.orders.urls')),
    path('api/', include('erp_backend.sku.urls')),
    path('api/', include('erp_backend.batch_number.urls')),
    path('api/', include('erp_backend.inventory_transaction.urls')),
    path('api/', include('erp_backend.supplier.urls')),
    path('api/', include('erp_backend.purchase_order.urls')),
    path('api/', include('erp_backend.printerConfig.urls')),
    path('api/', include('erp_backend.printer_manager.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)