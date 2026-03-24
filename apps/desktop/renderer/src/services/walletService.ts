import { api } from './api';

/**
 * SARITA Wallet Service - Desktop (Vía 5)
 */
export const walletService = {
  getAccounts: () => api.get('/finance/wallet/accounts/'),
  getWalletById: (id: string) => api.get(`/finance/wallet/accounts/${id}/`),
  getTransactions: () => api.get('/finance/wallet/transactions/'),

  // Soporte para depósitos desde la terminal de escritorio
  deposit: (walletId: string, amount: number) =>
    api.post(`/finance/wallet/accounts/${walletId}/deposit/`, { amount }),

  // Retrocompatibilidad
  getBalance: () => api.get('/finance/wallet/accounts/'),
};
