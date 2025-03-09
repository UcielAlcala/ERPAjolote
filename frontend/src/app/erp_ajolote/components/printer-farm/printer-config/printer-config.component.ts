import { Component, OnInit } from '@angular/core';
import { ConfirmationService, MessageService, PrimeNGConfig } from 'primeng/api';
import { Table } from 'primeng/table';
import { PrinterConfigService } from '../../../service/printerConfig.service'
import { PrinterConfig } from 'src/app/erp_ajolote/api/printer_config';
import { environment } from "src/environments/environment";


@Component({
    templateUrl: './printer-config.component.html',
    providers: [MessageService, ConfirmationService, PrinterConfigService]
})
export class PrinterConfigComponent implements OnInit {

    printerConfigDialog: boolean = false;
    deletePrinterConfigDialog: boolean = false;
    deleteConfigsDialog: boolean = false;

    printerConfigs: PrinterConfig[] = [];

    printer_config: PrinterConfig = {
            hostname: '',
            access_code: '',
            serial_number: '',
            printer_name: '', 
            printer_type: '',
    };

    selectedPrinterConfigs: PrinterConfig[] = [];

    submitted: boolean = false;

    cols: any[] = [];
    types: any[] = [];

    rowsPerPageOptions = [5, 10, 20];

    

    constructor(private config: PrimeNGConfig, private messageService: MessageService, private confirmationService: ConfirmationService, private printerConfigService: PrinterConfigService) {
        
    }

    ngOnInit() {
        this.printerConfigService.getPrinterConfigs().subscribe( (printerConfigs) => {
            this.printerConfigs = printerConfigs;
        })

        this.cols = [
            { field: 'id', header: 'ID' },
            { field: 'name', header: 'Nombre' },
            { field: 'type', header: 'Categoría Primaria' },
            { field: 'sub_type', header: 'Categoría Secundaria' },
            { field: 'color', header: 'Color' },
            { field: 'brand', header: 'Marca' },
            { field: 'cost_per_unit', header: 'Precio' },
        ];
        
        this.types = [
            { label: 'P1P', value: 'P1P' },
            { label: 'P1S', value: 'P1S' },
            { label: 'A1 Mini', value: 'A1 Mini' }
        ];
    }

    openNew() {
        
        this.printer_config = {
            hostname: '',
            access_code: '',
            serial_number: '',
            printer_name: '', 
            printer_type: '',
    };
        
        this.printerConfigDialog = true;
        this.submitted = false;
    }

    deleteSelectedPrinterConfigs() {
        this.deleteConfigsDialog = true;
    }
    
    editPrinterConfig(printer_config: PrinterConfig) {
        this.printer_config = { ...printer_config };
        this.printerConfigDialog = true;
    }

    deletePrinterConfig(printer_config: PrinterConfig) {
        this.deletePrinterConfigDialog = true;
        this.printer_config = { ...printer_config };
    }

    confirmDeleteSelected() {
        this.selectedPrinterConfigs.map( printer_config => {
            this.printerConfigService.deletePrinterConfig(printer_config.id).subscribe( () => {
                this.printerConfigs = this.printerConfigs.filter(pc => pc.id !== printer_config.id)
                }
            )
        
        }
        
        )
        
        this.selectedPrinterConfigs = [];
        this.deleteConfigsDialog = false    
    }

    confirmDelete(printer_config: PrinterConfig) {
        this.printerConfigService.deletePrinterConfig(printer_config.id).subscribe( () => {
            this.printerConfigs = this.printerConfigs.filter(pc => pc.id !== printer_config.id)
            this.messageService.add({ severity: 'success', summary: 'Exitoso', detail: 'Se ha borrado la configuración seleccionada', life: 3000 });
            this.deletePrinterConfigDialog = false;
        })
    }

    hideDialog() {
        this.printerConfigDialog = false;
        this.submitted = false;
    }

    savePrinterConfig() {

        // Si el material ya existe en la base de datos -> Se está editando el material.
        if (this.printer_config.id) {

            const formData = new FormData();
            formData.append('printer_name', this.printer_config.printer_name);
            formData.append('printer_type', this.printer_config.printer_type);
            formData.append('hostname', this.printer_config.hostname);
            formData.append('access_code', this.printer_config.access_code);
            formData.append('serial_number', this.printer_config.serial_number);


            this.printerConfigService.updatePrinterConfig(this.printer_config.id, formData).subscribe( (pc) => {
                this.printerConfigs[this.findIndexById(pc.id)] = pc;
                this.messageService.add({ severity: 'success', summary: 'Actualización Exitosa', detail: 'Se ha actualizado la impresora', life: 3000 });
                this.printerConfigDialog = false
                this.submitted = true;
                })
        } else {

            // El material es nuevo y no está en la base de datos

            const formData = new FormData();
            formData.append('printer_name', this.printer_config.printer_name);
            formData.append('printer_type', this.printer_config.printer_type);
            formData.append('hostname', this.printer_config.hostname);
            formData.append('access_code', this.printer_config.access_code);
            formData.append('serial_number', this.printer_config.serial_number);
    
            this.printerConfigService.createPrinterConfig(formData).subscribe( (newPrinterConfig) => {
                this.printerConfigs.push(newPrinterConfig)
                
                
                this.printer_config = {
            hostname: '',
            access_code: '',
            serial_number: '',
            printer_name: '', 
            printer_type: '',
    };

                this.printerConfigDialog = false
                this.submitted = true;
    
            })
        }
    }

    findIndexById(id: any): number {
        let index = -1;
        for (let i = 0; i < this.printerConfigs.length; i++) {
            if (this.printerConfigs[i].id === id) {
                index = i;
                break;
            }
        }

        return index;
    }

    onGlobalFilter(table: Table, event: Event) {
        table.filterGlobal((event.target as HTMLInputElement).value, 'contains');
    }


    
}
