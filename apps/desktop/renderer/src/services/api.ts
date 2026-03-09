import axios from 'axios';
import { tokenManager, httpClient } from '@sarita/shared-sdk';
import './storage';

/**
 * Cliente API para la versión de Escritorio.
 * Sincronizado con el Shared SDK y el backend central.
 */

const baseURL = (import.meta as any).env?.VITE_API_URL || 'https://api.sarita.travel/api/v1';

export const api = axios.create({
  baseURL,
  timeout: 15000,
});

// Sincronizar httpClient del SDK con la URL de Desktop
httpClient.defaults.baseURL = baseURL;

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
