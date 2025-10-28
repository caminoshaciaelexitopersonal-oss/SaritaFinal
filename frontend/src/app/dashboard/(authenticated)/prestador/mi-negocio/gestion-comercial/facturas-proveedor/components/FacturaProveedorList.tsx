// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/facturas-proveedor/components/FacturaProveedorList.tsx
'use client';

import React from 'react';
import { FacturaProveedor } from '../../../../hooks/useMiNegocioApi';

interface FacturaProveedorListProps {
  facturas: FacturaProveedor[];
  onView: (factura: FacturaProveedor) => void;
}

export default function FacturaProveedorList({ facturas, onView }: FacturaProveedorListProps) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">#</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Proveedor</th>
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
              <td className="px-6 py-4">{factura.proveedor_nombre || factura.proveedor}</td>
              <td className="px-6 py-4">{factura.fecha_emision}</td>
              <td className="px-6 py-4">{factura.total}</td>
              <td className="px-6 py-4"><span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800`}>{factura.estado}</span></td>
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
