// src/app/[locale]/(dashboard)/prestador/mi-negocio/hooks/useMiNegocioApi.ts
// ... (imports y interfaces existentes)

// --- Interfaces de Ventas ---
export interface ItemFactura {
  id?: number;
  producto: number;
  producto_nombre?: string;
  cantidad: number;
  precio_unitario: string;
  total_item?: string;
}

export interface FacturaVenta {
  id: number;
  cliente: number;
  cliente_nombre: string;
  fecha_emision: string;
  fecha_vencimiento: string;
  subtotal: string;
  impuestos: string;
  total: string;
  pagado: string;
  estado: 'BORRADOR' | 'EMITIDA' | 'PAGADA' | 'VENCIDA' | 'ANULADA';
  estado_display: string;
  items: ItemFactura[];
}

export type CreateFacturaVentaDTO = Omit<FacturaVenta, 'id' | 'cliente_nombre' | 'subtotal' | 'impuestos' | 'total' | 'pagado' | 'estado_display'> & {
  items: Omit<ItemFactura, 'id' | 'producto_nombre' | 'total_item'>[];
};


// --- NUEVAS Interfaces de Nómina ---
export interface Empleado {
  id: number;
  nombre: string;
  apellido: string;
  tipo_documento: 'CC' | 'CE' | 'PA';
  numero_documento: string;
  fecha_nacimiento: string;
  fecha_contratacion: string;
  salario_base: string;
  activo: boolean;
}

export type CreateEmpleadoDTO = Omit<Empleado, 'id'>;

export interface ConceptoNomina {
  id: number;
  codigo: string;
  descripcion: string;
  tipo: 'ingreso' | 'deduccion';
  es_fijo: boolean;
  valor: string;
}

export interface DetalleNomina {
  id: number;
  concepto: ConceptoNomina;
  valor_calculado: string;
}

export interface Nomina {
  id: number;
  fecha_inicio: string;
  fecha_fin: string;
  estado: 'borrador' | 'procesada' | 'pagada';
  total_ingresos: string;
  total_deducciones: string;
  neto_a_pagar: string;
  detalles: DetalleNomina[];
}


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

  // --- APIs de Ventas ---
  const getFacturasVenta = useCallback(async () => {
    return makeRequest(() => api.get<FacturaVenta[]>('/api/v1/mi-negocio/comercial/facturas-venta/').then(res => res.data));
  }, [makeRequest]);

  const createFacturaVenta = useCallback(async (data: CreateFacturaVentaDTO) => {
    return makeRequest(() => api.post<FacturaVenta>('/api/v1/mi-negocio/comercial/facturas-venta/', data).then(res => res.data), "Factura creada.");
  }, [makeRequest]);


  // --- APIs de Nómina ---
  const getEmpleados = useCallback(async () => {
    return makeRequest(() => api.get<Empleado[]>('/api/v1/mi-negocio/nomina/empleados/').then(res => res.data));
  }, [makeRequest]);

  const createEmpleado = useCallback(async (data: CreateEmpleadoDTO) => {
    return makeRequest(() => api.post<Empleado>('/api/v1/mi-negocio/nomina/empleados/', data).then(res => res.data), "Empleado creado.");
  }, [makeRequest]);

  const updateEmpleado = useCallback(async (id: number, data: Partial<CreateEmpleadoDTO>) => {
    return makeRequest(() => api.patch<Empleado>(`/api/v1/mi-negocio/nomina/empleados/${id}/`, data).then(res => res.data), "Empleado actualizado.");
  }, [makeRequest]);

  const getConceptos = useCallback(async () => {
    return makeRequest(() => api.get<ConceptoNomina[]>('/api/v1/mi-negocio/nomina/conceptos/').then(res => res.data));
  }, [makeRequest]);

  const getNominas = useCallback(async () => {
    return makeRequest(() => api.get<Nomina[]>('/api/v1/mi-negocio/nomina/nominas/').then(res => res.data));
  }, [makeRequest]);

  const procesarNomina = useCallback(async (fecha_inicio: string, fecha_fin: string) => {
    return makeRequest(() => api.post<Nomina>('/api/v1/mi-negocio/nomina/nominas/procesar/', { fecha_inicio, fecha_fin }).then(res => res.data), "Nómina procesada.");
  }, [makeRequest]);


  // --- APIs de Activos Fijos (Rutas corregidas) ---
  const getActivosFijos = useCallback(async () => {
    return makeRequest(() => api.get<ActivoFijo[]>('/api/v1/mi-negocio/activos/activos-fijos/').then(res => res.data));
  }, [makeRequest]);

  const createActivoFijo = useCallback(async (data: Omit<ActivoFijo, 'id' | 'depreciacion_acumulada' | 'valor_en_libros'>) => {
    return makeRequest(() => api.post<ActivoFijo>('/api/v1/mi-negocio/activos/activos-fijos/', data).then(res => res.data), "Activo creado.");
  }, [makeRequest]);

  const getHistorialDepreciacion = useCallback(async (activoId: number) => {
    return makeRequest(() => api.get<RegistroDepreciacion[]>(`/api/v1/mi-negocio/activos/activos-fijos/${activoId}/depreciaciones/`).then(res => res.data));
  }, [makeRequest]);


  return {
    // ... (funciones existentes)

    // --- funciones de Ventas ---
    getFacturasVenta,
    createFacturaVenta,

    // --- funciones de Nómina ---
    getEmpleados,
    createEmpleado,
    updateEmpleado,
    getConceptos,
    getNominas,
    procesarNomina,

    // --- funciones de Activos ---
    getActivosFijos,
    createActivoFijo,
    getHistorialDepreciacion,
  };
}
