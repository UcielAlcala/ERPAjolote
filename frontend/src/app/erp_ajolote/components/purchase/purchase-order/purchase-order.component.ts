import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import { PurchaseOrder } from 'src/app/erp_ajolote/api/purchase-order';
import { PurchaseOrderService } from 'src/app/erp_ajolote/service/purchase-order.servise';
import { Table } from 'primeng/table';
import { Material } from 'src/app/erp_ajolote/api/material';

// Servicios
import { SupplierService } from 'src/app/erp_ajolote/service/suppliers.service';
import { MaterialService } from 'src/app/erp_ajolote/service/materials.service';




@Component({
  selector: 'app-purchase-order',
  templateUrl: './purchase-order.component.html',
  styleUrls: ['./purchase-order.component.scss']
})
export class PurchaseOrderComponent implements OnInit {

  purchaseOrders: PurchaseOrder[] = [];
  purchaseOrder!: PurchaseOrder;  
  statuses: any[] = [];
  loading: boolean = true;
  suppliers: any[] = [];

  // Materiales
  materiales: any[] = [];
  selectedMateriales: any[] = [];

  // Dialogos
  purchaseOrderDialog: boolean = false;
  activeIndex: Number = 0;
  submitted: boolean = false;

  
  @ViewChild('filter') filter!: ElementRef;
  
  constructor(
    private purchaseOrderService: PurchaseOrderService,
    private supplierService: SupplierService,
    private materialService: MaterialService
  ) {
    this.voidValuesPurchaseOrder();
    this.getAllPurchaseOrders();
    this.getAllMaterials();
  }

  ngOnInit(): void {
    this.statuses = [
      { label: 'Pendiente', value: 'Pending' },
      { label: 'Aprobada', value: 'Approved' },
      { label: 'Recibida', value: 'Received' },
      { label: 'Cerrada', value: 'Closed' },
      { label: 'Cancelada', value: 'Canceled' },
    ];

    this.getSuppliersData();
  }

  // Funciones para Crear o Editar
  savePurchaseOrder(){

  }

  // Funciones para editar
  editPurchaseOrder(purchaseOrder: PurchaseOrder) {
    console.log(purchaseOrder)
  }

  // Funciones para eliminar
  deletePurchaseOrder(purchaseOrder: PurchaseOrder) {
    console.log(purchaseOrder)
  }

  // Controladores de Dialogos
  
  openNew() {
    this.voidValuesPurchaseOrder();
    this.purchaseOrderDialog = true;
  }

  closeDialog() {
    this.purchaseOrderDialog = false;
  }
  
  
  // Utilidades


  voidValuesPurchaseOrder(): void {
    this.purchaseOrder = {
      supplier: {
        name: '',
        contact_name: '',
      },
      order_date: new Date(),
      expected_date: new Date(),
      status: 'Pending',
      total_cost: 0,
      items: [],
      created_at: new Date(),
      updated_at: new Date(),
    }
  }

  getAllPurchaseOrders(): void {
    this.purchaseOrderService.getAllPurchaseOrders().subscribe(purchaseOrders => {
      this.purchaseOrders = purchaseOrders.map(purchaseOrder => {
        return {
          ...purchaseOrder,
          order_date: new Date(purchaseOrder.order_date),
          expected_date: new Date(purchaseOrder.expected_date),
          created_at: new Date(purchaseOrder.created_at),
          updated_at: new Date(purchaseOrder.updated_at),
        }
      });
      this.loading = false;
      console.log(this.purchaseOrders)
    });
  }

  getAllMaterials(): void {
    this.materialService.getMaterials().subscribe(materials => {
      materials.forEach(material => {
        this.materiales.push({ id: material.id, name: material.name, image: material.image });
      });
    });
  }


  clear(table: Table) {
    table.clear();
    this.filter.nativeElement.value = '';
  } 

  displayStatus(status: string): string {
    const foundStatus = this.statuses.find(s => s.value === status);
    return foundStatus ? foundStatus.label : '';
  }

  getSuppliersData(): void {
    this.supplierService.getSuppliers().subscribe(suppliers => {
      suppliers.forEach(supplier => {
        this.suppliers.push({ label: supplier.name, value: supplier.id });
      });
    });
  }

  getSupplierNameById(id: number): string | undefined {
    const supplier = this.suppliers.find(supplier => supplier.value === id);
    return supplier ? supplier.label : undefined;
  }

  onTabChange(index: number): void {
    this.activeIndex = index;
  }

  materialAdded(material: any): void {
    console.log(material);
    console.log(this.selectedMateriales)
  }

}
