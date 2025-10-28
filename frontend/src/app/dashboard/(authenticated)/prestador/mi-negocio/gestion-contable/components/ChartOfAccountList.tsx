// /app/dashboard/prestador/mi-negocio/gestion-contable/components/ChartOfAccountList.tsx
'use client';

import React from 'react';
import { ChartOfAccount } from '../../../hooks/useMiNegocioApi';

interface ChartOfAccountListProps {
  accounts: ChartOfAccount[];
  onEdit: (account: ChartOfAccount) => void;
  onDelete: (id: number) => void;
  isLoading: boolean;
}

export default function ChartOfAccountList({ accounts, onEdit, onDelete, isLoading }: ChartOfAccountListProps) {
  if (isLoading) {
    return <p>Cargando cuentas...</p>;
  }

  if (accounts.length === 0) {
    return <p>No se encontraron cuentas contables.</p>;
  }

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Código</th>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Naturaleza</th>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Permite Mov.</th>
            <th scope="col" className="relative px-6 py-3">
              <span className="sr-only">Acciones</span>
            </th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {accounts.map((account) => (
            <tr key={account.id}>
              <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{account.code}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{account.name}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{account.nature === 'DEBITO' ? 'Débito' : 'Crédito'}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${account.allows_transactions ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                  {account.allows_transactions ? 'Sí' : 'No'}
                </span>
              </td>
              <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <button onClick={() => onEdit(account)} className="text-indigo-600 hover:text-indigo-900 mr-4">Editar</button>
                <button onClick={() => onDelete(account.id)} className="text-red-600 hover:text-red-900">Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
