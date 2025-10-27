// /app/dashboard/prestador/mi-negocio/gestion-financiera/transacciones/page.tsx
'use client';

import { useEffect, useState, useCallback } from 'react';
import { useMiNegocioApi, CashTransaction, BankAccount, ChartOfAccount } from '../../../hooks/useMiNegocioApi';
import CashTransactionForm from '../components/CashTransactionForm';
import Modal from '@/components/ui/Modal';
import { FiPlus } from 'react-icons/fi';

export default function TransaccionesPage() {
  const {
    getCashTransactions,
    createCashTransaction,
    getBankAccounts,
    getChartOfAccounts,
    isLoading,
    error
  } = useMiNegocioApi();

  const [transactions, setTransactions] = useState<CashTransaction[]>([]);
  const [bankAccounts, setBankAccounts] = useState<BankAccount[]>([]);
  const [chartOfAccounts, setChartOfAccounts] = useState<ChartOfAccount[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchTransactions = useCallback(async () => {
    const data = await getCashTransactions();
    if (data) setTransactions(data);
  }, [getCashTransactions]);

  useEffect(() => {
    fetchTransactions();
    const fetchRelatedData = async () => {
        const [banks, accounts] = await Promise.all([getBankAccounts(), getChartOfAccounts()]);
        if(banks) setBankAccounts(banks);
        if(accounts) setChartOfAccounts(accounts);
    }
    fetchRelatedData();
  }, [fetchTransactions, getBankAccounts, getChartOfAccounts]);

  const handleFormSubmit = async (data: any) => {
    const success = await createCashTransaction(data);
    if (success) {
      fetchTransactions();
      setIsModalOpen(false);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-gray-800">Transacciones de Tesorería</h1>
        <button onClick={() => setIsModalOpen(true)} className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg flex items-center">
          <FiPlus className="mr-2" />
          Nueva Transacción
        </button>
      </div>

      <div className="bg-white shadow-md rounded-lg overflow-hidden">
        <table className="min-w-full leading-normal">
            <thead>
                <tr>
                    <th className="px-5 py-3 border-b-2 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase">Fecha</th>
                    <th className="px-5 py-3 border-b-2 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase">Tipo</th>
                    <th className="px-5 py-3 border-b-2 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase">Cuenta Bancaria</th>
                    <th className="px-5 py-3 border-b-2 bg-gray-100 text-right text-xs font-semibold text-gray-600 uppercase">Monto</th>
                </tr>
            </thead>
            <tbody>
                {isLoading && transactions.length === 0 ? (
                    <tr><td colSpan={4} className="text-center py-5">Cargando...</td></tr>
                ) : (
                    transactions.map(t => (
                        <tr key={t.id}>
                            <td className="px-5 py-4 border-b text-sm">{t.date}</td>
                            <td className="px-5 py-4 border-b text-sm">{t.transaction_type}</td>
                            <td className="px-5 py-4 border-b text-sm">{t.bank_account_name}</td>
                            <td className="px-5 py-4 border-b text-sm text-right font-mono">{t.amount}</td>
                        </tr>
                    ))
                )}
            </tbody>
        </table>
      </div>

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Crear Nueva Transacción">
        <CashTransactionForm
          onSubmit={handleFormSubmit}
          isLoading={isLoading}
          bankAccounts={bankAccounts}
          chartOfAccounts={chartOfAccounts}
        />
      </Modal>
    </div>
  );
}
