// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/facturacion/[id]/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useParams } from 'next/navigation';
import { useMiNegocioApi, FacturaVenta, PagoRecibido } from '../../../../hooks/useMiNegocioApi';
import RegistrarPagoForm from './components/RegistrarPagoForm';
import Modal from '../../../../componentes/Modal';

export default function FacturaVentaDetallePage() {
  const params = useParams();
  const { id } = params;
  const { getFacturaVenta, registrarPagoRecibido, isLoading, error } = useMiNegocioApi();

  const [factura, setFactura] = useState<FacturaVenta | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchFactura = useCallback(async () => {
    if (typeof id === 'string') {
      const data = await getFacturaVenta(parseInt(id, 10));
      if (data) setFactura(data);
    }
  }, [id, getFacturaVenta]);

  useEffect(() => {
    fetchFactura();
  }, [fetchFactura]);

  const handleRegistrarPago = async (pagoData: any) => {
    if (!factura) return;
    const dataToSend = { ...pagoData, factura: factura.id };
    const success = !!await registrarPagoRecibido(dataToSend);
    if (success) {
      await fetchFactura();
      setIsModalOpen(false);
    }
  };

  if (isLoading && !factura) return <p>Cargando factura...</p>;
  if (!factura) return <p>Factura no encontrada.</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">Factura #{factura.id}</h1>
      <p>Cliente: {factura.cliente_nombre}</p>
      <p>Total: {factura.total}</p>
      <p>Pagado: {factura.pagado}</p>
      <p>Estado: {factura.estado}</p>

      <button onClick={() => setIsModalOpen(true)} className="mt-4 px-4 py-2 bg-green-600 text-white rounded">
        Registrar Pago
      </button>

      {/* Aquí iría la lista de pagos */}

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Registrar Pago">
        <RegistrarPagoForm onSubmit={handleRegistrarPago} isLoading={isLoading} />
      </Modal>
    </div>
  );
}
