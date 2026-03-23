import { api } from './api';

/**
 * SARITA Delivery Service
 * Gestión de pedidos, restaurantes y seguimiento logístico.
 */

export const deliveryService = {
  // Operational Delivery (Real)
  getActiveOrders: () => api.get('/delivery/'),
  completeDelivery: (id: string, evidence: any) => api.patch(`/delivery/${id}/`, evidence),

  getRestaurants: () => api.get('/delivery/restaurants/'),
  getProducts: (restaurantId: string) => api.get(`/delivery/restaurants/${restaurantId}/products/`),
  createOrder: (data: any) => api.post('/delivery/orders/', data),
  getOrderTracking: (orderId: string) => api.get(`/delivery/orders/${orderId}/tracking/`),
};
