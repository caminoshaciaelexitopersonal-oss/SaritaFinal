import { api } from './api';

/**
 * SARITA Travel Orchestration Service (Fase 07)
 * Orquestación inteligente y autónoma del ciclo de viaje.
 */

export const orchestrationService = {
  orchestrateTrip: (destination: string, days: number, budget: number) =>
    api.post('/travel-orchestrator/', { destination, days, budget }),

  getTravelerProfile: () => api.get('/traveler-profile/'),

  getContextualRecommendations: (lat: number, lng: number) =>
    api.get('/contextual-experiences/', { params: { lat, lng } }),

  getLiveExperiences: () => api.get('/live-experiences/'),
};
