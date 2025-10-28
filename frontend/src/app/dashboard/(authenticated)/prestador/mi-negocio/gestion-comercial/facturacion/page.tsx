// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/facturacion/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useMiNegocioApi, FacturaVenta, Cliente } from '../../../../hooks/useMiNegocioApi';
import FacturaList from './components/FacturaList';
import FacturaForm from './components/FacturaForm';
import Modal from '../../../../componentes/Modal';

export default function FacturacionPage() {
  const {
    getFacturasVenta,
    createFacturaVenta,
    getClientes,
    isLoading,
    error
  } = useMiNegocioApi();

  const [facturas, setFacturas] = useState<FacturaVenta[]>([]);
  const [clientes, setClientes] = useState<Cliente[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchData = useCallback(async () => {
    const facturasData = await getFacturasVenta();
    if (facturasData) setFacturas(facturasData);
    const clientesData = await getClientes();
    if (clientesData) setClientes(clientesData);
  }, [getFacturasVenta, getClientes]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleSubmit = async (data: any) => {
    const success = !!await createFacturaVenta(data);
    if (success) {
      await fetchData();
      setIsModalOpen(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Facturación</h1>
      {error && <p className="text-red-500 bg-red-100 p-3 rounded mb-4">{error}</p>}
      <button onClick={() => setIsModalOpen(true)} className="px-4 py-2 bg-blue-600 text-white rounded mb-4">
        Nueva Factura
      </button>

      <FacturaList
        facturas={facturas}
        onView={(factura) => alert(`Viendo factura #${factura.id}`)} // Placeholder
      />

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Crear Nueva Factura">
        <FacturaForm
          onSubmit={handleSubmit}
          clientes={clientes}
          isLoading={isLoading}
        />
      </Modal>
    </div>
  );
}
