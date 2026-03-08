import { api } from '../../services/api';

/**
 * SARITA Commercial & CRM Service
 * Gestión de clientes, oportunidades, ventas y promociones.
 */

export const commercialService = {
  // Clientes
  getCustomers: (params = {}) => api.get('/customers/', { params }),
  createCustomer: (data: any) => api.post('/customers/', data),
  updateCustomer: (id: string, data: any) => api.put(`/customers/${id}/`, data),

  // Oportunidades
  getOpportunities: () => api.get('/opportunities/'),
  createOpportunity: (data: any) => api.post('/opportunities/', data),

  // Ventas
  getSales: () => api.get('/sales/'),
  recordSale: (data: any) => api.post('/sales/', data),

  // Promociones y Cupones
  getPromotions: () => api.get('/promotions/'),
  createCoupon: (data: any) => api.post('/coupons/', data),

  // Reportes
  getCommercialAnalytics: () => api.get('/commercial/analytics/'),
};
