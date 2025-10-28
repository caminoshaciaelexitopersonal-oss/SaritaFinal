// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/facturacion/components/FacturaList.tsx
'use client';

import React from 'react';
import { FacturaVenta } from '../../../../hooks/useMiNegocioApi';

interface FacturaListProps {
  facturas: FacturaVenta[];
  onView: (factura: FacturaVenta) => void;
}

export default function FacturaList({ facturas, onView }: FacturaListProps) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">#</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Cliente</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Fecha Emisión</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Total</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Estado</th>
            <th className="relative px-6 py-3"></th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {facturas.map((factura) => (
            <tr key={factura.id}>
              <td className="px-6 py-4">{factura.id}</td>
              <td className="px-6 py-4">{factura.cliente_nombre || factura.cliente}</td>
              <td className="px-6 py-4">{factura.fecha_emision}</td>
              <td className="px-6 py-4">{factura.total}</td>
              <td className="px-6 py-4"><span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800`}>{factura.estado}</span></td>
              <td className="px-6 py-4 text-right">
                <button onClick={() => onView(factura)} className="text-indigo-600 hover:text-indigo-900">Ver</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
