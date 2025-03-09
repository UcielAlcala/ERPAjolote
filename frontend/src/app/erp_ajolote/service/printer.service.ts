import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PrinterService {
  private apiUrl = `${environment.apiUrl}/printer/`;

  constructor(private http: HttpClient) { }

  /**
   * Conecta la impresora con el número de serie indicado.
   * @param serialNumber Número de serie de la impresora.
   */
  connect(serialNumber: string): Observable<any> {
    return this.http.post(`${this.apiUrl}${serialNumber}/connect/`, {});
  }

  /**
   * Desconecta la impresora con el número de serie indicado.
   * @param serialNumber Número de serie de la impresora.
   */
  disconnect(serialNumber: string): Observable<any> {
    return this.http.post(`${this.apiUrl}${serialNumber}/disconnect/`, {});
  }

  /**
   * Obtiene la temperatura del nozzle de la impresora.
   * @param serialNumber Número de serie de la impresora.
   */
  getNozzleTemp(serialNumber: string): Observable<any> {
    return this.http.get(`${this.apiUrl}${serialNumber}/nozzle-temp/`);
  }

  /**
   * Obtiene la temperatura de la cama de la impresora.
   * @param serialNumber Número de serie de la impresora.
   */
  getBedTemp(serialNumber: string): Observable<any> {
    return this.http.get(`${this.apiUrl}${serialNumber}/bed-temp/`);
  }

    /**
     * Obtiene el estado de la impresora.
     * @param serialNumber Número de serie de la impresora.
     */
    getState(serialNumber: string): Observable<any> {
        return this.http.get(`${this.apiUrl}${serialNumber}/mqtt-state/`);
    }

    /**
     * Obtiene el nombre del trabajo de impresión actual.
     */
    getJobName(serialNumber: string): Observable<any> {
        return this.http.get(`${this.apiUrl}${serialNumber}/job-name/`);
    }

    /**
     * Obtiene el tiempo restante del trabajo de impresión.
     */
    getRemainingTime(serialNumber: string): Observable<any> {
        return this.http.get(`${this.apiUrl}${serialNumber}/time-remaining/`);
    }
}
