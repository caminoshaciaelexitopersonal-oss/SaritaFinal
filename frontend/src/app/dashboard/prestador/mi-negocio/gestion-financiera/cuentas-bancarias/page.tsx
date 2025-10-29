// /app/dashboard/prestador/mi-negocio/gestion-financiera/cuentas-bancarias/page.tsx
'use client';

import { useEffect, useState, useCallback } from 'react';
import { useMiNegocioApi, BankAccount } from '../../../hooks/useMiNegocioApi';
import BankAccountForm from '../components/BankAccountForm';
import Modal from '@/components/ui/Modal';
import { FiEdit, FiTrash2, FiPlus } from 'react-icons/fi';

export default function CuentasBancariasPage() {
  const {
    getBankAccounts,
    createBankAccount,
    updateBankAccount,
    deleteBankAccount,
    getCurrencies,
    isLoading,
    error
  } = useMiNegocioApi();

  const [cuentas, setCuentas] = useState<BankAccount[]>([]);
  const [currencies, setCurrencies] = useState<{ code: string; name: string }[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingAccount, setEditingAccount] = useState<BankAccount | null>(null);

  const fetchCuentas = useCallback(async () => {
    const data = await getBankAccounts();
    if (data) setCuentas(data);
  }, [getBankAccounts]);

  useEffect(() => {
    fetchCuentas();
    const fetchCurrencies = async () => {
        const data = await getCurrencies();
        if(data) setCurrencies(data);
    }
    fetchCurrencies();
  }, [fetchCuentas, getCurrencies]);

  const handleFormSubmit = async (data: any) => {
    let success = false;
    if (editingAccount) {
      const result = await updateBankAccount(editingAccount.id, data);
      if(result) success = true;
    } else {
      const result = await createBankAccount(data);
       if(result) success = true;
    }

    if (success) {
      fetchCuentas();
      closeModal();
    }
  };

  const openCreateModal = () => {
    setEditingAccount(null);
    setIsModalOpen(true);
  };

  const openEditModal = (cuenta: BankAccount) => {
    setEditingAccount(cuenta);
    setIsModalOpen(true);
  };

  const handleDelete = async (id: number) => {
    if(window.confirm('¿Eliminar esta cuenta bancaria?')) {
        const success = await deleteBankAccount(id);
        if (success) fetchCuentas();
    }
  };

  const closeModal = () => setIsModalOpen(false);

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-gray-800">Cuentas Bancarias</h1>
        <button onClick={openCreateModal} className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg flex items-center">
          <FiPlus className="mr-2" />
          Nueva Cuenta
        </button>
      </div>

      <div className="bg-white shadow-md rounded-lg overflow-hidden">
        <table className="min-w-full leading-normal">
          <thead>
            <tr>
              <th className="px-5 py-3 border-b-2 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase">Banco</th>
              <th className="px-5 py-3 border-b-2 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase">Número</th>
              <th className="px-5 py-3 border-b-2 bg-gray-100 text-right text-xs font-semibold text-gray-600 uppercase">Saldo</th>
              <th className="px-5 py-3 border-b-2 bg-gray-100"></th>
            </tr>
          </thead>
          <tbody>
            {isLoading && !isModalOpen ? (
              <tr><td colSpan={4} className="text-center py-5">Cargando...</td></tr>
            ) : error ? (
              <tr><td colSpan={4} className="text-center py-5 text-red-500">{error}</td></tr>
            ) : (
              cuentas.map((cuenta) => (
                <tr key={cuenta.id} className="hover:bg-gray-50">
                  <td className="px-5 py-4 border-b text-sm">{cuenta.bank_name}</td>
                  <td className="px-5 py-4 border-b text-sm">{cuenta.account_number}</td>
                  <td className="px-5 py-4 border-b text-sm text-right font-mono">
                    {new Intl.NumberFormat('es-CO', { style: 'currency', currency: cuenta.currency_code }).format(parseFloat(cuenta.balance))}
                  </td>
                  <td className="px-5 py-4 border-b text-sm text-right">
                    <button onClick={() => openEditModal(cuenta)} className="text-blue-600 hover:text-blue-900 mr-3"><FiEdit /></button>
                    <button onClick={() => handleDelete(cuenta.id)} className="text-red-600 hover:text-red-900"><FiTrash2 /></button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      <Modal isOpen={isModalOpen} onClose={closeModal} title={editingAccount ? 'Editar Cuenta Bancaria' : 'Crear Cuenta Bancaria'}>
        <BankAccountForm
          onSubmit={handleFormSubmit}
          initialData={editingAccount}
          isLoading={isLoading}
          currencies={currencies}
        />
      </Modal>
    </div>
  );
}
