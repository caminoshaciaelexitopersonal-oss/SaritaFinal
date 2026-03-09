import { api } from './api';

/**
 * SARITA Delivery Service - Desktop
 */
export const deliveryService = {
  getRestaurants: () => api.get('/delivery/restaurants/'),
  getProducts: (restaurantId: string) => api.get(`/delivery/restaurants/${restaurantId}/products/`),
  placeOrder: (orderData: any) => api.post('/delivery/orders/', orderData),
  trackOrder: (orderId: string) => api.get(`/delivery/orders/${orderId}/track/`),
};
