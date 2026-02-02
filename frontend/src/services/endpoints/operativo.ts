import httpClient from '../index';

export const operativoEndpoints = {
  getPerfil: () => httpClient.get('/v1/mi-negocio/operativa/perfil/me/'),
  updatePerfil: (data: any) => httpClient.patch('/v1/mi-negocio/operativa/perfil/update-me/', data),
  getProductosServicios: () => httpClient.get('/v1/mi-negocio/operativa/productos-servicios/'),
  getReservas: () => httpClient.get('/v1/mi-negocio/operativa/reservas/'),
  getSST: () => httpClient.get('/v1/mi-negocio/operativa/sst/'),
  getNomina: () => httpClient.get('/v1/mi-negocio/operativa/nomina/'),
};
