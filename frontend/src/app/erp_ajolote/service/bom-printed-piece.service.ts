import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';  // Asegúrate de que la ruta sea correcta
import { BOM } from "../api/final_product";

@Injectable({
  providedIn: 'root'
})
export class BOMPrintedPieceService {

  private apiUrl = `${environment.apiUrl}/bom_printed_pieces/`;  // Asegúrate de que esta URL sea correcta

  constructor(private http: HttpClient) { }

  // Obtener todos los BOMPrintedPieces
  getBOMPrintedPieces(): Observable<BOM[]> {
    return this.http.get<BOM[]>(this.apiUrl);
  }

  // Obtener un BOMPrintedPiece por ID
  getBOMPrintedPiece(id: number): Observable<BOM> {
    return this.http.get<BOM>(`${this.apiUrl}${id}/`);
  }

  // Crear un nuevo BOMPrintedPiece
  createBOMPrintedPiece(bomPrintedPiece: BOM): Observable<BOM> {
    return this.http.post<BOM>(this.apiUrl, bomPrintedPiece);
  }

  // Actualizar un BOMPrintedPiece existente
  updateBOMPrintedPiece(id: number, bomPrintedPiece: BOM): Observable<BOM> {
    return this.http.put<BOM>(`${this.apiUrl}${id}/`, bomPrintedPiece);
  }

  // Eliminar un BOMPrintedPiece
  deleteBOMPrintedPiece(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }
}
