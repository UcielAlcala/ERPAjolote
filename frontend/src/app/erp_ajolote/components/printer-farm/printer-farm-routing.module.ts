import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

@NgModule({
    imports: [RouterModule.forChild([
        { path: 'configurar-impresoras', data: { breadcrumb: 'Configuración Impresoras' }, loadChildren: () => import('./printer-config/printer-config.module').then(m => m.PrinterConfigModule) },
    ])],
    exports: [RouterModule]
})
export class PrinterFarmRoutingModule { }
