// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/proveedores/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useMiNegocioApi, Proveedor } from '../../../../hooks/useMiNegocioApi';
import ProveedorList from './components/ProveedorList';
import ProveedorForm from './components/ProveedorForm';
import Modal from '../../../../componentes/Modal';

export default function ProveedoresPage() {
  const {
    getProveedores,
    createProveedor,
    updateProveedor,
    deleteProveedor,
    isLoading,
    error
  } = useMiNegocioApi();

  const [proveedores, setProveedores] = useState<Proveedor[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedProveedor, setSelectedProveedor] = useState<Proveedor | null>(null);

  const fetchProveedores = useCallback(async () => {
    const data = await getProveedores();
    if (data) setProveedores(data);
  }, [getProveedores]);

  useEffect(() => {
    fetchProveedores();
  }, [fetchProveedores]);

  const handleOpenModal = (proveedor: Proveedor | null = null) => {
    setSelectedProveedor(proveedor);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setSelectedProveedor(null);
    setIsModalOpen(false);
  };

  const handleSubmit = async (data: Omit<Proveedor, 'id'>) => {
    let success = false;
    if (selectedProveedor) {
      success = !!await updateProveedor(selectedProveedor.id, data);
    } else {
      success = !!await createProveedor(data);
    }

    if (success) {
      await fetchProveedores();
      handleCloseModal();
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Está seguro de que desea eliminar este proveedor?')) {
      const success = !!await deleteProveedor(id);
      if (success) {
        await fetchProveedores();
      }
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Gestión de Proveedores</h1>
      {error && <p className="text-red-500 bg-red-100 p-3 rounded mb-4">{error}</p>}
      <button onClick={() => handleOpenModal()} className="px-4 py-2 bg-blue-600 text-white rounded mb-4">
        Añadir Proveedor
      </button>

      <ProveedorList
        proveedores={proveedores}
        onEdit={handleOpenModal}
        onDelete={handleDelete}
      />

      <Modal isOpen={isModalOpen} onClose={handleCloseModal} title={selectedProveedor ? 'Editar Proveedor' : 'Nuevo Proveedor'}>
        <ProveedorForm
          onSubmit={handleSubmit}
          initialData={selectedProveedor}
          isLoading={isLoading}
        />
      </Modal>
    </div>
  );
}
