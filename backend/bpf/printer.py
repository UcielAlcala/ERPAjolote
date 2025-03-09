import json
import os
import copy
import time
from typing import Optional
from .observer import Observer
from .mqtt_client import MqttClient
from .utils import ConnectionState
from .ftp import IoTFTPSClient


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "utils/requests.json")

# Get the requests comands
with open(file_path, "r", encoding="utf-8") as file:
    requests = json.load(file)


class Printer(Observer):
    '''
    Represents a printer object that connects to an MQTT broker and provides methods for controlling the printer.
        printer_config (object): The configuration object for the printer.
    Attributes:
        mqtt_client (object): The MQTT client object used for communication with the MQTT broker.
        work_queue (list): The queue of work to be processed by the printer.
        mqtt_status (str): The status of the MQTT connection.
        nozzle_temp (int): The current temperature of the printer nozzle.
        nozzle_target_temper (int): The target temperature of the printer nozzle.
        bed_temp (int): The current temperature of the printer bed.
        bed_target_temper (int): The target temperature of the printer bed.
        gcode_state (str): The state of the G-code execution.
        chamber_temp (int): The current temperature of the printer chamber.
        job_completion (float): The completion percentage of the current print job.
        job_remaining_time (int): The estimated remaining time for the current print job.
        print_error (str): The error message, if any, encountered during printing.
        job_name (str): The name of the current print job.
        layer_number (int): The current layer number of the print job.
        total_layer_number (int): The total number of layers in the print job.
        nozzle_diameter (float): The diameter of the printer nozzle.
        nozzle_type (str): The type of the printer nozzle.
        led_status (bool): The status of the printer LED light.
        filament_color (str): The color of the filament being used.
        automate_printing (bool): Flag indicating whether printing is automated.
    Methods:
        connect(): Connects to the MQTT broker.
        disconnect(): Disconnects from the MQTT broker.
        stop_print(): Stops the printing process.
        pause_print(): Pauses the current print job.
        resume_print(): Resumes the paused printing process.
        get_complete_info(): Gets the complete information about the printer.
        unload_filament(): Unloads the filament from the printer.
        load_filament(): Loads the filament into the printer.
        send_gcode(gcode: str): Sends a G-code command to the printer.
        send_gcode_file(file_path: str): Sends a G-code file to the printer.
        print_3mf_file(file_name: str, bed_leveling: bool = True, timelapse: bool = False): Prints a 3MF file.
        toggle_light(): Toggles the printer light.
        set_speed_level(speed_level: int): Sets the speed level of the printer.
        set_nozzle_temp(temp: int): Sets the nozzle temperature of the printer.
        set_bed_temp(temp: int): Sets the bed temperature of the printer.
        eject_part(): Ejects the part from the printer.
        get_sdcard_contents(): Retrieves the contents of the SD card in the printer.
        delete_sdcard_file(file_path: str): Deletes a file from the SD card in the printer.
        upload_sdcard_file(src: str, dest: str) -> dict: Uploads a file to the SD card in the printer.
    '''


    def __init__(self, printer_config):
        super().__init__()
        self.printer_config = printer_config
        self.mqtt_client = self.mqtt_client = MqttClient(self.printer_config)
        self.work_queue = []

        # Atributos de la conexión MQTT
        self.mqtt_status = ConnectionState.NO_STATE
        self.nozzle_temp = None
        self.nozzle_target_temper = None
        self.bed_temp = None
        self.bed_target_temper = None
        self.bed_leveling = 0
        self.gcode_state = None
        self.chamber_temp = None
        self.job_completion = None
        self.job_remaining_time = None
        self.print_error = None
        self.job_name = None
        self.layer_number = None
        self.total_layer_number = None
        self.nozzle_diameter = None
        self.nozzle_type = None
        self.led_status = False
        self.filament_color = None
        self.automatic_printing = False

    def toogle_automatic_printing(self):
        """
        Toggles the automatic printing feature.
        This method changes the value of the `automatic_printing` attribute to its opposite value.
        If `automatic_printing` is currently True, it will be set to False, and vice versa.
        """

        self.automatic_printing = not self.automatic_printing


    def connect(self):
        """
        Connects to the MQTT broker.
        """
        self.mqtt_client.start_session()

    def disconnect(self):
        """
        Disconnects from the MQTT broker.
        """
        self.mqtt_client.end_session()

    def stop_print(self):
        """
        Stops the printing process.
        This method publishes a request to stop the printing process via MQTT.
        Parameters:
            None
        Returns:
            None
        """

        try:
            self.do_if_is_connected(
                lambda: self.mqtt_client.publish(json.dumps(requests["stop_print"]))
            )
        except TypeError as e:
            print(f"Error: {e}")

    def pause_print(self):
        """
        Pauses the current print job.
        This method publishes a request to pause the print job
            using the MQTT client.
        Parameters:
            None
        Returns:
            None
        """
        try:
            self.do_if_is_connected(
                lambda: self.mqtt_client.publish(json.dumps(requests["pause_print"]))
            )
        except TypeError as e:
            print(f"Error: {e}")

    def resume_print(self):
        """
        Resumes the paused printing process.
        This method publishes a request to the MQTT client to resume the
        print job.
        Parameters:
            None
        Returns:
            None
        """
        try:
            self.do_if_is_connected(
                lambda: self.mqtt_client.publish(json.dumps(requests["resume_print"]))
            )
        except TypeError as e:
            print(f"Error: {e}")

    def get_complete_info(self):
        """
        Gets the complete information about the printer.
        This method publishes a request to the MQTT client to get the complete
        information about the printer.
        Parameters:
            None
        Returns:
            None
        """
        try:
            self.do_if_is_connected(
                lambda: self.mqtt_client.publish(
                    json.dumps(requests["get_complete_info"])
                )
            )
        except TypeError as e:
            print(f"Error: {e}")

    def unload_filament(self):
        # TODO Add docstrings
        # TODO: Implement unload_filament method
        pass

    def load_filament(self):
        # TODO Add docstrings
        # TODO: Implement load_filament method
        pass

    def send_gcode(self, gcode: str):
        """
        Sends a G-code command to the printer.
        Args:
            gcode (str): The G-code command to send.
        Returns:
            None
        """
        try:
            cmd = copy.deepcopy(requests["send_gcode"])
            cmd["print"]["param"] = f"{gcode} \n"
            self.do_if_is_connected(lambda: self.mqtt_client.publish(json.dumps(cmd)))
        except TypeError as e:
            print(f"Error: {e}")

    def send_gcode_file(self, file_path: str):
        """
        Sends a G-code file to the printer.
        Args:
            file_path (str): The path to the G-code file to send.
        Returns:
            None
        """
        try:
            with open(file_path, "r") as file:
                for line in file:
                    self.send_gcode(line)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def print_3mf_file(
        self,
        file_name: str,
        timelapse: bool = False,
    ):
        """
        Prints a 3MF file.
        Args:
            file_name (str): The name of the 3MF file to be printed / The file must be placed in root sdcard.
            bed_leveling (bool, optional): Whether to perform bed leveling before printing. Defaults to True.
            timelapse (bool, optional): Whether to capture a timelapse during printing. Defaults to False.
        """

        try:
            cmd = copy.deepcopy(requests["print_3mf_file"])
            cmd["print"]["url"] = f"file:///sdcard/{file_name}"
            cmd["print"]["file"] = file_name
            if self.bed_leveling == 0:
                cmd["print"]["bed_leveling"] = True
                self.bed_leveling = 2
            else:
                cmd["print"]["bed_leveling"] = False
                self.bed_leveling = self.bed_leveling - 1
            cmd["print"]["timelapse"] = timelapse
            self.do_if_is_connected(lambda: self.mqtt_client.publish(json.dumps(cmd)))
        except TypeError as e:
            print(f"Error: {e}")

    def toogle_light(self):
        """
        Toggles the printer light.
        This method publishes a request to the MQTT client to toggle the printer light.
        Parameters:
            None
        Returns:
            None
        """
        # TODO Implementar el método toogle_light
        cmd = copy.deepcopy(requests["toogle_light"])
        if self.led_status == "on":
            cmd["system"]["led_mode"] = "off"
        else:
            cmd["system"]["led_mode"] = "on"

        try:
            self.do_if_is_connected(lambda: self.mqtt_client.publish(json.dumps(cmd)))
            self.led_status = not self.led_status
        except TypeError as e:
            print(f"Error: {e}")

    def do_if_is_connected(self, function):
        """
        Executes the given function if the printer is connected to the MQTT broker.
        """
        if not callable(function):
            raise TypeError("The argument passed is not a callable function.")

        if self.mqtt_status == ConnectionState.CONNECTED:
            # Ejecutar la función
            function()
        else:
            print("The printer is not connected to the MQTT broker.")

    def set_speed_level(self, speed_level: int):
        """
        Sets the speed level of the printer.
        Args:
            speed_level (int): The speed level to set.
                0 - Silent
                1 - Standard
                2 - Sport
                3 - Ludicrous
        Raises:
            TypeError: If the speed level is not an integer.
        Returns:
            None
        """
        if speed_level not in [0, 1, 2, 3]:
            raise ValueError(
                "Speed level must be 0 (Silent), 1 (Standard), 2 (Sport), or 3 / Ludicrous"
            )

        # TODO Implementar el método set_speed_level
        cmd = copy.deepcopy(requests["speed_level"])
        cmd["print"]["param"] = str(speed_level)
        try:
            self.do_if_is_connected(lambda: self.mqtt_client.publish(json.dumps(cmd)))
        except TypeError as e:
            print(f"Error: {e}")

    def set_nozzle_temp(self, temp: int):
        """
        Sets the nozzle temperature of the printer.
        Args:
            temp (int): The temperature to set.
        Raises:
            TypeError: If the temperature is not an integer.
        Returns:
            None
        """
        # TODO Implementar el método set_nozzle_temp
        cmd = copy.deepcopy(requests["send_gcode"])
        cmd["print"]["param"] = f"M104 S{temp} \n"
        try:
            self.do_if_is_connected(lambda: self.mqtt_client.publish(json.dumps(cmd)))
        except TypeError as e:
            print(f"Error: {e}")

    def set_bed_temp(self, temp: int):
        """
        Sets the bed temperature of the printer.
        Args:
            temp (int): The temperature to set.
        Raises:
            TypeError: If the temperature is not an integer.
        Returns:
            None
        """
        # TODO Implementar el método set_bed_temp
        cmd = copy.deepcopy(requests["send_gcode"])
        cmd["print"]["param"] = f"M140 S{temp} \n"
        try:
            self.do_if_is_connected(lambda: self.mqtt_client.publish(json.dumps(cmd)))
        except TypeError as e:
            print(f"Error: {e}")

    def eject_part(self, ejection_instruction: str):
        """
        Ejects the part from the printer.
        This method publishes a request to the MQTT client to eject the part from the printer.
        Parameters:
            None
        Returns:
            None
        """
        cmd1 = copy.deepcopy(requests[ejection_instruction]["cmd1"])
        cmd2 = copy.deepcopy(requests[ejection_instruction]["cmd2"])

        try:
            self.send_gcode(cmd1) # Command to take the extruder to a safe position and turn off the fans with the bed raised
            while self.bed_temp > 31:
                pass
            self.send_gcode(cmd2) # Command to turn off the fans and eject parts
            time.sleep(60)

        except TypeError as e:
            print(f"Error: {e}")

    def get_sdcard_contents(self):
        """
        Retrieves the contents of the SD card in the printer.
        Returns:
            None
        Raises:
            None
        """

        ftps = IoTFTPSClient(
            self.printer_config.hostname,
            990,
            "bblp",
            self.printer_config.access_code,
            ssl_implicit=True,
        )

        fs = self._get_sftp_files(ftps, "/")
        self._sdcard_contents = fs

        def search_for_and_remove_all_other_files(mask: str, entry: dict):
            """
            Recursively searches for files in the given entry and removes all other files that do not match the
            specified mask.
            Args:
                mask (str): The mask to match the file names against.
                entry (dict): The entry to search for files in.
            Returns:
                None
            """

            if "children" in entry:
                entry["children"] = list(
                    filter(
                        lambda i: i["id"].endswith(mask) or "children" in i.keys(),
                        entry["children"],
                    )
                )
                for child in entry["children"]:
                    search_for_and_remove_all_other_files(mask, child)

        self._sdcard_3mf_files = json.loads(json.dumps(self._sdcard_contents))
        search_for_and_remove_all_other_files(".3mf", self._sdcard_3mf_files)

    def _get_sftp_files(
        self, ftps: IoTFTPSClient, directory: str, mask: Optional[str] = None
    ):
        """
        Recursively retrieves a list of files and directories from the specified directory using SFTP.
        Args:
            ftps (IoTFTPSClient): The FTPS client used for file retrieval.
            directory (str): The directory path to retrieve files from.
            mask (Optional[str], optional): A file extension mask to filter the retrieved files. Defaults to None.
        Returns:
            dict: A dictionary representing the directory and its contents. The dictionary has the following keys:
                - 'id': The directory path.
                - 'name': The name of the directory.
                - 'children' (optional): A list of dictionaries representing the files and subdirectories within the
                  directory.
                  Each dictionary has the following keys:
                    - 'id': The file or subdirectory path.
                    - 'name': The name of the file or subdirectory.
        """

        try:
            files = sorted(ftps.list_files_ex(directory))
        except Exception as e:
            print(f"Error: {e}")
            return None

        dir = {}

        dir["id"] = directory + ("/" if directory != "/" else "")
        dir["name"] = (
            directory[directory.rindex("/") + 1 :]  # noqa
            if "/" in directory and directory != "/"
            else directory
        )

        items = []

        for file in files:
            if file[0][:1] == "d":
                item = {}
                item = self._get_sftp_files(
                    ftps,
                    directory + ("/" if directory != "/" else "") + file[1],
                    mask=mask,
                )
                items.append(item)
            else:
                if not mask or (mask and file[1].lower().endswith(mask)):
                    item = {}
                    item["id"] = dir["id"] + file[1]
                    item["name"] = file[1]
                    items.append(item)

        if len(items) > 0:
            dir["children"] = items
        return dir

    def delete_sdcard_file(self, file_path: str):
        """
        Deletes a file from the SD card in the printer.
        Args:
            file_path (str): The path of the file to delete.
        Returns:
            None
        Raises:
            None
        """

        ftps = IoTFTPSClient(
            self.printer_config.hostname,
            990,
            "bblp",
            self.printer_config.access_code,
            ssl_implicit=True,
        )

        ftps.delete_file(file_path)

        def search_for_and_remove_file(file_path: str, entry: dict):
            """
            Recursively searches for the file in the given entry and removes it.
            Args:
                file_path (str): The path of the file to remove.
                entry (dict): The entry to search for the file in.
            Returns:
                None
            """

            if "children" in entry:
                entry["children"] = list(
                    filter(
                        lambda i: i["id"] != file_path,
                        entry["children"],
                    )
                )
                for child in entry["children"]:
                    search_for_and_remove_file(file_path, child)

        search_for_and_remove_file(file_path, self._sdcard_contents)
        search_for_and_remove_file(file_path, self._sdcard_3mf_files)
        return self._sdcard_contents

    def upload_sdcard_file(self, src: str, dest: str) -> dict:
        """
        Uploads a file to the SD card in the printer.
        Args:
            src (str): The path of the file to upload.
            dest (str): The destination path of the file on the SD card.
        Returns:
            dict: A dictionary representing the updated contents of the SD card.
        Raises:
            None
        """
        ftps = IoTFTPSClient(
            self.printer_config.hostname,
            990,
            "bblp",
            self.printer_config.access_code,
            ssl_implicit=True,
        )

        ftps.upload_file(src, dest)
        return self.get_sdcard_contents()
