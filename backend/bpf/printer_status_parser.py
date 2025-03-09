# printer_status_parser.py

import json
from threading import Thread


class PrinterStatusParser:
    @staticmethod
    def parse_and_update(serial_number, payload):
        """
        Parse the JSON payload and update the printer's attributes.
        Args:
            serial_number (str): The serial number of the printer to update.
            payload (str): The JSON payload received from the MQTT message.
        """
        try:
            data = json.loads(payload)  # Parse the JSON payload

            # Obtener la instancia del controlador de la granja

            from .printer_farm_controller import PrinterFarmController

            controller = PrinterFarmController()

            # Obtener la impresora correspondiente por número de serie
            printer = controller.get_printer(serial_number)
            if not printer:
                print(f"No printer found with serial number: {serial_number}")
                return

            # Extraer datos del objeto "print" en el payload
            print_data = data.get("print", {})

            # Actualizar atributos de la impresora según los datos del JSON
            prev_gcode_state = printer.gcode_state

            # Actualizar atributos de la impresora según los datos del JSON
            printer.nozzle_temp = print_data.get("nozzle_temper", printer.nozzle_temp)
            printer.nozzle_target_temper = print_data.get(
                "nozzle_target_temper", printer.nozzle_target_temper
            )
            printer.bed_temp = print_data.get("bed_temper", printer.bed_temp)
            printer.bed_target_temper = print_data.get(
                "bed_target_temper", printer.bed_target_temper
            )
            printer.gcode_state = print_data.get("gcode_state", printer.gcode_state)
            printer.chamber_temp = print_data.get(
                "chamber_temper", printer.chamber_temp
            )
            printer.job_completion = print_data.get(
                "mc_percent", printer.job_completion
            )
            printer.job_remaining_time = print_data.get(
                "mc_remaining_time", printer.job_remaining_time
            )
            printer.print_error = print_data.get("print_error", printer.print_error)
            printer.job_name = print_data.get("file", printer.job_name)
            printer.layer_number = print_data.get("layer_num", printer.layer_number)
            printer.total_layer_number = print_data.get(
                "total_layer_num", printer.total_layer_number
            )
            printer.nozzle_diameter = print_data.get(
                "nozzle_diameter", printer.nozzle_diameter
            )
            printer.nozzle_type = print_data.get("nozzle_type", printer.nozzle_type)
            # Extraer y actualizar el led_status de lights_report/mode
            lights_report = print_data.get("lights_report", [])
            if lights_report:
                # Asumiendo que solo hay un objeto en la lista y se toma el primer elemento
                printer.led_status = lights_report[0].get("mode", printer.led_status)
            # Manejar otros campos si son relevantes para tu aplicación
            # Ejemplo: fan_gear, wifi_signal, etc.

            # Notificar al controlador si la impresora termino de imprimir
            if printer.automatic_printing:
                if prev_gcode_state == 'RUNNING' and printer.gcode_state == 'FINISH':
                    eject_and_print_thread = Thread(
                        target=controller.on_printer_state_change,
                        args=(printer.printer_config.serial_number,),
                    )
                    eject_and_print_thread.start()

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"Error updating printer status: {e}")
