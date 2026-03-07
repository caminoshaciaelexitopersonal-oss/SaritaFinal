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
  (error) => {
    if (error.response?.status === 401) {
      console.warn('SARITA API: Sesión expirada o inválida. Limpiando token...');
      tokenManager.clearToken();
    }
    return Promise.reject(error);
  }
);

export default httpClient;
