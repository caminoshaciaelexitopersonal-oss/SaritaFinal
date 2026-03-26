import { api } from './api';

/**
 * SARITA Wallet Service
 * Gestión de saldos, recargas y transacciones integradas.
 */

export const walletService = {
  // Endpoints normalizados (Vía 5)
  getAccounts: () => api.get('/finance/wallet/accounts/'),
  getWalletById: (id: string) => api.get(`/finance/wallet/accounts/${id}/`),
  deposit: (id: string, amount: number) => api.post(`/finance/wallet/accounts/${id}/deposit/`, { amount }),
  getTransactions: () => api.get('/finance/wallet/transactions/'),

  // Retrocompatibilidad (Legacy aliases)
  getBalance: () => api.get('/finance/wallet/accounts/'),
  topUp: (amount: number, method: string) => api.post('/finance/wallet/accounts/deposit/', { amount, method }),
};
