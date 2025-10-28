// src/app/[locale]/(dashboard)/prestador/mi-negocio/hooks/useMiNegocioApi.ts
// ... (imports y interfaces existentes)

// --- NUEVAS Interfaces de Activos Fijos ---
export interface ActivoFijo {
  id: number;
  nombre: string;
  fecha_adquisicion: string;
  costo_inicial: string;
  valor_residual: string;
  vida_util_meses: number;
  depreciacion_acumulada: string;
  valor_en_libros: string;
}

export interface RegistroDepreciacion {
  id: number;
  fecha: string;
  monto: string;
}


export function useMiNegocioApi() {
  // ... (setup y makeRequest sin cambios)

  // --- APIs existentes ---
  // ...

  // --- NUEVAS APIs de Activos Fijos ---
  const getActivosFijos = useCallback(async () => {
    return makeRequest(() => api.get<ActivoFijo[]>('/api/v1/prestadores/mi-negocio/activos/activos-fijos/').then(res => res.data));
  }, [makeRequest]);

  const createActivoFijo = useCallback(async (data: Omit<ActivoFijo, 'id' | 'depreciacion_acumulada' | 'valor_en_libros'>) => {
    return makeRequest(() => api.post<ActivoFijo>('/api/v1/prestadores/mi-negocio/activos/activos-fijos/', data).then(res => res.data), "Activo creado.");
  }, [makeRequest]);

  const getHistorialDepreciacion = useCallback(async (activoId: number) => {
    return makeRequest(() => api.get<RegistroDepreciacion[]>(`/api/v1/prestadores/mi-negocio/activos/activos-fijos/${activoId}/depreciaciones/`).then(res => res.data));
  }, [makeRequest]);


  return {
    // ... (funciones existentes)

    // --- NUEVAS funciones ---
    getActivosFijos,
    createActivoFijo,
    getHistorialDepreciacion,
  };
}
