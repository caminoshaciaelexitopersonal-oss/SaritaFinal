// src/app/[locale]/(dashboard)/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
import api from '@/services/api'; // Importa la instancia de Axios configurada
import { useAuth } from '@/contexts/AuthContext';
import { toast } from 'react-toastify';

// --- Tipos de Datos ---
interface PerfilData {
  nombre_comercial: string;
  telefono_principal: string;
  email_comercial: string;
  direccion: string;
  descripcion_corta: string;
}

export interface Cliente {
  id: number;
  nombre: string;
  email: string;
  telefono: string | null;
}

export function useMiNegocioApi() {
  const { token } = useAuth();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const makeRequest = useCallback(async <T>(requestFunc: () => Promise<T>, successMessage?: string, errorMessage?: string): Promise<T | null> => {
    if (!token) {
      setError("No autenticado.");
      return null;
    }

    setIsLoading(true);
    setError(null);
    try {
      const result = await requestFunc();
      if (successMessage) toast.success(successMessage);
      return result;
    } catch (err: any) {
      const msg = err.response?.data?.detail || errorMessage || "Ocurrió un error.";
      setError(msg);
      toast.error(msg);
      return null;
    } finally {
      setIsLoading(false);
    }
  }, [token]);

  // --- API de Perfil ---
  const getPerfil = useCallback(async () => {
    return makeRequest(() => api.get<PerfilData>('/prestadores/mi-negocio/operativa/genericos/perfil/me/').then(res => res.data), undefined, "No se pudo cargar el perfil.");
  }, [makeRequest]);

  const updatePerfil = useCallback(async (data: Partial<PerfilData>) => {
    return makeRequest(() => api.patch<PerfilData>('/prestadores/mi-negocio/operativa/genericos/perfil/update-me/', data).then(res => res.data), "Perfil actualizado con éxito.", "Error al actualizar el perfil.");
  }, [makeRequest]);

  // --- API de Clientes (CRM) ---
  const getClientes = useCallback(async () => {
    return makeRequest(() => api.get<Cliente[]>('/prestadores/mi-negocio/operativa/genericos/clientes/').then(res => res.data), undefined, "No se pudo cargar la lista de clientes.");
  }, [makeRequest]);

  const createCliente = useCallback(async (clienteData: Omit<Cliente, 'id'>) => {
    return makeRequest(() => api.post<Cliente>('/prestadores/mi-negocio/operativa/genericos/clientes/', clienteData).then(res => res.data), "Cliente creado con éxito.", "Error al crear el cliente.");
  }, [makeRequest]);

  const updateCliente = useCallback(async (id: number, clienteData: Partial<Omit<Cliente, 'id'>>) => {
    return makeRequest(() => api.patch<Cliente>(`/prestadores/mi-negocio/operativa/genericos/clientes/${id}/`, clienteData).then(res => res.data), "Cliente actualizado con éxito.", "Error al actualizar el cliente.");
  }, [makeRequest]);

  const deleteCliente = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/prestadores/mi-negocio/operativa/genericos/clientes/${id}/`), "Cliente eliminado con éxito.", "Error al eliminar el cliente.");
  }, [makeRequest]);

  return {
    isLoading,
    error,
    getPerfil,
    updatePerfil,
    getClientes,
    createCliente,
    updateCliente,
    deleteCliente
  };
}
