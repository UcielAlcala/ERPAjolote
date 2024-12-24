import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { FinalProductsComponent } from "./final-products.component";

@NgModule({
	imports: [RouterModule.forChild([
		{
			path: '', component: FinalProductsComponent
		}
	])],
	exports: [RouterModule]
})
export class FinalProductsRoutingModule { }
