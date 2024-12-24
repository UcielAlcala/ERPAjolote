import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { WHComponent } from "./warehouses.component";

@NgModule({
	imports: [RouterModule.forChild([
		{
			path: '', component: WHComponent
		}
	])],
	exports: [RouterModule]
})
export class SuppliersRoutingModule { }
