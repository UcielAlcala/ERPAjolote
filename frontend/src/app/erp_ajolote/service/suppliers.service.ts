import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Supplier } from '../api/supplier';

@Injectable({
  providedIn: 'root'
})
export class SupplierService {
    private apiUrl = `${environment.apiUrl}/suppliers/`;
  
    constructor(private http: HttpClient) { }
  
    // Obtener todos los proveedores
    getSuppliers(): Observable<Supplier[]> {
      return this.http.get<Supplier[]>(this.apiUrl);
    }
  
    // Obtener un proveedor por ID
    getSupplier(id: number): Observable<Supplier> {
      const url = `${this.apiUrl}${id}/`;
      return this.http.get<Supplier>(url);
    }
  
    // Crear un nuevo proveedor
    createSupplier(supplier: Supplier): Observable<Supplier> {
      const formData = this.createFormData(supplier);
      return this.http.post<Supplier>(this.apiUrl, formData);
    }
  
    // Actualizar un proveedor existente
    updateSupplier(id: number, supplier: Supplier): Observable<Supplier> {
      const formData = this.createFormData(supplier);
      const url = `${this.apiUrl}${id}/`;
      return this.http.put<Supplier>(url, formData);
    }
  
    // Eliminar un proveedor
    deleteSupplier(id: number): Observable<Supplier> {
      const url = `${this.apiUrl}${id}/`;
      return this.http.delete<Supplier>(url);
    }
  
    private createFormData(supplier: Supplier): FormData {
      const formData = new FormData();
      formData.append('name', supplier.name);
      formData.append('contact_name', supplier.contact_name);
      
      if (supplier.address) {
        formData.append('address', supplier.address);
      }
      if (supplier.contact_email) {
        formData.append('contact_email', supplier.contact_email);
      }
      if (supplier.contact_phone) {
        formData.append('contact_phone', supplier.contact_phone);
      }
      return formData;
    }
  }
