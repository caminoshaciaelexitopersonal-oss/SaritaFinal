import { api } from '../../services/api';

/**
 * SARITA Accounting Service (GESCONTABLE Mi Negocio)
 * Gestión de libros, PUC, balances y conciliación.
 */

export const accountingService = {
  // Plan de Cuentas Mi Negocio (/mi-negocio/contable/cuentas/)
  getCuentas: () => api.get('/mi-negocio/contable/cuentas/'),
  getCuentasTree: () => api.get('/mi-negocio/contable/cuentas/tree/'),
  createCuenta: (data: any) => api.post('/mi-negocio/contable/cuentas/', data),
  updateCuenta: (id: string, data: any) => api.put(`/mi-negocio/contable/cuentas/${id}/`, data),
  deleteCuenta: (id: string) => api.delete(`/mi-negocio/contable/cuentas/${id}/`),

  // Libro Diario y Asientos (legacy/ERP)
  getAccounts: () => api.get('/accounting/accounts/'),
  createAccount: (data: any) => api.post('/accounting/accounts/', data),
  getJournalEntries: (params = {}) => api.get('/accounting/journal/', { params }),
  createJournalEntry: (data: any) => api.post('/accounting/journal/', data),
  getLedger: (accountId: string) => api.get(`/accounting/ledger/${accountId}/`),
  getBalanceSheet: () => api.get('/accounting/balance-sheet/'),
  getIncomeStatement: () => api.get('/accounting/income-statement/'),
  getReconciliationData: () => api.get('/accounting/reconciliation/'),
  performReconciliation: (data: any) => api.post('/accounting/reconcile/', data),
  getAccountingAudit: () => api.get('/accounting/audit-log/'),
};

