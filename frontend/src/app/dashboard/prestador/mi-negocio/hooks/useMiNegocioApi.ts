// src/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import { toast } from 'react-toastify';
import { contableEndpoints } from '@/services/endpoints/contable';
import { operativoEndpoints } from '@/services/endpoints/operativo';
import { comercialEndpoints } from '@/services/endpoints/comercial';
import { financieroEndpoints } from '@/services/endpoints/financiero';
import { archivisticaEndpoints } from '@/services/endpoints/archivistica';
import { contableMapper } from '@/services/mappers/contableMapper';
import { commercialMapper } from '@/services/mappers/commercialMapper';

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

  // --- API de Ventas ---
  const getFacturas = useCallback(async () => {
    return makeRequest(() => comercialEndpoints.getFacturasVenta().then(res =>
      res.data.results.map(commercialMapper.mapFacturaToUI)
    ));
  }, [makeRequest]);

  // --- API Financiera ---
  const getBankAccounts = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getBankAccounts().then(res => res.data));
  }, [makeRequest]);

  const getCashTransactions = useCallback(async () => {
    return makeRequest(() => financieroEndpoints.getCashTransactions().then(res => res.data));
  }, [makeRequest]);

  // --- API Archivística ---
  const getArchivisticaDocumentos = useCallback(async () => {
    return makeRequest(() => archivisticaEndpoints.getDocumentos().then(res => res.data));
  }, [makeRequest]);

  return {
    isLoading,
    error,
    getPerfil,
    updatePerfil,
    getChartOfAccounts,
    getJournalEntries,
    getFacturas,
    getBankAccounts,
    getCashTransactions,
    getArchivisticaDocumentos,
  };
}
