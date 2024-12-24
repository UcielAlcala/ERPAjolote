import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: 'proveedores', data: { breadcrumb: 'Proveedores' }, loadChildren: () => import('./suppliers/suppliers.module').then(m => m.SuppliersModule) },
  { path: 'ordenes', loadChildren: () => import('./purchase-order/purchase-order.module').then(m => m.PurchaseOrderModule) }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PurchaseManagementRoutingModule { }
