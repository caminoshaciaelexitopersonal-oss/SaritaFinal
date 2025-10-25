// src/app/[locale]/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
import axios from 'axios';
import { useAuth } from '@/contexts/AuthContext';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

// Definición de un tipo genérico para los datos
type ApiData = Record<string, any>;

interface UseApiReturn<T> {
  data: T | null;
  error: string | null;
  isLoading: boolean;
  fetchData: (endpoint: string) => Promise<void>;
  createData: (endpoint: string, newData: ApiData) => Promise<T | null>;
  updateData: (endpoint: string, updatedData: ApiData) => Promise<T | null>;
  deleteData: (endpoint: string) => Promise<boolean>;
}

export function useMiNegocioApi<T extends ApiData>(): UseApiReturn<T> {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const { getAccessToken } = useAuth();

  const getHeaders = useCallback(() => {
    const token = getAccessToken();
    return {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    };
  }, [getAccessToken]);

  const fetchData = useCallback(async (endpoint: string) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await axios.get(`${API_BASE_URL}/prestadores/mi-negocio/${endpoint}`, {
        headers: getHeaders(),
      });
      setData(response.data as T);
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message || 'Ocurrió un error desconocido');
    } finally {
      setIsLoading(false);
    }
  }, [getHeaders]);

  const createData = useCallback(async (endpoint: string, newData: ApiData): Promise<T | null> => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await axios.post(`${API_BASE_URL}/prestadores/mi-negocio/${endpoint}`, newData, {
        headers: getHeaders(),
      });
      setData(response.data as T);
      return response.data as T;
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message || 'Error al crear el recurso');
      return null;
    } finally {
      setIsLoading(false);
    }
  }, [getHeaders]);

  const updateData = useCallback(async (endpoint: string, updatedData: ApiData): Promise<T | null> => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await axios.put(`${API_BASE_URL}/prestadores/mi-negocio/${endpoint}`, updatedData, {
        headers: getHeaders(),
      });
      setData(response.data as T);
      return response.data as T;
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message || 'Error al actualizar el recurso');
      return null;
    } finally {
      setIsLoading(false);
    }
  }, [getHeaders]);

  const deleteData = useCallback(async (endpoint: string): Promise<boolean> => {
    setIsLoading(true);
    setError(null);
    try {
      await axios.delete(`${API_BASE_URL}/prestadores/mi-negocio/${endpoint}`, {
        headers: getHeaders(),
      });
      setData(null);
      return true;
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message || 'Error al eliminar el recurso');
      return false;
    } finally {
      setIsLoading(false);
    }
  }, [getHeaders]);


  return { data, error, isLoading, fetchData, createData, updateData, deleteData };
}
