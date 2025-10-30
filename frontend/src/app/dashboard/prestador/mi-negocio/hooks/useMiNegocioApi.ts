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

// --- Tipos de Datos de Contabilidad ---
export interface ChartOfAccount {
  id: number;
  account_number: string;
  name: string;
  account_type: 'ASSET' | 'LIABILITY' | 'EQUITY' | 'REVENUE' | 'EXPENSE';
  is_active: boolean;
  parent: number | null;
}

export interface Transaction {
  id: number;
  account_number: string;
  debit: string; // Decimal is string in JSON
  credit: string;
  description: string;
}

export interface JournalEntry {
  id: number;
  date: string;
  description: string;
  cost_center: number | null;
  created_at: string;
  created_by_username: string;
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
  cliente: number;
  cliente_nombre?: string;
  fecha_emision: string;
  fecha_vencimiento: string;
  subtotal: string;
  impuestos: string;
  total: string;
  estado: string;
  items: ItemFactura[];
}
// --- Tipos de Datos Financieros ---
export interface BankAccount {
  id: number;
  bank_name: string;
  account_number: string;
  account_holder: string;
  account_type: 'SAVINGS' | 'CHECKING';
  currency_code: string;
  balance: string;
  is_active: boolean;
  linked_account: number | null;
}

export interface CashTransaction {
  id: number;
  bank_account_name: string;
  transaction_type: 'DEPOSIT' | 'WITHDRAWAL' | 'TRANSFER';
  amount: string;
  date: string;
  description: string;
  reference: string | null;
  created_at: string;
  created_by_username: string;
  journal_entry: number | null;
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
    return makeRequest(() => api.get<PerfilData>('/api/v1/prestadores/mi-negocio/operativa/genericos/perfil/me/').then(res => res.data), undefined, "No se pudo cargar el perfil.");
  }, [makeRequest]);

  const updatePerfil = useCallback(async (data: Partial<PerfilData>) => {
    return makeRequest(() => api.patch<PerfilData>('/api/v1/prestadores/mi-negocio/operativa/genericos/perfil/update-me/', data).then(res => res.data), "Perfil actualizado con éxito.", "Error al actualizar el perfil.");
  }, [makeRequest]);

  // --- API de Clientes (CRM) ---
  const getClientes = useCallback(async () => {
    return makeRequest(() => api.get<Cliente[]>('/api/v1/prestadores/mi-negocio/operativa/genericos/clientes/').then(res => res.data), undefined, "No se pudo cargar la lista de clientes.");
  }, [makeRequest]);

  const createCliente = useCallback(async (clienteData: Omit<Cliente, 'id'>) => {
    return makeRequest(() => api.post<Cliente>('/api/v1/prestadores/mi-negocio/operativa/genericos/clientes/', clienteData).then(res => res.data), "Cliente creado con éxito.", "Error al crear el cliente.");
  }, [makeRequest]);

  // --- API de Contabilidad ---
  const getChartOfAccounts = useCallback(async () => {
    return makeRequest(() => api.get<ChartOfAccount[]>('/api/v1/prestadores/mi-negocio/contable/chart-of-accounts/').then(res => res.data));
  }, [makeRequest]);

  const createChartOfAccount = useCallback(async (accountData: Omit<ChartOfAccount, 'id'>) => {
    return makeRequest(() => api.post<ChartOfAccount>('/api/v1/prestadores/mi-negocio/contable/chart-of-accounts/', accountData).then(res => res.data), "Cuenta creada con éxito.");
  }, [makeRequest]);

  const updateChartOfAccount = useCallback(async (id: number, accountData: Partial<Omit<ChartOfAccount, 'id'>>) => {
    return makeRequest(() => api.patch<ChartOfAccount>(`/api/v1/prestadores/mi-negocio/contable/chart-of-accounts/${id}/`, accountData).then(res => res.data), "Cuenta actualizada con éxito.");
  }, [makeRequest]);

  const deleteChartOfAccount = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/api/v1/prestadores/mi-negocio/contable/chart-of-accounts/${id}/`), "Cuenta eliminada con éxito.");
  }, [makeRequest]);

  const getJournalEntries = useCallback(async () => {
    return makeRequest(() => api.get<JournalEntry[]>('/api/v1/prestadores/mi-negocio/contable/journal-entries/').then(res => res.data));
  }, [makeRequest]);

  const createJournalEntry = useCallback(async (entryData: any) => {
    return makeRequest(() => api.post<JournalEntry>('/api/v1/prestadores/mi-negocio/contable/journal-entries/', entryData).then(res => res.data), "Asiento contable creado.");
  }, [makeRequest]);

  const updateJournalEntry = useCallback(async (id: number, entryData: any) => {
    return makeRequest(() => api.patch<JournalEntry>(`/api/v1/prestadores/mi-negocio/contable/journal-entries/${id}/`, entryData).then(res => res.data), "Asiento actualizado.");
  }, [makeRequest]);

  const deleteJournalEntry = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/api/v1/prestadores/mi-negocio/contable/journal-entries/${id}/`), "Asiento eliminado.");
  }, [makeRequest]);

  // --- API Financiera ---
  const getCurrencies = useCallback(async () => {
    return makeRequest(() => api.get<any[]>('/api/v1/prestadores/mi-negocio/contable/currencies/').then(res => res.data));
  }, [makeRequest]);

  const getBankAccounts = useCallback(async () => {
    return makeRequest(() => api.get<BankAccount[]>('/api/v1/prestadores/mi-negocio/financiera/bank-accounts/').then(res => res.data));
  }, [makeRequest]);

  const createBankAccount = useCallback(async (accountData: any) => {
    return makeRequest(() => api.post<BankAccount>('/api/v1/prestadores/mi-negocio/financiera/bank-accounts/', accountData).then(res => res.data), "Cuenta bancaria creada.");
  }, [makeRequest]);

  const updateBankAccount = useCallback(async (id: number, accountData: any) => {
    return makeRequest(() => api.patch<BankAccount>(`/api/v1/prestadores/mi-negocio/financiera/bank-accounts/${id}/`, accountData).then(res => res.data), "Cuenta bancaria actualizada.");
  }, [makeRequest]);

  const deleteBankAccount = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/api/v1/prestadores/mi-negocio/financiera/bank-accounts/${id}/`), "Cuenta bancaria eliminada.");
  }, [makeRequest]);

  const getCashTransactions = useCallback(async () => {
    return makeRequest(() => api.get<CashTransaction[]>('/api/v1/prestadores/mi-negocio/financiera/cash-transactions/').then(res => res.data));
  }, [makeRequest]);

  const createCashTransaction = useCallback(async (transactionData: any) => {
    return makeRequest(() => api.post<CashTransaction>('/api/v1/prestadores/mi-negocio/financiera/cash-transactions/', transactionData).then(res => res.data), "Transacción creada.");
  }, [makeRequest]);

  // --- API de Ventas ---
  const getFacturasVenta = useCallback(async () => {
    return makeRequest(() => api.get<{results: FacturaVenta[]}>('/api/v1/prestadores/mi-negocio/comercial/facturas-venta/').then(res => res.data.results), undefined, "No se pudo cargar la lista de facturas.");
  }, [makeRequest]);

  const createFacturaVenta = useCallback(async (facturaData: Omit<FacturaVenta, 'id' | 'subtotal' | 'impuestos' | 'total' | 'estado'>) => {
    return makeRequest(() => api.post<FacturaVenta>('/api/v1/prestadores/mi-negocio/comercial/facturas-venta/', facturaData).then(res => res.data), "Factura creada con éxito.", "Error al crear la factura.");
  }, [makeRequest]);


  return {
    isLoading,
    error,
    getPerfil,
    updatePerfil,
    getClientes,
    createCliente,
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
 
  };
}
