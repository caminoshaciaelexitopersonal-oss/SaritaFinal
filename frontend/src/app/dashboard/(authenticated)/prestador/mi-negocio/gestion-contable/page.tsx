// /app/dashboard/prestador/mi-negocio/gestion-contable/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import useMiNegocioApi, { ChartOfAccount } from '../../../hooks/useMiNegocioApi';
import ChartOfAccountList from './components/ChartOfAccountList';
import ChartOfAccountForm from './components/ChartOfAccountForm';
import Modal from './components/Modal';

export default function ContabilidadPage() {
  const {
    getChartOfAccounts,
    addChartOfAccount,
    updateChartOfAccount,
    deleteChartOfAccount,
    loading,
    error
  } = useMiNegocioApi();

  const [accounts, setAccounts] = useState<ChartOfAccount[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedAccount, setSelectedAccount] = useState<ChartOfAccount | null>(null);

  const fetchAccounts = useCallback(async () => {
    const data = await getChartOfAccounts();
    if (data) {
      setAccounts(data);
    }
  }, [getChartOfAccounts]);

  useEffect(() => {
    fetchAccounts();
  }, [fetchAccounts]);

  const handleOpenModal = (account: ChartOfAccount | null = null) => {
    setSelectedAccount(account);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setSelectedAccount(null);
    setIsModalOpen(false);
  };

  const handleSubmit = async (data: Omit<ChartOfAccount, 'id'>) => {
    let success = false;
    if (selectedAccount) {
      success = await updateChartOfAccount(selectedAccount.id, data);
    } else {
      success = await addChartOfAccount(data);
    }

    if (success) {
      await fetchAccounts();
      handleCloseModal();
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Está seguro de que desea eliminar esta cuenta?')) {
      const success = await deleteChartOfAccount(id);
      if (success) {
        await fetchAccounts();
      }
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Plan de Cuentas</h1>

      {error && <p className="text-red-500 bg-red-100 p-3 rounded-md mb-4">{error}</p>}

      <div className="mb-4">
        <button
          onClick={() => handleOpenModal()}
          className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
        >
          Añadir Nueva Cuenta
        </button>
      </div>

      <ChartOfAccountList
        accounts={accounts}
        onEdit={(account) => handleOpenModal(account)}
        onDelete={handleDelete}
        isLoading={loading && accounts.length === 0}
      />

      <Modal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        title={selectedAccount ? 'Editar Cuenta Contable' : 'Añadir Nueva Cuenta Contable'}
      >
        <ChartOfAccountForm
          onSubmit={handleSubmit}
          initialData={selectedAccount}
          isLoading={loading}
        />
      </Modal>
    </div>
  );
}
