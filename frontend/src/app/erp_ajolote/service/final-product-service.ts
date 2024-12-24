import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';  // Asegúrate de que la ruta sea correcta
import { FinalProduct } from "../api/final_product";

@Injectable({
  providedIn: 'root'
})
export class FinalProductService {

  private apiUrl = `${environment.apiUrl}/final_products/`;  // Asegúrate de que esta URL sea correcta

  constructor(private http: HttpClient) { }

  // Obtener todos los productos finales
  getFinalProducts(): Observable<FinalProduct[]> {
    return this.http.get<FinalProduct[]>(this.apiUrl);
  }

  // Obtener un producto final por ID
  getFinalProduct(id: number): Observable<FinalProduct> {
    return this.http.get<FinalProduct>(`${this.apiUrl}${id}/`);
  }

  // Crear un nuevo producto final
  createFinalProduct(finalProduct: FormData): Observable<FinalProduct> {
    return this.http.post<FinalProduct>(this.apiUrl, finalProduct);
  }

  // Actualizar un producto final existente
  updateFinalProduct(id: number, finalProduct: FormData): Observable<FinalProduct> {
    return this.http.put<FinalProduct>(`${this.apiUrl}${id}/`, finalProduct);
  }

  // Eliminar un producto final
  deleteFinalProduct(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }
}
