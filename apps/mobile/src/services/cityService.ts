import { api } from './api';

/**
 * SARITA City & Destination Service (Fase 06)
 * Infraestructura digital para destinos turísticos inteligentes.
 */

export const cityService = {
  getCityTourismData: (cityId: string) => api.get(`/cities/${cityId}/tourism-data/`),
  getDestinationMetrics: (regionId: string) => api.get(`/destinations/${regionId}/metrics/`),

  publishRegionalEvent: (data: any) => api.post('/destinations/events/', data),
  getRegionalOperators: (regionId: string) => api.get(`/destinations/${regionId}/operators/`),
};
