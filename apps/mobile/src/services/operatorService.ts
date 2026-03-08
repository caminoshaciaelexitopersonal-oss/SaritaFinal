import { api } from './api';

/**
 * SARITA Operator Service (Fase 04)
 * Marketplace de Experiencias Turísticas.
 */

export const operatorService = {
  getEarnings: () => api.get('/operator/earnings/'),
  getDashboardMetrics: () => api.get('/operator/dashboard/'),

  createTour: (data: any) => api.post('/operator/tours/', data),
  updateTour: (id: string, data: any) => api.put(`/operator/tours/${id}/`, data),

  getBookings: () => api.get('/operator/bookings/'),
};
