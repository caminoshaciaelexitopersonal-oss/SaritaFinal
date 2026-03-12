import { StorageProvider, tokenManager, httpClient } from '@sarita/shared-sdk';
import * as SecureStore from 'expo-secure-store';
import Constants from 'expo-constants';
import { API_URL as FALLBACK_API_URL, API_V1_PREFIX } from '../config/env';

/**
 * Proveedor de Almacenamiento Seguro para Mobile (Expo)
 */
class MobileStorageProvider implements StorageProvider {
  async getItem(key: string): Promise<string | null> {
    return await SecureStore.getItemAsync(key);
  }
  async setItem(key: string, value: string): Promise<void> {
    await SecureStore.setItemAsync(key, value);
  }
  async removeItem(key: string): Promise<void> {
    await SecureStore.deleteItemAsync(key);
  }
}

// Inyectar el proveedor en el SDK
tokenManager.setStorage(new MobileStorageProvider());

// Configurar la URL base del cliente HTTP del SDK de forma segura
const BASE_API_URL = Constants.expoConfig?.extra?.apiUrl || FALLBACK_API_URL;
httpClient.defaults.baseURL = `${BASE_API_URL}${API_V1_PREFIX}`;

// Interceptores para manejo de tokens (Fase 4: Consolidación Mobile)
httpClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // Si recibimos 401 y no hemos reintentado ya
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const refreshToken = await SecureStore.getItemAsync('refresh_token');
        if (!refreshToken) throw new Error('No refresh token available');

        // Intentar renovar el token
        const response = await httpClient.post('/auth/token/refresh/', { refresh: refreshToken });
        const { access } = response.data;

        // Guardar nuevo token y reintentar
        await tokenManager.setToken(access);
        httpClient.defaults.headers.common['Authorization'] = `Bearer ${access}`;
        originalRequest.headers['Authorization'] = `Bearer ${access}`;

        return httpClient(originalRequest);
      } catch (refreshError) {
        console.error('Mobile Auth: Falló la renovación del token. Redirigiendo a Login...');
        await tokenManager.clearToken();
        // El estado de AuthContext debería limpiar el usuario y disparar la navegación al AuthNavigator
        return Promise.reject(refreshError);
      }
    }
    return Promise.reject(error);
  }
);

export { httpClient as api };
