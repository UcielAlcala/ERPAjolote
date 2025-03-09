from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import get_controller

@api_view(['POST'])
def connect_printer(request, serial_number):
    """
    Endpoint para conectar una impresora.
    Se espera que la impresora ya esté registrada en el controlador.
    Si no se encuentra, devuelve un error.
    """
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada en el controlador."}, status=404)
    try:
        printer.connect()
        return Response({"status": "Impresora conectada."})
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
def disconnect_printer(request, serial_number):
    """
    Endpoint para desconectar una impresora.
    Se espera que la impresora ya esté registrada en el controlador.
    """
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada en el controlador."}, status=404)
    try:
        printer.disconnect()
        return Response({"status": "Impresora desconectada."})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(["POST"])
def stop_print(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    try:
        printer.stop_print()
        return Response({"status": "Comando para detener impresión enviado"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(["POST"])
def pause_print(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    try:
        printer.pause_print()
        return Response({"status": "Comando para pausar impresión enviado"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(["POST"])
def resume_print(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    try:
        printer.resume_print()
        return Response({"status": "Comando para reanudar impresión enviado"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)

#TODO Implementar la lógica para envíar archivos G-code a la impresora
@api_view(["POST"])
def send_gcode(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    gcode = request.data.get("gcode")
    if not gcode:
        return Response({"error": "Falta el parámetro 'gcode'"}, status=400)
    try:
        printer.send_gcode(gcode)
        return Response({"status": "Comando G-code enviado"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
#TODO Implementar la lógica para envíar archivos G-code a la impresora
@api_view(["POST"])
def send_gcode_file(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    file_path = request.data.get("file_path")
    if not file_path:
        return Response({"error": "Falta el parámetro 'file_path'"}, status=400)
    try:
        printer.send_gcode_file(file_path)
        return Response({"status": "Archivo G-code enviado"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)

#TODO Implementar la lógica para envíar archivos 3MF a la impresora
@api_view(["POST"])
def print_3mf_file(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    file_name = request.data.get("file_name")
    timelapse = request.data.get("timelapse", False)
    if not file_name:
        return Response({"error": "Falta el parámetro 'file_name'"}, status=400)
    try:
        printer.print_3mf_file(file_name, timelapse)
        return Response({"status": "Comando para imprimir archivo 3MF enviado"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(["POST"])
def toggle_light(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    try:
        printer.toogle_light()
        return Response({"status": "Comando para alternar luz enviado"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(["POST"])
def set_speed_level(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    speed_level = request.data.get("speed_level")
    if speed_level is None:
        return Response({"error": "Falta el parámetro 'speed_level'"}, status=400)
    try:
        speed_level = int(speed_level)
    except ValueError:
        return Response({"error": "El parámetro 'speed_level' debe ser un número entero"}, status=400)
    try:
        printer.set_speed_level(speed_level)
        return Response({"status": f"Nivel de velocidad establecido a {speed_level}"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(["POST"])
def set_nozzle_temp(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    temp = request.data.get("temp")
    if temp is None:
        return Response({"error": "Falta el parámetro 'temp'"}, status=400)
    try:
        temp = int(temp)
    except ValueError:
        return Response({"error": "El parámetro 'temp' debe ser un número entero"}, status=400)
    try:
        printer.set_nozzle_temp(temp)
        return Response({"status": f"Temperatura del nozzle establecida a {temp}"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(["POST"])
def set_bed_temp(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    temp = request.data.get("temp")
    if temp is None:
        return Response({"error": "Falta el parámetro 'temp'"}, status=400)
    try:
        temp = int(temp)
    except ValueError:
        return Response({"error": "El parámetro 'temp' debe ser un número entero"}, status=400)
    try:
        printer.set_bed_temp(temp)
        return Response({"status": f"Temperatura de la cama establecida a {temp}"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(["POST"])
def eject_part(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    ejection_instruction = request.data.get("ejection_instruction")
    if not ejection_instruction:
        return Response({"error": "Falta el parámetro 'ejection_instruction'"}, status=400)
    try:
        printer.eject_part(ejection_instruction)
        return Response({"status": "Comando de expulsión enviado"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)

#TODO Implementar la lógica para obtener el contenido de la SD card
@api_view(["GET"])
def get_sdcard_contents(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    try:
        printer.get_sdcard_contents()
        sd_contents = getattr(printer, "_sdcard_contents", None)
        return Response({"sdcard_contents": sd_contents})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
#TODO Implementar la lógica para borrar un archivo de la SD card
@api_view(["POST"])
def delete_sdcard_file(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    file_path = request.data.get("file_path")
    if not file_path:
        return Response({"error": "Falta el parámetro 'file_path'"}, status=400)
    try:
        sd_contents = printer.delete_sdcard_file(file_path)
        return Response({"status": "Archivo eliminado", "sdcard_contents": sd_contents})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
#TODO Implementar la lógica para subir un archivo a la SD card 
@api_view(["POST"])
def upload_sdcard_file(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    src = request.data.get("src")
    dest = request.data.get("dest")
    if not src or not dest:
        return Response({"error": "Faltan los parámetros 'src' o 'dest'"}, status=400)
    try:
        sd_contents = printer.upload_sdcard_file(src, dest)
        return Response({"status": "Archivo subido", "sdcard_contents": sd_contents})
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(["POST"])
def toggle_automatic_printing(request, serial_number):
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada"}, status=404)
    try:
        printer.toogle_automatic_printing()
        return Response({"status": f"Automatic printing toggled. Now is set to {printer.automatic_printing}"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def get_nozzle_temp(request, serial_number):
    """
    Endpoint para obtener la temperatura del nozzle.
    """
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada en el controlador."}, status=404)
    return Response({"nozzle_temp": printer.nozzle_temp})

@api_view(['GET'])
def get_bed_temp(request, serial_number):
    """
    Endpoint para obtener la temperatura de la cama.
    """
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada en el controlador."}, status=404)
    return Response({"bed_temp": printer.bed_temp})

@api_view(['GET'])
def get_time_remaining(request, serial_number):
    """
    Endpoint para obtener el tiempo restante de impresión.
    """
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada en el controlador."}, status=404)
    return Response({"job_remaining_time": printer.job_remaining_time})

@api_view(['GET'])
def get_job_name(request, serial_number):
    """
    Endpoint para obtener el nombre del trabajo actual.
    """
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada en el controlador."}, status=404)
    return Response({"job_name": printer.job_name})

@api_view(['GET'])
def get_printer_state(request, serial_number):
    """
    Endpoint para obtener el estado completo de la impresora.
    """
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada en el controlador."}, status=404)
    
    state = {
        "mqtt_status": str(printer.mqtt_status),
        "nozzle_temp": printer.nozzle_temp,
        "bed_temp": printer.bed_temp,
        "job_remaining_time": printer.job_remaining_time,
        "job_name": printer.job_name,
        "automatic_printing": printer.automatic_printing,
        # Se pueden incluir más datos según sea necesario.
    }
    return Response({"printer_state": state})

@api_view(['GET'])
def get_mqtt_state(request, serial_number):
    """
    Endpoint para obtener el estado del servicio MQTT.
    """
    controller = get_controller()
    printer = controller.get_printer(serial_number)
    if not printer:
        return Response({"error": "Impresora no registrada en el controlador."}, status=404)
    return Response({"mqtt_status": str(printer.mqtt_status)})
