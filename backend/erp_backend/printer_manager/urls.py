from django.urls import path
from . import views

urlpatterns = [
    path('printer/<str:serial_number>/connect/', views.connect_printer, name='connect_printer'),
    path('printer/<str:serial_number>/disconnect/', views.disconnect_printer, name='disconnect_printer'),
    path('printer/<str:serial_number>/nozzle-temp/', views.get_nozzle_temp, name='get_nozzle_temp'),
    path('printer/<str:serial_number>/bed-temp/', views.get_bed_temp, name='get_bed_temp'),
    path('printer/<str:serial_number>/time-remaining/', views.get_time_remaining, name='get_time_remaining'),
    path('printer/<str:serial_number>/state/', views.get_printer_state, name='get_printer_state'),
    path('printer/<str:serial_number>/stop-print/', views.stop_print, name='stop_print'),
    path('printer/<str:serial_number>/pause-print/', views.pause_print, name='pause_print'),
    path('printer/<str:serial_number>/resume-print/', views.resume_print, name='resume_print'),
    path('printer/<str:serial_number>/send-gcode-file/', views.send_gcode_file, name='send_gcode_file'),
    path('printer/<str:serial_number>/send-gcode/', views.send_gcode, name='send_gcode'),
    path('printer/<str:serial_number>/print-3mf/', views.print_3mf_file, name='print_3mf_file'),
    path('printer/<str:serial_number>/toggle-light/', views.toggle_light, name='toggle_light'),
    path('printer/<str:serial_number>/set-speed/', views.set_speed_level, name='set_speed_level'),
    path('printer/<str:serial_number>/set-nozzle-temp/', views.set_nozzle_temp, name='set_nozzle_temp'),
    path('printer/<str:serial_number>/set-bed-temp/', views.set_bed_temp, name='set_bed_temp'),
    path('printer/<str:serial_number>/eject-part/', views.eject_part, name='eject_part'),
    path('printer/<str:serial_number>/sdcard-contents/', views.get_sdcard_contents, name='get_sdcard_contents'),
    path('printer/<str:serial_number>/delete-sdcard-file/', views.delete_sdcard_file, name='delete_sdcard_file'),
    path('printer/<str:serial_number>/upload-sdcard-file/', views.upload_sdcard_file, name='upload_sdcard_file'),
    path('printer/<str:serial_number>/toggle-automatic/', views.toggle_automatic_printing, name='toggle_automatic_printing'),
    path('printer/<str:serial_number>/job-name/', views.get_job_name, name='job_name'),
    path('printer/<str:serial_number>/mqtt-state/', views.get_mqtt_state, name='get_mqtt_state'),
]
