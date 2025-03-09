from typing import Optional


class PrinterConfig:
    """
    This class is used to store the configuration of the printer.
    The configuration includes the
    hostname: the IP address of the printer,
    access code: the access code to the printer given on the printer's screen,
    serial number: the serial number of the printer given on the printer's screen,
    printer name: the name identifying the printer given for the user,
    and printer type: the type of the printer. Example: "A1", "A1 Mini", "P1P", "P1S", "X1", "X1C", "X1E"
    """

    def __init__(
        self,
        hostname: Optional[str] = None,
        access_code: Optional[str] = None,
        serial_number: Optional[str] = None,
        printer_name: Optional[str] = None,
        printer_type: Optional[str] = None,
    ):
        self.hostname = hostname
        self.access_code = access_code
        self.serial_number = serial_number
        self.printer_name = printer_name
        self.printer_type = printer_type

    @property
    def hostname(self):
        """
        Returns the hostname of the printer configuration.
        :return: The hostname of the printer configuration.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        self._hostname = hostname

    @property
    def access_code(self):
        """
        Returns the access code for the printer configuration.
        :return: The access code.
        """

        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        self._access_code = access_code

    @property
    def serial_number(self):
        """
        Returns the serial number of the printer.
        :return: The serial number of the printer.
        """

        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        self._serial_number = serial_number

    @property
    def printer_name(self):
        """
        Returns the name of the printer.
        Returns:
            str: The name of the printer.
        """

        return self._printer_name

    @printer_name.setter
    def printer_name(self, printer_name):
        self._printer_name = printer_name

    @property
    def printer_type(self):
        """
        Returns the printer type.
        :return: The printer type.
        """

        return self._printer_type

    @printer_type.setter
    def printer_type(self, printer_type):
        self._printer_type = printer_type
