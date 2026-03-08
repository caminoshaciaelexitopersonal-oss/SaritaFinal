import { api } from './api';

/**
 * SARITA Business ERP Service (Mi Negocio) - Desktop Version
 * Sincronizado 1:1 con la estructura de la API de Django.
 */

export const businessService = {
  // Gestión Operativa
  getOperativaDashboard: () => api.get('/mi-negocio/operativa/estadisticas/'),
  getProcesosOperativos: () => api.get('/mi-negocio/operativa/procesos/'),
  getOrdenesOperativas: () => api.get('/mi-negocio/operativa/ordenes/'),
  getIncidenciasOperativas: () => api.get('/mi-negocio/operativa/incidencias/'),
  getSST: () => api.get('/mi-negocio/operativa/sst/'),

  // Gestión Comercial
  getComercialDashboard: () => api.get('/mi-negocio/comercial/main_config/dashboard/'),
  getSales: () => api.get('/mi-negocio/comercial/sales/orders/'),
  getFunnels: () => api.get('/mi-negocio/comercial/funnels/'),

  // Gestión Financiera
  getFinancieraDashboard: () => api.get('/mi-negocio/financiera/dashboard/'),
  getFlujoCaja: () => api.get('/mi-negocio/financiera/flujo-caja/'),

  // Gestión Contable
  getContabilidadGeneral: () => api.get('/mi-negocio/contable/contabilidad/asientos/'),
  getNomina: () => api.get('/mi-negocio/contable/nomina/'),
  getActivosFijos: () => api.get('/mi-negocio/contable/activos-fijos/'),

  // Gestión Archivística
  getArchivisticaDocs: () => api.get('/mi-negocio/archivistica/documentos/'),
};
