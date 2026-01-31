import axios from 'axios';

const httpClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api',
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default httpClient;
