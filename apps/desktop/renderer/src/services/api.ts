import axios from 'axios';
import { tokenManager } from '@sarita/shared-sdk';

/**
 * Cliente API para la versión de Escritorio.
 * Sincronizado con el Shared SDK y el backend central.
 */

export const api = axios.create({
  baseURL: 'https://api.sarita.travel/api/v1',
  timeout: 15000,
});

api.interceptors.request.use(async (config) => {
  const token = await tokenManager.getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      console.warn('Sesión expirada en Escritorio. Limpiando...');
      tokenManager.clearToken();
    }
    return Promise.reject(error);
  }
);
