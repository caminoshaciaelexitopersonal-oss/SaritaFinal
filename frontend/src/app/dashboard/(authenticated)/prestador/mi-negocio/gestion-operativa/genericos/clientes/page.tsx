// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-operativa/genericos/clientes/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useMiNegocioApi, Cliente } from '../../../../../hooks/useMiNegocioApi';
import ClienteList from './components/ClienteList';
import ClienteForm from './components/ClienteForm';
import Modal from '../../../../../componentes/Modal'; // Importar desde la nueva ubicación

export default function ClientesPage() {
  const {
    getClientes,
    createCliente,
    updateCliente,
    deleteCliente,
    isLoading,
    error
  } = useMiNegocioApi();

  const [clientes, setClientes] = useState<Cliente[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedCliente, setSelectedCliente] = useState<Cliente | null>(null);

  const fetchClientes = useCallback(async () => {
    const data = await getClientes();
    if (data) setClientes(data);
  }, [getClientes]);

  useEffect(() => {
    fetchClientes();
  }, [fetchClientes]);

  const handleOpenModal = (cliente: Cliente | null = null) => {
    setSelectedCliente(cliente);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setSelectedCliente(null);
    setIsModalOpen(false);
  };

  const handleSubmit = async (data: Omit<Cliente, 'id'>) => {
    let success = false;
    if (selectedCliente) {
      success = !!await updateCliente(selectedCliente.id, data);
    } else {
      success = !!await createCliente(data);
    }

    if (success) {
      await fetchClientes();
      handleCloseModal();
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Está seguro de que desea eliminar este cliente?')) {
      const success = !!await deleteCliente(id);
      if (success) {
        await fetchClientes();
      }
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Gestión de Clientes</h1>
      {error && <p className="text-red-500 bg-red-100 p-3 rounded mb-4">{error}</p>}
      <button onClick={() => handleOpenModal()} className="px-4 py-2 bg-blue-600 text-white rounded mb-4">
        Añadir Cliente
      </button>

      <ClienteList
        clientes={clientes}
        onEdit={handleOpenModal}
        onDelete={handleDelete}
      />

      <Modal isOpen={isModalOpen} onClose={handleCloseModal} title={selectedCliente ? 'Editar Cliente' : 'Nuevo Cliente'}>
        <ClienteForm
          onSubmit={handleSubmit}
          initialData={selectedCliente}
          isLoading={isLoading}
        />
      </Modal>
    </div>
  );
}
