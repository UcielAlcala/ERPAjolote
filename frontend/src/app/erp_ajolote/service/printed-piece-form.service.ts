import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Material } from "src/app/erp_ajolote/api/material";
import { PrintedPiece } from "src/app/erp_ajolote/api/printed_piece";

@Injectable({
  providedIn: 'root'
})
export class PrintedPieceFormService {
  private printedPieceSubject = new BehaviorSubject<PrintedPiece>({
    name: '',
    quantity: 0,
    unit: '',
    printTime: 0,
    cost: 0
  });

  printedPiece$ = this.printedPieceSubject.asObservable();

  updatePrintedPiece(data: Partial<PrintedPiece>) {
    const currentPiece = this.printedPieceSubject.value;
    this.printedPieceSubject.next({ ...currentPiece, ...data });
  }

  savePrintedPiece(printedPiece: PrintedPiece) {
    // Lógica para hacer el POST a la base de datos
    // Ejemplo usando HttpClient:
    // return this.http.post('/api/printed-pieces', printedPiece);
  }
}
