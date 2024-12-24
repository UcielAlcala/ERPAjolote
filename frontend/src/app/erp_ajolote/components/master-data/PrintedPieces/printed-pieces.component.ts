import { Component, OnInit } from '@angular/core';
import { MaterialService } from 'src/app/erp_ajolote/service/materials.service';
import { PrintedPieceMaterialService } from 'src/app/erp_ajolote/service/printed-piece-material.service';
import { PrintedPieceService } from 'src/app/erp_ajolote/service/printed-pieces.service';
import { ConfirmationService, MessageService, MenuItem } from 'primeng/api';
import { Table } from 'primeng/table';
import { PrintedPiece, PrintedPieceMaterial } from 'src/app/erp_ajolote/api/printed_piece';
import { Material } from 'src/app/erp_ajolote/api/material';

@Component({
    templateUrl: './printed-pieces.component.html',
    providers: [MessageService, ConfirmationService, PrintedPieceService, MaterialService, PrintedPieceMaterialService]
})
export class PrintedPiecesComponent implements OnInit {

    selectedFile: File | null = null;

    materials: Material[] = [];
    displayedMaterials: any[] = [];
    addedMaterials: any[] = [];

    addMaterialCF: boolean = false;
    
    material: PrintedPieceMaterial = {};
    newMaterial: PrintedPieceMaterial | undefined; // Para guardar temporalmente el material nuevo

    activeIndex = 0;
    defaultDate!: Date;
    cancelMaterialCreation: PrintedPieceMaterial = {};

    pPieceDialog: boolean = false;

    deletePPieceDialog: boolean = false;
    confirmUpdateMaterialDialog: boolean = false

    deletePPiecesDialog: boolean = false;
    deleteMaterialDialog: boolean = false;

    pPieces: PrintedPiece[] = [];

    pPiece: PrintedPiece = {
        name: '',
        print_time: '',        // ISO 8601 duration string
        materials: []
    };

    unidades: any[] = [];

    pPMaterial: PrintedPieceMaterial[] = [];

    selectedPPieces: PrintedPiece[] = [];

    submitted: boolean = false;

    cols: any[] = [];

    statuses: any[] = [];
    types: any[] = [];
    subTypes: any[] = [];
    units: any[] = [];

    rowsPerPageOptions = [5, 10, 20];

    

    constructor(
        private messageService: MessageService,
        private confirmationService: ConfirmationService,
        private pPieceService: PrintedPieceService,
        private materialService: MaterialService,
        private pPieceMaterialService: PrintedPieceMaterialService,
    ) {
        
    }

    ngOnInit() {

        this.defaultDate = new Date();
        this.defaultDate.setHours(0, 0, 0, 0);

        this.pPieceService.getPrintedPieces().subscribe( (pPieces) => {
            this.pPieces = pPieces.map( piece => ({
                ...piece,
                materials: piece.materials || []
            }))
        })

        this.materialService.getMaterials().subscribe( (materials) => {
            this.materials = materials;
            this.materials.map( (material) => {
                this.displayedMaterials.push({ 'id': material.id, 'name': material.name, 'image': material.image });
            })
        })

        

        this.unidades = [
            { label: 'gramos', value: 'g'},
            { label: 'kilogramos', value: 'kg'},
        ]

        this.cols = [
            { field: 'id', header: 'ID' },
            { field: 'name', header: 'Nombre' },
            { field: 'material', header: 'Material Utilizado' },
            { field: 'quantity', header: 'Cantidad Utilizada' },
            { field: 'printTime', header: 'Tiempo de Impresión' },
            { field: 'cost', header: 'Costo' },
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
            { label: 'g', value: 'grams' },
            { label: 'Kg', value: 'kilograms' },
            { label: 'Pz', value: 'piece' },
        ];
    }

    openNew() {
        
        this.pPiece = {
            name: '',
            print_time: '',        // ISO 8601 duration string
            materials: []
        };
        
        this.pPieceDialog = true;
        this.submitted = false;
    }

    deleteSelectedPrintedPieces() {
        this.deletePPiecesDialog = true;
    }

    
    editPPiece(pPiece: PrintedPiece) {
        this.pPiece = { ...pPiece, materials: pPiece.materials || [] };
        this.pPieceDialog = true;
    }

    deletePPiece(pPiece: PrintedPiece) {
        this.deletePPieceDialog = true;
        this.pPiece = { ...pPiece };
    }

    confirmDeleteSelected() {
        this.selectedPPieces.map( pPiece => {
            this.pPieceService.deletePrintedPiece(pPiece.id).subscribe( () => {
                this.pPieces = this.pPieces.filter(piece => piece.id !== pPiece.id)
                }
            )
        
        }
        
        )
        
        this.selectedPPieces = [];
        this.deletePPiecesDialog = false    
    }

    confirmDelete(pPiece: PrintedPiece) {
        this.pPieceService.deletePrintedPiece(pPiece.id).subscribe( () => {
            this.pPieces = this.pPieces.filter(piece => piece.id !== pPiece.id)
            this.messageService.add({ severity: 'success', summary: 'Exitoso', detail: 'Se ha borrado la pieza impresa seleccionada', life: 3000 });
            this.deletePPieceDialog = false;
        })
    }

    hideDialog() {
        this.pPieceDialog = false;
        this.submitted = false;
        this.addedMaterials = [];
        this.addMaterialCF = false;
    }

    savePPiece() {



        if ( !this.pPiece.id ) {
            // Cuando la pieza no existe - Crea una nueva y sus materiales
            
            const materiales = [...this.pPiece.materials || []]
            delete this.pPiece.materials

            const formData = new FormData();
            formData.append('name', this.pPiece.name);
            formData.append('print_time', this.pPiece.print_time);

            if (this.selectedFile) {
                formData.append('image', this.selectedFile, this.selectedFile.name);
            }

            
            this.pPieceService.createPrintedPiece(formData).subscribe( pieza => {                
                
                this.pPiece = pieza
                this.pPiece.materials = materiales
                this.pPiece.materials.forEach( (material, index) => {
                    material.printed_piece = this.pPiece.id;
                    
                    if ( this.pPiece.materials) {
                        if ( index === this.pPiece.materials.length - 1 ) {
                            this.pPieceMaterialService.createPrintedPieceMaterial(material).subscribe( () => {
                                
                                if(this.pPiece.id) {
                                    this.pPieceService.getPrintedPiece(this.pPiece.id).subscribe( piece => {
                                        this.pPiece = piece
                                        this.pPieces.push(this.pPiece)
                                    })
                                }
                            })
                        } else {        
                            this.pPieceMaterialService.createPrintedPieceMaterial(material).subscribe()
                        }
                    }
                })

                this.selectedFile = null;
            })
        } else {
            // Cuando la pieza si existe - Actualiza la pieza y sus materiales
            const id = this.pPiece.id

            const materiales = [...this.pPiece.materials || []]

            if (this.pPiece.id){
                delete this.pPiece.id
                delete this.pPiece.materials

                const formData = new FormData();
                formData.append('name', this.pPiece.name);
                formData.append('print_time', this.pPiece.print_time);

                if (this.selectedFile) {
                    formData.append('image', this.selectedFile, this.selectedFile.name);
                }

                this.pPieceService.updatePrintedPiece(Number(id), formData).subscribe( piece => {
                    this.pPiece = piece;
                    this.selectedFile = null;
                })
            }

            if(materiales.length > 0) {
                materiales.forEach( (material, index) => {

                    if(material.id){
                        this.pPieceMaterialService.updatePrintedPieceMaterial(Number(material.id), material).subscribe( () => {
                            if ( index === materiales.length - 1 ) {
                                this.pPieceService.getPrintedPieces().subscribe( pieces => {
                                    this.pPieces = pieces
                                })
                            }
                        })
                    } else {
                        material.printed_piece = Number(id);
                        this.pPieceMaterialService.createPrintedPieceMaterial(material).subscribe( () =>{
                            if ( index === materiales.length - 1 ) {
                                this.pPieceService.getPrintedPieces().subscribe( pieces => {
                                    this.pPieces = pieces
                                })
                            }
                        })
                    }

                   

                })
            }
        }

        this.pPieceDialog = false

    }

    onTabChange(index: number): void {
        this.activeIndex = index;
      }
    
    addMaterialControlForm() {
        this.addMaterialCF = true
    }


    findIndexById(id: any): number {
        let index = -1;
        for (let i = 0; i < this.pPieces.length; i++) {
            if (this.pPieces[i].id === id) {
                index = i;
                break;
            }
        }

        return index;
    }

    getMaterialNameById(id: number): string {
        const material = this.materials.find(m => m.id === id);
        return material ? material.name : 'Unknown';
    }
    

    onGlobalFilter(table: Table, event: Event) {
        table.filterGlobal((event.target as HTMLInputElement).value, 'contains');
    }

    editMaterial(material: PrintedPieceMaterial) {
        this.addMaterialCF = true
        this.material = material
        this.cancelMaterialCreation = { ...material }
    }

    deleteMaterial(material: PrintedPieceMaterial) {
        this.deleteMaterialDialog = true;
        this.material = { ...material };
    }

    cancelMaterial(canceledMaterial: PrintedPieceMaterial){
        this.material = {...this.cancelMaterialCreation}
        this.cancelMaterialCreation = {}
        const index = this.pPiece.materials?.findIndex(m => m.id === this.material.id)

        if (index !== undefined && index !== -1) {
            // Actualizar el valor en el array usando el índice
            if (this.pPiece.materials) {
                this.pPiece.materials[index] = { ...this.material };
            }
        }
        
        this.addMaterialCF = false
    }

    confirmMaterial(newMaterial: PrintedPieceMaterial){
        this.newMaterial = newMaterial;
        const existingMaterial = this.checkExistingMaterial(newMaterial)

        if (!existingMaterial) {
            this.pPiece.materials?.push(newMaterial)
            this.material = {};
            this.addMaterialCF = false;
        }
    }

    checkExistingMaterial(newMaterial: PrintedPieceMaterial): boolean {
        const existingMaterial = this.pPiece.materials?.find( material => material.material === newMaterial.material)
1
        if ( existingMaterial ) {
            this.confirmUpdateMaterialDialog = true;
            return true
        } else {
            return false
        }
    }

    confirmDeleteMaterial(material: PrintedPieceMaterial){
        
        if ( material.id) {
            //Si ya existe un ID -> El registro del material ya está en la base de datos.
            this.pPieceMaterialService.deletePrintedPieceMaterial(material.id).subscribe( () => {
                //Alerta mencionando que se eliminó el material.
                this.messageService.add({ severity: 'warn', summary: 'Exitoso', detail: 'Se ha borrado el material seleccionado', life: 3000 });
                //Actualizar pPieces para que refleje los cambios
                if (this.pPiece.id){
                    this.pPieceService.getPrintedPiece(this.pPiece.id).subscribe( piece => {
                        this.pPiece = piece;
                        this.pPieces.map( p => {
                            if( p.id === this.pPiece.id){
                                p = this.pPiece
                            }
                        })
                    })
                    
                }
                this.deleteMaterialDialog = false;
            })
        } else {
            if( this.pPiece.materials) {
                this.pPiece.materials = this.pPiece.materials?.filter( m => m.material !== material.material)
            }
            this.deleteMaterialDialog = false;
            this.material = {};
        }
    }

    confirmUpdateMaterial() {
        if (this.newMaterial) {
            this.addOrUpdateMaterial(this.newMaterial);
            this.confirmUpdateMaterialDialog = false;
            this.addMaterialCF = false;
            this.newMaterial = undefined;
        }
    }

    addOrUpdateMaterial(newMaterial: PrintedPieceMaterial) {
        const existingMaterial = this.pPiece.materials?.find(material => material.material === newMaterial.material);

        if (existingMaterial) {
            // Actualizar material existente
            existingMaterial.quantity = newMaterial.quantity;
            existingMaterial.unit = newMaterial.unit;
        } else {
            // Añadir nuevo material
            this.pPiece.materials = [...(this.pPiece.materials || []), newMaterial];
        }
    }

    onSelect(event: any): void {
        this.selectedFile = event.files[0];
    }
}
