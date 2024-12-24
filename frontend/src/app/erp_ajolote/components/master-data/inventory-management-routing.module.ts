import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

@NgModule({
    imports: [RouterModule.forChild([
        { path: 'materiales', data: { breadcrumb: 'Materiales' }, loadChildren: () => import('./Materials/materials.module').then(m => m.MaterialsModule) },
        { path: 'piezas-impresas', data: { breadcrumb: 'Piezas Impresas' }, loadChildren: () => import('./PrintedPieces/printed-pieces.module').then(m => m.PrintedPiecesModule) },
        { path: 'productos-finales', data: { breadcrumb: 'Productos Finales' }, loadChildren: () => import('./FinalProducts/final-products.module').then(m => m.PrintedPiecesModule) },
    ])],
    exports: [RouterModule]
})
export class InventoryManagementRoutingModule { }
