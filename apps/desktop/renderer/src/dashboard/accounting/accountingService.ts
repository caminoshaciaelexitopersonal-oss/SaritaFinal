import { api } from '../../services/api';

/**
 * SARITA Accounting Service (GESCONTABLE)
 * Gestión de libros, asientos, balances y conciliación.
 */

export const accountingService = {
  // Plan de Cuentas
  getAccounts: () => api.get('/accounting/accounts/'),
  createAccount: (data: any) => api.post('/accounting/accounts/', data),

  // Libro Diario y Asientos
  getJournalEntries: (params = {}) => api.get('/accounting/journal/', { params }),
  createJournalEntry: (data: any) => api.post('/accounting/journal/', data),

  // Libro Mayor
  getLedger: (accountId: string) => api.get(`/accounting/ledger/${accountId}/`),

  // Estados Financieros
  getBalanceSheet: () => api.get('/accounting/balance-sheet/'),
  getIncomeStatement: () => api.get('/accounting/income-statement/'),

  // Conciliación
  getReconciliationData: () => api.get('/accounting/reconciliation/'),
  performReconciliation: (data: any) => api.post('/accounting/reconcile/', data),

  // Auditoría
  getAccountingAudit: () => api.get('/accounting/audit-log/'),
};
