// src/app/[locale]/(dashboard)/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
// ... (imports)

// --- Interfaces ---
// ... (existentes)
export interface PagoRecibido {
  id: number;
  factura: number;
  fecha_pago: string;
  monto: string;
}
export interface PagoRealizado {
  id: number;
  factura: number;
  fecha_pago: string;
  monto: string;
}
// ...

export function useMiNegocioApi() {
  // ... (setup y makeRequest sin cambios)

  // --- APIs existentes ---
  // ...

  // --- NUEVAS/MODIFICADAS APIs ---
  const getFacturaVenta = useCallback(async (id: number) => {
    return makeRequest(() => api.get<FacturaVenta>(`/api/v1/prestadores/mi-negocio/comercial/facturas-venta/${id}/`).then(res => res.data));
  }, [makeRequest]);

  const registrarPagoRecibido = useCallback(async (data: Omit<PagoRecibido, 'id'>) => {
    return makeRequest(() => api.post<PagoRecibido>('/api/v1/prestadores/mi-negocio/comercial/pagos-recibidos/', data).then(res => res.data), "Pago registrado con éxito.");
  }, [makeRequest]);

  const getFacturaProveedor = useCallback(async (id: number) => {
    return makeRequest(() => api.get<FacturaProveedor>(`/api/v1/prestadores/mi-negocio/compras/facturas-proveedor/${id}/`).then(res => res.data));
  }, [makeRequest]);

  const registrarPagoRealizado = useCallback(async (data: Omit<PagoRealizado, 'id'>) => {
    return makeRequest(() => api.post<PagoRealizado>('/api/v1/prestadores/mi-negocio/compras/pagos-realizados/', data).then(res => res.data), "Pago registrado con éxito.");
  }, [makeRequest]);


  return {
    // ... (funciones existentes)

    // --- NUEVAS funciones ---
    getFacturaVenta,
    registrarPagoRecibido,
    getFacturaProveedor,
    registrarPagoRealizado,
  };
}
