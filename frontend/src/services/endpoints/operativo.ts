import httpClient from '../index';

export const operativoEndpoints = {
  getPerfil: () => httpClient.get('/v1/mi-negocio/operativa/perfil/me/'),
  updatePerfil: (data: any) => httpClient.patch('/v1/mi-negocio/operativa/perfil/update-me/', data),
  getClientes: () => httpClient.get('/v1/mi-negocio/operativa/clientes/'),
  getProductosServicios: () => httpClient.get('/v1/mi-negocio/operativa/productos-servicios/'),
  getReservas: () => httpClient.get('/v1/mi-negocio/operativa/reservas/'),
  getSST: () => httpClient.get('/v1/mi-negocio/operativa/sst/'),
  getNomina: () => httpClient.get('/v1/mi-negocio/operativa/nomina/'),

  // Módulos Especializados
  getHotelRoomTypes: () => httpClient.get('/v1/mi-negocio/operativa/hotel/room-types/'),
  getRestaurantTables: () => httpClient.get('/v1/mi-negocio/operativa/restaurante/tables/'),
  getVehicles: () => httpClient.get('/v1/mi-negocio/operativa/transporte/vehicles/'),
  getTours: () => httpClient.get('/v1/mi-negocio/operativa/guias/tours/'),
};
