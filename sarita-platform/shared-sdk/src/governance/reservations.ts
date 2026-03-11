import { httpClient } from '../api/httpClient';

export interface ReservationData {
  id: string;
  client: string;
  service: string;
  startDate: string;
  endDate: string;
  status: 'PENDIENTE' | 'CONFIRMADA' | 'EN_CURSO' | 'FINALIZADA' | 'CANCELADA';
  price: string;
}

export class ReservationService {
  /**
   * Obtiene el listado de reservas para el prestador autenticado.
   */
  static async listReservations(): Promise<ReservationData[]> {
    const response = await httpClient.get('/operativa/reservas/');
    return response.data.map((r: any) => ({
      id: r.id.toString(),
      client: r.cliente_nombre || r.cliente_id,
      service: r.servicio_nombre,
      startDate: r.fecha_inicio,
      endDate: r.fecha_fin,
      status: r.estado,
      price: `$${r.monto_total.toLocaleString()}`
    }));
  }

  /**
   * Crea una nueva reserva.
   */
  static async createReservation(data: Partial<ReservationData>): Promise<ReservationData> {
    const response = await httpClient.post('/operativa/reservas/', data);
    return response.data;
  }

  /**
   * Actualiza el estado de una reserva.
   */
  static async updateStatus(id: string, status: string): Promise<void> {
    await httpClient.patch(`/operativa/reservas/${id}/`, { estado: status });
  }

  /**
   * Cancela una reserva.
   */
  static async cancelReservation(id: string): Promise<void> {
    await httpClient.post(`/operativa/reservas/${id}/cancel/`);
  }
}
