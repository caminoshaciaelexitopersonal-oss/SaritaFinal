import httpClient from '../index';

export const contableEndpoints = {
  getPlanCuentas: () => httpClient.get('/v1/mi-negocio/contable/contabilidad/planes-de-cuentas/'),
  getAsientosContables: () => httpClient.get('/v1/mi-negocio/contable/contabilidad/asientos/'),
  createAsientoContable: (data: any) => httpClient.post('/v1/mi-negocio/contable/contabilidad/asientos/', data),
  getBalances: () => httpClient.get('/v1/mi-negocio/contable/reportes/balance-general/'),
  getLibroMayor: () => httpClient.get('/v1/mi-negocio/contable/reportes/libro-mayor/'),
};
