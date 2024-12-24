import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PurchaseOrderRoutingModule } from './purchase-order-routing.module';

// Modulos NG-Prime
import { FormsModule } from '@angular/forms';
import { TableModule } from 'primeng/table';
import { ButtonModule } from 'primeng/button';
import { RippleModule } from 'primeng/ripple';
import { ToastModule } from 'primeng/toast';
import { ToolbarModule } from 'primeng/toolbar';
import { InputTextModule } from 'primeng/inputtext';
import { InputTextareaModule } from 'primeng/inputtextarea';
import { DropdownModule } from 'primeng/dropdown';
import { RadioButtonModule } from 'primeng/radiobutton';
import { InputNumberModule } from 'primeng/inputnumber';
import { DialogModule } from 'primeng/dialog';
import { MultiSelectModule } from 'primeng/multiselect';
import { TabViewModule } from 'primeng/tabview';
import { CardModule } from 'primeng/card';
import { SelectButtonModule } from 'primeng/selectbutton';
import { CalendarModule } from 'primeng/calendar';
import { PickListModule } from 'primeng/picklist';

import { PurchaseOrderComponent } from './purchase-order.component';
import { ZeroPadPipe } from 'src/app/erp_ajolote/pipes/zero-pad.pipe';


@NgModule({
  declarations: [
    PurchaseOrderComponent,
    ZeroPadPipe
  ],
  imports: [
    CommonModule,
    PurchaseOrderRoutingModule,
    ToastModule,
    ToolbarModule,
    TableModule,
    DialogModule,
    InputTextModule,
    FormsModule,
    ButtonModule,
    RippleModule,
    InputTextareaModule,
    DropdownModule,
    RadioButtonModule,
    InputNumberModule,
    MultiSelectModule,
    TabViewModule,
    CardModule,
    SelectButtonModule,
    CalendarModule,
    PickListModule
  ]
})
export class PurchaseOrderModule { }
