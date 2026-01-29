// src/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
import api from '@/services/api';
import { useAuth } from '@/contexts/AuthContext';
import { toast } from 'react-toastify';

 
// --- Tipos de Datos Genéricos---
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

// Interfaz para respuestas paginadas
export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export interface Proveedor {
  id: number;
  nombre: string;
  identificacion: string | null;
  telefono: string | null;
  email: string | null;
  direccion: string | null;
}

export interface FacturaCompra {
  id: number;
  proveedor: number;
  proveedor_nombre?: string;
  numero_factura: string;
  fecha_emision: string;
  fecha_vencimiento: string;
  subtotal: string;
  impuestos: string;
  total: string;
  estado: string;
}

export interface Producto {
  id: number;
  nombre: string;
  sku: string;
  categoria: number;
  categoria_nombre?: string;
  descripcion: string;
  costo: string;
  precio_venta: string;
  stock_actual: string;
  stock_minimo: string;
}

export interface Empleado {
  id: number;
  nombre: string;
  apellido: string;
  identificacion: string;
  email: string;
}

export interface Planilla {
  id: number;
  periodo_inicio: string;
  periodo_fin: string;
  total_neto: string;
}

export interface ConceptoNomina {
  id: number;
  codigo: string;
  descripcion: string;
  tipo: 'DEVENGADO' | 'DEDUCCION';
}

// --- Tipos de Datos de Contabilidad (Alineados con el Backend) ---
export interface ChartOfAccount {
  code: string;
  name: string;
  nature: 'DEBITO' | 'CREDITO';
  allows_transactions: boolean;
}

export interface Transaction {
  id?: number;
  account: string; // FK al código de ChartOfAccount
  debit: string;
  credit: string;
  cost_center?: number | null;
}

export interface JournalEntry {
  id: number;
  perfil: number;
  entry_date: string;
  description: string;
  entry_type: string;
  user: number;
  origin_document?: any; // GenericForeignKey
  created_at: string;
  transactions: Transaction[];
}

// --- Tipos de Datos de Ventas ---
export interface ItemFactura {
  id?: number;
  producto: number;
  cantidad: number;
  precio_unitario: string;
  producto_nombre?: string;
  total_item?: string;
}

export interface FacturaVenta {
  id: number;
  numero_factura: string;
  cliente_nombre: string;
  fecha_emision: string;
  total: string;
  estado: string;
  estado_display: string;
  // Los siguientes campos solo vienen en el detalle, no en la lista
  cliente?: number;
  fecha_vencimiento?: string;
  subtotal?: string;
  impuestos?: string;
  items?: ItemFactura[];
}
// --- Tipos de Datos Financieros (Alineados con el Backend) ---
export interface BankAccount {
  id: number;
  bank_name: string;
  account_number: string;
  account_holder: string;
  account_type: 'SAVINGS' | 'CHECKING';
  balance: string;
}

export interface CashTransaction {
  id: number;
  cuenta: number; // FK a CuentaBancaria
  fecha: string;
  tipo: 'INGRESO' | 'EGRESO' | 'TRANSFERENCIA';
  monto: string;
  descripcion: string;
  creado_por: number;
  creado_en: string;
}

// --- Tipos de Datos de Activos Fijos ---
export interface CategoriaActivo {
  id: number;
  nombre: string;
  descripcion: string;
}

export interface ActivoFijo {
  id: number;
  nombre: string;
  categoria: number;
  categoria_nombre?: string;
  descripcion: string;
  fecha_adquisicion: string;
  costo_adquisicion: string;
  valor_residual: string;
  vida_util_meses: number;
  metodo_depreciacion: string;
  depreciacion_acumulada: string;
  valor_en_libros: string;
}

export interface CalculoDepreciacion {
  id: number;
  activo: number;
  fecha: string;
  monto: string;
  creado_en: string;
}

// --- Tipos de Datos de Presupuesto ---
export interface Presupuesto {
  id: number;
  nombre: string;
  ano_fiscal: number;
  total_ingresos_presupuestado: string;
  total_gastos_presupuestado: string;
}

export interface PartidaPresupuestal {
  id: number;
  presupuesto: number;
  cuenta_contable: number;
  cuenta_contable_nombre?: string;
  tipo: 'INGRESO' | 'GASTO';
  monto_presupuestado: string;
  monto_ejecutado: string;
}

export interface EjecucionPresupuestal {
  id: number;
  partida: number;
  fecha: string;
  monto: string;
  descripcion: string;
}


export function useMiNegocioApi() {
  const { token } = useAuth();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const makeRequest = useCallback(async <T>(requestFunc: () => Promise<T>, successMessage?: string, errorMessage?: string): Promise<T | null> => {
    if (!token) { setError("No autenticado."); return null; }
    setIsLoading(true); setError(null);
    try {
      const result = await requestFunc();
      if (successMessage) toast.success(successMessage);
      return result;
    } catch (err: any) {
      const msg = err.response?.data?.detail || "Ocurrió un error.";
      setError(msg); toast.error(msg);
      return null;
    } finally { setIsLoading(false); }
  }, [token]);

 
  // --- API de Perfil ---
  const getPerfil = useCallback(async () => {
    return makeRequest(() => api.get<PerfilData>('/admin/plataforma/operativa/genericos/perfil/me/').then(res => res.data), undefined, "No se pudo cargar el perfil.");
  }, [makeRequest]);

  const updatePerfil = useCallback(async (data: Partial<PerfilData>) => {
    return makeRequest(() => api.patch<PerfilData>('/admin/plataforma/operativa/genericos/perfil/update-me/', data).then(res => res.data), "Perfil actualizado con éxito.", "Error al actualizar el perfil.");
  }, [makeRequest]);

  // --- API de Clientes (CRM) ---
  const getClientes = useCallback(async (page: number = 1, search: string = '') => {
    const params = new URLSearchParams({
        page: page.toString(),
        search: search,
    });
    return makeRequest(() => api.get<PaginatedResponse<Cliente>>(`/admin/plataforma/operativa/clientes/?${params.toString()}`).then(res => res.data), undefined, "No se pudo cargar la lista de clientes.");
  }, [makeRequest]);

  const createCliente = useCallback(async (clienteData: Omit<Cliente, 'id'>) => {
    return makeRequest(() => api.post<Cliente>('/admin/plataforma/operativa/clientes/', clienteData).then(res => res.data), "Cliente creado con éxito.", "Error al crear el cliente.");
  }, [makeRequest]);

  const updateCliente = useCallback(async (id: number, clienteData: Partial<Omit<Cliente, 'id'>>) => {
    return makeRequest(() => api.patch<Cliente>(`/admin/plataforma/operativa/clientes/${id}/`, clienteData).then(res => res.data), "Cliente actualizado con éxito.", "Error al actualizar el cliente.");
  }, [makeRequest]);

  const deleteCliente = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/admin/plataforma/operativa/clientes/${id}/`), "Cliente eliminado con éxito.", "Error al eliminar el cliente.");
  }, [makeRequest]);

  const getClienteById = useCallback(async (id: number) => {
    return makeRequest(() => api.get<Cliente>(`/admin/plataforma/operativa/clientes/${id}/`).then(res => res.data), undefined, "No se pudo cargar el cliente.");
  }, [makeRequest]);

  // --- API de Contabilidad ---
  const getChartOfAccounts = useCallback(async () => {
    return makeRequest(() => api.get<ChartOfAccount[]>('/admin/plataforma/contable/contabilidad/plan-cuentas/').then(res => res.data));
  }, [makeRequest]);

  const getJournalEntries = useCallback(async () => {
    return makeRequest(() => api.get<JournalEntry[]>('/admin/plataforma/contable/contabilidad/asientos-contables/').then(res => res.data));
  }, [makeRequest]);

  const createJournalEntry = useCallback(async (entryData: any) => {
    return makeRequest(() => api.post<JournalEntry>('/admin/plataforma/contable/contabilidad/asientos-contables/', entryData).then(res => res.data), "Asiento contable creado.");
  }, [makeRequest]);

  const updateJournalEntry = useCallback(async (id: number, entryData: any) => {
    return makeRequest(() => api.patch<JournalEntry>(`/admin/plataforma/contable/contabilidad/asientos-contables/${id}/`, entryData).then(res => res.data), "Asiento actualizado.");
  }, [makeRequest]);

  const deleteJournalEntry = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/admin/plataforma/contable/contabilidad/asientos-contables/${id}/`), "Asiento eliminado.");
  }, [makeRequest]);

  // --- API de Compras (Proveedores) ---
  const getProveedores = useCallback(async () => {
    return makeRequest(() => api.get<any>('/admin/plataforma/contable/compras/proveedores/').then(res => res.data));
  }, [makeRequest]);

  const createProveedor = useCallback(async (proveedorData: Omit<Proveedor, 'id'>) => {
    return makeRequest(() => api.post<Proveedor>('/admin/plataforma/contable/compras/proveedores/', proveedorData).then(res => res.data), "Proveedor creado con éxito.");
  }, [makeRequest]);

  const updateProveedor = useCallback(async (id: number, proveedorData: Partial<Omit<Proveedor, 'id'>>) => {
    return makeRequest(() => api.patch<Proveedor>(`/admin/plataforma/contable/compras/proveedores/${id}/`, proveedorData).then(res => res.data), "Proveedor actualizado con éxito.");
  }, [makeRequest]);

  const deleteProveedor = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/admin/plataforma/contable/compras/proveedores/${id}/`), "Proveedor eliminado con éxito.");
  }, [makeRequest]);

  const getFacturasCompra = useCallback(async () => {
    return makeRequest(() => api.get<any>('/admin/plataforma/contable/compras/facturas/').then(res => res.data));
  }, [makeRequest]);

  const createFacturaCompra = useCallback(async (facturaData: any) => {
    return makeRequest(() => api.post<FacturaCompra>('/admin/plataforma/contable/compras/facturas/', facturaData).then(res => res.data), "Factura de compra creada con éxito.");
  }, [makeRequest]);

  const updateFacturaCompra = useCallback(async (id: number, facturaData: any) => {
    return makeRequest(() => api.patch<FacturaCompra>(`/admin/plataforma/contable/compras/facturas/${id}/`, facturaData).then(res => res.data), "Factura de compra actualizada con éxito.");
  }, [makeRequest]);

  const pagarFacturaCompra = useCallback(async (id: number, cuentaBancariaId: number) => {
    return makeRequest(() => api.post(`/admin/plataforma/contable/compras/facturas/${id}/pagar/`, { cuenta_bancaria_id: cuentaBancariaId }).then(res => res.data), "Factura pagada con éxito.");
  }, [makeRequest]);

  // --- API de Inventario ---
  const getProductos = useCallback(async () => {
    return makeRequest(() => api.get<any>('/admin/plataforma/contable/inventario/productos/').then(res => res.data));
  }, [makeRequest]);

  const createProducto = useCallback(async (productoData: any) => {
    return makeRequest(() => api.post<Producto>('/admin/plataforma/contable/inventario/productos/', productoData).then(res => res.data), "Producto creado con éxito.");
  }, [makeRequest]);

  const updateProducto = useCallback(async (id: number, productoData: any) => {
    return makeRequest(() => api.patch<Producto>(`/admin/plataforma/contable/inventario/productos/${id}/`, productoData).then(res => res.data), "Producto actualizado con éxito.");
  }, [makeRequest]);

  const deleteProducto = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/admin/plataforma/contable/inventario/productos/${id}/`), "Producto eliminado con éxito.");
  }, [makeRequest]);

  const getMovimientosInventario = useCallback(async () => {
    return makeRequest(() => api.get<any>('/admin/plataforma/contable/inventario/movimientos/').then(res => res.data));
  }, [makeRequest]);

  const createMovimientoInventario = useCallback(async (movimientoData: any) => {
    return makeRequest(() => api.post('/admin/plataforma/contable/inventario/movimientos/', movimientoData).then(res => res.data), "Movimiento registrado con éxito.");
  }, [makeRequest]);

  // --- API de Nómina ---
  const getEmpleados = useCallback(async () => {
    return makeRequest(() => api.get<any>('/admin/plataforma/contable/nomina/empleados/').then(res => res.data));
  }, [makeRequest]);

  const createEmpleado = useCallback(async (empleadoData: any) => {
    return makeRequest(() => api.post<Empleado>('/admin/plataforma/contable/nomina/empleados/', empleadoData).then(res => res.data), "Empleado creado con éxito.");
  }, [makeRequest]);

  const updateEmpleado = useCallback(async (id: number, empleadoData: any) => {
    return makeRequest(() => api.patch<Empleado>(`/admin/plataforma/contable/nomina/empleados/${id}/`, empleadoData).then(res => res.data), "Empleado actualizado con éxito.");
  }, [makeRequest]);

  const deleteEmpleado = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/admin/plataforma/contable/nomina/empleados/${id}/`), "Empleado eliminado con éxito.");
  }, [makeRequest]);

  const getPlanillas = useCallback(async () => {
    return makeRequest(() => api.get<any>('/admin/plataforma/contable/nomina/planillas/').then(res => res.data));
  }, [makeRequest]);

  const createPlanilla = useCallback(async (planillaData: any) => {
    return makeRequest(() => api.post<Planilla>('/admin/plataforma/contable/nomina/planillas/', planillaData).then(res => res.data), "Planilla creada con éxito.");
  }, [makeRequest]);

  const getConceptosNomina = useCallback(async () => {
    return makeRequest(() => api.get<any>('/admin/plataforma/contable/nomina/conceptos/').then(res => res.data));
  }, [makeRequest]);

  // --- API de Reportes ---
  const getLibroMayor = useCallback(async (params: { codigo_cuenta: string, fecha_inicio: string, fecha_fin: string }) => {
    return makeRequest(() => api.get('/admin/plataforma/contable/contabilidad/reportes/libro-mayor/', { params }).then(res => res.data));
  }, [makeRequest]);

  const getBalanceComprobacion = useCallback(async (params: { fecha_fin: string }) => {
    return makeRequest(() => api.get('/admin/plataforma/contable/contabilidad/reportes/balance-comprobacion/', { params }).then(res => res.data));
  }, [makeRequest]);

  const getReporteFinanciero = useCallback(async (params: { reporte: string, fecha_fin: string }) => {
    return makeRequest(() => api.get('/admin/plataforma/contable/contabilidad/reportes/financieros/', { params }).then(res => res.data));
  }, [makeRequest]);

  const getReporteIngresosGastos = useCallback(async () => {
    return makeRequest(() => api.get('/admin/plataforma/financiera/reporte-ingresos-gastos/').then(res => res.data));
  }, [makeRequest]);

  // --- API Financiera ---
  const getCurrencies = useCallback(async () => {
    // Nota: Este endpoint puede necesitar ser implementado si es requerido
    return makeRequest(() => api.get<any[]>('/admin/plataforma/contable/contabilidad/currencies/').then(res => res.data));
  }, [makeRequest]);

  const getBankAccounts = useCallback(async () => {
    return makeRequest(() => api.get<BankAccount[]>('/admin/plataforma/financiera/cuentas-bancarias/').then(res => res.data));
  }, [makeRequest]);

  const createBankAccount = useCallback(async (accountData: any) => {
    return makeRequest(() => api.post<BankAccount>('/admin/plataforma/financiera/cuentas-bancarias/', accountData).then(res => res.data), "Cuenta bancaria creada.");
  }, [makeRequest]);

  const updateBankAccount = useCallback(async (id: number, accountData: any) => {
    return makeRequest(() => api.patch<BankAccount>(`/admin/plataforma/financiera/cuentas-bancarias/${id}/`, accountData).then(res => res.data), "Cuenta bancaria actualizada.");
  }, [makeRequest]);

  const deleteBankAccount = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/admin/plataforma/financiera/cuentas-bancarias/${id}/`), "Cuenta bancaria eliminada.");
  }, [makeRequest]);

  const getCashTransactions = useCallback(async () => {
    return makeRequest(() => api.get<CashTransaction[]>('/admin/plataforma/financiera/transacciones-bancarias/').then(res => res.data));
  }, [makeRequest]);

  const createCashTransaction = useCallback(async (transactionData: any) => {
    return makeRequest(() => api.post<CashTransaction>('/admin/plataforma/financiera/transacciones-bancarias/', transactionData).then(res => res.data), "Transacción creada.");
  }, [makeRequest]);

  // --- API de Ventas ---
  const getFacturasVenta = useCallback(async () => {
    return makeRequest(() => api.get<{results: FacturaVenta[]}>('/admin/plataforma/comercial/facturas-venta/').then(res => res.data.results), undefined, "No se pudo cargar la lista de facturas.");
  }, [makeRequest]);

  const createFacturaVenta = useCallback(async (facturaData: Omit<FacturaVenta, 'id' | 'subtotal' | 'impuestos' | 'total' | 'estado'>) => {
    return makeRequest(() => api.post<FacturaVenta>('/admin/plataforma/comercial/facturas-venta/', facturaData).then(res => res.data), "Factura creada con éxito.", "Error al crear la factura.");
  }, [makeRequest]);

  // --- API de Placeholders para Operativa ---
  const getNominaPlaceholder = useCallback(async () => {
    return makeRequest(() => api.get<any>('/admin/plataforma/contable/nomina/').then(res => res.data));
  }, [makeRequest]);

  const getProyectosPlaceholder = useCallback(async () => {
    return makeRequest(() => api.get<any>('/admin/plataforma/contable/proyectos/').then(res => res.data));
  }, [makeRequest]);

  // --- API de Activos Fijos ---
  const getCategoriasActivo = useCallback(async (page: number = 1, search: string = '') => {
      const params = new URLSearchParams({ page: page.toString(), search });
      return makeRequest(() => api.get<PaginatedResponse<CategoriaActivo>>(`/admin/plataforma/contable/activos-fijos/categorias/?${params.toString()}`).then(res => res.data));
  }, [makeRequest]);

  const createCategoriaActivo = useCallback(async (data: Omit<CategoriaActivo, 'id'>) => {
      return makeRequest(() => api.post<CategoriaActivo>('/admin/plataforma/contable/activos-fijos/categorias/', data).then(res => res.data), "Categoría creada.");
  }, [makeRequest]);

  const updateCategoriaActivo = useCallback(async (id: number, data: Partial<CategoriaActivo>) => {
      return makeRequest(() => api.patch<CategoriaActivo>(`/admin/plataforma/contable/activos-fijos/categorias/${id}/`, data).then(res => res.data), "Categoría actualizada.");
  }, [makeRequest]);

  const deleteCategoriaActivo = useCallback(async (id: number) => {
      return makeRequest(() => api.delete(`/admin/plataforma/contable/activos-fijos/categorias/${id}/`), "Categoría eliminada.");
  }, [makeRequest]);

  const getActivosFijos = useCallback(async (page: number = 1, search: string = '') => {
      const params = new URLSearchParams({ page: page.toString(), search });
      return makeRequest(() => api.get<PaginatedResponse<ActivoFijo>>(`/admin/plataforma/contable/activos-fijos/activos/?${params.toString()}`).then(res => res.data));
  }, [makeRequest]);

  const createActivoFijo = useCallback(async (data: Omit<ActivoFijo, 'id' | 'depreciacion_acumulada' | 'valor_en_libros'>) => {
      return makeRequest(() => api.post<ActivoFijo>('/admin/plataforma/contable/activos-fijos/activos/', data).then(res => res.data), "Activo creado.");
  }, [makeRequest]);

  const updateActivoFijo = useCallback(async (id: number, data: Partial<Omit<ActivoFijo, 'id' | 'depreciacion_acumulada' | 'valor_en_libros'>>) => {
      return makeRequest(() => api.patch<ActivoFijo>(`/admin/plataforma/contable/activos-fijos/activos/${id}/`, data).then(res => res.data), "Activo actualizado.");
  }, [makeRequest]);

  const deleteActivoFijo = useCallback(async (id: number) => {
      return makeRequest(() => api.delete(`/admin/plataforma/contable/activos-fijos/activos/${id}/`), "Activo eliminado.");
  }, [makeRequest]);

  const getDepreciaciones = useCallback(async (activoId: number, page: number = 1) => {
      const params = new URLSearchParams({ page: page.toString() });
      return makeRequest(() => api.get<PaginatedResponse<CalculoDepreciacion>>(`/admin/plataforma/contable/activos-fijos/depreciaciones/?activo=${activoId}&${params.toString()}`).then(res => res.data));
  }, [makeRequest]);

  const createDepreciacion = useCallback(async (data: { activo: number, fecha: string, monto: string }) => {
      return makeRequest(() => api.post<CalculoDepreciacion>('/admin/plataforma/contable/activos-fijos/depreciaciones/', data).then(res => res.data), "Cálculo de depreciación registrado.");
  }, [makeRequest]);

  // --- API de Presupuesto ---
  const getPresupuestos = useCallback(async (page: number = 1, search: string = '') => {
      const params = new URLSearchParams({ page: page.toString(), search });
      return makeRequest(() => api.get<PaginatedResponse<Presupuesto>>(`/admin/plataforma/contable/presupuesto/presupuestos/?${params.toString()}`).then(res => res.data));
  }, [makeRequest]);

  const createPresupuesto = useCallback(async (data: Omit<Presupuesto, 'id' | 'total_ingresos_presupuestado' | 'total_gastos_presupuestado'>) => {
      return makeRequest(() => api.post<Presupuesto>('/admin/plataforma/contable/presupuesto/presupuestos/', data).then(res => res.data), "Presupuesto creado.");
  }, [makeRequest]);

  const getPartidas = useCallback(async (presupuestoId: number, page: number = 1, search: string = '') => {
      const params = new URLSearchParams({ page: page.toString(), search, presupuesto: presupuestoId.toString() });
      return makeRequest(() => api.get<PaginatedResponse<PartidaPresupuestal>>(`/admin/plataforma/contable/presupuesto/partidas/?${params.toString()}`).then(res => res.data));
  }, [makeRequest]);

  const createPartida = useCallback(async (data: Omit<PartidaPresupuestal, 'id' | 'monto_ejecutado'>) => {
      return makeRequest(() => api.post<PartidaPrespuestal>('/admin/plataforma/contable/presupuesto/partidas/', data).then(res => res.data), "Partida creada.");
  }, [makeRequest]);

  const getEjecuciones = useCallback(async (partidaId: number, page: number = 1) => {
      const params = new URLSearchParams({ page: page.toString(), partida: partidaId.toString() });
      return makeRequest(() => api.get<PaginatedResponse<EjecucionPresupuestal>>(`/admin/plataforma/contable/presupuesto/ejecuciones/?${params.toString()}`).then(res => res.data));
  }, [makeRequest]);

  // --- API de Gestión Archivística ---
  const getArchivisticaDocumentos = useCallback(async () => {
    return makeRequest(() => api.get<any[]>('/admin/plataforma/archivistica/documentos/').then(res => res.data));
  }, [makeRequest]);

  const uploadArchivisticaDocumento = useCallback(async (file: File, metadata: any) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('metadata', JSON.stringify(metadata));
    return makeRequest(() => api.post('/admin/plataforma/archivistica/documentos/upload/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }).then(res => res.data), "Documento subido con éxito.");
  }, [makeRequest]);

  // --- API de Gestión Archivística ---
  const getArchivisticaDocumentos = useCallback(async () => {
    return makeRequest(() => api.get<any[]>('/v1/mi-negocio/archivistica/documentos/').then(res => res.data));
  }, [makeRequest]);

  const uploadArchivisticaDocumento = useCallback(async (file: File, metadata: any) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('metadata', JSON.stringify(metadata));
    return makeRequest(() => api.post('/v1/mi-negocio/archivistica/documentos/upload/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }).then(res => res.data), "Documento subido con éxito.");
  }, [makeRequest]);


  return {
    isLoading,
    getNominaPlaceholder,
    getProyectosPlaceholder,
    error,
    getPerfil,
    updatePerfil,
    getClientes,
    createCliente,
    updateCliente,
    deleteCliente,
    getClienteById,
    // Nuevas funciones
    getChartOfAccounts,
    createChartOfAccount,
    updateChartOfAccount,
    deleteChartOfAccount,
    getJournalEntries,
    createJournalEntry,
    updateJournalEntry,
    deleteJournalEntry,
    getCurrencies,
    getBankAccounts,
    createBankAccount,
    updateBankAccount,
    deleteBankAccount,
    getCashTransactions,
    createCashTransaction,
    getFacturasVenta,
    createFacturaVenta,
    // Proveedores
    getProveedores,
    createProveedor,
    updateProveedor,
    deleteProveedor,
    // Facturas de Compra
    getFacturasCompra,
    createFacturaCompra,
    updateFacturaCompra,
    pagarFacturaCompra,
    // Inventario
    getProductos,
    createProducto,
    updateProducto,
    deleteProducto,
    getMovimientosInventario,
    createMovimientoInventario,
    // Nómina
    getEmpleados,
    createEmpleado,
    updateEmpleado,
    deleteEmpleado,
    getPlanillas,
    createPlanilla,
    getConceptosNomina,
    // Reportes
    getLibroMayor,
    getBalanceComprobacion,
    getReporteFinanciero,
    getReporteIngresosGastos,
    // Activos Fijos
    getCategoriasActivo,
    createCategoriaActivo,
    updateCategoriaActivo,
    deleteCategoriaActivo,
    getActivosFijos,
    createActivoFijo,
    updateActivoFijo,
    deleteActivoFijo,
    getDepreciaciones,
    createDepreciacion,
    // Presupuesto
    getPresupuestos,
    createPresupuesto,
    getPartidas,
    createPartida,
    getEjecuciones,
    getArchivisticaDocumentos,
    uploadArchivisticaDocumento,
  };
}
