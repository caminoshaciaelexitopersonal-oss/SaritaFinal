import { api } from '../../../../services/api';

export const specializedService = {
  getHotels: () => api.get('/mi-negocio/operativa/esp/hoteles/rooms/'),
  getRestaurants: () => api.get('/mi-negocio/operativa/esp/restaurantes/tables/'),
  getTours: () => api.get('/mi-negocio/operativa/esp/agencias/packages/'),
  getGuides: () => api.get('/mi-negocio/operativa/esp/guias/list/'),
  getTransport: () => api.get('/mi-negocio/operativa/esp/transporte/vehicles/'),
};
