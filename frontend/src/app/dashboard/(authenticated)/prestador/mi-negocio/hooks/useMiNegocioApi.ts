// src/app/[locale]/(dashboard)/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
import api from '@/services/api';
// ... (imports)

// --- Interfaces ---
// ... (interfaces existentes)
export interface FacturaVenta {
  // ...
  centro_costo?: number;
}
export interface FacturaProveedor {
  // ...
  centro_costo?: number;
}
export interface CostCenter { // Ya existe pero la redefino para claridad
  id: number;
  code: string;
  name: string;
}
// ... (resto de interfaces)

export function useMiNegocioApi() {
  // ... (setup sin cambios)

  // --- Lógica de makeRequest sin cambios ---

  // --- APIs existentes ---
  // ... (APIs de Comercial, Compras, etc.)

  // --- NUEVAS APIs de Centros de Costo ---
  const getCostCenters = useCallback(async () => {
    return makeRequest(() => api.get<CostCenter[]>('/api/v1/prestadores/mi-negocio/contable/cost-centers/').then(res => res.data));
  }, [makeRequest]);

  const createCostCenter = useCallback(async (data: Omit<CostCenter, 'id'>) => {
    return makeRequest(() => api.post<CostCenter>('/api/v1/prestadores/mi-negocio/contable/cost-centers/', data).then(res => res.data), "Centro de Costo creado.");
  }, [makeRequest]);

  const updateCostCenter = useCallback(async (id: number, data: Partial<Omit<CostCenter, 'id'>>) => {
    return makeRequest(() => api.patch<CostCenter>(`/api/v1/prestadores/mi-negocio/contable/cost-centers/${id}/`, data).then(res => res.data), "Centro de Costo actualizado.");
  }, [makeRequest]);

  const deleteCostCenter = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/api/v1/prestadores/mi-negocio/contable/cost-centers/${id}/`), "Centro de Costo eliminado.");
  }, [makeRequest]);


  return {
    // ... (funciones existentes)

    // --- NUEVAS funciones ---
    getCostCenters,
    createCostCenter,
    updateCostCenter,
    deleteCostCenter,
  };
}
