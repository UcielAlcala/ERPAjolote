from django.apps import AppConfig


class BomPrintedPiecesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'erp_backend.bom_printed_pieces'

    def ready(self):
            import erp_backend.bom_printed_pieces.signals