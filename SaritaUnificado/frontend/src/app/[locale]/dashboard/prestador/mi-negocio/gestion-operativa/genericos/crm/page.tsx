"use client";

import React, { useState, useEffect } from 'react';
import Modal from '../../../components/Modal';
import ClientForm from '../../../components/ClientForm';
import { useMiNegocioApi } from '../../../hooks/useMiNegocioApi';

// Tipo de dato para Cliente
interface Client {
  id: number;
  nombre: string;
  email: string;
  telefono: string;
  notas: string;
}

export default function ClientesPage() {
  const { data: clients, isLoading, error, fetchData, createData, updateData, deleteData } = useMiNegocioApi<Client[]>();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingClient, setEditingClient] = useState<Client | undefined>(undefined);

  // Cargar datos al montar
  useEffect(() => {
    fetchData('operativa/clientes/');
  }, [fetchData]);

  const handleOpenCreateModal = () => {
    setEditingClient(undefined);
    setIsModalOpen(true);
  };

  const handleOpenEditModal = (client: Client) => {
    setEditingClient(client);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => setIsModalOpen(false);

  const handleFormSubmit = async (formData: any) => {
    if (editingClient) {
      await updateData(`operativa/clientes/${editingClient.id}/`, formData);
    } else {
      await createData('operativa/clientes/', formData);
    }
    fetchData('operativa/clientes/'); // Recargar
    handleCloseModal();
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este cliente?')) {
      await deleteData(`operativa/clientes/${id}/`);
      fetchData('operativa/clientes/'); // Recargar
    }
  };

  return (
    <div className="p-4 sm:p-6 lg:p-8">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-bold text-gray-800">Mis Clientes (CRM)</h1>
        <button
          onClick={handleOpenCreateModal}
          className="bg-blue-600 text-white px-4 py-2 rounded-md shadow-sm hover:bg-blue-700"
        >
          Añadir Cliente
        </button>
      </div>

      {isLoading && <p>Cargando clientes...</p>}
      {error && <p className="text-red-600">Error: {error}</p>}

      {!isLoading && !error && (
        <div className="bg-white p-6 rounded-lg shadow-md">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Nombre</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Email</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Teléfono</th>
                <th className="relative px-6 py-3"><span className="sr-only">Acciones</span></th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {(clients && clients.length > 0) ? clients.map((client) => (
                <tr key={client.id}>
                  <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{client.nombre}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{client.email}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{client.telefono}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium space-x-4">
                    <button onClick={() => handleOpenEditModal(client)} className="text-blue-600 hover:text-blue-900">
                      Editar
                    </button>
                    <button onClick={() => handleDelete(client.id)} className="text-red-600 hover:text-red-900">
                      Eliminar
                    </button>
                  </td>
                </tr>
              )) : (
                <tr>
                  <td colSpan={4} className="px-6 py-4 text-center text-sm text-gray-500">
                    No tienes clientes registrados.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      )}

      {isModalOpen && (
        <Modal isOpen={isModalOpen} onClose={handleCloseModal} title={editingClient ? "Editar Cliente" : "Añadir Nuevo Cliente"}>
          <ClientForm
            initialData={editingClient}
            onSubmit={handleFormSubmit}
            onCancel={handleCloseModal}
            isSaving={isLoading}
          />
        </Modal>
      )}
    </div>
  );
}
