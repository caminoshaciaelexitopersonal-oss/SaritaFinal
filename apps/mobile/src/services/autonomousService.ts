import { api } from './api';

/**
 * SARITA Autonomous Global Intelligence Service (Fase 10)
 * Motor central de IA para gobernanza, planificación y optimización del turismo mundial.
 */

export const autonomousService = {
  // Inteligencia Global
  getGlobalAIInsights: () => api.get('/autonomous/global-insights/'),
  getRegionalOptimizations: (regionId: string) => api.get(`/autonomous/regional-optimization/${regionId}/`),

  // Planificación Autónoma
  generateAutonomousPlan: (regionId: string, constraints: any) =>
    api.post(`/autonomous/plan-regional/${regionId}/`, { constraints }),

  // Simulación y Alertas
  runGlobalSimulation: (scenario: string) => api.post('/autonomous/simulate-global/', { scenario }),
  getGlobalAlerts: () => api.get('/autonomous/alerts/'),

  // Sostenibilidad y Economía
  getGlobalSustainabilityIndex: () => api.get('/autonomous/sustainability-index/'),
};
