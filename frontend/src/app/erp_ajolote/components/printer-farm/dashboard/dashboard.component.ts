import { Component, OnInit } from '@angular/core';
import {
    ConfirmationService,
    MessageService,
    PrimeNGConfig,
} from 'primeng/api';
import { environment } from 'src/environments/environment';
import { PrinterConfigService } from "src/app/erp_ajolote/service/printerConfig.service";
import { PrinterService } from "src/app/erp_ajolote/service/printer.service";

@Component({
    templateUrl: './dashboard.component.html',
    providers: [MessageService, ConfirmationService, PrinterConfigService, PrinterService],
})
export class DashboardComponent implements OnInit {

    printers: any[] = [];

    ngOnInit(): void {
        this.pcService.getPrinterConfigs().subscribe( pcs => {
            pcs.forEach( (pc, index) => {
                if (!this.printers[index]){
                    this.printers[index] = { printerConfig: null };
                }
                this.printers[index].printerConfig = pc;
                this.printerService.getState(pc.serial_number).subscribe( state => {
                    this.printers[index].mqtt_state = state.mqtt_status;
                });
                this.printerService.getJobName(pc.serial_number).subscribe( jobName => {
                    this.printers[index].job_name = jobName.job_name;
                });
                this.printerService.getRemainingTime(pc.serial_number).subscribe( remainingTime => {
                    this.printers[index].remaining_time = remainingTime.job_remaining_time;
                });
            })
        })
    }

    constructor( private pcService: PrinterConfigService, private printerService: PrinterService) { }
}
