import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { PrinterConfigComponent } from './printer-config.component';

@NgModule({
	imports: [RouterModule.forChild([
		{ path: '', component: PrinterConfigComponent }
	])],
	exports: [RouterModule]
})
export class PrinterConfigRoutingModule { }
