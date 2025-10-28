// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-contable/centros-de-costo/components/CostCenterList.tsx
'use client';

import React from 'react';
import { CostCenter } from '../../../../../hooks/useMiNegocioApi';

interface CostCenterListProps {
  costCenters: CostCenter[];
  onEdit: (costCenter: CostCenter) => void;
  onDelete: (id: number) => void;
}

export default function CostCenterList({ costCenters, onEdit, onDelete }: CostCenterListProps) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Código</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Nombre</th>
            <th className="relative px-6 py-3"></th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {costCenters.map((cc) => (
            <tr key={cc.id}>
              <td className="px-6 py-4">{cc.code}</td>
              <td className="px-6 py-4">{cc.name}</td>
              <td className="px-6 py-4 text-right">
                <button onClick={() => onEdit(cc)} className="text-indigo-600 hover:text-indigo-900 mr-4">Editar</button>
                <button onClick={() => onDelete(cc.id)} className="text-red-600 hover:text-red-900">Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
