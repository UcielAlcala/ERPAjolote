import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { PurchaseOrder } from '../api/purchase-order';

@Injectable({
    providedIn: 'root'
})
export class PurchaseOrderService {
    
    private apiUrl = `${environment.apiUrl}/purchase_orders/`;

    constructor(private http: HttpClient) { }

    getAllPurchaseOrders(): Observable<PurchaseOrder[]> {
        return this.http.get<PurchaseOrder[]>(this.apiUrl);
    }

    getPurchaseOrderById(id: number): Observable<PurchaseOrder> {
        const url = `${this.apiUrl}/${id}`;
        return this.http.get<PurchaseOrder>(url);
    }

    createPurchaseOrder(purchaseOrder: PurchaseOrder): Observable<PurchaseOrder> {
        return this.http.post<PurchaseOrder>(this.apiUrl, purchaseOrder);
    }

    updatePurchaseOrder(id: number, purchaseOrder: PurchaseOrder): Observable<PurchaseOrder> {
        const url = `${this.apiUrl}/${id}`;
        return this.http.put<PurchaseOrder>(url, purchaseOrder);
    }

    deletePurchaseOrder(id: number): Observable<void> {
        const url = `${this.apiUrl}/${id}`;
        return this.http.delete<void>(url);
    }
}