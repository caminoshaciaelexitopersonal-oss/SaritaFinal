import { api } from './api';

/**
 * SARITA AI & Recommendation Service (Fase 04)
 * Consume el motor de IA del backend para recomendaciones personalizadas.
 */

export const aiService = {
  async getRecommendations() {
    try {
      const response = await api.get('/recommendations/');
      return response.data.recommended_tours || [];
    } catch (error) {
      console.error('Error fetching AI recommendations:', error);
      return [];
    }
  },

  async getDynamicPrice(tourId: string) {
    try {
      const response = await api.get(`/tours/${tourId}/dynamic-price/`);
      return response.data;
    } catch (error) {
      return null;
    }
  }
};
