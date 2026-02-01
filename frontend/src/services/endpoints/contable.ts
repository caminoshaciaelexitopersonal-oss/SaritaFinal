import httpClient from '../index';

export const contableEndpoints = {
  getPlanCuentas: () => httpClient.get('/v1/mi-negocio/contable/contabilidad/plan-cuentas/'),
  getAsientosContables: () => httpClient.get('/v1/mi-negocio/contable/contabilidad/asientos-contables/'),
  createAsientoContable: (data: any) => httpClient.post('/v1/mi-negocio/contable/contabilidad/asientos-contables/', data),
  getBalances: () => httpClient.get('/v1/mi-negocio/contable/reportes/balance-general/'),
  getLibroMayor: () => httpClient.get('/v1/mi-negocio/contable/reportes/libro-mayor/'),
};
