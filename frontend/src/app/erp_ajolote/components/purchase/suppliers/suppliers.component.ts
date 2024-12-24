import { Component, OnInit } from '@angular/core';
import { Supplier } from "src/app/erp_ajolote/api/supplier";
import { Table } from 'primeng/table';
import { ConfirmationService, MessageService } from 'primeng/api';
import { SupplierService } from "../../../service/suppliers.service";

@Component({
  selector: 'app-suppliers',
  templateUrl: './suppliers.component.html',
  providers: [ConfirmationService, MessageService, SupplierService ]
})
export class SuppliersComponent implements OnInit{

  // Definición de variables
  suppliers: Supplier[] = [];
  supplier!: Supplier;
  selectedSuppliers: Supplier[] = [];

  // Controladores de Dialogos
  supplierDialog: boolean = false;
  deleteSupplierDialog: boolean = false;
  


  submitted: boolean = false;


  cols!: any[];

  ngOnInit(): void {

    this.cols = [
      'Nombre de Proveedor',
      'Nombre de Contacto',
      'Correo de Contacto',
      'Teléfono de Contacto',
      'Dirección'
    ]

    this.supplier = {
      name: '',
      contact_name: '',
    }

    this.getSuppliers();
    
  }

  constructor(
    private supplierService: SupplierService,
    private messageService: MessageService
  
  ) {

  }

  openNew() {
    this.supplierDialog = true;

  }

  editSupplier(supplier: Supplier) {
    this.supplier = supplier;
    this.openNew();

  }

  deleteSupplier(supplier: Supplier) {
    this.supplier = supplier;
    this.deleteSupplierDialog = true;

  }

  hideDialog() {
    this.supplierDialog = false;
    this.supplier = {
      name: '',
      contact_name: ''
    }

  }

  saveSupplier() {
    if( this.supplier.id) {
      // El proveedor ya existe

      this.supplierService.updateSupplier(this.supplier.id, this.supplier).subscribe( () =>{
        
          this.messageService.add({ severity: 'success', summary: 'Actualización Exitosa', detail: 'Se ha actualizado el proveedor', life: 3000 });
          this.getSuppliers()
          this.supplier = {
              name: '',
              contact_name: ''
          }
          this.hideDialog();
      })
  } else {
      // Es un nuevo proveedor

      this.supplierService.createSupplier(this.supplier).subscribe( () =>{
          this.messageService.add({ severity: 'success', summary: 'Alta Exitosa', detail: 'Se ha registrado un nuevo proveedor', life: 3000 });
          this.getSuppliers()
          this.supplier = {
              name: '',
              contact_name: ''
          }
          this.hideDialog();
      })
  }

  }

  closeDeleteDialog() {
    this.deleteSupplierDialog = false;

  }

  confirmDelete() {
    if ( this.supplier.id ) {
      this.supplierService.deleteSupplier(this.supplier.id).subscribe( () => {
        this.getSuppliers()
        this.messageService.add({ severity: 'error', summary: 'Borrado Exitoso', detail: 'Se ha eliminado al proveedor seleccionado', life: 3000 });
        this.deleteSupplierDialog = false;
      })
    }

  }

  onGlobalFilter(table: Table, event: Event) {
    table.filterGlobal((event.target as HTMLInputElement).value, 'contains');
  }

  getSuppliers() {
    this.supplierService.getSuppliers().subscribe( (sups) => {
      this.suppliers = sups;
    })
  }

}
