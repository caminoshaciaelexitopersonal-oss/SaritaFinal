import httpClient from '../index';

export const financieroEndpoints = {
  getBankAccounts: () => httpClient.get('/v1/mi-negocio/financiera/cuentas-bancarias/'),
  getCashTransactions: () => httpClient.get('/v1/mi-negocio/financiera/transacciones-bancarias/'),
};
