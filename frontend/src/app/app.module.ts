import { NgModule, LOCALE_ID } from '@angular/core';
import { HashLocationStrategy, LocationStrategy, registerLocaleData } from '@angular/common';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AppLayoutModule } from './layout/app.layout.module';
import localeEsMx from '@angular/common/locales/es-MX';
import { PrimeNGConfig } from 'primeng/api';

registerLocaleData(localeEsMx);

@NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        AppRoutingModule,
        AppLayoutModule
    ],
    providers: [
        { provide: LOCALE_ID, useValue: 'es-MX' }
    ],
    bootstrap: [AppComponent]
})
export class AppModule {
    constructor( private primengConfig: PrimeNGConfig) {
        this.primengConfig.setTranslation({
        dateFormat: 'dd/mm/yy',
        firstDayOfWeek: 1,
        dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        dayNamesShort: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'],
        dayNamesMin: ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sáb'],
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthNamesShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        today: 'Hoy',
        clear: 'Limpiar',
        weekHeader: 'Semana',
        apply: 'Aplicar',
        startsWith: 'Empieza con',
        contains: 'Contiene',
        notContains: 'No contiene',
        endsWith: 'Termina con',
        equals: 'Igual a',
        notEquals: 'Diferente de',
        noFilter: 'Sin filtro',
        lt: 'Menor que',
        lte: 'Menor o igual que',
        gt: 'Mayor que',
        gte: 'Mayor o igual que',
        dateIs: 'Es',
        dateIsNot: 'No es',
        dateBefore: 'Antes',
        dateAfter: 'Después',
        matchAll: 'Cumple todos',
        matchAny: 'Cumple alguno',
        addRule: 'Agregar filtro',
        removeRule: 'Eliminar filtro',
        accept: 'Si',
        reject: 'No',
        choose: 'Elegir',
        upload: 'Subir',
        cancel: 'Cancelar',
        after: 'Después',
        before: 'Antes',
        am: 'AM',
        chooseDate: 'Elegir fecha',
        chooseMonth: 'Elegir mes',
        chooseYear: 'Elegir año',
        emptyFilterMessage: 'No hay filtros seleccionados',
        emptyMessage: 'No hay registros que mostrar',
        emptySearchMessage: 'No se encontraron coincidencias',
        emptySelectionMessage: 'No hay selección',
        })
    }
}
