// demo/components/materials/material.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Material } from '../api/material';  // Asegúrate de tener la interfaz Material definida
import { environment } from '../../../environments/environment';  // Asegúrate de que la ruta sea correcta

@Injectable({
  providedIn: 'root'
})
export class MaterialService {

  private apiUrl = `${environment.apiUrl}/materials/`;  // Asegúrate de que esta URL sea correcta

  constructor(private http: HttpClient) { }

  getMaterials(): Observable<Material[]> {
    return this.http.get<Material[]>(this.apiUrl);
  }

  getMaterial(id: number): Observable<Material> {
    return this.http.get<Material>(`${this.apiUrl}${id}/`);
  }

  createMaterial(material: FormData): Observable<Material> {
    return this.http.post<Material>(this.apiUrl, material);
  }

  updateMaterial(id: number, material: FormData): Observable<Material> {
    return this.http.put<Material>(`${this.apiUrl}${id}/`, material);
  }

  deleteMaterial(id: any): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }

  getInsumos(): Observable<Material[]> {
    let apiUrlInsumos = `${this.apiUrl}?custom_filter=Insumos,Pegamento`
    return this.http.get<Material[]>(apiUrlInsumos);
  }
}
