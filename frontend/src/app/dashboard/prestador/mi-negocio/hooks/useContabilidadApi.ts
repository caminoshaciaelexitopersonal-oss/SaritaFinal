import useSWR from 'swr';
import { useApi } from '@/services/api';
import { useCallback } from 'react';

// TODO: Definir interfaces más estrictas para los objetos de la API
export interface CostCenter {
    id: number;
    code: string;
    name: string;
}

export interface JournalEntry {
    id: number;
    entry_date: string;
    description: string;
    transactions: {
        account: {
            code: string;
            name: string;
        };
        debit: string;
        credit: string;
    }[];
}

export const useContabilidadApi = () => {
    const { api } = useApi();

    const fetcher = useCallback((url: string) => api.get(url).then(res => res.data), [api]);

    // --- Cost Centers ---
    const { data: costCenters, error: costCentersError, mutate: mutateCostCenters } = useSWR('/v1/mi-negocio/contable/contabilidad/cost-centers/', fetcher);

    const createCostCenter = useCallback(async (data: { code: string; name: string }) => {
        const response = await api.post('/v1/mi-negocio/contable/contabilidad/cost-centers/', data);
        mutateCostCenters();
        return response.data;
    }, [api, mutateCostCenters]);

    // --- Chart of Accounts (Read-only) ---
    const { data: chartOfAccounts, error: chartOfAccountsError } = useSWR('/v1/mi-negocio/contable/contabilidad/chart-of-accounts/', fetcher);

    // --- Journal Entries ---
    const { data: journalEntries, error: journalEntriesError, mutate: mutateJournalEntries } = useSWR<{ results: JournalEntry[] }>('/v1/mi-negocio/contable/contabilidad/journal-entries/', fetcher);

    const createJournalEntry = useCallback(async (data: any) => {
        const response = await api.post('/v1/mi-negocio/contable/contabilidad/journal-entries/', data);
        mutateJournalEntries();
        return response.data;
    }, [api, mutateJournalEntries]);


    return {
        // Cost Centers
        costCenters: costCenters?.results || [],
        costCentersLoading: !costCenters && !costCentersError,
        costCentersError,
        createCostCenter,

        // Chart of Accounts
        chartOfAccounts: chartOfAccounts?.results || [],
        chartOfAccountsLoading: !chartOfAcounts && !chartOfAccountsError,
        chartOfAccountsError,

        // Journal Entries
        journalEntries: journalEntries?.results || [],
        journalEntriesLoading: !journalEntries && !journalEntriesError,
        journalEntriesError,
        createJournalEntry,
    };
};
