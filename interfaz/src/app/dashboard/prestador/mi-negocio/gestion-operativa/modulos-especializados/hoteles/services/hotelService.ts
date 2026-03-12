import { httpClient } from '../../../../../../../../sarita-platform/shared-sdk/src/api/httpClient';

export const hotelService = {
  getRoomTypes: () => httpClient.get('/providers/tourism-services/'), // Unificado
  getRooms: () => httpClient.get('/mi-negocio/operativa/esp/hoteles/rooms/'),
  createRoom: (data: any) => httpClient.post('/mi-negocio/operativa/esp/hoteles/rooms/', data),
};
