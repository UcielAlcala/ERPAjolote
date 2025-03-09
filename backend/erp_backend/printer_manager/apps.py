from django.apps import AppConfig
import sys


class PrinterManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'erp_backend.printer_manager'

    def ready(self):
        # Evitamos ejecutar connect_printers si estamos ejecutando collectstatic u otro comando que no requiere conexión
        if 'collectstatic' in sys.argv or 'migrate' in sys.argv:
            return
        from . import services
        services.add_printers()
        services.connect_all_printers()