import { Component, OnInit } from '@angular/core';
import { ConfirmationService, MessageService } from 'primeng/api';
import { Table } from 'primeng/table';
import { Warehouse  } from "src/app/erp_ajolote/api/warehouse";

// Servicios
import { WHService } from "src/app/erp_ajolote/service/warehouses.service";

@Component({
    templateUrl: './warehouses.component.html',
    providers: [MessageService, ConfirmationService, WHService]
})


export class WHComponent implements OnInit {

    wHS: Warehouse[] = [];
    wH: Warehouse = {
        name: ''
    }

    selectedWHS: Warehouse[] = [];
    cols: any[] = []; 

    // Dialogos
    wHDialog: boolean = false;
    deleteWHDialog: boolean = false;

    // Control de Formularios
    submitted: boolean = false;

  ngOnInit(): void {
    this.getWHS()

    

    this.cols = [
        { field: 'name', header: 'Nombre' },
    ];
  }

  

  constructor( private wHService: WHService) {
  }

  openNew() {
    this.wHDialog = true;

  }

  editWH(wH: Warehouse) {
    this.wH = wH;
    this.wHDialog = true;

  }

  deleteWH(wH: Warehouse) {
    this.wH = wH;
    this.deleteWHDialog = true;
  }

  confirmDelete() {
    this.wHService.deleteWH(this.wH.id).subscribe( () =>{
        this.getWHS()
        this.wH = {
            name: ''
        }
        this.deleteWHDialog = false;
    })

  }

  saveWH() {
    if( this.wH.id) {
        // El almacén ya existe

        const formData = new FormData()
        formData.append('name', this.wH.name)

        this.wHService.updateWH(this.wH.id, formData).subscribe( () =>{
            this.getWHS()
            this.wH = {
                name: ''
            }
        })
    } else {
        // Es un nuevo almacén
        const formData = new FormData()
        formData.append('name', this.wH.name)

        this.wHService.createWH(formData).subscribe( () =>{
            this.getWHS()
            this.wH = {
                name: ''
            }
        })
    }
  }

  hideDialog() {
    this.wHDialog = false;
  }

  closeDeleteDialog() {
    this.wH = {
        name: ''
    }
    this.deleteWHDialog = false;
  }


  onGlobalFilter(table: Table, event: Event) {
    table.filterGlobal((event.target as HTMLInputElement).value, 'contains');
  }

  getWHS() {
    this.wHService.getWHS().subscribe( warehouses => {
        this.wHS = warehouses
        this.wHDialog = false;
    })
  }
}
