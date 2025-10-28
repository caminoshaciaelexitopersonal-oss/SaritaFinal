// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-operativa/inventario/productos/components/ProductoList.tsx
'use client';

import React from 'react';
import { Producto } from '../../../../../hooks/useMiNegocioApi';

interface ProductoListProps {
  productos: Producto[];
}

export default function ProductoList({ productos }: ProductoListProps) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Nombre</th>
            <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Stock</th>
            <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Costo Promedio</th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {productos.map((p) => (
            <tr key={p.id}>
              <td className="px-6 py-4">{p.nombre}</td>
              <td className="px-6 py-4 text-right">{p.cantidad_en_stock}</td>
              <td className="px-6 py-4 text-right">{p.costo_promedio_ponderado}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
