// src/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import { toast } from 'react-toastify';
import { contableEndpoints } from '@/services/endpoints/contable';
import { operativoEndpoints } from '@/services/endpoints/operativo';
import { comercialEndpoints } from '@/services/endpoints/comercial';
import { financieroEndpoints } from '@/services/endpoints/financiero';
import { archivisticaEndpoints } from '@/services/endpoints/archivistica';
import { nominaEndpoints } from '@/services/endpoints/nomina';
import { saritaEndpoints } from '@/services/endpoints/sarita';
import { contableMapper } from '@/services/mappers/contableMapper';
import { commercialMapper } from '@/services/mappers/commercialMapper';

export interface Cliente {
  id: number;
  nombre: string;
  email: string;
}

export interface Producto {
  id: number;
  nombre: string;
  precio_venta: string;
}

export interface ItemFactura {
  producto: number;
  cantidad: number;
  precio_unitario: string;
}

export function useMiNegocioApi() {
  const { token } = useAuth();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const makeRequest = useCallback(async <T>(requestFunc: () => Promise<T>, successMessage?: string): Promise<T | null> => {
    if (!token) { setError("No autenticado."); return null; }
    setIsLoading(true); setError(null);
    try {
      const result = await requestFunc();
      if (successMessage) toast.success(successMessage);
      return result;
    } catch (err: any) {
      const msg = err.message || "Ocurrió un error.";
      setError(msg); toast.error(msg);
      return null;
    } finally { setIsLoading(false); }
  }, [token]);

  // --- API de Perfil ---
  const getPerfil = useCallback(async () => {
    return makeRequest(() => operativoEndpoints.getPerfil().then(res => res.data));
  }, [makeRequest]);

  const updatePerfil = useCallback(async (data: any) => {
    return makeRequest(() => operativoEndpoints.updatePerfil(data).then(res => res.data), "Perfil actualizado con éxito.");
  }, [makeRequest]);

  // --- API de Contabilidad ---
  const getChartOfAccounts = useCallback(async () => {
    return makeRequest(() => contableEndpoints.getPlanCuentas().then(res =>
      res.data.map(contableMapper.mapAccountToUI)
    ));
  }, [makeRequest]);

  const getJournalEntries = useCallback(async () => {
    return makeRequest(() => contableEndpoints.getAsientosContables().then(res =>
      res.data.map(contableMapper.mapAsientoToUI)
    ));
  }, [makeRequest]);

  const getLibroDiario = useCallback(async (fechaInicio: string, fechaFin: string) => {
    return makeRequest(() => contableEndpoints.getLibroDiario(fechaInicio, fechaFin).then(res => res.data));
  }, [makeRequest]);

  const getLibroMayor = useCallback(async (cuentaCodigo: string, fechaInicio: string, fechaFin: string) => {
    return makeRequest(() => contableEndpoints.getLibroMayor(cuentaCodigo, fechaInicio, fechaFin).then(res => res.data));
  }, [makeRequest]);

  const getBalanceComprobacion = useCallback(async (periodoId: string) => {
    return makeRequest(() => contableEndpoints.getBalanceComprobacion(periodoId).then(res => res.data));
  }, [makeRequest]);

  const getEstadoResultados = useCallback(async (fechaInicio: string, fechaFin: string) => {
    return makeRequest(() => contableEndpoints.getEstadoResultados(fechaInicio, fechaFin).then(res => res.data));
  }, [makeRequest]);

  const getBalanceGeneral = useCallback(async (fechaCorte: string) => {
    return makeRequest(() => contableEndpoints.getBalanceGeneral(fechaCorte).then(res => res.data));
  }, [makeRequest]);

  const getFlujoCaja = useCallback(async (fechaInicio: string, fechaFin: string) => {
    return makeRequest(() => contableEndpoints.getFlujoCaja(fechaInicio, fechaFin).then(res => res.data));
  }, [makeRequest]);

  const getConciliacionWallet = useCallback(async (providerId: string) => {
    return makeRequest(() => contableEndpoints.getConciliacionWallet(providerId).then(res => res.data));
  }, [makeRequest]);

  // --- API de Ventas ---
  const getFacturas = useCallback(async () => {
    return makeRequest(() => comercialEndpoints.getFacturasVenta().then(res =>
      res.data.results.map(commercialMapper.mapFacturaToUI)
    ));
  }, [makeRequest]);

  const createFacturaVenta = useCallback(async (data: any) => {
    return makeRequest(() => comercialEndpoints.createFacturaVenta(data).then(res => res.data), "Factura creada con éxito.");
  }, [makeRequest]);

  const getClientes = useCallback(async () => {
    return makeRequest(() => operativoEndpoints.getClientes().then(res => res.data));
  }, [makeRequest]);

  const getProductos = useCallback(async () => {
    return makeRequest(() => operativoEndpoints.getProductosServicios().then(res => res.data));
  }, [makeRequest]);

  // --- API Financiera ---
  const getBankAccounts = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getBankAccounts().then(res => res.data));
  }, [makeRequest]);

  const getCashTransactions = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getCashTransactions().then(res => res.data));
  }, [makeRequest]);

  const getEstadoResultados = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getEstadoResultados().then(res => res.data));
  }, [makeRequest]);

  const getBalanceGeneral = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getBalanceGeneral().then(res => res.data));
  }, [makeRequest]);

  const getProyecciones = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getProyecciones().then(res => res.data));
  }, [makeRequest]);

  const getRiesgos = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getRiesgos().then(res => res.data));
  }, [makeRequest]);

  const getTesoreria = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getTesoreria().then(res => res.data));
  }, [makeRequest]);

  const getPresupuestos = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getPresupuestos().then(res => res.data));
  }, [makeRequest]);

  const getCreditos = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getCreditos().then(res => res.data));
  }, [makeRequest]);

  const getIndicadores = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getIndicadores().then(res => res.data));
  }, [makeRequest]);

  const getAlertas = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getAlertas().then(res => res.data));
  }, [makeRequest]);

  const resolverAlerta = useCallback(async (id: string) => {
    return makeRequest(() => financieroEndpoints.resolverAlerta(id).then(res => res.data), "Alerta resuelta.");
  }, [makeRequest]);

  // --- API SG-SST ---
  const getSSTRisks = useCallback(async () => {
    return makeRequest(() => operativoEndpoints.getSSTRisks().then(res => res.data));
  }, [makeRequest]);

  const getSSTIncidents = useCallback(async () => {
    return makeRequest(() => operativoEndpoints.getSSTIncidents().then(res => res.data));
  }, [makeRequest]);

  const reportSSTIncident = useCallback(async (data: any) => {
    return makeRequest(() => operativoEndpoints.reportSSTIncident(data).then(res => res.data), "Incidente reportado exitosamente.");
  }, [makeRequest]);

  // --- API Archivística ---
  const getArchivisticaDocumentos = useCallback(async () => {
    return makeRequest(() => archivisticaEndpoints.getDocumentos().then(res => res.data));
  }, [makeRequest]);

  // --- API Nómina ---
  const getEmpleados = useCallback(async () => {
    return makeRequest(() => nominaEndpoints.getEmpleados().then(res => res.data));
  }, [makeRequest]);

  const createEmpleado = useCallback(async (data: any) => {
    return makeRequest(() => nominaEndpoints.createEmpleado(data).then(res => res.data), "Empleado creado.");
  }, [makeRequest]);

  const updateEmpleado = useCallback(async (id: number, data: any) => {
    return makeRequest(() => nominaEndpoints.updateEmpleado(id, data).then(res => res.data), "Datos de empleado actualizados.");
  }, [makeRequest]);

  const deleteEmpleado = useCallback(async (id: number) => {
    return makeRequest(() => nominaEndpoints.deleteEmpleado(id).then(res => res.data), "Empleado eliminado.");
  }, [makeRequest]);

  const getPlanillas = useCallback(async () => {
    return makeRequest(() => nominaEndpoints.getPlanillas().then(res => res.data));
  }, [makeRequest]);

  const createPlanilla = useCallback(async (data: any) => {
    return makeRequest(() => nominaEndpoints.createPlanilla(data).then(res => res.data), "Periodo de nómina creado.");
  }, [makeRequest]);

  const liquidarPlanilla = useCallback(async (id: string) => {
    return makeRequest(() => nominaEndpoints.liquidarPlanilla(id).then(res => res.data), "Planilla liquidada.");
  }, [makeRequest]);

  const contabilizarPlanilla = useCallback(async (id: string) => {
    return makeRequest(() => nominaEndpoints.contabilizarPlanilla(id).then(res => res.data), "Planilla contabilizada y procesada para pago.");
  }, [makeRequest]);

  // --- API Especializada ---
  const getVehicles = useCallback(async () => {
    return makeRequest(() => operativoEndpoints.getVehicles().then(res => res.data));
  }, [makeRequest]);

  const getTours = useCallback(async () => {
    return makeRequest(() => operativoEndpoints.getTours().then(res => res.data));
  }, [makeRequest]);

  const getProcesosOperativos = useCallback(async () => {
    return makeRequest(() => operativoEndpoints.getProcesosOperativos().then(res => res.data));
  }, [makeRequest]);

  const updateProcesoEstado = useCallback(async (id: string, nuevo_estado: string) => {
    return makeRequest(() => operativoEndpoints.updateProcesoEstado(id, nuevo_estado).then(res => res.data), "Estado operativo actualizado.");
  }, [makeRequest]);

  // --- API de Órdenes Operativas (Fase 3) ---
  const getOrdenesOperativas = useCallback(async () => {
    return makeRequest(() => operativoEndpoints.getOrdenesOperativas().then(res => res.data));
  }, [makeRequest]);

  const updateOrdenEstado = useCallback(async (id: string, nuevo_estado: string, motivo: string = "") => {
    return makeRequest(() => operativoEndpoints.updateOrdenEstado(id, nuevo_estado, motivo).then(res => res.data), "Transición de estado enviada a gobernanza.");
  }, [makeRequest]);

  const reportIncidente = useCallback(async (data: any) => {
    return makeRequest(() => operativoEndpoints.reportIncidente(data).then(res => res.data), "Incidencia reportada en el motor operativo.");
  }, [makeRequest]);

  const triggerMission = useCallback(async (type: string, parameters: any) => {
    return makeRequest(() => saritaEndpoints.triggerMission(type, parameters).then(res => res.data), "Misión delegada exitosamente.");
  }, [makeRequest]);

  return {
    isLoading,
    error,
    getPerfil,
    updatePerfil,
    getChartOfAccounts,
    getJournalEntries,
    getLibroDiario,
    getLibroMayor,
    getBalanceComprobacion,
    getEstadoResultados,
    getBalanceGeneral,
    getFlujoCaja,
    getConciliacionWallet,
    getFacturas,
    createFacturaVenta,
    getClientes,
    getProductos,
    getBankAccounts,
    getCashTransactions,
    getEstadoResultados,
    getBalanceGeneral,
    getProyecciones,
    getRiesgos,
    getTesoreria,
    getPresupuestos,
    getCreditos,
    getIndicadores,
    getAlertas,
    resolverAlerta,
    getSSTRisks,
    getSSTIncidents,
    reportSSTIncident,
    getArchivisticaDocumentos,
    getEmpleados,
    createEmpleado,
    updateEmpleado,
    deleteEmpleado,
    getPlanillas,
    createPlanilla,
    liquidarPlanilla,
    contabilizarPlanilla,
    getVehicles,
    getTours,
    getProcesosOperativos,
    updateProcesoEstado,
    getOrdenesOperativas,
    updateOrdenEstado,
    reportIncidente,
    triggerMission,
  };
}
