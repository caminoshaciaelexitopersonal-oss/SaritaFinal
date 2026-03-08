import { api } from './api';

/**
 * SARITA Governance & Simulation Service (Fase 09)
 * Gestión de crisis, simulaciones y coordinación internacional.
 */

export const governanceService = {
  // Gemelo Digital y Simulación
  getDigitalTwin: (destinationId: string) => api.get(`/governance/digital-twin/${destinationId}/`),
  runSimulation: (scenario: string, params: any) => api.post('/governance/simulate/', { scenario, ...params }),

  // Centro de Control
  getGlobalAlerts: () => api.get('/governance/alerts/'),
  getInternationalMetrics: () => api.get('/governance/global-metrics/'),

  // Coordinación
  updateCrisisProtocol: (destinationId: string, status: string) =>
    api.post(`/governance/crisis-protocol/${destinationId}/`, { status }),

  publishResearchData: (datasetId: string) => api.post(`/governance/research/publish/${datasetId}/`),
};
