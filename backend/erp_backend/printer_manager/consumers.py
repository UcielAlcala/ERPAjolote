# erp_backend/printer_manager/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PrinterStateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extraer el número de serie desde la URL
        self.printer_serial = self.scope['url_route']['kwargs']['serial_number']
        self.group_name = f'printer_{self.printer_serial}'

        # Unirse al grupo de la impresora
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Salir del grupo
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Opcional: manejar mensajes recibidos del cliente, si es necesario
        data = json.loads(text_data)
        # Puedes realizar alguna acción según lo recibido
        pass

    async def printer_state_update(self, event):
        """
        Este método se invoca cuando se recibe un mensaje del grupo.
        Se espera que 'event' contenga la clave 'state' con la información actualizada.
        """
        state = event['state']
        await self.send(text_data=json.dumps({
            'printer_state': state
        }))
