import { api } from './api';

/**
 * SARITA Payment Service (Fase 03)
 * Integración con Stripe para pagos digitales.
 */

export const paymentService = {
  async createPaymentIntent(reservationId: string) {
    try {
      const response = await api.post('/payments/create-intent/', {
        reservation_id: reservationId
      });
      return response.data; // { client_secret: "..." }
    } catch (error) {
      console.error('Error creating payment intent:', error);
      throw error;
    }
  },

  async confirmPayment(paymentIntentId: string) {
    try {
      const response = await api.post('/payments/confirm/', {
        payment_intent_id: paymentIntentId
      });
      return response.data;
    } catch (error) {
      console.error('Error confirming payment:', error);
      throw error;
    }
  },

  async payWithWallet(reservationId: string) {
    try {
      const response = await api.post('/wallet/pay/', {
        reservation_id: reservationId
      });
      return { success: true, data: response.data };
    } catch (error: any) {
      console.error('Error paying with wallet:', error);
      return { success: false, message: error.response?.data?.message || 'Saldo insuficiente o error en wallet.' };
    }
  }
};
