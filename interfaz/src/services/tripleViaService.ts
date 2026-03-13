import api from '@/services/api';

export const governmentService = {
  getOfficials: () => api.get('/v1/government/'),
  createOfficial: (data: any) => api.post('/v1/government/', data),
  getPolicies: () => api.get('/v1/governance/policies/'),
};

export const businessService = {
  getProviders: () => api.get('/v1/business/'),
  createService: (data: any) => api.post('/v1/turismo/tourism-services/', data),
};

export const touristService = {
  getDestinations: () => api.get('/v1/turismo/tourism-providers/'),
  makeReservation: (data: any) => api.post('/v1/turismo/tourism-reservations/', data),
};

export const deliveryService = {
  getActiveOrders: () => api.get('/v1/delivery/'),
  completeDelivery: (id: string) => api.post(`/v1/delivery/${id}/complete/`),
};
