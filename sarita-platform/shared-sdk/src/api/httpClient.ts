import axios from 'axios';
import { tokenManager } from '../auth/tokenManager';

/**
 * Cliente HTTP estandarizado de SARITA.
 * Implementa interceptores para autenticación JWT y manejo de errores centralizado.
 */

export const httpClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || process.env.API_URL || 'http://localhost:8000/api/v1',
  timeout: 10000,
});

httpClient.interceptors.request.use(async (config) => {
  const token = await tokenManager.getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Interceptor de respuesta para manejo de errores de clase mundial
httpClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // Manejo de Error 401 (Unauthorized) - Intento de Refresh Token
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      console.warn('SARITA API: Sesión expirada. Intentando refrescar token...');

      // Aquí se implementaría la lógica de refresh token real con el backend
      // Por ahora, si falla el refresh, limpiamos y redirigimos
      await tokenManager.clearToken();
    }

    // Manejo de Error 500+ (Server Errors)
    if (error.response?.status >= 500) {
      console.error('SARITA API: Error crítico en el servidor.', error.response.data);
    }

    // Manejo de Error de Conexión (Offline)
    if (!error.response) {
      console.warn('SARITA API: Error de red. El dispositivo podría estar offline.');
    }

    return Promise.reject(error);
  }
);

export default httpClient;
