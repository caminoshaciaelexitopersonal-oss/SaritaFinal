// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-contable/activos-fijos/components/ActivoFijoList.tsx
'use client';

import React from 'react';
import { ActivoFijo } from '../../../../../hooks/useMiNegocioApi';

interface ActivoFijoListProps {
  activos: ActivoFijo[];
  onView: (id: number) => void;
}

export default function ActivoFijoList({ activos, onView }: ActivoFijoListProps) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left">Nombre</th>
            <th className="px-6 py-3 text-right">Valor en Libros</th>
            <th className="px-6 py-3 text-right">Dep. Acumulada</th>
            <th className="relative px-6 py-3"></th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {activos.map((a) => (
            <tr key={a.id}>
              <td className="px-6 py-4">{a.nombre}</td>
              <td className="px-6 py-4 text-right">{a.valor_en_libros}</td>
              <td className="px-6 py-4 text-right">{a.depreciacion_acumulada}</td>
              <td className="px-6 py-4 text-right">
                <button onClick={() => onView(a.id)} className="text-indigo-600">Ver Detalle</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
