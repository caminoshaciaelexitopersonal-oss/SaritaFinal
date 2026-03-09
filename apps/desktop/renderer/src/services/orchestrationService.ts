import { api } from './api';

/**
 * SARITA Travel Orchestration Service - Desktop
 */
export const orchestrationService = {
  orchestrateTrip: (destination: string, days: number, budget: number) =>
    api.post('/travel-orchestrator/', { destination, days, budget }),
  getLiveExperiences: () => api.get('/live-experiences/'),
};
