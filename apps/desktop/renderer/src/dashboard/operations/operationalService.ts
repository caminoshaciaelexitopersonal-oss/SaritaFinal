import { httpClient } from '../../../../../sarita-platform/shared-sdk/src/api/httpClient';

export const operationalService = {
  // Unificación con prefijo 'esp' (Fase 8.5)
  getHotels: () => httpClient.get('/mi-negocio/operativa/esp/hoteles/rooms/'),
  getRestaurants: () => httpClient.get('/mi-negocio/operativa/esp/restaurantes/tables/'),
  getGuides: () => httpClient.get('/mi-negocio/operativa/esp/guias/list/'),
  getTransport: () => httpClient.get('/mi-negocio/operativa/esp/transporte/vehicles/'),

  // Perfil del prestador
  getProfile: () => httpClient.get('/providers/business-profiles/me/'),
};
