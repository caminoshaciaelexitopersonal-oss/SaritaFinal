// SaritaUnificado/frontend/src/hooks/useApi.ts
import { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from '@/contexts/AuthContext'; // Asumiendo que el contexto de autenticación se llama así

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1/prestadores/mi-negocio/',
});

api.interceptors.request.use(config => {
  const token = localStorage.getItem('auth_token');
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

export const useApi = (endpoint) => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await api.get(endpoint);
      setData(response.data.results); // Asumiendo paginación de DRF
      setError(null);
    } catch (e) {
      setError(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [endpoint]);

  const createItem = async (item) => {
    try {
      const response = await api.post(endpoint, item);
      setData([...data, response.data]);
    } catch (e) {
      // Manejar error
      console.error("Error creating item:", e);
    }
  };

  const updateItem = async (id, updatedItem) => {
    try {
      const response = await api.put(`${endpoint}${id}/`, updatedItem);
      setData(data.map(item => (item.id === id ? response.data : item)));
    } catch (e) {
      console.error("Error updating item:", e);
    }
  };

  const deleteItem = async (id) => {
    try {
      await api.delete(`${endpoint}${id}/`);
      setData(data.filter(item => item.id !== id));
    } catch (e) {
      console.error("Error deleting item:", e);
    }
  };

  return { data, loading, error, fetchData, createItem, updateItem, deleteItem };
};
