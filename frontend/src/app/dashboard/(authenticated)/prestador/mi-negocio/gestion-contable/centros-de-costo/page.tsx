// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-contable/centros-de-costo/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useMiNegocioApi, CostCenter } from '../../../../../hooks/useMiNegocioApi';
import CostCenterList from './components/CostCenterList';
import CostCenterForm from './components/CostCenterForm';
import Modal from '../../../../../componentes/Modal';

export default function CentrosDeCostoPage() {
  const {
    getCostCenters,
    createCostCenter,
    updateCostCenter,
    deleteCostCenter,
    isLoading,
    error
  } = useMiNegocioApi();

  const [costCenters, setCostCenters] = useState<CostCenter[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedCC, setSelectedCC] = useState<CostCenter | null>(null);

  const fetchData = useCallback(async () => {
    const data = await getCostCenters();
    if (data) setCostCenters(data);
  }, [getCostCenters]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleOpenModal = (cc: CostCenter | null = null) => {
    setSelectedCC(cc);
    setIsModalOpen(true);
  };

  const handleSubmit = async (data: Omit<CostCenter, 'id'>) => {
    let success = false;
    if (selectedCC) {
      success = !!await updateCostCenter(selectedCC.id, data);
    } else {
      success = !!await createCostCenter(data);
    }

    if (success) {
      await fetchData();
      setIsModalOpen(false);
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Eliminar Centro de Costo?')) {
      const success = !!await deleteCostCenter(id);
      if (success) await fetchData();
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Centros de Costo</h1>
      {error && <p className="text-red-500 bg-red-100 p-3 rounded mb-4">{error}</p>}
      <button onClick={() => handleOpenModal()} className="px-4 py-2 bg-blue-600 text-white rounded mb-4">
        Nuevo Centro de Costo
      </button>

      <CostCenterList
        costCenters={costCenters}
        onEdit={handleOpenModal}
        onDelete={handleDelete}
      />

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={selectedCC ? 'Editar' : 'Nuevo'}>
        <CostCenterForm
          onSubmit={handleSubmit}
          initialData={selectedCC}
          isLoading={isLoading}
        />
      </Modal>
    </div>
  );
}
