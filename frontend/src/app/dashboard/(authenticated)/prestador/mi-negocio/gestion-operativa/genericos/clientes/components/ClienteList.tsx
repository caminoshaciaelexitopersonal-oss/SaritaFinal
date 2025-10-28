// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-operativa/genericos/clientes/components/ClienteList.tsx
'use client';

import React from 'react';
import { Cliente } from '../../../../../hooks/useMiNegocioApi';

interface ClienteListProps {
  clientes: Cliente[];
  onEdit: (cliente: Cliente) => void;
  onDelete: (id: number) => void;
}

export default function ClienteList({ clientes, onEdit, onDelete }: ClienteListProps) {
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
          {clientes.map((cliente) => (
            <tr key={cliente.id}>
              <td className="px-6 py-4 whitespace-nowrap">{cliente.nombre}</td>
              <td className="px-6 py-4 whitespace-nowrap">{cliente.email}</td>
              <td className="px-6 py-4 whitespace-nowrap">{cliente.telefono}</td>
              <td className="px-6 py-4 whitespace-nowrap text-right">
                <button onClick={() => onEdit(cliente)} className="text-indigo-600 hover:text-indigo-900 mr-4">Editar</button>
                <button onClick={() => onDelete(cliente.id)} className="text-red-600 hover:text-red-900">Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
