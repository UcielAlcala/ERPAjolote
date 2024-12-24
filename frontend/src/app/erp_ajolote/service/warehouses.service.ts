// demo/components/materials/material.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Warehouse } from "src/app/erp_ajolote/api/warehouse";
import { environment } from '../../../environments/environment';  // Asegúrate de que la ruta sea correcta

@Injectable({
  providedIn: 'root'
})
export class WHService {

  private apiUrl = `${environment.apiUrl}/warehouses/`;  // Asegúrate de que esta URL sea correcta

  constructor(private http: HttpClient) { }

  getWHS(): Observable<Warehouse[]> {
    return this.http.get<Warehouse[]>(this.apiUrl);
  }

  getWH(id: number): Observable<Warehouse> {
    return this.http.get<Warehouse>(`${this.apiUrl}${id}/`);
  }

  createWH(warehouse: FormData): Observable<Warehouse> {
    return this.http.post<Warehouse>(this.apiUrl, warehouse);
  }

  updateWH(id: number, warehouse: FormData): Observable<Warehouse> {
    return this.http.put<Warehouse>(`${this.apiUrl}${id}/`, warehouse);
  }

  deleteWH(id: any): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }
}
