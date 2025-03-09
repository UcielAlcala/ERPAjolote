from typing import List
from .task import Task


class TaskAssignment:
    @staticmethod
    def assign_task_based_on_filament_color(printer, print_jobs: List[Task]) -> int:
        """
        Assigns the next print job to the printer based on the filament color.
        This method prioritizes minimizing filament changes.
        Args:
            printer (Printer): The printer to assign a job to.
            print_jobs (List[dict]): The list containing print jobs to be assigned.
        Returns:
            int: The index of the assigned job.
        Raises:
            ValueError: If no matching job is found for the printer's filament color.
        """
        
        #Filter for Jobs availables
        available_jobs = [job for job in print_jobs if job.status != "in_progress" and job.color == printer.filament_color]
        
        if available_jobs:
            available_jobs.sort(key=lambda job: job.priority)
            job = available_jobs[0]
            printer.print_3mf_file(job.name)
            job.mark_in_progress()
            printer.job_name = job.name
            print(f"Assigned job {job} (Priority {job.priority}) to printer {printer.printer_config.serial_number}")
        else:
            raise ValueError(
                f"No matching jobs for printer {printer.printer_config.serial_number} with filament color {printer.filament_color}."
            )

    @staticmethod
    def assign_task_based_on_priority(printer, print_jobs: List[dict]) -> int:
        """
        Assigns the next print job to the printer based on task priority.
        If multiple jobs have the same priority, prefer jobs that match the current filament color.
        Args:
            printer (Printer): The printer to assign a job to.
            print_jobs (List[dict]): The list containing print jobs to be assigned.
        Returns:
            int: The index of the assigned job.
        Raises:
            ValueError: If no jobs are available.
        """
        print_jobs.sort(key=lambda job: job.priority)

        # First, check if there's a job with the same priority and matching color
        for job in print_jobs:
            if job.status == "in_progress":
                continue  # Skip jobs already in progress

            if job.priority == min(
                [j.priority for j in print_jobs if j.status != "in_progress"]
            ):
                if job.color == printer.filament_color:
                    # If there's a job with the same priority and matching color, assign it
                    printer.print_3mf_file(job.name)
                    job.status = "in_progress"
                    printer.job_name = job.name
                    print(
                        f"Assigned job {job.name} (Priority {job.priority}) to printer {printer.printer_config.serial_number}"
                    )
                    return print_jobs.index(job)

        # If no matching color, assign the first job with the highest priority
        for job in print_jobs:
            if job.status == "in_progress":
                continue

            if job.priority == min(
                [j.priority for j in print_jobs if j.status != "in_progress"]
            ):
                # Assign job regardless of color if no matching color was found
                print(
                    f"Printer {printer.printer_config.serial_number} requires filament change for high-priority job {job.name}."
                )
                printer.unload_filament()
                raise ValueError(
                    f"Filament change required for printer {printer.printer_config.serial_number}."
                )

        raise ValueError(
            f"No jobs available for printer {printer.printer_config.serial_number}."
        )


# TODO Implementar una función que
# revise si el archivo está en la SDCard de la impresora, si no, hay que enviarlo.
