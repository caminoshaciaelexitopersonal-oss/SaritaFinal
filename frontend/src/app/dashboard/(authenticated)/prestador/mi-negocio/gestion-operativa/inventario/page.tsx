// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-operativa/inventario/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useMiNegocioApi, Producto, MovimientoInventario } from '../../../../../hooks/useMiNegocioApi';
import KardexList from './components/KardexList';

export default function InventarioPage() {
  const { getProductos, getKardex, isLoading } = useMiNegocioApi();

  const [productos, setProductos] = useState<Producto[]>([]);
  const [selectedProducto, setSelectedProducto] = useState<number | null>(null);
  const [movimientos, setMovimientos] = useState<MovimientoInventario[]>([]);

  useEffect(() => {
    async function loadProductos() {
      const data = await getProductos();
      if (data) setProductos(data);
    }
    loadProductos();
  }, [getProductos]);

  const handleProductoChange = useCallback(async (e: React.ChangeEvent<HTMLSelectElement>) => {
    const productoId = parseInt(e.target.value, 10);
    if (productoId) {
      setSelectedProducto(productoId);
      const data = await getKardex(productoId);
      if (data) setMovimientos(data);
    } else {
      setSelectedProducto(null);
      setMovimientos([]);
    }
  }, [getKardex]);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Consulta de Kardex</h1>

      <select onChange={handleProductoChange} className="w-full p-2 border rounded mb-4">
        <option value="">-- Seleccione un Producto --</option>
        {productos.map(p => <option key={p.id} value={p.id}>{p.nombre}</option>)}
      </select>

      {isLoading && <p>Cargando movimientos...</p>}

      {selectedProducto && <KardexList movimientos={movimientos} />}
    </div>
  );
}
