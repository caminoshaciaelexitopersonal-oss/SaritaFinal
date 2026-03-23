import { api } from '../../services/api';

/**
 * Gestión Comercial Mi Negocio
 */

export const commercialService = {
  // Operaciones
  getOperaciones: () => api.get('/mi-negocio/gestion_comercial/operaciones/'),
  createOperacion: (data: any) => api.post('/mi-negocio/gestion_comercial/operaciones/', data),
  getStats: () => api.get('/mi-negocio/gestion_comercial/operaciones/stats/'),

  // Clientes
  getClientes: () => api.get('/mi-negocio/gestion_comercial/clientes/'),
  createCliente: (data: any) => api.post('/mi-negocio/gestion_comercial/clientes/', data),

  // POS
  posVentaRapida: (data: any) => api.post('/mi-negocio/gestion_comercial/pos/', data),

// Reports
  getReports: () => api.get('/mi-negocio/gestion_comercial/reports/'),
  // Facturación DIAN
  triggerDian: (op_id: string) => api.post('/mi-negocio/gestion_comercial/facturas/trigger_dian/', { operacion_id: op_id }),
  getFactura: (cufe: string) => api.get(`/mi-negocio/gestion_comercial/facturas/?cufe=${cufe}`),
  downloadPDF: (cufe: string) => api.get(`/mi-negocio/gestion_comercial/facturas/${cufe}/pdf/`, { responseType: 'blob' }),
};

