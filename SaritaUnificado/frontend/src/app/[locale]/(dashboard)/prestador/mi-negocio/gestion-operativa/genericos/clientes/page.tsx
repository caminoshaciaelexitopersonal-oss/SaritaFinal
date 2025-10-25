// src/app/[locale]/(dashboard)/prestador/mi-negocio/gestion-operativa/genericos/clientes/page.tsx
'use client';

import { useState, useEffect } from 'react';
import { useMiNegocioApi, Cliente } from '../../../hooks/useMiNegocioApi';

export default function ClientesPage() {
  const [clientes, setClientes] = useState<Cliente[]>([]);
  const { isLoading, error, getClientes, deleteCliente } = useMiNegocioApi();

  const loadClientes = async () => {
    const data = await getClientes();
    if (data) {
      setClientes(data);
    }
  };

  useEffect(() => {
    loadClientes();
  }, []);

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar este cliente?')) {
      await deleteCliente(id);
      loadClientes(); // Recargar la lista después de eliminar
    }
  };

  if (isLoading && clientes.length === 0) {
    return <div className="p-6 text-center">Cargando clientes...</div>;
  }

  if (error && clientes.length === 0) {
    return <div className="p-6 text-red-500 text-center">Error: {error}</div>;
  }

  return (
    <div className="p-4 sm:p-6 md:p-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-gray-800">Mis Clientes (CRM)</h1>
        <button className="px-4 py-2 bg-blue-600 text-white font-medium rounded-md hover:bg-blue-700">
          Añadir Cliente
        </button>
      </div>
      <div className="bg-white p-6 rounded-lg shadow-md">
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Teléfono</th>
                <th scope="col" className="relative px-6 py-3">
                  <span className="sr-only">Acciones</span>
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {clientes.length > 0 ? (
                clientes.map((cliente) => (
                  <tr key={cliente.id}>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{cliente.nombre}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{cliente.email}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{cliente.telefono}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                      <button className="text-blue-600 hover:text-blue-900">Editar</button>
                      <button onClick={() => handleDelete(cliente.id)} className="ml-4 text-red-600 hover:text-red-900">Eliminar</button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={4} className="px-6 py-4 text-center text-sm text-gray-500">No hay clientes registrados.</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
