import { api } from './api';
import { hybridAI } from '@sarita/shared-sdk';

/**
 * SARITA AI Assistant Service - Desktop (INTEGRACIÓN HÍBRIDA)
 */
export const aiService = {
  // Utiliza el motor híbrido del SDK para soporte Offline con Ollama
  askAssistant: (query: string) => hybridAI.ask(query),
  getRecommendations: () => api.get('/recommendations/'),
};
