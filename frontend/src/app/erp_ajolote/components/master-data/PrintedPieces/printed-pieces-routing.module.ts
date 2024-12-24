import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { PrintedPiecesComponent } from './printed-pieces.component';
@NgModule({
	imports: [RouterModule.forChild([
		{
			path: '', component: PrintedPiecesComponent
		}
	])],
	exports: [RouterModule]
})
export class PrintedPiecesRoutingModule { }
