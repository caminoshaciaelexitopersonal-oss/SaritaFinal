// src/app/[locale]/(dashboard)/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
import api from '@/services/api';
// ... (imports)

// --- INTERFACES ---
export interface Cliente { /* ... */ }
export interface FacturaVenta { /* ... */ }
export interface Proveedor { /* ... */ }
export interface FacturaProveedor { /* ... */ }
export interface CostCenter { /* ... */ }
export interface Producto { /* ... */ }
export interface MovimientoInventario { /* ... */ }
// ... (y todas las demás)

export function useMiNegocioApi() {
  const { token } = useAuth();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const makeRequest = useCallback(async <T>(requestFunc: () => Promise<T>, successMessage?: string, errorMessage?: string): Promise<T | null> => {
    // ... (lógica de makeRequest)
  }, [token]);

  // --- API Comercial ---
  const getClientes = useCallback(async () => { /* ... */ });
  const createCliente = useCallback(async (data: any) => { /* ... */ });
  const updateCliente = useCallback(async (id: number, data: any) => { /* ... */ });
  const deleteCliente = useCallback(async (id: number) => { /* ... */ });
  const getFacturasVenta = useCallback(async () => { /* ... */ });
  const createFacturaVenta = useCallback(async (data: any) => { /* ... */ });

  // --- API Compras ---
  const getProveedores = useCallback(async () => { /* ... */ });
  const createProveedor = useCallback(async (data: any) => { /* ... */ });
  const updateProveedor = useCallback(async (id: number, data: any) => { /* ... */ });
  const deleteProveedor = useCallback(async (id: number) => { /* ... */ });
  const getFacturasProveedor = useCallback(async () => { /* ... */ });
  const createFacturaProveedor = useCallback(async (data: any) => { /* ... */ });

  // --- API Contabilidad ---
  const getCostCenters = useCallback(async () => { /* ... */ });
  const createCostCenter = useCallback(async (data: any) => { /* ... */ });
  // ... (otras)

  // --- API Inventario ---
  const getProductos = useCallback(async () => { /* ... */ });
  const createProducto = useCallback(async (data: any) => { /* ... */ });
  const getKardex = useCallback(async (id: number) => { /* ... */ });

  return {
    isLoading, error,
    getClientes, createCliente, updateCliente, deleteCliente,
    getFacturasVenta, createFacturaVenta,
    getProveedores, createProveedor, updateProveedor, deleteProveedor,
    getFacturasProveedor, createFacturaProveedor,
    getCostCenters, createCostCenter,
    getProductos, createProducto, getKardex,
    // ... (todas las demás funciones)
  };
}
