// src/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
import api from '@/services/api';
import { useAuth } from '@/contexts/AuthContext';
import { toast } from 'react-toastify';

// --- Tipos de Datos (Interfaces) ---
export interface ChartOfAccount { id: number; account_number: string; name: string; account_type: string; is_active: boolean; parent: number | null; }
export interface Transaction { id: number; account_number: string; debit: string; credit: string; description: string; }
export interface JournalEntry { id: number; date: string; description: string; transactions: Transaction[]; }
export interface BankAccount { id: number; bank_name: string; account_number: string; account_holder: string; account_type: string; currency_code: string; balance: string; is_active: boolean; }
export interface CashTransaction { id: number; bank_account_name: string; transaction_type: string; amount: string; date: string; description: string; }
export interface Currency { code: string; name: string; }
// Tipos para Informes
export interface LibroMayorEntry { account: ChartOfAccount; initial_balance: string; transactions: Transaction[]; }
export interface SumasSaldosEntry { account: ChartOfAccount; total_debit: string; total_credit: string; balance: string; }
export interface EstadoResultadosData { ingresos: string; gastos: string; utilidad_neta: string; }
export interface BalanceGeneralData { asset: string; liability: string; equity: string; }


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

  // --- Contabilidad CRUD ---
  const getChartOfAccounts = useCallback(() => makeRequest(() => api.get<ChartOfAccount[]>('/api/v1/mi-negocio/contable/chart-of-accounts/').then(res => res.data)), [makeRequest]);
  const createChartOfAccount = useCallback((data: any) => makeRequest(() => api.post('/api/v1/mi-negocio/contable/chart-of-accounts/', data).then(res => res.data), "Cuenta creada."), [makeRequest]);
  const updateChartOfAccount = useCallback((id: number, data: any) => makeRequest(() => api.patch(`/api/v1/mi-negocio/contable/chart-of-accounts/${id}/`, data).then(res => res.data), "Cuenta actualizada."), [makeRequest]);
  const deleteChartOfAccount = useCallback((id: number) => makeRequest(() => api.delete(`/api/v1/mi-negocio/contable/chart-of-accounts/${id}/`), "Cuenta eliminada."), [makeRequest]);
  const getJournalEntries = useCallback(() => makeRequest(() => api.get<JournalEntry[]>('/api/v1/mi-negocio/contable/journal-entries/').then(res => res.data)), [makeRequest]);
  const createJournalEntry = useCallback((data: any) => makeRequest(() => api.post('/api/v1/mi-negocio/contable/journal-entries/', data).then(res => res.data), "Asiento creado."), [makeRequest]);

  // --- Financiero CRUD ---
  const getCurrencies = useCallback(() => makeRequest(() => api.get<Currency[]>('/api/v1/mi-negocio/contable/currencies/').then(res => res.data)), [makeRequest]);
  const getBankAccounts = useCallback(() => makeRequest(() => api.get<BankAccount[]>('/api/v1/mi-negocio/financiera/bank-accounts/').then(res => res.data)), [makeRequest]);
  const createBankAccount = useCallback((data: any) => makeRequest(() => api.post('/api/v1/mi-negocio/financiera/bank-accounts/', data).then(res => res.data), "Cuenta bancaria creada."), [makeRequest]);
  const updateBankAccount = useCallback((id: number, data: any) => makeRequest(() => api.patch(`/api/v1/mi-negocio/financiera/bank-accounts/${id}/`, data).then(res => res.data), "Cuenta bancaria actualizada."), [makeRequest]);
  const deleteBankAccount = useCallback((id: number) => makeRequest(() => api.delete(`/api/v1/mi-negocio/financiera/bank-accounts/${id}/`), "Cuenta bancaria eliminada."), [makeRequest]);
  const getCashTransactions = useCallback(() => makeRequest(() => api.get<CashTransaction[]>('/api/v1/mi-negocio/financiera/cash-transactions/').then(res => res.data)), [makeRequest]);
  const createCashTransaction = useCallback((data: any) => makeRequest(() => api.post('/api/v1/mi-negocio/financiera/cash-transactions/', data).then(res => res.data), "Transacción creada."), [makeRequest]);

  // --- API de Informes ---
  const getLibroDiario = useCallback((start: string, end: string) => makeRequest(() => api.get<JournalEntry[]>(`/api/v1/mi-negocio/contable/informes/libro-diario/?start_date=${start}&end_date=${end}`).then(res => res.data)), [makeRequest]);
  const getLibroMayor = useCallback((start: string, end: string) => makeRequest(() => api.get<LibroMayorEntry[]>(`/api/v1/mi-negocio/contable/informes/libro-mayor/?start_date=${start}&end_date=${end}`).then(res => res.data)), [makeRequest]);
  const getSumasYSaldos = useCallback((end: string) => makeRequest(() => api.get<SumasSaldosEntry[]>(`/api/v1/mi-negocio/contable/informes/balance-sumas-saldos/?end_date=${end}`).then(res => res.data)), [makeRequest]);
  const getEstadoResultados = useCallback((start: string, end: string) => makeRequest(() => api.get<EstadoResultadosData>(`/api/v1/mi-negocio/contable/informes/estado-resultados/?start_date=${start}&end_date=${end}`).then(res => res.data)), [makeRequest]);
  const getBalanceGeneral = useCallback((end: string) => makeRequest(() => api.get<BalanceGeneralData>(`/api/v1/mi-negocio/contable/informes/balance-general/?end_date=${end}`).then(res => res.data)), [makeRequest]);

  return {
    isLoading, error,
    getChartOfAccounts, createChartOfAccount, updateChartOfAccount, deleteChartOfAccount,
    getJournalEntries, createJournalEntry,
    getCurrencies, getBankAccounts, createBankAccount, updateBankAccount, deleteBankAccount,
    getCashTransactions, createCashTransaction,
    getLibroDiario, getLibroMayor, getSumasYSaldos, getEstadoResultados, getBalanceGeneral,
  };
}
