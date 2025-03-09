import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

@NgModule({
    imports: [RouterModule.forChild([
        { path: 'configurar-impresoras', data: { breadcrumb: 'Configuración Impresoras' }, loadChildren: () => import('./printer-config/printer-config.module').then(m => m.PrinterConfigModule) },
        { path: 'dashboard', data: { breadcrumb: 'Dashboard' }, loadChildren: () => import('./dashboard/dashboard.module').then(m => m.DashboardModule) },
    ])],
    exports: [RouterModule]
})
export class PrinterFarmRoutingModule { }
