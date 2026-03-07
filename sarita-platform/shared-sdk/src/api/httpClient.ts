import axios from 'axios';
import { tokenManager } from '../auth/tokenManager';

export const httpClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || process.env.API_URL || 'http://localhost:8000/api/v1',
  timeout: 10000,
});

httpClient.interceptors.request.use((config) => {
  const token = tokenManager.getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default httpClient;
