// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/facturas-proveedor/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useMiNegocioApi, FacturaProveedor, Proveedor, CostCenter } from '../../../../hooks/useMiNegocioApi';
import FacturaProveedorList from './components/FacturaProveedorList';
import FacturaProveedorForm from './components/FacturaProveedorForm';
import Modal from '../../../../componentes/Modal';

export default function FacturasProveedorPage() {
  const {
    getFacturasProveedor,
    createFacturaProveedor,
    getProveedores,
    getCostCenters,
    isLoading,
    error
  } = useMiNegocioApi();

  const [facturas, setFacturas] = useState<FacturaProveedor[]>([]);
  const [proveedores, setProveedores] = useState<Proveedor[]>([]);
  const [costCenters, setCostCenters] = useState<CostCenter[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchData = useCallback(async () => {
    const facturasData = await getFacturasProveedor();
    if (facturasData) setFacturas(facturasData);
    const proveedoresData = await getProveedores();
    if (proveedoresData) setProveedores(proveedoresData);
    const costCentersData = await getCostCenters();
    if (costCentersData) setCostCenters(costCentersData);
  }, [getFacturasProveedor, getProveedores, getCostCenters]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleSubmit = async (data: any) => {
    const success = !!await createFacturaProveedor(data);
    if (success) {
      await fetchData();
      setIsModalOpen(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Facturas de Proveedor</h1>
      {error && <p className="text-red-500 bg-red-100 p-3 rounded mb-4">{error}</p>}
      <button onClick={() => setIsModalOpen(true)} className="px-4 py-2 bg-blue-600 text-white rounded mb-4">
        Registrar Factura
      </button>

      <FacturaProveedorList
        facturas={facturas}
        onView={(factura) => alert(`Viendo factura de proveedor #${factura.id}`)}
      />

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Registrar Nueva Factura de Proveedor">
        <FacturaProveedorForm
          onSubmit={handleSubmit}
          proveedores={proveedores}
          costCenters={costCenters}
          isLoading={isLoading}
        />
      </Modal>
    </div>
  );
}
