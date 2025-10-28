// src/app/[locale]/(dashboard)/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useState, useCallback } from 'react';
import api from '@/services/api';
import { useAuth } from '@/contexts/AuthContext';
import { toast } from 'react-toastify';

// --- Tipos de Datos Genéricos---
interface PerfilData {
  nombre_comercial: string;
  // ...otros campos de perfil
}

// --- Tipos de Datos del Ciclo Comercial ---
export interface Cliente {
  id: number;
  nombre: string;
  identificacion?: string;
  email?: string;
  telefono?: string;
  direccion?: string;
  is_active: boolean;
}

export interface ItemFactura {
  id: number;
  descripcion: string;
  cantidad: number;
  precio_unitario: string; // Decimal
  total_item: string; // Decimal
}

export interface FacturaVenta {
  id: number;
  cliente: number; // ID
  cliente_nombre?: string; // Para mostrar en UI
  fecha_emision: string;
  fecha_vencimiento: string;
  subtotal: string;
  impuestos: string;
  total: string;
  pagado: string;
  estado: 'BORRADOR' | 'EMITIDA' | 'PAGADA' | 'VENCIDA' | 'ANULADA';
  items: ItemFactura[];
}

// ... (Otras interfaces de Contabilidad y Financiero) ...
export interface ChartOfAccount {
  id: number;
  code: string;
  name: string;
  nature: 'DEBITO' | 'CREDITO';
  allows_transactions: boolean;
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
// ...

export function useMiNegocioApi() {
  const { token } = useAuth();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const makeRequest = useCallback(async <T>(requestFunc: () => Promise<T>, successMessage?: string, errorMessage?: string): Promise<T | null> => {
    // ... (lógica de makeRequest sin cambios) ...
        if (!token) {
      setError("No autenticado.");
      return null;
    }

    setIsLoading(true);
    setError(null);
    try {
      const result = await requestFunc();
      if (successMessage) toast.success(successMessage);
      return result;
    } catch (err: any) {
      const msg = err.response?.data?.detail || Object.values(err.response?.data || {}).join(', ') || errorMessage || "Ocurrió un error.";
      setError(msg);
      toast.error(msg);
      return null;
    } finally {
      setIsLoading(false);
    }
  }, [token]);


  // --- API de Perfil ---
  // ... (sin cambios) ...

  // --- API Comercial (Ciclo de Ingresos) ---
  const getClientes = useCallback(async () => {
    return makeRequest(() => api.get<Cliente[]>('/api/v1/prestadores/mi-negocio/comercial/clientes/').then(res => res.data));
  }, [makeRequest]);

  const createCliente = useCallback(async (data: Omit<Cliente, 'id'>) => {
    return makeRequest(() => api.post<Cliente>('/api/v1/prestadores/mi-negocio/comercial/clientes/', data).then(res => res.data), "Cliente creado con éxito.");
  }, [makeRequest]);

  const updateCliente = useCallback(async (id: number, data: Partial<Omit<Cliente, 'id'>>) => {
    return makeRequest(() => api.patch<Cliente>(`/api/v1/prestadores/mi-negocio/comercial/clientes/${id}/`, data).then(res => res.data), "Cliente actualizado con éxito.");
  }, [makeRequest]);

  const deleteCliente = useCallback(async (id: number) => {
    return makeRequest(() => api.delete(`/api/v1/prestadores/mi-negocio/comercial/clientes/${id}/`), "Cliente eliminado con éxito.");
  }, [makeRequest]);

  const getFacturasVenta = useCallback(async () => {
    return makeRequest(() => api.get<FacturaVenta[]>('/api/v1/prestadores/mi-negocio/comercial/facturas-venta/').then(res => res.data));
  }, [makeRequest]);

  const createFacturaVenta = useCallback(async (data: any) => {
    return makeRequest(() => api.post<FacturaVenta>('/api/v1/prestadores/mi-negocio/comercial/facturas-venta/', data).then(res => res.data), "Factura creada con éxito.");
  }, [makeRequest]);

  // ... (Aquí irían update/delete para facturas, y funciones para pagos y notas de crédito) ...

  // ... (Otras APIs de Contabilidad y Financiero sin cambios) ...
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


  return {
    isLoading,
    error,
    // Perfil
    getPerfil,
    updatePerfil,
    // Comercial
    getClientes,
    createCliente,
    updateCliente,
    deleteCliente,
    getFacturasVenta,
    createFacturaVenta,
    // Contabilidad
    getChartOfAccounts,
    createChartOfAccount,
    updateChartOfAccount,
    deleteChartOfAccount,
    getJournalEntries,
    createJournalEntry,
    updateJournalEntry,
    deleteJournalEntry,
    // Financiero
    getCurrencies,
    getBankAccounts,
    createBankAccount,
    updateBankAccount,
    deleteBankAccount,
    getCashTransactions,
    createCashTransaction,
  };
}
