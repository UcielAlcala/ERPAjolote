# Importing the required libraries
from .printer import Printer
from .singleton_base import SingletonMeta
from .task import Task
from .task_assignment import TaskAssignment


class PrinterFarmController(metaclass=SingletonMeta):
    """
    A class representing the controller for the printer farm.
    Attributes:
        printers (Dict[str, Printer]): A dictionary of printers in the farm, where the key is the serial number.
        print_tasks (List[Dict[str, str]]): A list of print tasks in the queue.
        task_assignment_method (str): The method used for task assignment.
            Possible values: "filament_color", "priority".
    Methods:
        get_or_create_printer(printer_config: PrinterConfig) -> Printer: Adds a printer to the farm if it doesn't exist, or returns the existing printer.
        remove_printer(printer_serial_number: str): Removes a printer from the farm.
        add_print_job(file_name: str, color: str, quantity: int): Adds a print job to the queue.
        print_next_job(printer_serial_number: str): Prints the next job in the queue for the specified printer.
        stop_printing(printer_serial_number: str): Stops the printing process for the specified printer.
        get_printer(printer_serial_number: str) -> Printer: Returns a printer by serial number.
        get_all_printers_serial_numbers() -> List[str]: Returns the serial numbers of all printers in the farm.
        count_registered_printers() -> int: Returns the number of registered printers in the farm.
        on_printer_state_change(printer_serial_number: str): Handles the state change of a printer.
    """

    def __init__(self):
        self.printers = {}
        self.print_tasks = []
        self.task_assignment_method = "priority"

    def get_or_create_printer(self, printer_config):
        """
        Adds a printer to the farm, ensuring no duplicates.
        Args:
            printer (Printer): The printer to add.
        """

        serial_number = printer_config.serial_number

        # Verificar si una impresora con el mismo número de serie ya existe
        existing_printer = self.get_printer(serial_number)
        if existing_printer:
            print(
                f"Printer with serial number {serial_number} already exists in the farm."
            )
            return existing_printer
        else:
            new_printer = Printer(printer_config)
            self.printers[serial_number] = new_printer
            print(f"Printer {serial_number} added to the farm.")
            return new_printer

    def remove_printer(self, printer_serial_number):
        """
        Removes a printer from the farm.
        Args:
            printer (Printer): The printer to remove.
        """
        existing_printer = self.get_printer(printer_serial_number)
        if existing_printer:
            self.printers.pop(existing_printer.printer_config.serial_number)
            print(f"Printer {printer_serial_number} removed from the farm.")
        else:
            print(
                "No printer with serial number {printer_serial_number} found in the farm."
            )

    def add_print_task(self, task: Task):
        """
        Adds a print job to the queue.
        Args:
            task (Task): The print job to add to the queue.
        """
        self.print_tasks.append(task)

    def print_next_job(self, printer_serial_number):
        """
        Prints the next job in the queue for the specified printer.
        Args:
            printer_serial_number: The printer to print the next job for.
        """
        # Print the next job for the printer
        pass

    def stop_printing(self, printer_serial_number):
        """
        Stops the printing process for the specified printer.
        Args:
            printer_serial_number: The printer to stop printing for.
        """
        # Stop printing for the printer
        pass

    def get_printer(self, printer_serial_number: str):
        """
        Returns a printer by serial number.
        Args:
            printer_serial_number (str): The serial number of the printer to return.
        Returns:
            Printer: The printer object with the specified serial number, or None if not found.
        """
        return self.printers.get(printer_serial_number)

    def get_all_printers_serial_numbers(self):
        """

        Returns the names of all printers in the farm.
        Returns:
            List[str]: A list of printer names.
        """

        return [
            printer.printer_config.serial_number for printer in self.printers.values()
        ]

    def count_registered_printers(self):
        """
        Returns the number of registered printers in the farm.
        Returns:
            int: The number of registered printers.
        """
        return len(self.printers)

    def on_printer_state_change(self, printer_serial_number, skip_eject = False):
        """
        Handles the executed commands to perform when a printer finish the print.
        Args:
            printer_serial_number: The serial number of the printer.
        """
        printer = self.get_printer(printer_serial_number)
        
        if not skip_eject:
            # Find and remove the completed job from the list
            for i, task in enumerate(self.print_tasks):
                if task.name == printer.job_name and task.is_in_progress():
                    printer.eject_part(task.ejection_instruction)
                    print(task.ejection_instruction)
                    print(
                        f"Completed task {task.name} on printer {printer_serial_number}. Removing from the list."
                    )
                    task.mark_completed()
                    del self.print_tasks[i]
                    break



        # Try to assign the next job from the list to this printer
        try:
            if printer.automatic_printing:
                if self.task_assignment_method == "filament_color":
                    TaskAssignment.assign_task_based_on_filament_color(
                        printer, self.print_tasks
                    )
                elif self.task_assignment_method == "priority":
                    TaskAssignment.assign_task_based_on_priority(printer, self.print_tasks)
                else:
                    raise ValueError(
                        f"Unknown task assignment method: {self.task_assignment_method}"
                    )
        except ValueError as e:
            print(f"Error: {e}")
            # Handle the error, such as logging it, notifying the user, or taking corrective action

    def set_task_assignment_method(self, method):
        """
        Sets the task assignment method to be used.
        Args:
            method (Callable): The task assignment method to use.
        """
        self.task_assignment_method = method
