import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PrintedPiece } from '../api/printed_piece';  // Asegúrate de tener la interfaz PrintedPiece definida
import { environment } from '../../../environments/environment';  // Asegúrate de que la ruta sea correcta

@Injectable({
  providedIn: 'root'
})
export class PrintedPieceService {

  private apiUrl = `${environment.apiUrl}/printed_pieces/`;  // Asegúrate de que esta URL sea correcta

  constructor(private http: HttpClient) { }

  getPrintedPieces(): Observable<PrintedPiece[]> {
    return this.http.get<PrintedPiece[]>(this.apiUrl);
  }

  getPrintedPiece(id: number): Observable<PrintedPiece> {
    return this.http.get<PrintedPiece>(`${this.apiUrl}${id}/`);
  }

  createPrintedPiece(printedPiece: FormData): Observable<PrintedPiece> {
    return this.http.post<PrintedPiece>(this.apiUrl, printedPiece);
  }

  updatePrintedPiece(id: number, printedPiece: FormData): Observable<PrintedPiece> {
    return this.http.put<PrintedPiece>(`${this.apiUrl}${id}/`, printedPiece);
  }

  deletePrintedPiece(id: any): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }
}
