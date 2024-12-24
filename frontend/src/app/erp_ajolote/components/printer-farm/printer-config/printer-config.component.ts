import { Component, OnInit } from '@angular/core';
import { Product } from 'src/app/demo/api/product'; 
import { ProductService } from 'src/app/demo/service/product.service';
import { ConfirmationService, MessageService, PrimeNGConfig } from 'primeng/api';
import { Table } from 'primeng/table';
import { MaterialService } from '../../../service/materials.service'
import { Material } from 'src/app/erp_ajolote/api/material';
import { environment } from "src/environments/environment";


@Component({
    templateUrl: './printer-config.component.html',
    providers: [MessageService, ConfirmationService, MaterialService]
})
export class PrinterConfigComponent implements OnInit {

    // Url de carga de archivos:
    mediaUrl = `${environment.mediaurl}/materials`
    selectedFile: File | null = null;

    productDialog: boolean = false;
    materialDialog: boolean = false;

    deleteProductDialog: boolean = false;
    deleteMaterialDialog: boolean = false;

    deleteProductsDialog: boolean = false;
    deleteMaterialsDialog: boolean = false;

    products: Product[] = [];
    materials: Material[] = [];

    product: Product = {};
    material: Material = {
            name: '',
            type: '',       // e.g., Producción, Empaque, Envío
            sub_type: '',    // e.g., Filamento, Pegamento, etc.
            brand: '',
            color: '',
            unit: '',       // e.g., g, ml, m, unidades
            cost_per_unit: 0,
            description: ''
    };

    selectedProducts: Product[] = [];
    selectedMaterials: Material[] = [];

    submitted: boolean = false;

    cols: any[] = [];

    statuses: any[] = [];
    types: any[] = [];
    subTypes: any[] = [];
    units: any[] = [];

    rowsPerPageOptions = [5, 10, 20];

    

    constructor(private config: PrimeNGConfig, private productService: ProductService, private messageService: MessageService, private confirmationService: ConfirmationService, private materialService: MaterialService) {
        
    }

    ngOnInit() {
        this.productService.getProducts().then(data => this.products = data);

        this.materialService.getMaterials().subscribe( (materials) => {
            this.materials = materials;
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
            { label: 'Producción', value: 'production' },
            { label: 'Empaque', value: 'packaging' },
            { label: 'Envío', value: 'shipment' }
        ];
        
        this.subTypes = [
            { label: 'Filamento', value: 'filament' },
            { label: 'Pegamento', value: 'glue' },
            { label: 'Insumos', value: 'supplies' },
            { label: 'Refacciones', value: 'spare_parts' },
        ];

        this.units = [
            { label: 'Gramos', value: 'g' },
            { label: 'Kilogramos', value: 'kg' },
            { label: 'Pieza', value: 'pz' },
        ];
    }

    openNew() {
        
        this.material = {
            name: '',
            type: '',       // e.g., Producción, Empaque, Envío
            sub_type: '',    // e.g., Filamento, Pegamento, etc.
            brand: '',
            color: '',
            unit: '',       // e.g., g, ml, m, unidades
            cost_per_unit: 0,
            description: '',
        }
        
        this.materialDialog = true;
        this.submitted = false;
    }

    deleteSelectedMaterials() {
        this.deleteMaterialsDialog = true;
    }

    editProduct(product: Product) {
        this.product = { ...product };
        this.productDialog = true;
    }
    
    editMaterial(material: Material) {
        this.material = { ...material };
        this.materialDialog = true;
    }

    deleteMaterial(material: Material) {
        this.deleteMaterialDialog = true;
        this.material = { ...material };
    }

    confirmDeleteSelected() {
        this.selectedMaterials.map( material => {
            this.materialService.deleteMaterial(material.id).subscribe( () => {
                this.materials = this.materials.filter(mat => mat.id !== material.id)
                }
            )
        
        }
        
        )
        
        this.selectedMaterials = [];
        this.deleteMaterialsDialog = false    
    }

    confirmDelete(material: Material) {
        this.materialService.deleteMaterial(material.id).subscribe( () => {
            this.materials = this.materials.filter(mat => mat.id !== material.id)
            this.messageService.add({ severity: 'success', summary: 'Exitoso', detail: 'Se ha borrado el producto seleccionado', life: 3000 });
            this.deleteMaterialDialog = false;
        })
    }

    hideDialog() {
        this.materialDialog = false;
        this.submitted = false;
    }

    saveMaterial() {

        // Si el material ya existe en la base de datos -> Se está editando el material.
        if (this.material.id) {

            const formData = new FormData();
            formData.append('name', this.material.name);
            formData.append('type', this.material.type);
            formData.append('sub_type', this.material.sub_type);
            formData.append('brand', this.material.brand);
            formData.append('color', this.material.color);
            formData.append('unit', this.material.unit);
            formData.append('cost_per_unit', this.material.cost_per_unit.toString());
            formData.append('description', this.material.description);

            if (this.selectedFile) {
                formData.append('image', this.selectedFile, this.selectedFile.name);
            }


            this.materialService.updateMaterial(this.material.id, formData).subscribe( (material) => {
                this.materials[this.findIndexById(material.id)] = material;
                this.messageService.add({ severity: 'success', summary: 'Actualización Exitosa', detail: 'Se ha actualizado el material', life: 3000 });
                this.materialDialog = false
                this.submitted = true;
                this.selectedFile = null;
                })
        } else {

            // El material es nuevo y no está en la base de datos

            const formData = new FormData();
            formData.append('name', this.material.name);
            formData.append('type', this.material.type);
            formData.append('sub_type', this.material.sub_type);
            formData.append('brand', this.material.brand);
            formData.append('color', this.material.color);
            formData.append('unit', this.material.unit);
            formData.append('cost_per_unit', this.material.cost_per_unit.toString());
            formData.append('description', this.material.description);

            if (this.selectedFile) {
                formData.append('image', this.selectedFile, this.selectedFile.name);
            }
    
            this.materialService.createMaterial(formData).subscribe( (newMaterial) => {
                this.materials.push(newMaterial)
                
                
                this.material = {
                    name: '',
                    type: '',       // e.g., Producción, Empaque, Envío
                    sub_type: '',    // e.g., Filamento, Pegamento, etc.
                    brand: '',
                    color: '',
                    unit: '',       // e.g., g, ml, m, unidades,
                    cost_per_unit: 0,
                    description: '',
                }

                this.materialDialog = false
                this.submitted = true;
                this.selectedFile = null;
    
            })
        }
    }

    findIndexById(id: any): number {
        let index = -1;
        for (let i = 0; i < this.materials.length; i++) {
            if (this.materials[i].id === id) {
                index = i;
                break;
            }
        }

        return index;
    }

    onGlobalFilter(table: Table, event: Event) {
        table.filterGlobal((event.target as HTMLInputElement).value, 'contains');
    }

    onSelect(event: any): void {
        this.selectedFile = event.files[0];
      }
    


    
}
