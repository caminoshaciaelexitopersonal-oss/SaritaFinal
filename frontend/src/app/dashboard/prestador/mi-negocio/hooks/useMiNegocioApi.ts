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
}

export interface Cliente {
  id: number;
  nombre: string;
  email: string;
}

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export interface ChartOfAccount {
  code: string;
  name: string;
  nature: 'DEBITO' | 'CREDITO';
}

export interface JournalEntry {
  id: number;
  entry_date: string;
  description: string;
  entry_type: string;
}

export interface BankAccount {
  id: number;
  bank_name: string;
  account_number: string;
  balance: string;
  account_type: string;
}

export interface CashTransaction {
  id: number;
  fecha: string;
  tipo: 'INGRESO' | 'EGRESO';
  monto: string;
  descripcion: string;
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
      const msg = err.response?.data?.detail || "Ocurrió un error.";
      setError(msg); toast.error(msg);
      return null;
    } finally { setIsLoading(false); }
  }, [token]);

  // --- API de Perfil ---
  const getPerfil = useCallback(async () => {
    return makeRequest(() => api.get<PerfilData>('/v1/mi-negocio/operativa/perfil/me/').then(res => res.data));
  }, [makeRequest]);

  // --- API de Contabilidad ---
  const getChartOfAccounts = useCallback(async () => {
    return makeRequest(() => api.get<ChartOfAccount[]>('/v1/mi-negocio/contable/contabilidad/plan-cuentas/').then(res => res.data));
  }, [makeRequest]);

  const getJournalEntries = useCallback(async () => {
    return makeRequest(() => api.get<JournalEntry[]>('/v1/mi-negocio/contable/contabilidad/asientos-contables/').then(res => res.data));
  }, [makeRequest]);

  // --- API Financiera ---
  const getBankAccounts = useCallback(async () => {
    return makeRequest(() => api.get<BankAccount[]>('/v1/mi-negocio/financiera/cuentas-bancarias/').then(res => res.data));
  }, [makeRequest]);

  const getCashTransactions = useCallback(async () => {
    return makeRequest(() => api.get<CashTransaction[]>('/v1/mi-negocio/financiera/transacciones-bancarias/').then(res => res.data));
  }, [makeRequest]);

  // --- API de Gestión Archivística ---
  const getArchivisticaDocumentos = useCallback(async () => {
    return makeRequest(() => api.get<any[]>('/v1/mi-negocio/archivistica/documentos/').then(res => res.data));
  }, [makeRequest]);

  return {
    isLoading,
    error,
    getPerfil,
    getChartOfAccounts,
    getJournalEntries,
    getBankAccounts,
    getCashTransactions,
    getArchivisticaDocumentos,
  };
}
