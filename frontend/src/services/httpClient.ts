import axios from 'axios';
import { setupInterceptors } from './interceptors';

const httpClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api',
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Apply systemic interceptors
setupInterceptors(httpClient);

export default httpClient;
