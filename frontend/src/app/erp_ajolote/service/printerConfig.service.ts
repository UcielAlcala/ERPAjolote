// demo/components/materials/material.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PrinterConfig } from '../api/printer_config';  // Asegúrate de tener la interfaz Material definida
import { environment } from '../../../environments/environment';  // Asegúrate de que la ruta sea correcta

@Injectable({
  providedIn: 'root'
})
export class PrinterConfigService {

  private apiUrl = `${environment.apiUrl}/printer-config/`;  // Asegúrate de que esta URL sea correcta

  constructor(private http: HttpClient) { }

  getPrinterConfigs(): Observable<PrinterConfig[]> {
    return this.http.get<PrinterConfig[]>(this.apiUrl);
  }

  getPrinterConfig(id: number): Observable<PrinterConfig> {
    return this.http.get<PrinterConfig>(`${this.apiUrl}${id}/`);
  }

  createPrinterConfig(PrinterConfig: FormData): Observable<PrinterConfig> {
    return this.http.post<PrinterConfig>(this.apiUrl, PrinterConfig);
  }

  updatePrinterConfig(id: number, PrinterConfig: FormData): Observable<PrinterConfig> {
    return this.http.put<PrinterConfig>(`${this.apiUrl}${id}/`, PrinterConfig);
  }

  deletePrinterConfig(id: any): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }
}
