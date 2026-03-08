import { api } from './api';

/**
 * SARITA AI Assistant Service - Desktop
 */
export const aiService = {
  askAssistant: (query: string) => api.post('/ai/assistant/', { query }),
  getRecommendations: () => api.get('/recommendations/'),
};
