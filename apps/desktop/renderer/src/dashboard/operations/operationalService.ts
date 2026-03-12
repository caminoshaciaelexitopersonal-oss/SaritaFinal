import { api } from '../../services/api';

/**
 * SARITA Operational Service
 * Gestión de tours, personal, recursos físicos y programación de reservas.
 */

export const operationalService = {
  // Tours y Experiencias
  getTours: () => api.get('/business/tours/'),
  createTour: (data: any) => api.post('/business/tours/', data),
  updateTour: (id: string, data: any) => api.put(`/business/tours/${id}/`, data),

  // Reservas (Calendario)
  getOperationalBookings: (params = {}) => api.get('/business/operational-bookings/', { params }),

  // Personal (Guías, Operadores)
  getStaff: () => api.get('/business/staff/'),
  updateStaffAssignment: (bookingId: string, staffId: string) =>
    api.post(`/business/bookings/${bookingId}/assign-staff/`, { staff_id: staffId }),

  // Recursos (Lanchas, Vehículos)
  getResources: () => api.get('/business/resources/'),
  checkResourceAvailability: (date: string) => api.get('/business/resources/availability/', { params: { date } }),

  // Métricas Operativas
  getOperationsMetrics: () => api.get('/business/operations/metrics/'),
};
