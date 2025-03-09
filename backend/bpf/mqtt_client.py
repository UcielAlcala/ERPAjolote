# Import necessary libraries
import ssl
import paho.mqtt.client as mqtt
import threading
import logging
from logging.handlers import RotatingFileHandler
from .utils import ConnectionState
from .printer_status_parser import PrinterStatusParser

# Configurando el handler para rotar los archivos de log
handler = RotatingFileHandler("mqtt_messages.log", maxBytes=1024*1024*5, backupCount=5)
# Configuración básica del logger
logging.basicConfig(
    filename="mqtt_messages.log",  # Archivo donde se guardarán los logs
    level=logging.INFO,  # Nivel de logging
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Formato de los logs
)

logger = logging.getLogger(__name__)  # Obtener una instancia del logger


class MqttClient:
    """
    A class representing an MQTT client for communication with a printer.
    Args:
        printer_config (PrinterConfig): The configuration object for the printer.
    Attributes:
        printer_config (PrinterConfig): The configuration object for the printer.
        client (mqtt.Client): The MQTT client instance.
    Methods:
        connect(): Connects to the MQTT broker.
        on_connect(client, userdata, flags, rc):
            Callback function called when the client connects to the broker.
        on_message(client, userdata, message):
            Callback function called when a message is received.
        on_disconnect(client, userdata, rc):
            Callback function called when the client disconnects from the broker.
    """

    def __init__(self, printer_config):
        """
        Initializes a new instance of the MqttClient class.
        Args:
            printer_config (PrinterConfig): The configuration object for the printer.
        """
        self.printer_config = printer_config
        self.client = None

    def start_session(self):
        """
        Starts a session with the MQTT broker.
        Raises:
            ValueError: If the printer configuration is not complete.
        """

        # Check if the printer configuration is complete
        if (
            self.printer_config.hostname is None
            or self.printer_config.access_code is None
            or self.printer_config.serial_number is None
        ):
            raise ValueError("Printer configuration is not complete")

        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.tls_set(tls_version=ssl.PROTOCOL_TLS, cert_reqs=ssl.CERT_NONE)
        self.client.tls_insecure_set(True)
        self.client.reconnect_delay_set(min_delay=1, max_delay=1)
        self.client.username_pw_set(
            username="bblp", password=self.printer_config.access_code
        )

        def on_connect(client, userdata, flags, rc, properties):
            """
            Callback function called when the client connects to the MQTT broker.
            Args:
                client (mqtt.Client): The MQTT client instance.
                userdata: The user data associated with the client.
                flags: The flags associated with the connection.
                rc (int): The result code of the connection.
            """

            if rc == 0:
                from .printer_farm_controller import PrinterFarmController

                controller = PrinterFarmController()
                printer = controller.get_printer(self.printer_config.serial_number)
                printer.mqtt_status = ConnectionState.CONNECTED
                printer.get_complete_info()
                self.client.subscribe(
                    f"device/{self.printer_config.serial_number}/report"
                )
                print("Se ha establecido una conexión con la impresora")
            else:
                print(f"Connection failed with result code {rc}")

        def on_message(client, userdata, message):
            """
            Callback function called when a message is received.
            Args:
                client (mqtt.Client): The MQTT client instance.
                userdata: The user data associated with the client.
                message (mqtt.MQTTMessage): The received message.
            """

            try:

                payload = message.payload.decode()  # Decodificar el payload
                PrinterStatusParser.parse_and_update(
                    self.printer_config.serial_number, payload
                )  # Parsear y actualizar el estado de la impresora
                logger.info(
                    f"Message received: {payload} from device {self.printer_config.serial_number}"
                )
            except Exception as e:
                logger.error(f"Error al procesar el mensaje {e}")

        def on_disconnect(client, userdata, flags, rc, propierties):
            """
            Callback function called when the client disconnects from the MQTT broker.
            Args:
                client (mqtt.Client): The MQTT client instance.
                userdata: The user data associated
                 with the client.
                rc (int): The result code of the disconnection.
            """

            from .printer_farm_controller import PrinterFarmController

            controller = PrinterFarmController()
            printer = controller.get_printer(self.printer_config.serial_number)
            printer.mqtt_status = ConnectionState.DISCONNECTED
            print(f"Disconnected with result code {rc}")

        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.on_disconnect = on_disconnect
        self.client.connect(self.printer_config.hostname, 8883, 60)

        mqtt_thread = threading.Thread(target=self.client.loop_forever)
        mqtt_thread.start()

    def publish(self, message):
        """
        Publishes a message to the MQTT broker.
        Args:
            message (str): The message to publish.
        """

        self.client.publish(
            f"device/{self.printer_config.serial_number}/request", message
        )
        logger.info(
            f"Message published: {message} to device {self.printer_config.serial_number}"
        )

    def end_session(self):
        """
        Stops the session with the MQTT broker.
        """
        self.client.disconnect()
        self.client.loop_stop()
        print("Session stopped")
