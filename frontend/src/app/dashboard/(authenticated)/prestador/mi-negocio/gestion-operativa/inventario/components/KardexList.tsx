// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-operativa/inventario/components/KardexList.tsx
'use client';

import React from 'react';
import { MovimientoInventario } from '../../../../../hooks/useMiNegocioApi';

interface KardexListProps {
  movimientos: MovimientoInventario[];
}

export default function KardexList({ movimientos }: KardexListProps) {
  return (
    <div className="overflow-x-auto mt-4">
      <h3 className="font-bold">Movimientos (Kardex)</h3>
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Fecha</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Tipo</th>
            <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Cantidad</th>
            <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Costo Unit.</th>
            <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Costo Total</th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {movimientos.map((m) => (
            <tr key={m.id}>
              <td className="px-6 py-4">{m.fecha}</td>
              <td className="px-6 py-4">{m.tipo}</td>
              <td className="px-6 py-4 text-right">{m.cantidad}</td>
              <td className="px-6 py-4 text-right">{m.costo_unitario}</td>
              <td className="px-6 py-4 text-right">{m.costo_total}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
