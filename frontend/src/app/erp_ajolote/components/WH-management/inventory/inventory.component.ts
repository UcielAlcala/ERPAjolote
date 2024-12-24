import { Component, OnInit } from '@angular/core';
import { ConfirmationService, MessageService, MenuItem } from 'primeng/api';

@Component({
    templateUrl: './inventory.component.html',
    providers: [MessageService, ConfirmationService,]
})
export class InventoryComponent implements OnInit {

        ngOnInit(): void {
            
        }
}
