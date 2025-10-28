// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-contable/activos-fijos/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useRouter } from 'next/navigation';
import { useMiNegocioApi, ActivoFijo } from '../../../../../hooks/useMiNegocioApi';
import ActivoFijoList from './components/ActivoFijoList';
import ActivoFijoForm from './components/ActivoFijoForm';
import Modal from '../../../../../componentes/Modal';

export default function ActivosFijosPage() {
  const { getActivosFijos, createActivoFijo, isLoading, error } = useMiNegocioApi();
  const [activos, setActivos] = useState<ActivoFijo[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const router = useRouter();

  const fetchData = useCallback(async () => {
    const data = await getActivosFijos();
    if (data) setActivos(data);
  }, [getActivosFijos]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleSubmit = async (data: any) => {
    const success = !!await createActivoFijo(data);
    if (success) {
      await fetchData();
      setIsModalOpen(false);
    }
  };

  const handleViewDetails = (id: number) => {
    router.push(`/dashboard/prestador/mi-negocio/gestion-contable/activos-fijos/${id}`);
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Activos Fijos</h1>
      {error && <p className="text-red-500">{error}</p>}
      <button onClick={() => setIsModalOpen(true)} className="px-4 py-2 bg-blue-600 text-white rounded mb-4">
        Nuevo Activo Fijo
      </button>
      <ActivoFijoList activos={activos} onView={handleViewDetails} />
      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Nuevo Activo Fijo">
        <ActivoFijoForm onSubmit={handleSubmit} isLoading={isLoading} />
      </Modal>
    </div>
  );
}
