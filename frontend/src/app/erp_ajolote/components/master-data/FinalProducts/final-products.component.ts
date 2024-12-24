import { Component, OnInit } from '@angular/core';
import { ConfirmationService, MessageService } from 'primeng/api';
import { Table } from 'primeng/table';
import { BOM, FinalProduct } from 'src/app/erp_ajolote/api/final_product';
import { FinalProductService } from 'src/app/erp_ajolote/service/final-product-service';
import { MaterialService } from 'src/app/erp_ajolote/service/materials.service';
import { PrintedPieceService } from 'src/app/erp_ajolote/service/printed-pieces.service';
import * as _ from 'lodash';
import { BOMPrintedPieceService } from 'src/app/erp_ajolote/service/bom-printed-piece.service';

@Component({
    templateUrl: './final-products.component.html',
    providers: [
        MessageService,
        ConfirmationService,
        FinalProductService,
        MaterialService,
        PrintedPieceService,
        BOMPrintedPieceService,
    ],
})
export class FinalProductsComponent implements OnInit {

    selectedFile: File | null = null;

    // Definición de Materiales y Piezas Impresas
    materialMap: Map<number, {content_type: number, name: string}> = new Map();
    pPieceMap: Map<number, {content_type: number, name: string}> = new Map();

    // Definición de Productos Finales
    fProducts: FinalProduct[] = [];
    fProduct!: FinalProduct;

    // Dialogos
    createFinalProductDialog: boolean = false;
    addComponentCF: boolean = false;
    confirmEditComponentDialog: boolean = false;
    confirmDeleteComponentDialog: boolean = false;
    confirmDeleteFProductDialog: boolean = false;

    // Opciones dropdown formulario
    displayedType!: any[];
    insumos: any[] = [];

    // Control del Formulario
    submitted: boolean = false;
    newComponent!: BOM;
    newComponentData!: any;
    originalProduct!: any;
    originalComponent!: any;

    // Utilidades Extras
    activeIndex: Number = 0;

    constructor(
        private messageService: MessageService,
        private fProductService: FinalProductService,
        private materialService: MaterialService,
        private pPieceService: PrintedPieceService,
        private bomPrintedPieceService: BOMPrintedPieceService
    ) {}

    ngOnInit() {
        // Asignando valores
        this.displayedType = [
            { label: 'Pieza Impresa', value: 8 },
            { label: 'Insumo', value: 7 },
        ];

        this.newComponent = {
            content_type: 0,
            object_id: 0,
            quantity: 0,
        };

        this.newComponentData = {
            data: {
                id: 0,
                content_type: 0,
            }
        }

        //Obteniendo los Productos Finales de la base de datos
        this.fProductService.getFinalProducts().subscribe((p) => {
            this.fProducts = p;
        });

        //Obteniendo los Materiales de la base de datos
        this.materialService.getMaterials().subscribe((m) => {
            m.forEach((material) => {
                const filteredMaterial = {
                    name: material.name,
                    content_type: 7
                }
                if (material.id) {
                    this.materialMap.set(material.id, filteredMaterial);
                }
            });
        });

        //Obteniendo las Piezas Impresas de la base de datos

        //Modificar para que además de insumos, también traiga elementos del empaque
        this.pPieceService.getPrintedPieces().subscribe((pP) => {
            pP.forEach((piece) => {
                if (piece.id) {
                    const filteredPPiece = {
                        name: piece.name,
                        content_type: 8
                    }
                    this.pPieceMap.set(piece.id, filteredPPiece);
                    this.insumos.push({ name: piece.name, image: piece.image,  data: {id: piece.id, content_type: 8} });
                }
            });
        });

        this.materialService.getInsumos().subscribe((ins) => {
            ins.map((insumo) => {
                this.insumos.push({ name: insumo.name, image: insumo.image, data: {id: insumo.id, content_type: 7} });
            });
        });
    }

    // Funciones para mostrar dialogos

    openNew() {
        this.fProduct = {
            name: '',
            description: '',
            bom: [],
        };

        this.createFinalProductDialog = true;
        this.submitted = false;
    }

    addCompCF() {
        this.addComponentCF = true;
    }

    // Funciones de creación

    createUpdateNewfProduct() {
        // Revisando si se modificaron o no los name o description de algún producto

        if (this.fProduct.id) {
            // El Producto final ya existe y hay que modificarlo

            if (
                this.fProduct.name !== this.originalProduct.name ||
                this.fProduct.description !== this.originalProduct.description ||
                this.selectedFile
            ) {
                //Se modificó el nombre o descripción, entonces hay que actualizarlo

                const formData = new FormData;
                formData.append('name', this.fProduct.name )
                formData.append('description', this.fProduct.description )

                if (this.selectedFile) {
                    formData.append('image', this.selectedFile, this.selectedFile.name);
                }

                this.fProductService
                    .updateFinalProduct(this.fProduct.id, formData)
                    .subscribe(() => {
                        this.fProductService.getFinalProducts().subscribe( products => {
                            this.fProducts = products
                        })

                        this.selectedFile = null;
                    });
            }

            const diffComponents = this.checkDifferences();

            // Eliminando los componentes seleccionados por el usuario
            if (diffComponents.removed) {
                diffComponents.removed.forEach((component: any) => {
                    this.bomPrintedPieceService
                        .deleteBOMPrintedPiece(component.id)
                        .subscribe(() => {
                            // Eliminar el componente de fProduct.bom
                            if (this.fProduct.bom) {
                                this.fProduct.bom = this.fProduct.bom.filter(
                                    (b) => b.id !== component.id
                                );

                                // Actualizar fProducts con el nuevo fProduct
                                this.fProductService.getFinalProducts().subscribe( products => {
                                    this.fProducts = products
                                  })
                            }
                        });
                });
            }

            // Agregando los nuevos componentes
            if (diffComponents.added) {
                diffComponents.added.forEach((component) => {
                    if (this.fProduct.id) {
                        component.final_product = this.fProduct.id;
                    }
                    this.bomPrintedPieceService
                        .createBOMPrintedPiece(component)
                        .subscribe((createdComponent) => {

                            const index = this.fProduct.bom?.findIndex( (b) => b.content_type === createdComponent.content_type && b.object_id === createdComponent.object_id)

                            if (index && index > -1) {
                                // Actualizar componente existente
                                if ( this.fProduct.bom) {
                                    this.fProduct.bom[index] = createdComponent;
                                }

                            } else {
                                // Agregar nuevo componente
                                this.fProduct.bom?.push(createdComponent);
                            }

                            // Asignar la nueva referencia para que Angular detecte el cambio

                            // Ahora actualizar fProducts con el nuevo fProduct
                            this.fProductService.getFinalProducts().subscribe( products => {
                                this.fProducts = products
                              })
                        });
                });
            }

            // Actualizando los componentes modificados
            if (diffComponents.modified) {
                diffComponents.modified.forEach((component) => {
                    let modifiedComponent = {
                        object_id: component.object_id,
                        content_type: component.content_type,
                        final_product: this.fProduct.id,
                        quantity: component.quantity,
                    };

                    if (component.id) {
                        this.bomPrintedPieceService.updateBOMPrintedPiece(component.id, modifiedComponent).subscribe((updatedComponent) => {
                            if (this.fProduct.bom) {
                                const index = this.fProduct.bom.findIndex(
                                    (b) =>
                                        b.content_type === updatedComponent.content_type &&
                                        b.object_id === updatedComponent.object_id
                                );

                                if (index !== -1) {
                                    this.fProduct.bom[index] = updatedComponent;

                                    // Actualizar fProducts
                                    this.fProductService.getFinalProducts().subscribe( products => {
                                        this.fProducts = products
                                      })
                                }
                            }
                        });
                    }
                });
            }

        } else {

            // Se está generando un nuevo producto final y sus componentes

            if (this.fProduct.name && this.fProduct.description) {

                const formData = new FormData();
                formData.append('name', this.fProduct.name)
                formData.append('description', this.fProduct.description)

                if (this.selectedFile) {
                    formData.append('image', this.selectedFile, this.selectedFile.name);
                }

                this.fProductService
                    .createFinalProduct(formData)
                    .subscribe((product) => {
                        this.selectedFile = null;
                        this.fProduct.id = product.id;
                        // Añadiendo el ID de la nueva pieza a los componentes
                        this.fProduct.bom?.forEach((b, index) => {
                            b.final_product = product.id;

                            let bomIndex = index
                            this.bomPrintedPieceService
                                .createBOMPrintedPiece(b)
                                .subscribe( createdComponent => {
                                    
                                    if (this.fProduct.bom) {
                                        this.fProduct.bom[bomIndex] = createdComponent
                                    }

                                    if ( this.fProduct.bom && bomIndex === this.fProduct.bom.length - 1){
                                        // Añadiendo el nuevo producto al listado
                                      this.fProductService.getFinalProducts().subscribe( products => {
                                        this.fProducts = products
                                      })
                                    }
                                });
                        });
                    });
            }
        }

        // Actualizando o añadiendo los componentes del producto
        this.messageService.add({ severity: 'success', summary: 'Exitoso', detail: 'Se ha registrado la información del producto', life: 3000 });
        this.createFinalProductDialog = false;
    }

    addNewComponent() {

        if ( this.newComponentData.data ) {
            this.newComponent.object_id = this.newComponentData.data.id;
            this.newComponent.content_type = this.newComponentData.data.content_type;
        }

        const isExistingComponent = this.fProduct.bom?.some((bom) => {
            if (bom.object_id && bom.object_id === this.newComponent.object_id) {
                // Desplegar un nuevo modal confirmando la modificación
                this.confirmEditComponentDialog = true;
                return true;
            }
            return false;
        });


        if (!isExistingComponent) {
            this.fProduct.bom?.push(this.newComponent);
            this.addComponentCF = false;
            
            this.newComponent = {
                content_type: 0,
                object_id: 0,
                quantity: 0,
            };
    
            this.newComponentData = {
                data: {
                    id: 0,
                    content_type: 0
                }
            }
        }
    }

    confirmUpdateComponent() {
        this.fProduct.bom?.forEach((bom, index) => {
            if (bom.object_id && bom.object_id === this.newComponent.object_id) {
                if (this.fProduct.bom) {
                    this.fProduct.bom[index] = _.cloneDeep(this.newComponent);
                    this.newComponent = {
                        content_type: 0,
                        object_id: 0,
                        quantity: 0
                    }
                    
                    this.newComponentData = {
                        data: {
                            id: 0,
                            content_type: 0
                        }
                    }
                }
            }
        });

       

        this.confirmEditComponentDialog = false;
        this.addComponentCF = false;
    }

    //Funciones de Edición
    editFinalProduct(product: FinalProduct) {
        this.originalProduct = _.cloneDeep(product);
        this.fProduct = product;
        this.createFinalProductDialog = true;
    }

    editComponent(bom: BOM) {
        this.originalComponent = { ...bom };
        this.newComponent = bom;
        this.newComponentData = {
            data: {
                id: this.newComponent.object_id,
                content_type: this.newComponent.content_type
            }
        }
        this.addComponentCF = true;
    }

    cancelNewComponent() {
        // Revisar si el componente existe

        if (this.newComponent.id) {
            // Buscar el componente y resetearlo al valor original
            this.fProduct.bom?.forEach((bom, index) => {
                if (bom.id && bom.id === this.newComponent.id) {
                    if (this.fProduct.bom) {
                        this.fProduct.bom[index] = this.originalComponent;
                    }

                    this.originalComponent = {};
                    this.addComponentCF = false;
                }
            });
        }

        this.newComponent = {
            content_type: 0,
            object_id: 0,
            quantity: 0,
        };
        this.addComponentCF = false;
    }

    // Funciones de Borrado
    deleteFProduct(fProduct: FinalProduct) {
        if (fProduct) {
         this.fProduct = fProduct;   
        }

        this.confirmDeleteFProductDialog = true;
    }

    deleteFinalProduct() {
        if (!this.fProduct.id) return;  // Verificar que el producto tiene un ID

        this.fProductService.deleteFinalProduct(this.fProduct.id).subscribe({
            next: () => {
                // Manejar el éxito
                this.fProducts = this.fProducts.filter(p => p.id !== this.fProduct.id);
                this.confirmDeleteFProductDialog = false;
                this.messageService.add({ severity: 'success', summary: 'Exitoso', detail: 'Se ha borrado el producto seleccionado', life: 3000 });
            },
            error: error => {
                // Manejar el error
                console.error('Error eliminando el producto:', error);
                this.messageService.add({ severity: 'warn', summary: 'Alerta', detail: 'No se ha podido borrar el producto seleccionado', life: 3000 });
            }
        });
    }

    deleteComponent(bom: BOM) {
        this.originalComponent = bom;
        this.confirmDeleteComponentDialog = true;
    }

    confirmDeleteComponent() {
        if (this.originalComponent.id) {
            this.fProduct.bom?.forEach((b, index) => {
                if (b.id === this.originalComponent.id) {
                    if (this.fProduct.bom) {
                        delete this.fProduct.bom[index];
                    }
                }
            });
        } else {
            this.fProduct.bom?.forEach((b, index) => {
                if (
                    b.content_type == this.originalComponent.content_type &&
                    b.object_id === this.originalComponent.object_id
                ) {
                    if (this.fProduct.bom) {
                        delete this.fProduct.bom[index];
                    }
                }
            });
        }

        this.originalComponent = {};

        this.confirmDeleteComponentDialog = false;
    }

    // Utilidades control de componentes visibles

    getContentTypeName(contentTypeId: number): string {
        switch (contentTypeId) {
            case 7:
                return 'Insumo';
            case 8:
                return 'Pieza Impresa';
            default:
                return 'Unknown';
        }
    }

    closeDialog() {
        if ( this.fProduct.id){
            this.fProducts.forEach((product, index) => {
                if (product.id === this.originalProduct.id) {
                    this.fProducts[index] = this.originalProduct;
                }
            });
        }
        
        this.originalProduct = {};
        this.addComponentCF = false;
        this.createFinalProductDialog = false;
    }

    getItemName(contentTypeId: number, objectId: number): string {
        switch (contentTypeId) {
            case 7:
                const material = this.materialMap.get(objectId);
                return material ? material.name : 'Material Desconocido';
            case 8:    
                const pPiece = this.pPieceMap.get(objectId);
                return pPiece ? pPiece.name : 'Pieza Desconocida'
            default:
                return 'No se conoce la información del componente';
        }
    }

    onTabChange(index: number): void {
        this.activeIndex = index;
    }

    onGlobalFilter(table: Table, event: Event) {
        table.filterGlobal(
            (event.target as HTMLInputElement).value,
            'contains'
        );
    }

    checkDifferences() {
        const added = this.fProduct.bom?.filter(
            (fbom: BOM) =>
                !this.originalProduct.bom.some(
                    (obom: BOM) => obom.id === fbom.id
                )
        );
        const removed = this.originalProduct.bom.filter(
            (obom: BOM) =>
                !this.fProduct.bom?.some((fbom: BOM) => fbom.id === obom.id)
        );
        const modified = this.fProduct.bom?.filter((fbom: BOM) => {
            const original = this.originalProduct.bom.find(
                (obom: BOM) => obom.id === fbom.id
            );
            return original && !_.isEqual(fbom, original);
        });

        return { added, removed, modified };
    }

    onSelect(event: any): void {
        this.selectedFile = event.files[0];
    }
}
