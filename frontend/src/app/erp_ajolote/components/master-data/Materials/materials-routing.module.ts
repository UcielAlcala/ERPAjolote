import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { MaterialsComponent } from './materials.component';

@NgModule({
	imports: [RouterModule.forChild([
		{ path: '', component: MaterialsComponent }
	])],
	exports: [RouterModule]
})
export class MaterialsRoutingModule { }
