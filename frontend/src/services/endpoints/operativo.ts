import httpClient from '../index';

export const operativoEndpoints = {
  getPerfil: () => httpClient.get('/v1/mi-negocio/operativa/perfil/me/'),
  updatePerfil: (data: any) => httpClient.patch('/v1/mi-negocio/operativa/perfil/update-me/', data),
  getClientes: () => httpClient.get('/v1/mi-negocio/operativa/clientes/'),
  getProductosServicios: () => httpClient.get('/v1/mi-negocio/operativa/productos-servicios/'),
  getReservas: () => httpClient.get('/v1/mi-negocio/operativa/reservas/'),
  getSST: () => httpClient.get('/v1/mi-negocio/operativa/sst/'),
  getSSTRisks: () => httpClient.get('/v1/mi-negocio/operativa/sst/matriz-riesgos/'),
  getSSTIncidents: () => httpClient.get('/v1/mi-negocio/operativa/sst/incidentes-laborales/'),
  reportSSTIncident: (data: any) => httpClient.post('/v1/mi-negocio/operativa/sst/incidentes-laborales/', data),
  getNomina: () => httpClient.get('/v1/mi-negocio/operativa/nomina/'),

  // Módulos Especializados
  getHotelRoomTypes: () => httpClient.get('/v1/mi-negocio/operativa/hotel/room-types/'),
  getRestaurantTables: () => httpClient.get('/v1/mi-negocio/operativa/restaurante/tables/'),
  getVehicles: () => httpClient.get('/v1/mi-negocio/operativa/transporte/vehicles/'),
  getTours: () => httpClient.get('/v1/mi-negocio/operativa/guias/tours/'),
  getProcesosOperativos: () => httpClient.get('/v1/mi-negocio/operativa/procesos/'),
  updateProcesoEstado: (id: string, nuevo_estado: string) => httpClient.post(`/v1/mi-negocio/operativa/procesos/${id}/avanzar_estado/`, { nuevo_estado }),

  // Motor Operativo Genérico (Fase 3)
  getOrdenesOperativas: () => httpClient.get('/v1/mi-negocio/operativa/ordenes/'),
  updateOrdenEstado: (id: string, nuevo_estado: string, motivo: string) => httpClient.post(`/v1/mi-negocio/operativa/ordenes/${id}/cambiar-estado/`, { nuevo_estado, motivo }),
  reportIncidente: (data: any) => httpClient.post('/v1/mi-negocio/operativa/incidencias/', data),
};
