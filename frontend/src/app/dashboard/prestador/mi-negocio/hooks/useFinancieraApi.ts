import useSWR from 'swr';
import { useApi } from '@/services/api';
import { useCallback } from 'react';

// --- Tipos de Datos ---
export interface BankAccount {
    id: number;
    name: string;
    account_number: string;
    bank_name: string;
    linked_account_code: string;
}
export interface CashTransaction {
    id: number;
    transaction_date: string;
    description: string;
    amount: string;
    transaction_type: string;
    status: string;
    bank_account_name: string;
}

export const useFinancieraApi = () => {
    const { api } = useApi();
    const fetcher = useCallback((url: string) => api.get(url).then(res => res.data), [api]);

    // --- Reportes ---
    const { data: reporteIngresosGastos, error: reporteError } = useSWR('/v1/mi-negocio/financiera/reporte-ingresos-gastos/', fetcher);

    // --- Cuentas Bancarias ---
    const { data: bankAccounts, error: bankAccountsError, mutate: mutateBankAccounts } = useSWR<{ results: BankAccount[] }>('/v1/mi-negocio/financiera/bank-accounts/', fetcher);

    const createBankAccount = useCallback(async (data: any) => {
        await api.post('/v1/mi-negocio/financiera/bank-accounts/', data);
        mutateBankAccounts();
    }, [api, mutateBankAccounts]);

    // --- Transacciones Bancarias ---
    const { data: cashTransactions, error: cashTransactionsError, mutate: mutateCashTransactions } = useSWR<{ results: CashTransaction[] }>('/v1/mi-negocio/financiera/cash-transactions/', fetcher);

    const createCashTransaction = useCallback(async (data: any) => {
        await api.post('/v1/mi-negocio/financiera/cash-transactions/', data);
        mutateCashTransactions();
        // Podríamos querer mutar las cuentas si el saldo se derivara, pero ahora viene de contabilidad
    }, [api, mutateCashTransactions]);

    return {
        // Cuentas Bancarias
        bankAccounts: bankAccounts?.results || [],
        bankAccountsLoading: !bankAccounts && !bankAccountsError,
        bankAccountsError,
        createBankAccount,

        // Transacciones Bancarias
        cashTransactions: cashTransactions?.results || [],
        cashTransactionsLoading: !cashTransactions && !cashTransactionsError,
        cashTransactionsError,
        createCashTransaction,

        // Reportes
        reporteIngresosGastos,
        reporteLoading: !reporteIngresosGastos && !reporteError,
        reporteError,
    };
};
