import * as Location from 'expo-location';

/**
 * Hallazgo 11: Geofencing para prestadores.
 * Monitorea la ubicación del turista y activa el motor de geocercas del backend.
 */

export async function initGeofenceMonitoring() {
  const { status } = await Location.requestForegroundPermissionsAsync();
  if (status !== 'granted') {
    console.error('SARITA: Permiso de ubicación denegado');
    return false;
  }

  // En una implementación real, se iniciaría un rastreo en segundo plano
  // const { status: bgStatus } = await Location.requestBackgroundPermissionsAsync();

  const location = await Location.getCurrentPositionAsync({});
  console.log('SARITA Tourist Current Location:', location.coords);

  return location.coords;
}

export async function sendLocationToBackend(latitude: number, longitude: number, api: any) {
  try {
    // Envía la ubicación actual al motor de geofencing del backend
    const response = await api.post('/v1/geofence/update-location/', {
      latitude,
      longitude,
      timestamp: new Date().toISOString()
    });
    return response.data;
  } catch (error) {
    console.error('SARITA: Error al actualizar geolocalización:', error);
    return null;
  }
}
