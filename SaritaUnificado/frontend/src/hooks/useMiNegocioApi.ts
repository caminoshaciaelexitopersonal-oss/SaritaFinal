import { useState, useCallback } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';

/**
 * Hook placeholder para centralizar la lógica de la API del panel "Mi Negocio".
 * En el futuro, puede manejar estados de carga globales, caching, y sincronización.
 */
export const useMiNegocioApi = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const get = useCallback(async <T>(url: string): Promise<T | null> => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await api.get<T>(url);
      return response.data;
    } catch (err) {
      setError(err as Error);
      toast.error(`Error al obtener datos de ${url}`);
      return null;
    } finally {
      setIsLoading(false);
    }
  }, []);

  const post = useCallback(async <T>(url: string, data: any): Promise<T | null> => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await api.post<T>(url, data);
      toast.success('¡Recurso creado con éxito!');
      return response.data;
    } catch (err) {
      setError(err as Error);
      toast.error(`Error al crear recurso en ${url}`);
      return null;
    } finally {
      setIsLoading(false);
    }
  }, []);

  return { isLoading, error, get, post };
};