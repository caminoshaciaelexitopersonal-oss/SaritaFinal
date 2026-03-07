import { api } from './api';

export const bookingService = {
  getReservations: (params = {}) => api.get('/reservations', { params }),
  createReservation: (data: any) => api.post('/reservations/', data),
  getReservationDetail: (id: string) => api.get(`/reservations/${id}`),
};
