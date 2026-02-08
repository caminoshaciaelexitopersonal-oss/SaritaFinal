import httpClient from '../httpClient';

export const nominaEndpoints = {
  getEmpleados: () => httpClient.get('/v1/mi-negocio/contable/nomina/empleados/'),
  getPlanillas: () => httpClient.get('/v1/mi-negocio/contable/nomina/planillas/'),
  createEmpleado: (data: any) => httpClient.post('/v1/mi-negocio/contable/nomina/empleados/', data),
  updateEmpleado: (id: number, data: any) => httpClient.patch(`/v1/mi-negocio/contable/nomina/empleados/${id}/`, data),
  deleteEmpleado: (id: number) => httpClient.delete(`/v1/mi-negocio/contable/nomina/empleados/${id}/`),
};
