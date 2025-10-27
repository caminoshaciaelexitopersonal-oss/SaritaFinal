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

export interface ProductoServicio {
  id: number;
  nombre: string;
  descripcion: string;
  precio: number;
  activo: boolean;
}

export interface Inventario {
  id: number;
  nombre: string;
  cantidad: number;
  unidad: string;
}

export interface Costo {
  id: number;
  descripcion: string;
  valor: number;
  frecuencia: string;
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
    return makeRequest(() => api.get<PerfilData>('/api/v1/mi-negocio/operativa/genericos/perfil/me/').then(res => res.data), undefined, "No se pudo cargar el perfil.");
  }, [makeRequest]);

  const updatePerfil = useCallback(async (data: Partial<PerfilData>) => {
    return makeRequest(() => api.patch<PerfilData>('/api/v1/mi-negocio/operativa/genericos/perfil/update-me/', data).then(res => res.data), "Perfil actualizado con éxito.", "Error al actualizar el perfil.");
  }, [makeRequest]);

  // --- API de Clientes (CRM) ---
  const getClientes = useCallback(async () => {
    return makeRequest(() => api.get<Cliente[]>('/api/v1/mi-negocio/operativa/genericos/clientes/').then(res => res.data), undefined, "No se pudo cargar la lista de clientes.");
  }, [makeRequest]);

  const createCliente = useCallback(async (clienteData: Omit<Cliente, 'id'>) => {
    return makeRequest(() => api.post<Cliente>('/api/v1/mi-negocio/operativa/genericos/clientes/', clienteData).then(res => res.data), "Cliente creado con éxito.", "Error al crear el cliente.");
  }, [makeRequest]);

  const updateCliente = useCallback(async (id: number, clienteData: Partial<Omit<Cliente, 'id'>>) => {
    return makeRequest(() => api.patch<Cliente>(`/api/v1/mi-negocio/operativa/genericos/clientes/${id}/`, clienteData).then(res => res.data), "Cliente actualizado con éxito.", "Error al actualizar el cliente.");
  }, [makeRequest]);

  const deleteCliente = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/api/v1/mi-negocio/operativa/genericos/clientes/${id}/`), "Cliente eliminado con éxito.", "Error al eliminar el cliente.");
  }, [makeRequest]);

  // --- API de Productos/Servicios ---
  const getProductosServicios = useCallback(async () => {
    return makeRequest(() => api.get<ProductoServicio[]>('/api/v1/mi-negocio/operativa/genericos/productos-servicios/').then(res => res.data), undefined, "No se pudo cargar la lista de productos/servicios.");
  }, [makeRequest]);

  const createProductoServicio = useCallback(async (data: Omit<ProductoServicio, 'id'>) => {
    return makeRequest(() => api.post<ProductoServicio>('/api/v1/mi-negocio/operativa/genericos/productos-servicios/', data).then(res => res.data), "Producto/Servicio creado con éxito.", "Error al crear el producto/servicio.");
  }, [makeRequest]);

  const updateProductoServicio = useCallback(async (id: number, data: Partial<Omit<ProductoServicio, 'id'>>) => {
    return makeRequest(() => api.patch<ProductoServicio>(`/api/v1/mi-negocio/operativa/genericos/productos-servicios/${id}/`, data).then(res => res.data), "Producto/Servicio actualizado con éxito.", "Error al actualizar el producto/servicio.");
  }, [makeRequest]);

  const deleteProductoServicio = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/api/v1/mi-negocio/operativa/genericos/productos-servicios/${id}/`), "Producto/Servicio eliminado con éxito.", "Error al eliminar el producto/servicio.");
  }, [makeRequest]);

  // --- API de Inventario ---
  const getInventario = useCallback(async () => {
    return makeRequest(() => api.get<Inventario[]>('/api/v1/mi-negocio/operativa/genericos/inventario/').then(res => res.data), undefined, "No se pudo cargar el inventario.");
  }, [makeRequest]);

  const createItemInventario = useCallback(async (data: Omit<Inventario, 'id'>) => {
    return makeRequest(() => api.post<Inventario>('/api/v1/mi-negocio/operativa/genericos/inventario/', data).then(res => res.data), "Ítem de inventario creado.", "Error al crear el ítem.");
  }, [makeRequest]);

  const updateItemInventario = useCallback(async (id: number, data: Partial<Omit<Inventario, 'id'>>) => {
    return makeRequest(() => api.patch<Inventario>(`/api/v1/mi-negocio/operativa/genericos/inventario/${id}/`, data).then(res => res.data), "Ítem de inventario actualizado.", "Error al actualizar el ítem.");
  }, [makeRequest]);

  const deleteItemInventario = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/api/v1/mi-negocio/operativa/genericos/inventario/${id}/`), "Ítem de inventario eliminado.", "Error al eliminar el ítem.");
  }, [makeRequest]);

  // --- API de Costos ---
  const getCostos = useCallback(async () => {
    return makeRequest(() => api.get<Costo[]>('/api/v1/mi-negocio/operativa/genericos/costos/').then(res => res.data), undefined, "No se pudo cargar la lista de costos.");
  }, [makeRequest]);

  const createCosto = useCallback(async (data: Omit<Costo, 'id'>) => {
    return makeRequest(() => api.post<Costo>('/api/v1/mi-negocio/operativa/genericos/costos/', data).then(res => res.data), "Costo creado con éxito.", "Error al crear el costo.");
  }, [makeRequest]);

  const updateCosto = useCallback(async (id: number, data: Partial<Omit<Costo, 'id'>>) => {
    return makeRequest(() => api.patch<Costo>(`/api/v1/mi-negocio/operativa/genericos/costos/${id}/`, data).then(res => res.data), "Costo actualizado con éxito.", "Error al actualizar el costo.");
  }, [makeRequest]);

  const deleteCosto = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/api/v1/mi-negocio/operativa/genericos/costos/${id}/`), "Costo eliminado con éxito.", "Error al eliminar el costo.");
  }, [makeRequest]);

  return {
    isLoading,
    error,
    getPerfil,
    updatePerfil,
    getClientes,
    createCliente,
    updateCliente,
    deleteCliente,
    getProductosServicios,
    createProductoServicio,
    updateProductoServicio,
    deleteProductoServicio,
    getInventario,
    createItemInventario,
    updateItemInventario,
    deleteItemInventario,
    getCostos,
    createCosto,
    updateCosto,
    deleteCosto,
  };
}
