import { api } from './api';

/**
 * SARITA Wallet Service
 * Gestión de saldos, recargas y transacciones integradas.
 */

export const walletService = {
  getBalance: () => api.get('/wallet/balance/'),
  topUp: (amount: number, method: string) => api.post('/wallet/topup/', { amount, method }),
  getTransactions: () => api.get('/wallet/transactions/'),
  pay: (amount: number, target: string, reason: string) =>
    api.post('/wallet/pay/', { amount, target, reason }),
};
