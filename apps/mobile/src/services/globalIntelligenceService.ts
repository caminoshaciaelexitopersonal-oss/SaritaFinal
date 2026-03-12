import { api } from './api';

/**
 * SARITA Global Intelligence Service (Fase 08)
 * Analítica de datos turísticos a gran escala y predicción de tendencias globales.
 */

export const globalIntelligenceService = {
  getGlobalTrends: () => api.get('/global-intelligence/trends/'),
  getDemandPrediction: (destinationId: string) => api.get(`/global-intelligence/demand-prediction/${destinationId}/`),

  getTourismEconomicImpact: (regionId: string) => api.get(`/global-intelligence/economic-impact/${regionId}/`),

  getEmergingDestinations: () => api.get('/global-intelligence/emerging-destinations/'),
};
