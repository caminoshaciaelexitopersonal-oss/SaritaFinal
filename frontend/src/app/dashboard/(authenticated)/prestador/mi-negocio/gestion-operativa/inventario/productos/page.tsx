// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-operativa/inventario/productos/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useMiNegocioApi, Producto } from '../../../../../hooks/useMiNegocioApi';
import ProductoList from './components/ProductoList';
import ProductoForm from './components/ProductoForm';
import Modal from '../../../../../componentes/Modal';

export default function ProductosPage() {
  const { getProductos, createProducto, isLoading, error } = useMiNegocioApi();
  const [productos, setProductos] = useState<Producto[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchData = useCallback(async () => {
    const data = await getProductos();
    if (data) setProductos(data);
  }, [getProductos]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleSubmit = async (data: any) => {
    const success = !!await createProducto(data);
    if (success) {
      await fetchData();
      setIsModalOpen(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Maestro de Productos</h1>
      {error && <p className="text-red-500">{error}</p>}
      <button onClick={() => setIsModalOpen(true)} className="px-4 py-2 bg-blue-600 text-white rounded mb-4">
        Nuevo Producto
      </button>
      <ProductoList productos={productos} />
      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Nuevo Producto">
        <ProductoForm onSubmit={handleSubmit} isLoading={isLoading} />
      </Modal>
    </div>
  );
}
