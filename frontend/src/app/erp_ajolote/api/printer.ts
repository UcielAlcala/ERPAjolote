import { PrinterConfig } from "./printer_config";

export interface Printer {
    id: number;
    filament_color?: string;
    automating_printing: boolean;
    printer_config: PrinterConfig;
}