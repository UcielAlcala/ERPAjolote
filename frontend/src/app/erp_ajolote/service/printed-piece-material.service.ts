import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PrintedPieceMaterial } from '../api/printed_piece';  // Asegúrate de tener la interfaz PrintedPiece definida
import { environment } from '../../../environments/environment';  // Asegúrate de que la ruta sea correcta

@Injectable({
    providedIn: 'root'
  })

  export class PrintedPieceMaterialService {
  
    private apiUrl = `${environment.apiUrl}/printed_piece_materials/`;  // Asegúrate de que esta URL sea correcta
  
    constructor(private http: HttpClient) { }
  
    // Método para obtener todos los PrintedPieceMaterials
  getPrintedPieceMaterials(): Observable<PrintedPieceMaterial[]> {
    return this.http.get<PrintedPieceMaterial[]>(this.apiUrl);
  }

  // Método para obtener un PrintedPieceMaterial por su ID
  getPrintedPieceMaterial(id: number): Observable<PrintedPieceMaterial> {
    return this.http.get<PrintedPieceMaterial>(`${this.apiUrl}${id}/`);
  }

  // Método para crear un nuevo PrintedPieceMaterial
  createPrintedPieceMaterial(printedPieceMaterial: PrintedPieceMaterial): Observable<PrintedPieceMaterial> {
    return this.http.post<PrintedPieceMaterial>(this.apiUrl, printedPieceMaterial);
  }

  // Método para actualizar un PrintedPieceMaterial existente
  updatePrintedPieceMaterial(id: number, printedPieceMaterial: PrintedPieceMaterial): Observable<PrintedPieceMaterial> {
    return this.http.put<PrintedPieceMaterial>(`${this.apiUrl}${id}/`, printedPieceMaterial);
  }

  // Método para eliminar un PrintedPieceMaterial por su ID
  deletePrintedPieceMaterial(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }


  }