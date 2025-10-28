// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/facturas-proveedor/[id]/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useParams } from 'next/navigation';
import { useMiNegocioApi, FacturaProveedor } from '../../../../hooks/useMiNegocioApi';
import RegistrarPagoRealizadoForm from './components/RegistrarPagoRealizadoForm';
import Modal from '../../../../componentes/Modal';

export default function FacturaProveedorDetallePage() {
  const params = useParams();
  const { id } = params;
  const { getFacturaProveedor, registrarPagoRealizado, isLoading, error } = useMiNegocioApi();

  const [factura, setFactura] = useState<FacturaProveedor | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchFactura = useCallback(async () => {
    if (typeof id === 'string') {
      const data = await getFacturaProveedor(parseInt(id, 10));
      if (data) setFactura(data);
    }
  }, [id, getFacturaProveedor]);

  useEffect(() => {
    fetchFactura();
  }, [fetchFactura]);

  const handleRegistrarPago = async (pagoData: any) => {
    if (!factura) return;
    const dataToSend = { ...pagoData, factura: factura.id };
    const success = !!await registrarPagoRealizado(dataToSend);
    if (success) {
      await fetchFactura();
      setIsModalOpen(false);
    }
  };

  if (!factura) return <p>Cargando...</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">Factura de Proveedor #{factura.id}</h1>
      <p>Proveedor: {factura.proveedor_nombre}</p>
      <p>Total: {factura.total}</p>
      <p>Estado: {factura.estado}</p>

      <button onClick={() => setIsModalOpen(true)} className="mt-4 px-4 py-2 bg-green-600 text-white rounded">
        Registrar Pago
      </button>

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Registrar Pago a Proveedor">
        <RegistrarPagoRealizadoForm onSubmit={handleRegistrarPago} isLoading={isLoading} />
      </Modal>
    </div>
  );
}
