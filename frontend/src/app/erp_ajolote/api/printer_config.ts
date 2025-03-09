export interface PrinterConfig {
    id?: number;
    hostname: string;
    access_code: string;
    serial_number: string;   
    printer_name: string;    
    printer_type: string;
    createdAt?: Date;
    updatedAt?: Date;
  }
  