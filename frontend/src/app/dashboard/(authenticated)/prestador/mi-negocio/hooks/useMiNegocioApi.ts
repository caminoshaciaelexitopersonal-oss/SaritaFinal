// src/app/[locale]/(dashboard)/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
import api from '@/services/api';
import { useAuth } from '@/contexts/AuthContext';
import { toast } from 'react-toastify';

// --- Interfaces existentes ---
export interface Cliente {
  id: number;
  nombre: string;
  identificacion?: string;
  email?: string;
  telefono?: string;
  direccion?: string;
  is_active: boolean;
}
export interface ItemFactura { /* ... */ }
export interface FacturaVenta { /* ... */ }
export interface ChartOfAccount { /* ... */ }
export interface JournalEntry { /* ... */ }
export interface BankAccount { /* ... */ }
export interface CashTransaction { /* ... */ }

// --- NUEVAS Interfaces del Ciclo de Compras ---
export interface Proveedor {
  id: number;
  nombre: string;
  identificacion?: string;
  email?: string;
  telefono?: string;
  direccion?: string;
  is_active: boolean;
}

export interface ItemFacturaProveedor {
  id: number;
  descripcion: string;
  cantidad: number;
  costo_unitario: string; // Decimal
}

export interface FacturaProveedor {
  id: number;
  proveedor: number; // ID
  proveedor_nombre?: string;
  fecha_emision: string;
  fecha_vencimiento: string;
  total: string;
  estado: 'PENDIENTE' | 'PAGADA' | 'VENCIDA';
  items: ItemFacturaProveedor[];
}


export function useMiNegocioApi() {
  const { token } = useAuth();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const makeRequest = useCallback(async <T>(requestFunc: () => Promise<T>, successMessage?: string, errorMessage?: string): Promise<T | null> => {
    // ... (lógica de makeRequest sin cambios) ...
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
      const msg = err.response?.data?.detail || Object.values(err.response?.data || {}).join(', ') || errorMessage || "Ocurrió un error.";
      setError(msg);
      toast.error(msg);
      return null;
    } finally {
      setIsLoading(false);
    }
  }, [token]);

  // --- APIs existentes (Comercial, Contabilidad, etc.) ---
  const getClientes = useCallback(async () => {
    return makeRequest(() => api.get<Cliente[]>('/api/v1/prestadores/mi-negocio/comercial/clientes/').then(res => res.data));
  }, [makeRequest]);
  const createCliente = useCallback(async (data: Omit<Cliente, 'id'>) => { /* ... */ return makeRequest(() => api.post<Cliente>('/api/v1/prestadores/mi-negocio/comercial/clientes/', data).then(res => res.data), "Cliente creado con éxito."); }, [makeRequest]);
  const updateCliente = useCallback(async (id: number, data: Partial<Omit<Cliente, 'id'>>) => { /* ... */ return makeRequest(() => api.patch<Cliente>(`/api/v1/prestadores/mi-negocio/comercial/clientes/${id}/`, data).then(res => res.data), "Cliente actualizado con éxito."); }, [makeRequest]);
  const deleteCliente = useCallback(async (id: number) => { /* ... */ return makeRequest(() => api.delete(`/api/v1/prestadores/mi-negocio/comercial/clientes/${id}/`), "Cliente eliminado con éxito."); }, [makeRequest]);
  const getFacturasVenta = useCallback(async () => { /* ... */ return makeRequest(() => api.get<FacturaVenta[]>('/api/v1/prestadores/mi-negocio/comercial/facturas-venta/').then(res => res.data)); }, [makeRequest]);
  const createFacturaVenta = useCallback(async (data: any) => { /* ... */ return makeRequest(() => api.post<FacturaVenta>('/api/v1/prestadores/mi-negocio/comercial/facturas-venta/', data).then(res => res.data), "Factura creada con éxito."); }, [makeRequest]);
  // ... (otras funciones existentes)

  // --- NUEVAS APIs del Ciclo de Compras ---
  const getProveedores = useCallback(async () => {
    return makeRequest(() => api.get<Proveedor[]>('/api/v1/prestadores/mi-negocio/compras/proveedores/').then(res => res.data));
  }, [makeRequest]);

  const createProveedor = useCallback(async (data: Omit<Proveedor, 'id'>) => {
    return makeRequest(() => api.post<Proveedor>('/api/v1/prestadores/mi-negocio/compras/proveedores/', data).then(res => res.data), "Proveedor creado con éxito.");
  }, [makeRequest]);

  const updateProveedor = useCallback(async (id: number, data: Partial<Omit<Proveedor, 'id'>>) => {
    return makeRequest(() => api.patch<Proveedor>(`/api/v1/prestadores/mi-negocio/compras/proveedores/${id}/`, data).then(res => res.data), "Proveedor actualizado con éxito.");
  }, [makeRequest]);

  const deleteProveedor = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/api/v1/prestadores/mi-negocio/compras/proveedores/${id}/`), "Proveedor eliminado con éxito.");
  }, [makeRequest]);

  const getFacturasProveedor = useCallback(async () => {
    return makeRequest(() => api.get<FacturaProveedor[]>('/api/v1/prestadores/mi-negocio/compras/facturas-proveedor/').then(res => res.data));
  }, [makeRequest]);

  const createFacturaProveedor = useCallback(async (data: any) => {
    return makeRequest(() => api.post<FacturaProveedor>('/api/v1/prestadores/mi-negocio/compras/facturas-proveedor/', data).then(res => res.data), "Factura de proveedor creada con éxito.");
  }, [makeRequest]);


  return {
    isLoading,
    error,
    // ... (funciones existentes)
    getClientes, createCliente, updateCliente, deleteCliente, getFacturasVenta, createFacturaVenta,

    // --- NUEVAS funciones ---
    getProveedores,
    createProveedor,
    updateProveedor,
    deleteProveedor,
    getFacturasProveedor,
    createFacturaProveedor,
  };
}
