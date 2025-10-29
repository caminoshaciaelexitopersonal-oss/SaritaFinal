// /app/dashboard/prestador/mi-negocio/gestion-contable/plan-de-cuentas/page.tsx
'use client';

import { useEffect, useState, useCallback } from 'react';
import { useMiNegocioApi, ChartOfAccount } from '../../../hooks/useMiNegocioApi';
import ChartOfAccountForm from '../components/ChartOfAccountForm';
import Modal from '@/components/ui/Modal';
import { FiEdit, FiTrash2, FiPlus } from 'react-icons/fi';

export default function PlanDeCuentasPage() {
  const {
    getChartOfAccounts,
    createChartOfAccount,
    updateChartOfAccount,
    deleteChartOfAccount,
    isLoading,
    error
  } = useMiNegocioApi();

  const [cuentas, setCuentas] = useState<ChartOfAccount[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingAccount, setEditingAccount] = useState<ChartOfAccount | null>(null);

  const fetchCuentas = useCallback(async () => {
    const data = await getChartOfAccounts();
    if (data) {
      setCuentas(data);
    }
  }, [getChartOfAccounts]);

  useEffect(() => {
    fetchCuentas();
  }, [fetchCuentas]);

  const handleFormSubmit = async (data: Omit<ChartOfAccount, 'id'>) => {
    let success = false;
    if (editingAccount) {
      const result = await updateChartOfAccount(editingAccount.id, data);
      if(result) success = true;
    } else {
      const result = await createChartOfAccount(data);
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

  const openEditModal = (cuenta: ChartOfAccount) => {
    setEditingAccount(cuenta);
    setIsModalOpen(true);
  };

  const handleDelete = async (id: number) => {
    if(window.confirm('¿Está seguro de que desea eliminar esta cuenta?')) {
        const success = await deleteChartOfAccount(id);
        if (success) {
            fetchCuentas();
        }
    }
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-gray-800">Plan de Cuentas</h1>
        <button
          onClick={openCreateModal}
          className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg flex items-center"
        >
          <FiPlus className="mr-2" />
          Nueva Cuenta
        </button>
      </div>

      <div className="bg-white shadow-md rounded-lg overflow-hidden">
        {/* ... (código de la tabla similar al anterior, pero con botones de acción) ... */}
         <table className="min-w-full leading-normal">
            <thead>
              <tr>
                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Número</th>
                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Nombre</th>
                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Tipo</th>
                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Activa</th>
                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100"></th>
              </tr>
            </thead>
            <tbody>
              {isLoading && !isModalOpen ? (
                <tr><td colSpan={5} className="text-center py-5">Cargando...</td></tr>
              ) : error ? (
                 <tr><td colSpan={5} className="text-center py-5 text-red-500">{error}</td></tr>
              ) : cuentas.map((cuenta) => (
                  <tr key={cuenta.id} className="hover:bg-gray-50">
                    <td className="px-5 py-4 border-b border-gray-200 text-sm">{cuenta.account_number}</td>
                    <td className="px-5 py-4 border-b border-gray-200 text-sm">{cuenta.name}</td>
                    <td className="px-5 py-4 border-b border-gray-200 text-sm">{cuenta.account_type}</td>
                    <td className="px-5 py-4 border-b border-gray-200 text-sm">
                        <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${cuenta.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                            {cuenta.is_active ? 'Sí' : 'No'}
                        </span>
                    </td>
                    <td className="px-5 py-4 border-b border-gray-200 text-sm text-right">
                        <button onClick={() => openEditModal(cuenta)} className="text-blue-600 hover:text-blue-900 mr-3"><FiEdit /></button>
                        <button onClick={() => handleDelete(cuenta.id)} className="text-red-600 hover:text-red-900"><FiTrash2 /></button>
                    </td>
                  </tr>
                ))
              }
            </tbody>
          </table>
      </div>

      <Modal isOpen={isModalOpen} onClose={closeModal} title={editingAccount ? 'Editar Cuenta' : 'Crear Nueva Cuenta'}>
        <ChartOfAccountForm
          onSubmit={handleFormSubmit}
          initialData={editingAccount}
          isLoading={isLoading}
        />
      </Modal>
    </div>
  );
}
