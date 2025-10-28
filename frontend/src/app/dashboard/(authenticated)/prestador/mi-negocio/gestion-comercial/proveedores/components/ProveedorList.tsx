// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/proveedores/components/ProveedorList.tsx
'use client';

import React from 'react';
import { Proveedor } from '../../../../hooks/useMiNegocioApi';

interface ProveedorListProps {
  proveedores: Proveedor[];
  onEdit: (proveedor: Proveedor) => void;
  onDelete: (id: number) => void;
}

export default function ProveedorList({ proveedores, onEdit, onDelete }: ProveedorListProps) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Nombre</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Email</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Teléfono</th>
            <th className="relative px-6 py-3"></th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {proveedores.map((proveedor) => (
            <tr key={proveedor.id}>
              <td className="px-6 py-4">{proveedor.nombre}</td>
              <td className="px-6 py-4">{proveedor.email}</td>
              <td className="px-6 py-4">{proveedor.telefono}</td>
              <td className="px-6 py-4 text-right">
                <button onClick={() => onEdit(proveedor)} className="text-indigo-600 hover:text-indigo-900 mr-4">Editar</button>
                <button onClick={() => onDelete(proveedor.id)} className="text-red-600 hover:text-red-900">Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
