import { api } from './api';

/**
 * SARITA Business ERP Service (Mi Negocio)
 * Gestión comercial, operativa, financiera y contable para prestadores.
 */

export const businessService = {
  // Alineación total con la estructura de URLs del backend Django (apps/prestadores/mi_negocio/urls.py)

  // Gestión Operativa (Genérica y Específica)
  getOperativaDashboard: () => api.get('/mi-negocio/operativa/estadisticas/'),
  getProcesosOperativos: () => api.get('/mi-negocio/operativa/procesos/'),
  getOrdenesOperativas: () => api.get('/mi-negocio/operativa/ordenes/'),
  getIncidenciasOperativas: () => api.get('/mi-negocio/operativa/incidencias/'),
  getSST: () => api.get('/mi-negocio/operativa/sst/'),

  // Gestión Comercial (Sales & Funnels)
  getComercialDashboard: () => api.get('/mi-negocio/comercial/main_config/dashboard/'),
  getSales: () => api.get('/mi-negocio/comercial/sales/orders/'),
  getFunnels: () => api.get('/mi-negocio/comercial/funnels/'),

  // Gestión Financiera (Tesorería y Caja)
  getFinancieraDashboard: () => api.get('/mi-negocio/financiera/dashboard/'),
  getFlujoCaja: () => api.get('/mi-negocio/financiera/flujo-caja/'),

  // Gestión Contable (Ledger Engine)
  getContabilidadGeneral: () => api.get('/mi-negocio/contable/contabilidad/asientos/'),
  getNomina: () => api.get('/mi-negocio/contable/nomina/'),
  getActivosFijos: () => api.get('/mi-negocio/contable/activos-fijos/'),

  // Gestión Archivística (Inmutabilidad SHA-256)
  getArchivisticaDocs: () => api.get('/mi-negocio/archivistica/documentos/'),
};
