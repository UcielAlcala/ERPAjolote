import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

@NgModule({
    imports: [RouterModule.forChild([
        { path: 'almacenes', data: { breadcrumb: 'Almacenes' }, loadChildren: () => import('./warehouses/warehouses.module').then(m => m.WHModule) },
        { path: 'inventario', data: { breadcrumb: 'Inventario' }, loadChildren: () => import('./inventory/inventory.module').then(m => m.InventoryModule) },
    ])],
    exports: [RouterModule]
})
export class WHManagementRoutingModule { }
