# printer_manager/services.py

from bpf import PrinterFarmController
# Importamos la clase de configuración del core (la definida en printer_farm_controller/printer_config.py)
from bpf import PrinterConfig as CorePrinterConfig
# Importamos el modelo Django (la definición de la base de datos)
from erp_backend.printerConfig.models import PrinterConfig as DjangoPrinterConfig

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

# Variable global para almacenar la instancia única del controlador
_controller_instance = None

def get_controller():
    """
    Retorna la instancia única del PrinterFarmController.
    Si no existe, la crea.
    """
    global _controller_instance
    if _controller_instance is None:
        _controller_instance = PrinterFarmController()
    return _controller_instance

def add_printers():
    """
    Obtiene todas las configuraciones de impresoras desde la base de datos (modelo Django),
    las convierte a la estructura usada por el core y, para cada una, crea o recupera la impresora
    en el controlador, para luego conectarla.
    """
    controller = get_controller()
    # Se obtienen todas las configuraciones almacenadas en la BD
    django_configs = DjangoPrinterConfig.objects.all()

    for config in django_configs:
        # Se crea una instancia de la configuración del core usando los datos del modelo Django
        core_config = CorePrinterConfig(
            hostname=config.hostname,
            access_code=config.access_code,
            serial_number=config.serial_number
        )
        # Se obtiene o crea la impresora en el controlador
        printer = controller.get_or_create_printer(core_config)

def connect_all_printers():
    """
    Itera sobre todas las impresoras registradas en el controlador y las conecta.
    Se asume que cada objeto Printer tiene un método connect().
    """
    controller = get_controller()
    # Se obtienen todas las configuraciones almacenadas en la BD
    django_configs = DjangoPrinterConfig.objects.all()

    for config in django_configs:
        printer = controller.get_printer(config.serial_number)
        try:
            printer.connect()
            print(f"Conectada la impresora: {printer.printer_config.printer_name} (Serial: {config.serial_number})")
        except Exception as e:
            print(f"Error al conectar la impresora {printer.printer_config.printer_name} (Serial: {config.serial_number}): {e}")


def disconnect_all_printers():
    """
    Itera sobre todas las impresoras registradas en el controlador y las desconecta.
    Se asume que cada objeto Printer tiene un método disconnect().
    """
    controller = get_controller()
    for serial, printer in controller.printers.items():
        try:
            printer.disconnect()
            print(f"Desconectada la impresora: {printer.printer_config.printer_name} (Serial: {serial})")
        except Exception as e:
            print(f"Error al desconectar la impresora {printer.printer_config.printer_name} (Serial: {serial}): {e}")

def send_printer_update(serial_number, state):
    channel_layer = get_channel_layer()
    group_name = f'printer_{serial_number}'
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'printer_state_update',
            'state': state  # Aquí 'state' debe ser un diccionario serializable a JSON
        }
    )
