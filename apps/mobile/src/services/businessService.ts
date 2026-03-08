import { api } from './api';

/**
 * SARITA Business ERP Service (Mi Negocio)
 * Gestión comercial, operativa, financiera y contable para prestadores.
 */

export const businessService = {
  getDashboard: () => api.get('/business/dashboard/'),
  getServices: () => api.get('/business/services/'),
  getOrders: () => api.get('/business/orders/'),
  getFinanceReport: () => api.get('/business/finance/report/'),
  getAccountingBook: () => api.get('/business/accounting/ledger/'),
  getDocuments: () => api.get('/business/documents/'),
};
