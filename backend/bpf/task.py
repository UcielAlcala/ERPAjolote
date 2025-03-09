class Task:
    def __init__(self, name: str, ejection_instruction: str, color: str, priority: int):
        """
        Initializes a Task object.
        Args:
            name (str): The name of the print job (e.g., the file name).
            color (str): The color of the filament required for the task.
            priority (int): The priority of the task (lower number means higher priority).

        NOTE: The file must be on sdcard root directory and must be only one plate whit the object(s) to print.
        """
        self.name = name  # Name of the print job, typically the file name.
        self.ejection_instruction = ejection_instruction # Ejection instruction on the requests.json for the printer.
        self.color = color  # Required filament color for this task.
        self.priority = priority  # Priority of the task (0 is the highest priority).
        self.status = "pending"  # Task status, initialized as "pending".

    def mark_in_progress(self):
        """Marks the task as 'in_progress'."""
        self.status = "in_progress"

    def mark_completed(self):
        """Marks the task as 'completed'."""
        self.status = "completed"

    def is_in_progress(self) -> bool:
        """Returns True if the task is currently in progress."""
        return self.status == "in_progress"

    def __repr__(self):
        """Returns a string representation of the Task object."""
        return f"Task(name={self.name}, ejection_instruction = {self.ejection_instruction}, color={self.color}, priority={self.priority}, status={self.status})"
